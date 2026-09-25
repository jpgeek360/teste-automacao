from app import app


def test_home_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"SERVER-HUB" in response.data


def test_api_endpoint():
    client = app.test_client()
    response = client.get("/api")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "sucesso"
    assert data["versao"] == "2.0.0"
