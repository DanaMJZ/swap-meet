class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self,item):
        inventory = self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            inventory = self.inventory.remove(item)
            return item
        return False
    
    def get_by_id(self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None  # Return None if no match is found