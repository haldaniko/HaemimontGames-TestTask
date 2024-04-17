import sys
import os
import create_report


def main() -> None:

    pins = sys.argv[1].split(',') if len(sys.argv) > 1 else None
    min_credit = float(sys.argv[2])
    start_date = sys.argv[3]
    end_date = sys.argv[4]
    output_format = sys.argv[5].lower() if len(sys.argv) > 5 else None
    directory_path = sys.argv[6]

    student_data = create_report.fetch_student_data_from_db(pins, min_credit, start_date, end_date)
    if output_format == "html":
        html_report = create_report.generate_html_report(student_data)
        file_path = f"{directory_path}/report.html"
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        with open(file_path, "w") as file:
            file.write(html_report)
    elif output_format == "csv":
        csv_data = create_report.generate_csv_report(student_data)
        file_path = f"{directory_path}/report.csv"
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        with open(file_path, "w", newline="") as csv_file:
            csv_file.write(csv_data)


if __name__ == "__main__":
    main()
