# wethenew-client

## Overview

The wethenew-client is an unofficial Python wrapper for the API of the Wethenew sneaker platform. It facilitates interactions with the platform, allowing users to manage their sneaker listings and offers. This project is independent and is not officially associated with Wethenew.

## Installation

You can install the package using pip:

```python
pip install wethenew-client
```

## Functions

Below is a table of the functions available in the WethenewClient object, detailing whether user login is required.

| Function Name          | Description                                      | Login Required |
| ---------------------- | ------------------------------------------------ | -------------- |
| `get_current_listings` | Retrieves the current sneaker listings.          | Yes            |
| `get_current_offers`   | Fetches the current sneaker offers.              | Yes            |
| `extend_listings`      | Extends the expiration date of sneaker listings. | Yes            |
| `accept_offer`         | Accepts a specific offer.                        | Yes            |
| `reject_offer`         | Rejects a specific offer.                        | Yes            |

### Filters

When listing a product or retrieving current listings, you can specify filters to narrow down the results or to set the conditions of your listing. Below are the filter types and their possible values:

#### ListingDuration

This filter is used to specify the duration for which a product will be listed on the platform. The possible values are:

- `Days15`: List the product for 15 days.
- `Days30`: List the product for 30 days.
- `Days60`: List the product for 60 days.

## Usage Example

```python
from wethenew import WethenewClient, ListingDuration

# Initialize the WethenewClient with your credentials.
client = WethenewClient(
    email='your_email@example.com',
    password='your_password',
    proxies_file_name='path_to_proxies_file.txt'
)

# Retrieve current listings and print them.
listings = client.get_current_listings()
print(listings)

# Accept an offer.
client.accept_offer(offer_id='some_offer_id', variant_id=123)

# Extend a listing.
client.extend_listings(days=ListingDuration.DAYS60, apply_to_same_variants=True)
```

## Note

The use of proxies is recommended to avoid potential rate limits or blocks by the Wethenew API. You can specify proxies in a file, as shown in the example.
