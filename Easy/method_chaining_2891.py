import pandas as pd

def findHeavyAnimals(animals):
    df = pd.DataFrame(animals.sort_values("weight", ascending = False).query("weight > 100").name)
    return df

def main():
    hmap = {
        "name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Alex"],
        "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"], 
        "age":[98, 50, 6, 45, 100, 26],
        "weight": [464, 41, 328, 463, 50, 349]
    }
    animals = pd.DataFrame(hmap)
    print(animals)
    print(findHeavyAnimals(animals))

main()
