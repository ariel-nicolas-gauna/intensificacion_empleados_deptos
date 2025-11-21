from vista.empleado_view import empleado_menu
from vista.departamento_view import departamento_menu
from modelo.data_manager import load_data

def main_menu():
    data = load_data()
    while True:
        print("===============================================")
        print("ABM Empleados y Departamentos")
        print("1) Empleados")
        print("2) Departamentos")
        print("0) Salir")
        print("===============================================")
        op = input("Opción: ").strip()

        if op == "1":
            empleado_menu(data)
        elif op == "2":
            departamento_menu(data)
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
