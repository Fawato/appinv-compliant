from appinv.inventory import load


def test_load_splits_valid_and_invalid_rows(tmp_path):
    f = tmp_path / "inv.csv"
    f.write_text(
        "app_id,app_name,owner_email,criticality\n"
        "APP-0001,Payroll,a@b.com,High\n"
        "BAD,Ledger,x@y.com,low\n"
    )
    accepted, rejected = load(f)
    assert [r["app_id"] for r in accepted] == ["APP-0001"]
    assert accepted[0]["criticality"] == "high"
    assert rejected[0]["line"] == 3
