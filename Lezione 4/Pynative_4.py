name = (input("Insert the name of the employee: "))

def show_employee(name: str, salary: float = 9000):

    print(f"Name:{name} Salary:{salary}")


show_employee(name)

show_employee("Jessa", 1200.59)