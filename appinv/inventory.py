"""Load application inventory records, rejecting the invalid ones."""
import csv

from appinv.validation import validate


def load(path):
    """Return (accepted, rejected); rejected rows carry their problems."""
    accepted, rejected = [], []
    with open(path, newline="") as f:
        for line, row in enumerate(csv.DictReader(f), start=2):
            problems = validate(row)
            if problems:
                rejected.append({"line": line, "row": row, "problems": problems})
            else:
                accepted.append(normalise(row))
    return accepted, rejected


def normalise(row):
    return {
        "app_id": row["app_id"].strip(),
        "app_name": row["app_name"].strip(),
        "owner_email": row["owner_email"].strip().lower(),
        "criticality": row["criticality"].strip().lower(),
    }
