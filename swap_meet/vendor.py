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
    
    def swap_items(self, other_vendor, my_item, their_item): # test fatimah.swap_items(jolie, item_b, item_d) python automatically provide self.
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
    
        self.inventory.remove(my_item)
        other_vendor.inventory.remove(their_item)
    
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
    
        return True