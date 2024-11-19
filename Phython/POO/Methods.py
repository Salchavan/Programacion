class potato:
    def __init__(self, size, weight, taste):
        self.size = size
        self.weight = weight
        self.taste = taste

    def clean(self):
        print(f"You clean the potato")

potato1 = potato("10cm", "800g", "good")

potato1.clean()
