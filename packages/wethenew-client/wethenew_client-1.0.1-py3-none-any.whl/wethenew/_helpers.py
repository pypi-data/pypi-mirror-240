from datetime import datetime, timezone


def date_expiry_difference(date: str) -> int:
    current_datetime = datetime.now(timezone.utc)
    given_datetime_naive = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    given_datetime = given_datetime_naive.replace(tzinfo=timezone.utc)

    difference = given_datetime - current_datetime
    days_difference = difference.days

    return days_difference


