# Report Generator
This script generates reports based on student data fetched from a database.

## Usage
To use the script, run it from the command line with the following syntax:

- `<PINs>`: Comma-separated list of student PINs.
- `<minimum_credit>`: Minimum credit required for the report.
- `<start_date>`: Start date of the date range for the report (format: YYYY-MM-DD).
- `<end_date>`: End date of the date range for the report (format: YYYY-MM-DD).
- `<output_format>`: Output format of the report (either "html" or "csv").
- `<directory_path>`: Path to the directory where the report file will be saved.

All arguments are mandatory. Note that if any argument is missing or incorrect, an error will occur. Unfortunately, due to time constraints, error handling and making certain elements optional were not implemented in this version of the script.

## Example
• python main.py 9412011005,9501011014,9507141009 50 2018-01-01 2024-04-01 csv new_derictory/another_one/my_dir
• python main.py 9412011005,9507141009 50 2015-01-01 2024-04-01 html beautiful/dir/in/dir

