
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
    

    def get_by_category(self, category):
        # create empty list called result list
        # we need to loop over inventory items, 
        # at each iteration we call get_category function subclasses
        # compare input category with item category.
        # if same categories add to result list.

        result_list = []
        for item in self.inventory:      # assuming inventory is part of the other 4 classes
            item_category = item.get_category()  # get_category() is a ref to other classes [composition]
            if item_category == category:
                result_list.append(item)
        return result_list
    

    def get_best_by_category(self, category):
        best_item = None
        highest_condition = 0  # Start with a very low condition

        for item in self.inventory:
            if item.get_category() == category and item.condition >= highest_condition:
                best_item = item
                highest_condition = item.condition  

        return best_item
    
    def swap_best_by_category(self, other_vendor,my_priority, their_priority):
        
        
        my_best = self.get_best_by_category(their_priority) # what Iam giving
        their_best = other_vendor.get_best_by_category(my_priority)  # what iam getting

        if my_best not in self.inventory or their_best not in other_vendor.inventory:
            return False
    
        self.inventory.remove(my_best)
        other_vendor.inventory.remove(their_best)
    
        self.inventory.append(their_best)
        other_vendor.inventory.append(my_best)
    
        return True
        