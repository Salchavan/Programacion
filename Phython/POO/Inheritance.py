class Tuber:
    def __init__(self, grow, color, habitat):
        self.grow = grow
        self.habitat = habitat

class Potato(Tuber):
    def __init__(self, grow, color, habitat, size, weight, clean, status, taste):
        super().__init__(grow, color, habitat)
        self.size = size
        self.weight = weight
        self.clean = clean 
        self.status = status
        self.taste = taste
        
class SweetPotato(Tuber):
    def __init__(self, size, weight, clean, status, taste):
        super().__init__(grow, color, habitat)
        self.size = size
        self.weight = weight
        self.clean = clean 
        self.status = status
        self.taste = taste

potato1 = Potato("underground", "brown", "frank", "15cm", "800g", "False", "90%", "good")
sweetPotato1 = SweetPotato("underground", "purple", "frank", "25cm", "800g", "True", "70%", "goodly")

print(potato1.color)