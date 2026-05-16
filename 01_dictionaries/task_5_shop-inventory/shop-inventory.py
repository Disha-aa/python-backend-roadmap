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


def main():
    print(f"Stock: {stock}")
    print(f"Delivery: {deliver}")

    stock_after_update = update_stock(stock, deliver)
    print(f"Stock after delivery: {stock_after_update}")

    low_stock = sorted_low_stock(stock_after_update)
    print(f"Low stock items:")
    for key, value in low_stock.items():
        print(f"{key}: {value}")

    written_off = stock_after_update.pop("apple")
    print(f"Written off: apple ({written_off} units)")

    print(f"Final stock: {stock_after_update}")


if __name__ == "__main__":
    main()