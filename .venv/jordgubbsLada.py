from Lib.ketlib import try_int, try_string

# Prissättning baserat på antal askar användaren vill köpa
pricing = {
    (1, 5): 30,
    (6, 10): 25,
    (11, float('inf')): 20
}

# En funktion för att göra beräkningen lite smidigare och slippa använda nästlade if-satser
def calculate_price(boxes: int) -> int:
    if boxes <= 5:
        return boxes * pricing[(1, 5)]
    elif boxes <= 10:
        return 5 * pricing[(1, 5)] + (boxes - 5) * pricing[(6, 10)]
    else:
        return 5 * pricing[(1, 5)] + 5 * pricing[(6, 10)] + (boxes - 10) * pricing[(11, float('inf'))]

# Sätter själva programmet i en funktion för att kunna köra det om och om igen
def strawberry_box():
    while True:
        # Skriv ut en lättläst prislista
        print("\n.:* Välkommen till JordgubbsLådan 0.1 *:.\n"
              "|\tPriser:\t\t\t\t\t\t\t\t|\n"
              "|\tAsk 1-5:\t\t\t30 kr\t\t\t|\n"
              "|\tAsk 6-10:\t\t\t25 kr\t\t\t|\n"
              "|\tAsk 11+:\t\t\t20 kr\t\t\t|\n"
              "-----------------------------------------")

        # Kolla hur många askar användaren vill köpa och slänger in en try för att se till att det inte blir några fel
        boxes_of_strawberries = try_int(input("Hur många askar vill du köpa? "))

        # Se till så att vi får åtminstone en ask som input
        if boxes_of_strawberries <= 0:
            print("Du måste välja en eller flera askar")
            continue

        # Beräkna det totala priset baserat på antal askar användaren vill köpa
        total_price = calculate_price(boxes_of_strawberries)

        # Skriv ut resultatet med en extra liten fiffighet för att hålla det grammatiskt korrekt
        print("_________________________________________")
        unit = "Ask" if boxes_of_strawberries == 1 else "Askar"
        print(f"|\t{boxes_of_strawberries} {unit} jordgubbar\t{total_price} kr\t\t\t|")
        print("-----------------------------------------")

        # Kolla om användaren vill köra igen
        restart = try_string(input("\nVill du köpa igen? ja/nej: ")).lower()
        if not restart.startswith("j"):
            print("Tack för ditt köp! Hejdå!")
            break

# Kör själva skriptet
strawberry_box()
