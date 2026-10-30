# appinv

Loads the application inventory CSV and rejects invalid records.
See [docs/PROCESSING_SPEC.md](docs/PROCESSING_SPEC.md) for what it accepts and produces.

Changes go through pull requests; CI runs unit and input-validation tests;
merges to `main` deploy to the `production` environment after reviewer approval.
