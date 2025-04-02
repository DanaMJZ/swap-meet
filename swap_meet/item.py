import uuid

class Item:

    def __init__(self, id=None, condition= 0):
        # self.id = id if id is not None else uuid.uuid4().int
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    

    def condition_description(self):
        if self.condition in range (0,1):
            return "horrible"
        elif self.condition in range (1,2):
            return "poor"
        elif self.condition in range (2,3):
            return "fair"
        elif self.condition in range (3,4):
            return "good"
        else:
            return "mint"
        