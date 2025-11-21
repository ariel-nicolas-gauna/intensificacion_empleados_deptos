from controlador.empleado_controller import (
    add_employee, modify_employee, delete_employee, list_employees
)
from modelo.repositories import find_employee, find_department
from controlador.departamento_controller import associate_employee_to_department

def empleado_menu(data):
    while True:
        print("\n--- Menú Empleados ---")
        print("1) Agregar")
        print("2) Modificar")
        print("3) Eliminar")
        print("4) Listar")
        print("0) Volver")
        op = input("Opción: ").strip()

        if op == "1":
            nombre = input("Nombre: ")
            dedicacion = input("Dedicación: ")
            categoria = input("Categoría: ")
            add_employee(data, nombre, dedicacion, categoria)
            print("Empleado agregado.\n")

        elif op == "2":
            try:
                eid = int(input("ID del empleado: "))
            except:
                print("ID inválido.")
                continue
            e = find_employee(data, eid)
            if not e:
                print("No encontrado.")
                continue
            nombre = input(f"Nombre [{e['nombre']}]: ") or e["nombre"]
            dedicacion = input(f"Dedicación [{e['dedicacion']}]: ") or e["dedicacion"]
            categoria = input(f"Categoría [{e['categoria']}]: ") or e["categoria"]
            modify_employee(data, eid, nombre, dedicacion, categoria)
            print("Modificado.\n")

        elif op == "3":
            try:
                eid = int(input("ID del empleado: "))
            except:
                print("ID inválido.")
                continue
            if delete_employee(data, eid):
                print("Eliminado.\n")
            else:
                print("No encontrado.\n")

        elif op == "4":
            emps = list_employees(data)
            print("\n--- Empleados ---")
            for e in emps:
                dept = find_department(data, e.get("department_id"))
                dept_str = dept["nombre"] if dept else "Sin departamento"
                print(f"ID: {e['id']} | {e['nombre']} | {dept_str}")

        elif op == "0":
            break
