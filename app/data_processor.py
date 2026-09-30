import json


def load_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def process_data(data):
    employees = data.get("employees", [])

    total_employees = len(employees)

    total_salary = sum(
        employee.get("salary", 0)
        for employee in employees
    )

    average_salary = (
        total_salary / total_employees
        if total_employees > 0
        else 0
    )

    departments = {}

    for employee in employees:
        department = employee.get("department", "Unknown")

        departments[department] = departments.get(
            department, 0
        ) + 1

    return {
        "total_employees": total_employees,
        "total_salary": total_salary,
        "average_salary": average_salary,
        "departments": departments,
        "employees": employees
    }
