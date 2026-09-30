import time
from datetime import datetime
from app.data_processor import load_data, process_data
from app.report_generator import generate_report


def run_scheduler():

    print("Automation scheduler started.")

    while True:

        current_time = datetime.now()

        print(
            f"Checking schedule: "
            f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        try:
            data = load_data("data/sample_data.json")
            processed_data = process_data(data)

            generate_report(
                processed_data,
                "output/scheduled_report.pdf"
            )

            print("Scheduled report generated.")

        except Exception as error:
            print(f"Error: {error}")

        # Run every 60 seconds
        time.sleep(60)


if __name__ == "__main__":
    run_scheduler()
