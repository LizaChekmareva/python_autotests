import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "b31c868a2ce46ec9d30899bba12482f2"
HEADER = {"Content-Type":"application/json", "trainer_token":TOKEN} 
TRAINER_ID = "7640"

def test_status_code():
    response = requests.get(url=f"{URL} /trainers", params={trainer_id: TRAINER_ID})
    assert response.status_code==200