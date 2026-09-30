import unittest
from app.data_processor import process_data


class TestDataProcessor(unittest.TestCase):

    def test_employee_count(self):

        data = {
            "employees": [
                {
                    "id": 1,
                    "name": "Test User",
                    "department": "IT",
                    "salary": 50000
                }
            ]
        }

        result = process_data(data)

        self.assertEqual(
            result["total_employees"],
            1
        )

        self.assertEqual(
            result["total_salary"],
            50000
        )


if __name__ == "__main__":
    unittest.main()
