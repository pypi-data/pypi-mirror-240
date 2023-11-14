from wethenew._http_manager import _HTTPManager
from typing import Any
from wethenew._helpers import date_expiry_difference
from wethenew.models import ListingDuration


class WethenewClient(_HTTPManager):
    def __init__(self, email: str, password: str, proxies_file_name: str) -> None:
        super().__init__(email, password, proxies_file_name)

    def get_current_listings(self) -> list[dict[str, Any]] | None:
        """
        Retrieves the current available listings.

        Returns a list of dictionaries, each containing details of a listing, or None if no listings are available.
        """
        return self._get_listings_details()

    def get_current_offers(self) -> list[dict[str, Any]] | None:
        """
        Retrieves the current available offers.

        Returns a list of dictionaries, each representing an offer, or None if no offers are available.
        """
        return self._get_offers_details()

    def extend_listings(
        self, days: ListingDuration = ListingDuration.DAYS30, apply_to_same_variants: bool = True
    ) -> None:
        """
        Extends the expiration date of eligible listings. It will extend listings that are expiring within 7 days.

        days: An instance of ListingDuration indicating the number of days to extend the listings. Defaults to ListingDuration.DAYS30.
        apply_to_same_variants: A boolean flag indicating whether the extension should apply to listings of the same variants. Defaults to True.
        """
        listings = self._get_listings_details()
        if not listings:
            return

        self._extend_eligible_listings(listings, days, apply_to_same_variants)

    def accept_offer(self, offer_id: str, variant_id: int) -> dict[str, Any]:
        """
        The `accept_offer` function accepts an offer by processing it with the given offer ID, variant ID,
        and status.

        :return: A dictionary with status(0 - failed, 1 - success) and msg(if any)
        """
        return self._process_offer(offer_id, variant_id, "ACCEPTED")

    def reject_offer(self, offer_id: str, variant_id: int) -> dict[str, Any]:
        """
        The `reject_offer` function rejects an offer by processing it with the given offer ID, variant ID,
        and status.

        :return: A dictionary with status(0 - failed, 1 - success) and msg(if any)
        """
        return self._process_offer(offer_id, variant_id, "REFUSED_PRICE_DISAGREEMENT")

    def _extend_eligible_listings(
        self, listings: list[dict[str, Any]], days: ListingDuration, apply_to_same_variants: bool
    ) -> None:
        filtered_listings = [
            listing
            for listing in listings
            if listing["isExpiringSoon"] or date_expiry_difference(listing["expirationDate"]) <= 7
        ]

        if not filtered_listings:
            return

        for listing in filtered_listings:
            self._extend_offer_expiration_date(listing["name"], days.value, apply_to_same_variants)
