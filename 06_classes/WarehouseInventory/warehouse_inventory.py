class Product:
    def __init__(self, sku: str, name: str, price: float, quantity: int):
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        return self.price * self.quantity


class Warehouse:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.products = []

    def load_products(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                try:
                    sku, name, price, quantity = clean_line.split(",")
                    self.products.append(
                        Product(sku, name, float(price), int(quantity))
                    )
                except ValueError:
                    continue

    def get_low_stock_items(self, threshold: int) -> list[Product]:
        low_stock = []
        for product in self.products:
            if product.quantity < threshold:
                low_stock.append(product)
        return low_stock

    def get_total_warehouse_value(self) -> float:
        total_sum = 0.0
        for product in self.products:
            total_sum += product.get_total_value()
        return total_sum


def main():
    path_file = "inventory.txt"

    warehouse = Warehouse(path_file)
    warehouse.load_products()

    low_stock = warehouse.get_low_stock_items(5)
    total_value = warehouse.get_total_warehouse_value()

    print("Product with a critical balance:")
    for product in low_stock:
        money = product.get_total_value()
        print(
            f"Product: {product.name} | Remaining: {product.quantity} | Product's total value: {money}"
        )
    print(f"Total warehouse value: {total_value}")


if __name__ == "__main__":
    main()
