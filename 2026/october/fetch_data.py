import requests
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s, %(message)s')

def fetch_users_from_api(url: str) -> list[dict]:
    logging.info(f"Fetching data url {url}")

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Successfully fetched {len(data)} users")
        return data
    except requests.exceptions.RequestException as e:
        logging.info(f"Fetch failed: {e}")
        logging.info("try again")
        return []

if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/users"
    users_data = fetch_users_from_api(API_URL)
    if users_data:
        first_user = users_data[0]
        name = first_user.get("name")
        email = first_user.get("email")

        logging.info(f"User: {name}, Email: {email}")
        logging.info("activity done")
