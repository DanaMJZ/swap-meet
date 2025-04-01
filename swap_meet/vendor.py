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
        return None         # Returns None if no match is found
    
    def swap_item(vendor, item1,item2):
        pass


    
    def swap_items(self, other_vendor, my_item, their_item): # test fatimah.swap_items(jolie, item_b, item_d) python automatically provide self.
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
    
        self.inventory.remove(my_item)
        other_vendor.inventory.remove(their_item)
    
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
    
        return True



    def swap_first_item(self,vendor): 
        #swaps first item of vendor arguement, with first item of inventory of the instance vendor calling the method
        
        inventory1 = vendor.inventory
        inventory2 = self.inventory

        if not inventory1 or not inventory2:
            return False
        
        helper = inventory1[0]
        inventory1[0] = inventory2[0]
        inventory2[0] = helper

        return inventory2