class Category:
    total = 0

    def __init__(self, name: str, id: int = None):
        self.id = id
        self.name = name
        Category.total += 1

    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"