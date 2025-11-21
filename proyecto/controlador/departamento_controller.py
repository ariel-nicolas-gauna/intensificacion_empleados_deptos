from modelo.data_manager import save_data
from modelo.repositories import find_department, find_department_by_code, find_employee
from typing import Dict, Any, Optional

def add_department(data: Dict[str, Any], codigo: str, nombre: str) -> bool:
    if find_department_by_code(data, codigo):
        return False
    did = data["next_department_id"]
    dept = {"id": did, "codigo": codigo, "nombre": nombre}
    data["departments"].append(dept)
    data["next_department_id"] += 1
    save_data(data)
    return True

def modify_department(data: Dict[str, Any], did: int, codigo: str, nombre: str) -> bool:
    d = find_department(data, did)
    if not d:
        return False
    if codigo != d["codigo"] and find_department_by_code(data, codigo):
        return False
    d.update({"codigo": codigo, "nombre": nombre})
    save_data(data)
    return True

def delete_department(data: Dict[str, Any], did: int) -> bool:
    d = find_department(data, did)
    if not d:
        return False
    data["departments"] = [dept for dept in data["departments"] if dept["id"] != did]
    for e in data["employees"]:
        if e.get("department_id") == did:
            e["department_id"] = None
    save_data(data)
    return True

def list_departments(data: Dict[str, Any]):
    return data["departments"]

def associate_employee_to_department(data: Dict[str, Any], eid: int, did: int) -> bool:
    e = find_employee(data, eid)
    d = find_department(data, did)
    if not e or not d:
        return False
    e["department_id"] = did
    save_data(data)
    return True

def get_department_info(data: Dict[str, Any], did: Optional[int] = None, code: Optional[str] = None):
    d = None
    if did is not None:
        d = find_department(data, did)
    elif code is not None:
        d = find_department_by_code(data, code)
    
    if not d:
        return None
        
    emps = [e for e in data["employees"] if e.get("department_id") == d["id"]]
    return d, emps
