from controlador.departamento_controller import (
    add_department, modify_department, delete_department,
    list_departments, associate_employee_to_department,
    get_department_info
)

def departamento_menu(data):
    while True:
        print("\n--- Menú Departamentos ---")
        print("1) Agregar")
        print("2) Modificar")
        print("3) Eliminar")
        print("4) Listar")
        print("5) Asociar empleado")
        print("6) Ver info")
        print("0) Volver")
        op = input("Opción: ").strip()

        if op == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            if add_department(data, codigo, nombre):
                print("Departamento agregado.")
            else:
                print("Código ya existente.")

        elif op == "2":
            try:
                did = int(input("ID: "))
            except:
                print("ID inválido.")
                continue
            codigo = input("Nuevo código: ")
            nombre = input("Nuevo nombre: ")
            if modify_department(data, did, codigo, nombre):
                print("Modificado.")
            else:
                print("Error al modificar.")

        elif op == "3":
            try:
                did = int(input("ID: "))
            except:
                print("ID inválido.")
                continue
            if delete_department(data, did):
                print("Eliminado.")
            else:
                print("No existe.")

        elif op == "4":
            deps = list_departments(data)
            print("\n--- Departamentos ---")
            for d in deps:
                print(f"ID {d['id']} | {d['codigo']} | {d['nombre']}")

        elif op == "5":
            try:
                eid = int(input("ID empleado: "))
                did = int(input("ID depto: "))
            except:
                print("ID inválido.")
                continue
            if associate_employee_to_department(data, eid, did):
                print("Asociado.")
            else:
                print("Error.")

        elif op == "6":
            modo = input("Buscar por (1)ID o (2)Código: ")
            d = None
            if modo == "1":
                try:
                    did = int(input("ID: "))
                    d = get_department_info(data, did=did)
                except:
                    print("ID inválido.")
                    continue
            else:
                code = input("Código: ")
                d = get_department_info(data, code=code)

            if not d:
                print("No encontrado.")
                continue

            dept, emps = d
            print(f"\nID {dept['id']} | {dept['codigo']} | {dept['nombre']}")
            if not emps:
                print("Sin empleados.")
            else:
                print("Empleados:")
                for e in emps:
                    print(f"{e['id']} - {e['nombre']}")

        elif op == "0":
            break
