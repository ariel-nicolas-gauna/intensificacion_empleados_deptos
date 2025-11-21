from typing import Dict, Any, Optional

def find_employee(data: Dict[str, Any], eid: int) -> Optional[Dict[str, Any]]:
    return next((e for e in data["employees"] if e["id"] == eid), None)

def find_department(data: Dict[str, Any], did: int) -> Optional[Dict[str, Any]]:
    return next((d for d in data["departments"] if d["id"] == did), None)

def find_department_by_code(data: Dict[str, Any], code: str) -> Optional[Dict[str, Any]]:
    return next((d for d in data["departments"] if d["codigo"] == code), None)
