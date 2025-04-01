from swap_meet.item import item

class Clothing:
    def __init__(self, id=None, fabric="Unknown"):
        super().__init__(id)
        self.id = id if id is not None else uuid.uuid4().int    
        self.fabric = fabric
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}.\n It is made from {self.fabric} fabric."
    pass