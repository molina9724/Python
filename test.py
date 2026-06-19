INVENTORY_PRODUCTS: dict[str, dict[str, str]] = {
    "Sauce Labs Backpack": {
        "description": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
        "price": "$29.99",
    },
    "Sauce Labs Bike Light": {
        "description": "A red light isn't the caused of traffic jams on the information super highway. And it's not caused by a Problem User either. Water-resistant with 3 lighting modes, 1 AAA battery included.",
        "price": "$9.99",
    },
    "Sauce Labs Bolt T-Shirt": {
        "description": "Get your testing superhero on with the Sauce Labs bolt T-shirt. From any browser, on any OS, any day of the week. 100% Cotton. Hand wash only.",
        "price": "$15.99",
    },
    "Sauce Labs Fleece Jacket": {
        "description": "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a]]",
        "price": "$49.99",
    },
    "Sauce Labs Onesie": {
        "description": "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
        "price": "$7.99",
    },
    "Test.allTheThings() T-Shirt (Red)": {
        "description": "This classic Sauce Labs t-shirt is perfect to wear when cashing in an ideation session. Code!",
        "price": "$15.99",
    },
}

prices = list()
for name_product in INVENTORY_PRODUCTS.keys():
    for key, value in INVENTORY_PRODUCTS[name_product].items():
        if key == "price":
            prices.append(value)

another_prices = [float(price[1::]) for price in prices]


values = INVENTORY_PRODUCTS.values()
# print(values["price"])
