import unittest
from app.mock import app, fetch_last_page, fetch_random_fact, process_last_page, process_fact
from unittest.mock import patch
from fastapi.testclient import TestClient

client = TestClient(app)

class TestMain(unittest.TestCase):
    @patch("app.mock.fetch_random_fact")
    @patch("app.mock.process_fact")
    def test_get_and_process_fact(self, mock_process_data, mock_fetch_data):
        mock_response = {"fact": "value", "length": 5}
        mock_fetch_data.return_value = mock_response

        mock_processed_data = "value"
        mock_process_data.return_value = mock_processed_data

        response = client.get("/random_fact")

        mock_fetch_data.assert_called_once()
        mock_process_data.assert_called_once_with(mock_response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"random fact": "value"})

    @patch("app.mock.fetch_last_page")
    @patch("app.mock.process_last_page")
    def test_get_and_process_last_page(self, mock_process_data, mock_fetch_data):
        mock_response = {
            "current_page": 1,
            "data": [{"fact": "value", "length": 5}],
            "first_page_url": "https:\\catfact.ninja\\facts?page=1",
            "from": 1,
            "last_page": 34,
            "last_page_url": "https:\\catfact.ninja\\facts?page=34",
            "links": [],
            "next_page_url": "https:\\catfact.ninja\\facts?page=2",
            "path": "https:\\catfact.ninja\\facts",
            "per_page": 10,
            "prev_page_url": None,
            "to": 10,
            "total": 332
        }
        mock_fetch_data.return_value = mock_response

        mock_processed_data = {"last_page": 34}
        mock_process_data.return_value = mock_processed_data

        response = client.get("/last_page")

        mock_fetch_data.assert_called_once()
        mock_process_data.assert_called_once_with(mock_response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mock_processed_data)

# python -m pytest tests/test_mock.py