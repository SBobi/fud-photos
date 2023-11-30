
# Generate data
import json

# Selct random
import random as rd

# Genetal Data
import pandas as pd
df = pd.read_csv("restaurant_mock.csv")

# Image
link_photos = [
    f" https://raw.githubusercontent.com/SBobi/fud-photos/main/Restaurant/{i}.jpg"
    for i in range(1, 10)
]

# GeoPoint Uniandes
lat = 4.603083
lon = -74.065319

data = {}

for i in df.iterrows():
    idR = int(i[1]['id'])+5
    name = i[1]['name'].split(',')[0]
    image = rd.choice(link_photos)
    latM = lat + rd.random()
    lonM = lon + rd.random()

    aux = {"id": idR, "name": name, "image": image, "lat": latM, "lon": lonM}
    data[i[0]] = aux
    # print(aux)

with open("restaurant_data.json", "w") as outfile:
    json.dump(data, outfile)
