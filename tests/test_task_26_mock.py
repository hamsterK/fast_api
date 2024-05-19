import unittest
from unittest.mock import patch, MagicMock
from practice.task_26_mock.app import get_and_process_data

class TestApp(unittest.TestCase):

    @patch("app.fetch_data_from_api")
    @patch("app.process_data")
    def test_get_and_process_data(self, mock_process_data: MagicMock, mock_fetch_data:MagicMock):
        mock_response = {"key": "value"}
        mock_fetch_data.return_value = mock_response

        mock_process_data = {"KEY": "VALUE"}
        mock_process_data.return_value = mock_process_data

        result = get_and_process_data()

        mock_fetch_data.assert_called_once()
        mock_process_data.assert_called_once_with(mock_response)
        self.assertEqual(result, mock_process_data)