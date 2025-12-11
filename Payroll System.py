import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create employee table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    basic_pay REAL NOT NULL,
    deductions REAL NOT NULL
)
''')

# Function to add employee
def add_employee():
    name = input("Enter employee name: ")
    basic_pay = float(input("Enter basic pay: "))
    deductions = float(input("Enter deductions: "))
    cursor.execute("INSERT INTO employee (name, basic_pay, deductions) VALUES (?, ?, ?)", 
                   (name, basic_pay, deductions))
    conn.commit()
    print("Employee added successfully!")

# Function to view all employees
def view_employees():
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    print("\nID | Name | Basic Pay | Deductions | Net Pay")
    print("-"*40)
    for emp in employees:
        net_pay = emp[2] - emp[3]
        print(f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]} | {net_pay}")

# Function to update employee
def update_employee():
    emp_id = int(input("Enter employee ID to update: "))
    cursor.execute("SELECT * FROM employee WHERE id=?", (emp_id,))
    emp = cursor.fetchone()
    if emp:
        name = input(f"Enter name [{emp[1]}]: ") or emp[1]
        basic_pay = input(f"Enter basic pay [{emp[2]}]: ") or emp[2]
        deductions = input(f"Enter deductions [{emp[3]}]: ") or emp[3]
        cursor.execute("UPDATE employee SET name=?, basic_pay=?, deductions=? WHERE id=?", 
                       (name, float(basic_pay), float(deductions), emp_id))
        conn.commit()
        print("Employee updated successfully!")
    else:
        print("Employee not found!")

# Function to delete employee
def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    cursor.execute("DELETE FROM employee WHERE id=?", (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")

# Menu
def menu():
    while True:
        print("\n--- Employee Payroll System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    menu()
    conn.close()
