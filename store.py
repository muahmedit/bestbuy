from products import Product
from typing import List, Tuple


class Store:
    def __init__(self, product_list: List[Product] = None):
        if product_list is None:
            self.products = []
        else:
            self.products = list(product_list)

    def add_product(self, product: Product):
        if product not in self.products:
            self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_order_price = 0.0
        for product, quantity in shopping_list:
            total_order_price += product.buy(quantity)
        return total_order_price


# Test block to verify functionality
if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print("Total store quantity:", best_buy.get_total_quantity())
    print("Order cost:", best_buy.order([(products[0], 1), (products[1], 2)]))
    print("Total store quantity after order:", best_buy.get_total_quantity())