class Pokemon:
    def __init__(self,name,type,id,categorie,height,weight,color):
        self.name = name
        self.type = type
        self.id = id
        self.categorie = categorie
        self.height = height
        self.weight = weight
        self.color = color
    
    def __str__(self):
        return self.name

#Registrate a new Pokemon

def registration():
    name1 = input("Name: ")
    type1 = input("Type: ")
    while True:
        id1 = input("Id: ")
        try: 
            id1= int(id1)
            break
        except:
            print("Valid input please.")
    categorie1 = input("Categorie: ")
    while True:
        height1 = input("Height: ")
        try:
            height1 = float(height1)
            break
        except:
            print("Valid input please.")
    while True:
        weight1 = input("Weight: ")
        try:
            weight1 = float(weight1)
            break
        except:
            print("Valid input please.")
    color1 = input("Color: ")
    name1 = Pokemon(name1,type1,id1,categorie1,height1,weight1,color1)
    print(f"Registration of {name1} completed!")
    return name1

def main():
    while True:
        registration()
        while True:
            another_one = input("Do you want to registrate another one ? (y or n)")
            try:
                if another_one == "n" or another_one == "y":
                    break
            except:
                print("y or n")
        if another_one == "n":
            break

main()
