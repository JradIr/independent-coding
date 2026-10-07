def calculate_total(cart_total: float, is_admin: bool, discount_code: str) -> dict:
    final_price = cart_total
    message = "initial message"

    if is_admin:
        final_price = final_price * 2
        message = "this is multiplied by 2" 
    elif discount_code == "discount":
        final_price = final_price * 3
        message = "this is multiplied by 3"
    return {"total": final_price, "message": message}


result = calculate_total(150.50, True, "NONE")
print(result)