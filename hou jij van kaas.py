if input("Is de kaas geel? (J/N) : ") == 'J':
    if input("zitten er gaten in? (J/N) : ") == 'J':
        if input("Is de kaas blechelijk duur? (J/N) : ") == 'J':
            print("Emmenthaler")
        else:
            print("Leerdammer")
    else: 
        if input("Is de kaas hard als steen? (J/N) : ") == 'J':
            print("Pamigiano Reggiano")
        else:
            print("Goudse Kaas")
else:
    if input ("Heeft de kaas blauwe schimmels? (J/N) : ") == 'J':
        if input ("Heeft de kaas een korst? (J/N) : ") == 'J':
            print("Blue de Rochbaron")
        else:
            print("Foume d'Ambert")
    else:
        if input ("Heeft de kaas een korst? (J/N) : ") == 'J':
            print("Camembert")
        else:
            print("Mozzerella")
