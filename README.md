# Premier League Performance Lab

A football data analysis project, currently focused on inspecting
OpenFootball's English Premier League 2024/25 dataset.

## Current functionality

- Loads a versioned JSON dataset containing 380 match records.
- Checks score availability, structure and goal values.
- Reports missing half-time scores in 16 records.

## Run the inspection

Requires Python 3. Tested with Python 3.14.7.
No third-party packages are required.

From the repository root:

```bash
python scripts/inspect_source.py
```

## Data source

Data provided by OpenFootball and its contributors under CC0 1.0 Universal.
See [Data sources](docs/SOURCES.md) for the source version, download URL
and SHA256 checksum.

This project is independent and is not officially affiliated with the
Premier League, its clubs or OpenFootball.

The data license does not determine the license of this project's code.