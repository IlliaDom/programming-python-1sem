import json
from datetime import date

print("Oleksandr Romaniuk, IT-31")

order_dictionary = {
  "date": date(2026, 11, 10),
  "amount": 500,
  "table": 23,
  "meals": ["rice cereal", "soup"]
}

# first way

# def serialize_date(object):
#     if isinstance(object, date):
#         return object.isoformat()
    

# serialized = json.dumps(order_dictionary, default=serialize_date)
# print(serialized == order_dictionary)

# second way

def serialize_every_date(dictionary, restore=False):
    new_orders = {}
    
    for key, value in dictionary.items():
        if isinstance(value, date) and not restore:
            new_orders[key] = value.isoformat()
        elif isinstance(value, str) and restore:
            new_orders[key] = date.fromisoformat(value)
        else:
            new_orders[key] = value

    return new_orders
            

serialized_data = serialize_every_date(order_dictionary)

unserialized_data = serialize_every_date(serialized_data, True)

print(f"Is unserialized equal to originatal: {order_dictionary == unserialized_data}")