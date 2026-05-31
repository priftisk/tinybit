class BoundManager:
    def __init__(self, manager, owner):
        self.manager = manager
        self.owner = owner

    def get(self, id: int):
        print(f"Search {id} in {self.owner.__name__}")


class ObjectManager:
    def __get__(self, instance, owner):
        return BoundManager(self, owner)
