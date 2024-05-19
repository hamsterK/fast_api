from fastapi.testclient import TestClient
from app.user_t import app

client = TestClient(app)

class TestMain:

    def test_correct_reg_user(self):
        response = client.post("/registration?username=Alex&password=qwerty")
        assert response.status_code == 200
        assert response.json() == {"message": "Success!"}

    def test_incorrect_reg_user(self):
        response = client.post("/registration?username=Alex&password=qwerty")
        assert response.status_code == 409
        assert response.json() == {"detail": "User already exists"}

    def test_correct_me(self):
        response = client.get("/me?username=Ron")
        assert response.status_code == 404
        assert response.json() == {"detail": "User not found"}

    def test_correct_delete(self):
        response = client.delete("/user?username=Alex")
        assert response.status_code == 200

    def test_incorrect_delete(self):
        response = client.delete("/user?username=Ron")
        assert response.status_code == 404
        assert response.json() == {"detail": "User not found"}
