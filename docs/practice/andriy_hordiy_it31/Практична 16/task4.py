from pathlib import Path
from datetime import date
task4_path = Path(__file__).resolve().parent/"data"/"task4.json"
task4_dict = {
    "date": date(2026,9, 11),
    "category": "Food",
    "amount":150.00,
    "comment":"Обід"}
def dateiso(date):
    return date.isoformat()
