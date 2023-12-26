#declaring the cat class to hold cal details
class cat :
    def __init__(self, name="", color="") :
        self.name=name
        self.color=color

    def __str__(self) :
        return self.name+", Color : "+self.color

    def meows(self):
        return "Meooooooooooow!"

    name=""
    color=""

kit=cat("Kit", "Black")
kat=cat("Kat", "White")

print(kit)
print(kat)
print(kit.meows())
print(kat.meows())
