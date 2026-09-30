import argparse
from app.data_processor import load_data, process_data
from app.report_generator import generate_report


def main():
    parser = argparse.ArgumentParser(
        description="Enterprise Python Automation - PDF Report Generator"
    )

    parser.add_argument(
        "--input",
        default="data/sample_data.json",
        help="Input JSON file"
    )

    parser.add_argument(
        "--output",
        default="output/report.pdf",
        help="Output PDF file"
    )

    args = parser.parse_args()

    print("====================================")
    print(" Enterprise Python Automation")
    print(" Automated PDF Report Generator")
    print("====================================")

    print("\n[1] Loading data...")
    data = load_data(args.input)

    print("[2] Processing data...")
    report_data = process_data(data)

    print("[3] Generating PDF report...")
    generate_report(report_data, args.output)

    print("\nReport generated successfully!")
    print(f"File: {args.output}")


if __name__ == "__main__":
    main()
