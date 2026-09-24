from app import app


def test_home_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_conteudo():
    client = app.test_client()
    response = client.get("/")
    json_data = response.get_json()
    assert json_data["status"] == "sucesso"
    assert "versao" in json_data


def test_health_check():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_saudacao_parametro():
    client = app.test_client()
    response = client.get("/api/saudacao?nome=Joao")
    assert response.status_code == 200
    assert "Joao" in response.get_json()["mensagem"]
