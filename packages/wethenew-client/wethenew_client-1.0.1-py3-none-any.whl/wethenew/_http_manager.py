from typing import Any
import random
import cloudscraper
from requests import Response
from playwright.sync_api import sync_playwright, TimeoutError, Error, Page, Browser, Request
from undetected_playwright import stealth_sync
from wethenew._proxy_manager import ProxyManager


class _HTTPManager:
    _AUTH_TOKEN: str | None = None
    _BASE_URL = "https://sell.wethenew.com"
    _API_BASE_URL = "https://api-sell.wethenew.com"
    _LOGIN_URL = f"{_BASE_URL}/en/login"
    _HOME_URL = f"{_BASE_URL}/"
    _DEFAULT_RETRY_AFTER_SECONDS = 180

    def __init__(self, email: str, password: str, proxies_file_name: str) -> None:
        self.email = email
        self.password = password
        self.proxy_manager = ProxyManager(proxies_file_name)
        self._session = cloudscraper.create_scraper()
        self._session.proxies.update(self.proxy_manager.get_next_proxy())

    def _login(self) -> bool:
        try:
            browser, page = self._initialize_browser()
            self._handle_cookies(page)
            if not self._authenticate(page):
                return False
            browser.close()
            return True
        except Error:
            return False

    def _initialize_browser(self) -> tuple[Browser, Page]:
        browser = sync_playwright().start().chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        )
        stealth_sync(context)
        page = context.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.on("request", self._handle_request)
        page.goto(self._LOGIN_URL, wait_until="domcontentloaded")
        return browser, page

    def _handle_request(self, request: Request) -> None:
        headers = request.headers
        auth_value = headers.get("authorization")
        if auth_value:
            _HTTPManager._AUTH_TOKEN = auth_value

    def _handle_cookies(self, page: Page) -> None:
        try:
            cookies_button = page.wait_for_selector("button[id='didomi-notice-agree-button']", timeout=5000)
            cookies_button.click()
        except TimeoutError:
            return

    def _authenticate(self, page: Page) -> bool:
        try:
            email_field = page.wait_for_selector("input[name='email']", timeout=7500)
            password_field = page.wait_for_selector("input[name='password']", timeout=7500)
            submit_button = page.wait_for_selector("button[type='submit']", timeout=7500)
        except TimeoutError:
            return False
        email_field.type(self.email)
        password_field.type(self.password)
        submit_button.click()
        page.wait_for_url(self._HOME_URL, wait_until="networkidle")
        return True

    def _get(self, url: str, **kwargs) -> dict[str, Any]:
        return self._request_wrapper('GET', url, **kwargs)

    def _post(self, url: str, **kwargs) -> dict[str, Any]:
        return self._request_wrapper('POST', url, **kwargs)

    def _patch(self, url: str, **kwargs) -> dict[str, Any]:
        return self._request_wrapper('PATCH', url, **kwargs)

    def _request_wrapper(self, method: str, url: str, **kwargs) -> dict[str, Any]:
        method_map = {'GET': self._session.get, 'POST': self._session.post, 'PATCH': self._session.patch}
        kwargs["headers"] = {"Authorization": f"{_HTTPManager._AUTH_TOKEN}"}

        try:
            res = method_map[method](url, **kwargs)
            return self._handle_response(method, res, url, **kwargs)
        except Exception as e:
            if self.proxy_manager.proxies and len(self.proxy_manager.proxies) > 0:
                self._session.proxies.update(self.proxy_manager.get_next_proxy())
            return {"success": 0, "msg": f"Proxy error: {e}"}

    def _get_details(self, endpoint: str, limit: int = 100, skip: int = 0) -> list[dict[str, Any]] | None:
        results = []
        separator = '&' if '?' in endpoint else '?'
        url = f"{self._API_BASE_URL}/{endpoint}{separator}skip={skip}&take={limit}"
        res_json = self._get(url)
        results.extend(res_json.get("results", []))
        skip += limit
        try:
            if res_json.get("pagination", {}).get("totalItems", -1) > skip:
                next_results = self._get_details(endpoint, limit, skip)
                if next_results:
                    results.extend(next_results)
        except TypeError:
            pass
        return results

    def _get_listings_details(self, limit: int = 100, skip: int = 0) -> list[dict[str, Any]] | None:
        listings = self._get_details("listings", limit, skip)
        return listings

    def _get_offers_details(self, limit: int = 100, skip: int = 0) -> list[dict[str, Any]] | None:
        offers = self._get_details("offers", limit, skip)
        return offers

    def _get_consignment_slots_details(self, limit: int = 100, skip: int = 0) -> list[dict[str, Any]] | None:
        consignments = self._get_details("consignment-slots", limit, skip)
        return consignments

    def _get_consignment_slots_details_by_sku(
        self, sku: str, limit: int = 100, skip: int = 0
    ) -> list[dict[str, Any]] | None:
        consignments = self._get_details(f"consignment-slots?keywordSearch={sku}", limit, skip)
        return consignments

    def _extend_offer_expiration_date(self, offer_id: str, days: int, apply_to_same_variants: bool) -> bool:
        payload = {"applyToSameVariants": apply_to_same_variants, "lifespan": days}
        return self._patch(f"{self._API_BASE_URL}/listings/{offer_id}", json=payload)

    def _process_offer(self, offer_id: str, variant_id: int, status: str) -> dict[str, Any]:
        payload = {"name": offer_id, "status": status, "variantId": variant_id}
        return self._post(f"{self._API_BASE_URL}/offers", json=payload)

    def _handle_response(self, method: str, res: Response, url: str, **kwargs) -> dict[str, Any] | bool:
        if res.status_code in {401, 403}:
            return self._handle_unauthorized(method, url, **kwargs)

        if res.status_code in {408, 429, 500, 502, 503, 504}:
            return self._handle_errors(res)

        return self._handle_success(method, res)

    def _handle_unauthorized(self, method: str, url: str, **kwargs) -> dict[str, Any]:
        _HTTPManager._AUTH_TOKEN = None
        if not self._login():
            return {"success": 0, "msg": "Could not authenticate."}
        return self._request_wrapper(method, url, **kwargs)

    def _handle_errors(self, res: Response) -> dict[str, int]:
        if self.proxy_manager.proxies and len(self.proxy_manager.proxies) > 0:
            self._session.proxies.update(self.proxy_manager.get_next_proxy())
            return {"success": 0, "msg": "Proxy error"}

        retry_after = res.headers.get("Retry-After", self._DEFAULT_RETRY_AFTER_SECONDS)
        return {"success": 0, "retry_after": retry_after}

    def _handle_success(self, method: str, res: Response) -> dict[str, Any]:
        success_map = {
            "GET": {200},
            "POST": {200, 201},
            "PATCH": {200},
        }

        if res.status_code in success_map[method.upper()]:
            json_res = {"success": 1}
            return json_res | res.json() if method.upper() == "GET" else json_res
        return {"success": 0, "msg": f"Unknown error on success - {res.status_code}"}
