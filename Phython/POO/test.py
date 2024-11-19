class Tuber:
    def __init__(self, grow, habitat):
        self.grow = grow
        self.habitat = habitat

class Potato(Tuber):
    def __init__(self, grow, color, habitat, size, weight, clean, status, taste):
        super().__init__(grow, habitat)  # Corregir aquí: Eliminar color y weight de la llamada
        self.color = color
        self.size = size
        self.weight = weight  # Corregir aquí: Cambiar weigth a weight
        self.clean = clean 
        self.status = status
        self.taste = taste

class SweetPotato(Tuber):
    def __init__(self, grow, color, habitat, size, weight, clean, status, taste):
        super().__init__(grow, habitat)  # Corregir aquí: Eliminar color y weight de la llamada
        self.color = color
        self.size = size
        self.weight = weight  # Corregir aquí: Cambiar weigth a weight
        self.clean = clean 
        self.status = status
        self.taste = taste

class PotatoAndSweetPotatoStew(Potato, SweetPotato):
    def __init__(self, grow, color, habitat, size, weight, clean, status, taste, temperature, cooking):
        Potato.__init__(self, grow, color, habitat, size, weight, clean, status, taste)
        SweetPotato.__init__(self, grow, color, habitat, size, weight, clean, status, taste)
        self.temperature = temperature
        self.cooking = cooking

potato1 = Potato("underground", "brown", "frank", "15cm", "800g", False, "90%", "good")
sweetPotato1 = SweetPotato("underground", "purple", "frank", "25cm", "800g", True, "70%", "delicious")
stew = PotatoAndSweetPotatoStew("underground", "lite brown", "frank", "15cm", "900g", True, "90%", "good", "50ºc", "100%")

print(potato1.color)
print(sweetPotato1.grow)
print(stew.color)

