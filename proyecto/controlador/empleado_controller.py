from modelo.data_manager import save_data
from modelo.repositories import find_employee, find_department
from typing import Dict, Any

def add_employee(data: Dict[str, Any], nombre: str, dedicacion: str, categoria: str) -> None:
    eid = data["next_employee_id"]
    empleado = {
        "id": eid,
        "nombre": nombre,
        "dedicacion": dedicacion,
        "categoria": categoria,
        "department_id": None
    }
    data["employees"].append(empleado)
    data["next_employee_id"] += 1
    save_data(data)

def modify_employee(data: Dict[str, Any], eid: int, nombre: str, dedicacion: str, categoria: str) -> bool:
    e = find_employee(data, eid)
    if not e:
        return False
    e.update({"nombre": nombre, "dedicacion": dedicacion, "categoria": categoria})
    save_data(data)
    return True

def delete_employee(data: Dict[str, Any], eid: int) -> bool:
    e = find_employee(data, eid)
    if not e:
        return False
    data["employees"] = [emp for emp in data["employees"] if emp["id"] != eid]
    save_data(data)
    return True

def list_employees(data: Dict[str, Any]):
    return data["employees"]
