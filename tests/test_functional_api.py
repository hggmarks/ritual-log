from fastapi.testclient import TestClient
from rituallog.api import api 

client = TestClient(api)


def test_create_ritual_via_api():
    response = client.post(
        "/rituals/",
        json={
            "name": "Cicatrização",
            "element": "Morte",
            "circle": 1,
            "cost": 1,
            "execution": "ação padrão",
            "range": "toque",
            "target": "Um personagem",
            "duration": "Instantâneo",
}, 
    )

    result = response.json()
    
    assert response.status_code == 201
    assert result['name'] == 'Cicatrização'
    assert result['element'] == 'Morte'
