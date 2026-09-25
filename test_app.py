from app import app


def test_home_status_code():
    """Testa se a rota principal responde com status HTTP 200 e contém o título SERVER-HUB."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"SERVER-HUB" in response.data


def test_home_canvas_element():
    """Testa se o elemento Canvas 2D da ilustração está presente no HTML."""
    client = app.test_client()
    response = client.get("/")
    assert b'id="serverCanvas"' in response.data


def test_api_endpoint():
    """Testa se o endpoint /api retorna a estrutura JSON e versão esperadas."""
    client = app.test_client()
    response = client.get("/api")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "sucesso"
    assert data["versao"] == "2.1.0"
    assert data["topico"] == "Servidores Web e Infraestrutura"
