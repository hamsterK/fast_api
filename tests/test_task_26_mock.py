import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch
from practice.task_26_mock.app import app, fetch_data_from_api, process_data

client = TestClient(app)

class TestApp(unittest.TestCase):

    @patch("app.fetch_data_from_api")  # patch - used to replace functions with fake objects
    @patch("app.process_data")
    def test_get_and_process_data(self, mock_process_data, mock_fetch_data):
        mock_response = {"key": "value"}
        mock_fetch_data.return_value = mock_response

        mock_process_data = {"KEY": "VALUE"}
        mock_process_data.return_value = mock_process_data

        response = client.get("/data/")

        mock_fetch_data.assert_called_once()
        mock_process_data.assert_called_once_with(mock_response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mock_process_data)