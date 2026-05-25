print("\n 1. Добавление продуктов")

from pymongo import MongoClient

class Products:
    """A class for working with a collection of items in MongoDB."""

    def __init__(self, collection) -> None:
        """
        Args:
            collection: MongoDB collection.
        """
        self.collection = collection

    def clear(self) -> None:
        """Clears all documents in the collection."""
        self.collection.delete_many({})

    def add_products(self, products: list[dict]) -> None:
        """
        Adds a list of products to the collection.

        Args:
            products: a list of dictionaries containing product data.
        """
        self.collection.insert_many(products)

    def count(self) -> int:
        """Returns the number of documents in the collection."""
        return self.collection.count_documents({})


def main() -> None:
    """Connects to MongoDB and adds products to the collection."""
    client = MongoClient(
        "mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/"
        "?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
    )
    db = client["ich_edit"]
    collection = db["products_121225ptm_OlegV"]

    products_data = [
        {"name": "Apple", "price": 1.99, "stock": 100},
        {"name": "Banana", "price": 0.99, "stock": 150},
        {"name": "Orange", "price": 2.49, "stock": 80}
    ]

    products = Products(collection)
    products.clear()
    products.add_products(products_data)
    print(f"{products.count()} products inserted.")

if __name__ == '__main__':
    main()



print("\n 2. Увеличение цен")

from pymongo import MongoClient

class Products:
    """A class for working with a collection of items in MongoDB."""

    def __init__(self, collection) -> None:
        """
        Args:
            collection: MongoDB collection.
        """
        self.collection = collection

    def clear(self) -> None:
        """Clears all documents in the collection."""
        self.collection.delete_many({})

    def add_products(self, products: list[dict]) -> None:
        """
        Adds a list of products to a collection.

        Args:
            products: a list of dictionaries containing product data.
        """
        self.collection.insert_many(products)

    def count(self) -> int:
        """Returns the number of documents in the collection."""
        return self.collection.count_documents({})

    def update_prices(self, multiplier: float) -> int:
        """
        Increases the prices of all items by the specified multiplier.

        Args:
            multiplier: price multiplier, e.g. 1.2 = +20%.

        Returns:
            The number of updated documents.
        """
        result = self.collection.update_many({}, {"$mul": {"price": multiplier}})
        return result.modified_count

    def get_all(self) -> list[dict]:
        """Returns all items from the collection."""
        return list(self.collection.find({}))


def format_products(products: list[dict]) -> str:
    """Formats the list of products into a single line."""
    return "\n".join(
        f"- {p['name']} — ${p['price']:.2f}"
        for p in products
    )

def main() -> None:
    """"Connects to MongoDB, updates prices and displays products."""
    client = MongoClient(
        "mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/"
        "?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
    )
    db = client["ich_edit"]
    collection = db["products_121225ptm_OlegV"]

    products_data = [
        {"name": "Pen", "price": 1.50, "stock": 100},
        {"name": "Notebook", "price": 3.99, "stock": 50},
        {"name": "Backpack", "price": 25.00, "stock": 20}
    ]

    products = Products(collection)
    products.clear()
    products.add_products(products_data)

    updated_count = products.update_prices(1.2)
    print(f"Prices updated for {updated_count} products.\n")
    print("Updated products:")
    print(format_products(products.get_all()))

if __name__ == '__main__':
    main()