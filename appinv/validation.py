"""Input validation for application inventory records."""
import re

REQUIRED = ("app_id", "app_name", "owner_email", "criticality")
CRITICALITY = {"low", "medium", "high", "critical"}
APP_ID = re.compile(r"^APP-\d{4}$")
EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate(record):
    """Return a list of problems with the record; empty means it is valid."""
    problems = []
    for field in REQUIRED:
        if not str(record.get(field) or "").strip():
            problems.append(f"{field} is missing")
    if problems:
        return problems
    if not APP_ID.match(record["app_id"].strip()):
        problems.append("app_id must look like APP-1234")
    if not EMAIL.match(record["owner_email"].strip()):
        problems.append("owner_email is not a valid email address")
    if record["criticality"].strip().lower() not in CRITICALITY:
        problems.append("criticality must be one of " + ", ".join(sorted(CRITICALITY)))
    return problems
