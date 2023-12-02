
# Generate data
import json

# Selct random
import random as rd

# Genetal Data
import pandas as pd
df = pd.read_csv("plate_mock.csv", sep=",")

# Image
link_photos = [
    f"https://raw.githubusercontent.com/SBobi/fud-photos/main/Food/{i}.jpg"
    for i in range(1, 24)
]

# Category
cat = ['Desayuno', 'Almuerzo', 'Cena']
ty = ['Vegano', 'Vegetariano', 'Normal']

data = {}

for cnt, i in enumerate(df.iterrows(), start=1):
    idP = cnt
    name = str(i[1]['name']).split(',')[0]
    image = rd.choice(link_photos)
    desc = i[1]['description']
    price = rd.randint(30, 100)
    offerPrice = rd.randint(0, 50)
    rating = round(rd.randint(1, 5)*rd.random(), 2)
    restaurantId = rd.randint(6, 15)
    category = rd.choice(cat)
    typ = rd.choice(ty)
    inOffer = rd.random() > .9

    aux = {"id": idP, "name": name, "image": image, "category": category, "description": desc,
           "inOffer": inOffer, "offerPrice": offerPrice, "price": price, "rating": rating,
           "restaurantId": restaurantId, "type": typ}
    data[cnt] = aux
    # print(aux)

    if cnt > 100:
        break

with open("plate_data_2.json", "w") as outfile:
    json.dump(data, outfile)
