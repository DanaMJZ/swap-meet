class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

