import pytest
from .subscribers_repository import SubscriberRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name": "Marcelo",
        "email": "teste@gmail.com",
        "evento_id": 1
    }
    sub_repo = SubscriberRepository()
    sub_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_evento():
    email = "teste@gmail.com"
    evento_id = 10

    sub_repo = SubscriberRepository()
    result = sub_repo = sub_repo.select_subscriber(email, evento_id)
    print(result.nome)

@pytest.mark.skip("Select in DB")
def test_ranking():
    evento_id = 1
    sub_repo = SubscriberRepository()   
    response = sub_repo.get_ranking(evento_id)

    for elem in response:
        print(f"Link: {elem.link}, total de inscritos {elem.total}")