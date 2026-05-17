def update_stock(products: dict, delivery: dict) -> dict[str, int]:
    new_stock = products.copy()

    for key, value in delivery.items():
        new_stock[key] = new_stock.get(key, 0) + value

    return new_stock


def sorted_low_stock(products: dict) -> dict[str, int]:
    reserve = {
        key: value for key, value in products.items() if value < 40
    }

    sorted_reserve_stock = dict(sorted(reserve.items(), key=lambda item: item[1]))
    return sorted_reserve_stock


def write_off(products: dict, item: str, quantity: int) -> dict[str, int]:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    if item not in products:
        raise KeyError(f"Item '{item}' not found")
    if quantity > products[item]:
        raise ValueError("Quantity exceeds stock")

    written_off = products.copy()
    written_off[item] -= quantity

    if written_off[item] == 0:
        del written_off[item]

    return written_off

def main():
    stock = {
        "apple": 50,
        "banana": 30,
        "milk": 10,
        "bread": 25
    }

    deliver = {
        "banana": 20,
        "milk": 15,
        "eggs": 40,
        "bread": 10
    }

    print(f"Stock: {stock}")
    print(f"Delivery: {deliver}")

    stock_after_update = update_stock(stock, deliver)
    print(f"Stock after delivery: {stock_after_update}")

    low_stock = sorted_low_stock(stock_after_update)
    print(f"Low stock items:")
    for key, value in low_stock.items():
        print(f"{key}: {value}")

    while True:
        item = input("Enter item or 'stop' to stop: ")
        if item  == "stop":
            break

        try:
            quantity = int(input("Enter quantity: "))
            stock_after_update = write_off(stock_after_update, item, quantity)
            print(f"Success, current products list: {stock_after_update}")

        except ValueError as e:
            print(f"Error: {e}")
        except KeyError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()