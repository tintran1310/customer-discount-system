# def calculate_discount(total_amount):
#     if total_amount >= 50000000:
#         return 0.1
#     else:
#         return 0
def calculate_discount(total_purchase, customer_type):
    total_value = total_purchase + customer_type
    if total_value >= 50000000:
        return 0.1
    return 0