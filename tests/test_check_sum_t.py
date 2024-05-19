from fastapi.testclient import TestClient
from app.check_sum_t import app

client = TestClient(app)


def test_calculate_sum():
    # positive numbers
    response = client.get("/sum/?a=5&b=10")
    assert response.status_code == 200
    assert response.json() == {"result": 15}

    # negative numbers
    response = client.get("/sum?a=-8&b=-3")
    assert response.status_code == 200
    assert response.json() == {"result": -11}

    # positive + zero
    response = client.get("/sum?a=0&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 7}

    # one number
    response = client.get("/sum?a=3")
    assert response.status_code == 422
    assert response.json() == {
        "detail":[
            {
                "type":"missing",
                "loc":["query","b"],
                "msg":"Field required",
                "input":None,
                "url":"https://errors.pydantic.dev/2.6/v/missing"}]}

# python -m pytest
