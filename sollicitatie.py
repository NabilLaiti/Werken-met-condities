print("-------------------------------------------------------------------")
def main():
    if float(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? : ")) <= 4:
        if float(input("Hoeveel jaar heeft u met jongleren? : ")) <= 5:
            if float(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? : ")) <= 3:
                return False

    if input("Bent u in bezit van een MBO-4 Diploma ondernemen? (J/N) : ") == "N":
        return False
        
    if input("Bent u in bezit van een geldig vrachtwagen rijbewijs? (J/N) : ") == "N":
        return False

    if input("Bent u in bezit van een hoge hoed? (J/N) : ") == "N":
        return False

    if input("Bent u een man/vrouw? : ") == 'MAN':
        if float(input("Hoeveel cm breed is uw snor? : ")) <= 10:
            return False
    else:
        if input("Heeft u rood krullhaar? (J/N) : ") == "N":
            return False
        if float(input("Hoeveel cm lang zijn uw haren? : ")) <= 20:
             return False 

    if float(input("Hoeveel cm lang bent u? : ")) <= 150:
        return False

    if float(input("Hoeveel kg weegt u? : ")) <= 90:
        return False
    
    if input("Bent u in bezit van een Certificaat “Overleven met gevaarlijk personeel? (J/N) : ") == "N":
        return False

    if input("Bent u in bezit van een auto? (J/N) : ") == "N":
        return False

    if input("Kunt u tellen tot 10? (J/N) : ") == "N":
        return False
    
    if input("Heeft u ervaring met kinderen? (J/N) : ") == "N":
        return False

    if input("Heeft u ervaring met het aannemen van personeel? (J/N) : ") == "N":
        return False


    return True


      

if __name__ == "__main__":
    if main():
        print("U bent gekozen..")
    else:
        print("U voldoet niet aan de eisen voor de functie Circusdirecteur voor Circus HotelDeBotel, Het spijt ons !")
print("-------------------------------------------------------------------")
