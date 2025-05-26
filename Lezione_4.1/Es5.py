inventory: list = []

def add_item (code: str, name: str, quantity: int, price: float ) -> dict:

    item: dict = {}

    if item not in inventory:

        for i in range(4):
            
            item["Code"] = code
            item["Name"] = name
            item["Quantity"] = quantity
            item["Price"] = price
        
        inventory.append(item)


def remove_item(item):

    if item in inventory:

        inventory.remove(item)




add_item("ABC", "Salmone", 50, 19.99)
add_item("DFG", "Bistecca", 40, 20.99)
remove_item("DFG")
print(inventory)