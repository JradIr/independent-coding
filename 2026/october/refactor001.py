import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

TAX_RATE = 0.10

def calculate_order_total(price: float, qty: int) -> float:
    subtotal = price * qty
    final_total = subtotal + (subtotal * TAX_RATE)
    return final_total

def process_orders(order_list: list[dict]) -> list[dict]:
    processed = []
    logging.info("Starting order processing job.")

    for o in order_list:
        logging.info(f"Processing order {o['id']}")

        try:
            final = calculate_order_total(o['price'], o['qty'])
            if final > 0:
                logging.info(f"success for order {o['id']} - total: {final}")
                processed.append({'id': o['id'], 'total': final})
            else:
                logging.warning(f"bad price for order {o['id']}. total was {final}")
        except TypeError as e:
            logging.error(f"Data type error on order {o['id']}: {e}")
    return processed

orders = [
    {"id": 1, "item": "Laptop", "price": 1200.00, "qty": 2},
    {"id": 2, "item": "Mouse", "price": 25.50, "qty": "one"}, 
    {"id": 3, "item": "Keyboard", "price": 100.00, "qty": 1},
    {"id": 4, "item": "Monitor", "price": -300.00, "qty": 1} 
]

if __name__ == "__main__":
    final_results = process_orders(orders)
    logging.info(f"Job done. Processed successfully: {len(final_results)}")