import json
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def load_users(filepath: str) -> list[dict]:
    """Reads users from a JSON file."""
    try:
        # TODO: Open the file in read mode and return the loaded JSON data
        with open(filepath, "r") as file:
            loaded_data = json.load(file)
            logging.info(loaded_data)
        return loaded_data
    except FileNotFoundError:
        logging.error(f"Could not find file: {filepath}")
        return []

def save_users(filepath: str, data: list[dict]) -> None:
    """Saves a list of dictionaries to a JSON file."""
    # TODO: Open the file in write mode and dump the data with an indent of 4
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

def process_users(user_list: list[dict]) -> list[dict]:
    """Filters out users missing an email address."""
    valid_users = []
    
    for u in user_list:
        try:
            # TODO: Extract the email to trigger a KeyError if it is missing
            email = u["email"]
            valid_users.append(u)
            # TODO: If successful, append the entire user dictionary 'u' to valid_users
            pass
        except KeyError as e:
            logging.error(f"Skipping user {u.get('name', 'Unknown')} - missing {e}")
            
    return valid_users

if __name__ == "__main__":
    # 1. Load the raw data
    raw_data = load_users("raw_users.json")
    
    if raw_data:
        # 2. Process it
        clean_data = process_users(raw_data)
        
        # 3. Save the results
        save_users("valid_users.json", clean_data)
        logging.info(f"Job complete. Saved {len(clean_data)} valid users.")