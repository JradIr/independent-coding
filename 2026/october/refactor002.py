#Guided challenge for OJT preparation with senior developers
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def get_approved_employees(employee_list: list[dict]) -> list[str]:
    approved = []
    logging.info("checking employees...")

    for emp in employee_list:
        try:
            if emp["age"] >= 18:
                logging.info(f"{emp['name']} is approved.")
                approved.append(emp["name"])
            else:
                logging.info(f"{emp['name']} is denied.")
        except TypeError as e:
            logging.error(f"data format is not supported {emp['name']}: {e}")
    return approved

employees = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": "thirty"}, # Someone typed a string instead of an int!
    {"name": "Diana", "age": 40}
]

if __name__ == "__main__":
    approved_list = get_approved_employees(employees)
    logging.info(f"total approved is: {len(approved_list)}")