import csv

import os

folder = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(folder, "employees.csv")
output_file = os.path.join(folder, "payroll_summary.csv")

total_payroll = 0

try:
    with open(input_file, "r", newline="") as file:

        reader = csv.DictReader(file)

        required_columns = {"employee_id", "name", "basic_salary"}

        if not required_columns.issubset(reader.fieldnames or []):
            raise ValueError("CSV file has missing column headings.")

        employees = list(reader)

    if len(employees) == 0:
        print("No employee records found.")

    else:
        with open(output_file, "w", newline="") as file:

            fieldnames = [
                "Employee ID",
                "Name",
                "Basic Salary",
                "HRA",
                "DA",
                "Gross Salary",
                "PF",
                "Tax",
                "Total Deductions",
                "Net Salary"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            print("\n===== EMPLOYEE PAYROLL SUMMARY =====")

            for employee in employees:

                try:
                    employee_id = employee["employee_id"]
                    name = employee["name"]
                    basic = float(employee["basic_salary"])

                    if not employee_id or not name:
                        raise ValueError("Missing employee details.")

                    if basic < 0:
                        raise ValueError("Salary cannot be negative.")

                    hra = basic * 0.20
                    da = basic * 0.10

                    gross = basic + hra + da

                    pf = basic * 0.12
                    tax = gross * 0.05

                    deductions = pf + tax
                    net_salary = gross - deductions

                    total_payroll += net_salary

                    writer.writerow({
                        "Employee ID": employee_id,
                        "Name": name,
                        "Basic Salary": round(basic, 2),
                        "HRA": round(hra, 2),
                        "DA": round(da, 2),
                        "Gross Salary": round(gross, 2),
                        "PF": round(pf, 2),
                        "Tax": round(tax, 2),
                        "Total Deductions": round(deductions, 2),
                        "Net Salary": round(net_salary, 2)
                    })

                    print("\nEmployee ID:", employee_id)
                    print("Name:", name)
                    print("Basic Salary: Rs.", basic)
                    print("Gross Salary: Rs.", round(gross, 2))
                    print("Total Deductions: Rs.", round(deductions, 2))
                    print("Net Salary: Rs.", round(net_salary, 2))

                except (ValueError, TypeError) as e:
                    print("Invalid employee record:", e)

        print("\nTotal Net Payroll: Rs.", round(total_payroll, 2))
        print("Payroll summary saved to", output_file)

except FileNotFoundError:
    print("Error: Employee CSV file not found.")

except PermissionError:
    print("Error: Permission denied.")

except (csv.Error, OSError, ValueError) as e:
    print("Error:", e)
