import json
import os
from typing import Dict, Any

DATA_FILE = "data.json"

def load_data() -> Dict[str, Any]:
    if not os.path.exists(DATA_FILE):
        return {
            "next_employee_id": 1,
            "next_department_id": 1,
            "employees": [],
            "departments": []
        }
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        print("Advertencia: no se pudo leer data.json. Se creará uno nuevo.")
        return {
            "next_employee_id": 1,
            "next_department_id": 1,
            "employees": [],
            "departments": []
        }

def save_data(data: Dict[str, Any]) -> None:
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
