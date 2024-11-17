import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "b31c868a2ce46ec9d30899bba12482f2"
HEADER = {"Content-Type":"application/json", "trainer_token":TOKEN} 

body_registration = {
   "trainer_token": TOKEN,
   "email": "nyelizavea@yandex.ru",
   "password": "Fromki18"
}

body_confirmation = {
  "trainer_token": TOKEN
}

body_create = {
    "name": "Liza",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "135720",
    "name": "Poki",
    "photo_id": 1
}

body_catch = {
    "pokemon_id": "135720"
}

response = requests.post(url=f"{URL}/trainers/reg", headers=HEADER, json=body_registration)
print(response.text)

response_confirmation = requests.post(url=f"{URL}/trainers/confirm_email", headers=HEADER, json=body_confirmation)
print(response_confirmation.text)

#Создание покемона
response_create = requests.put(url=f"{URL}/pokemons", headers=HEADER, json=body_create)
print(response_create.text)

#Смена имени покемона
response_change = requests.post(url=f"{URL}/pokemons", headers=HEADER, json=body_change)
print(response_change.text)

#Поймать покемона в покебол
response_catch = requests.post(url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=body_catch)
print(response_catch.text)
