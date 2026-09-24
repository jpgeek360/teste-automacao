from app import app

def test_home_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_home_conteudo():
    client = app.test_client()
    response = client.get('/')
    json_data = response.get_json()
    assert json_data["status"] == "sucesso"