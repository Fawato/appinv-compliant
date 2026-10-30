import pytest

from appinv.validation import validate

GOOD = {"app_id": "APP-0001", "app_name": "Payroll", "owner_email": "a@b.com", "criticality": "high"}


def test_valid_record_is_accepted():
    assert validate(GOOD) == []


@pytest.mark.parametrize("field", ["app_id", "app_name", "owner_email", "criticality"])
def test_missing_required_field_is_rejected(field):
    assert validate({**GOOD, field: ""}) == [f"{field} is missing"]


@pytest.mark.parametrize("field,value", [
    ("app_id", "1234"),
    ("owner_email", "not-an-email"),
    ("criticality", "urgent"),
])
def test_malformed_field_is_rejected(field, value):
    assert validate({**GOOD, field: value})
