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

