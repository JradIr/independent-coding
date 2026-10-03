import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s, %(message)s')

user_list = [
    {"id": 1, "name": "Alice", "email": "alice@company.com", "phone": "555-0101"},
    {"id": 2, "name": "Bob", "email": "bob@company.com"}, # Missing optional phone
    {"id": 3, "name": "Charlie", "phone": "555-0202"},
    {"id": 4, "name": "Raven", "email": "delarosa@gmail.com"} # Missing mandatory email
]


def register_users(user_list: list[dict]) -> list[int]:
    registered_users = []
    logging.info("Processing the users...")
    for u in user_list:
        try:
            phone = u.get("phone", "no phone provided")
            email = u["email"]
            registered_users.append(u["id"])            
        except KeyError as e:
            logging.error(f"There is a keyerror: {e}")
        
    
    return registered_users


if __name__ == "__main__":
    logging.info(register_users(user_list))
    logging.info(f"This is the main")
