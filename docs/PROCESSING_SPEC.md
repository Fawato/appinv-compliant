# appinv processing specification

## Inputs
CSV with a header row and columns `app_id`, `app_name`, `owner_email`, `criticality`.

## Validation
A row is rejected, with the reasons recorded, when:
- any of the four columns is blank;
- `app_id` does not match `APP-` followed by four digits;
- `owner_email` is not an email address;
- `criticality` is not one of `low`, `medium`, `high`, `critical` (case-insensitive).

## Processing
Accepted rows have surrounding whitespace trimmed, and `owner_email` and `criticality` lower-cased.

## Outputs
- Accepted records.
- Rejected rows, each with its CSV line number and the list of problems.
