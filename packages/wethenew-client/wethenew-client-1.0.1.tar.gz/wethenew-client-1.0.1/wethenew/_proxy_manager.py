from typing import Generator, Any


class ProxyManager:
    def __init__(self, filename: str) -> None:
        self.proxies = self.read_and_format_proxy(filename)
        self.proxy_generator = self.proxy_cycle()

    def proxy_cycle(self) -> Generator[dict[str, str], Any, None]:
        while True:
            for proxy in self.proxies:
                yield proxy

    def get_next_proxy(self) -> dict[str, str]:
        return next(self.proxy_generator)

    def read_proxies_from_file(self, filename: str) -> list[str]:
        with open(filename, "r", encoding="utf-8") as f:
            proxies = f.read().splitlines()
        return [proxy.split(":") for proxy in proxies]

    def format_proxy(self, proxy: list[str]) -> str:
        return f"{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}"

    def create_proxy_dict(self, formatted_proxy: str) -> dict[str, str]:
        return {"http": f"http://{formatted_proxy}", "https": f"http://{formatted_proxy}"}

    def read_and_format_proxy(self, filename: str) -> list[dict[str, str]]:
        proxies = self.read_proxies_from_file(filename)
        formatted_proxies = [self.format_proxy(proxy) for proxy in proxies]
        proxies_dict_format = [self.create_proxy_dict(proxy) for proxy in formatted_proxies]
        return proxies_dict_format
