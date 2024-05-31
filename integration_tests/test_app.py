import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
test_user_data = {"name": "John Doe", "email": "jogndoe@mail.com"}

class TestMain:
    def test_auth_user(self):
        response = client.post("/auth/login", auth=(test_user_data["name"], test_user_data["email"]))
        assert response.status_code == 200

    def test_reg_user(self):
        test_data = {"name": "John Doe 2", "email": "jogndoe2@mail.com"}

        response = client.post("/auth/reg", content=json.dumps(test_data))
        assert response.status_code == 409

    def test_add_product(self):
        test_product = {"name": "coke", "price": 9.99}

        response = client.post("/access/add_product", content=json.dumps(test_product), auth=(test_user_data["name"], test_user_data["email"]))
        assert response.status_code == 200

    def test_get_product(self):
        response = client.get("/access/get_product?name=coke", auth=(test_user_data["name"], test_user_data["email"]))
        assert response.status_code == 200

    def test_update_product(self):
        response = client.put("/access/change_product?name=coke&price=9.99", auth=(test_user_data["name"], test_user_data["email"]))
        assert response.status_code == 200

    def test_delete_product(self):
        response = client.delete("/access/delete_product?name=coke", auth=(test_user_data["name"], test_user_data["email"]))
        assert response.status_code == 200
