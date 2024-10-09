from Lib.ketlib import try_int, try_string


boxes_of_strawberries: int
total_price: int
box_5_price = 30
box_10_price = 25
box_11_price = 20

# Vi sätter allt i en funktion så att vi kan köra den om och om igen
def strawberryBox():
    # Prislista utskriven i ett lite mer läsbart format
    print(f"\n.:* Välkommen till JordgubbsLådan 0.1 *:.\n"
          "|\tPriser:\t\t\t\t\t\t\t\t|\n"
          "|\tAsk 1-5:\t\t\t30kr\t\t\t|\n"
          "|\tAsk 6-10:\t\t\t25kr\t\t\t|\n"
          "|\tAsk 11+:\t\t\t20kr\t\t\t|\n"
          "-----------------------------------------")
    # Ta reda på hur många askar personen vill köpa samt slänger in en try för att undvika fel
    boxes_of_strawberries = try_int(input("Hur många askar vill du köpa? "))
    # Se till att vi inte får negativa siffror eller nollor
    if boxes_of_strawberries <= 0:
        print("Du måste välja en eller flera askar")
    # Om det är 1-5 lådor så gångrar vi bara med 30 för att få fram priset
    elif boxes_of_strawberries <= 5:
        total_price = boxes_of_strawberries * box_5_price
    # Om det är 6-10 lådor så multiplicerar vi de första 5 med 30 och sen subtraherar vi de första fem från totalen
    # och multiplicerar de återstående med 25
    elif boxes_of_strawberries <= 10:
        total_price = 5 * box_5_price + ((boxes_of_strawberries - 5) * box_10_price)
    # Om det är 11+ lådor så multiplicerar vi dem med sina respektive priser och sen subtraherar vi de första tio
    # från totalen och sen multiplicerar de återstående med 20
    else:
          total_price = (5 * box_5_price) + (5 * box_10_price) + ((boxes_of_strawberries - 10) * box_11_price)
    print("_________________________________________")
    # Om det bara är en ask så printar vi den här strängen
    if boxes_of_strawberries == 1:
        print(f"|\t{boxes_of_strawberries} Ask jordgubbar\t{total_price} kr\t\t\t|")
    # Annars denna
    else:
        print(f"|\t{boxes_of_strawberries} Askar jordgubbar\t{total_price} kr\t\t\t|")
    print("-----------------------------------------")
    # Sen kollar vi om användaren vill köra en gång till
    restart = try_string(input("\nEn gång till? ja/nej ")).lower()
    if restart.startswith("j"):
        strawberryBox()
    else:
        exit()

strawberryBox()
