import configparser
import unittest
from unittest.mock import patch, Mock
from traceforward.config import \
    _get_available_networks,\
    _set_network_id,\
    init


def _get_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config['FORWARD_SERVER'] = {}
    config['FORWARD_SERVER']['URL'] = 'http://test'
    config['FORWARD_SERVER']['username'] = 'test'
    config['FORWARD_SERVER']['password'] = 'test'
    return config


class TestConfig(unittest.TestCase):

    @patch('traceforward.config.requests.get')
    def test__get_available_networks_got_response(self, mock_requests_get):
        mock_data = Mock(return_value=[
            {"name": "testName1", "id": "101"},
            {"name": "testName2", "id": "102"}
        ])
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json = mock_data
        expected_networks = [("testName1","101"), ("testName2","102")]
        actual_networks = _get_available_networks('http://test', 'test', 'test')
        self.assertEqual(actual_networks, expected_networks)

    @patch('traceforward.config.requests.get')
    def test__get_available_networks_wrong_status_code(self, mock_requests_get):
        mock_requests_get.return_value.status_code = 400
        actual_networks = _get_available_networks('http://test', 'test', 'test')
        self.assertIsNone(actual_networks)

    @patch('traceforward.config.requests.get')
    def test__get_available_networks_exception(self, mock_requests_get):
        mock_requests_get.side_effect = Exception()
        actual_networks = _get_available_networks('http://test', 'test', 'test')
        self.assertIsNone(actual_networks)

    @patch('traceforward.config._get_available_networks')
    def test__set_network_id_one_network_returned(self, mock__get_available_networks):
        expected_config = _get_config()
        expected_config['FORWARD_SERVER']['NETWORK_ID'] = "101"
        mock__get_available_networks.return_value = [("testName1","101")]
        self.assertEqual(_set_network_id(_get_config()), expected_config)

    @patch('builtins.input')
    @patch('traceforward.config._get_available_networks')
    def test__set_network_id_two_networks_returned(self, mock__get_available_networks, mock_input):
        expected_config = _get_config()
        expected_config['FORWARD_SERVER']['NETWORK_ID'] = "102"
        mock__get_available_networks.return_value = [("testName1","101"), ("testName1","102")]
        mock_input.return_value = "102"
        self.assertEqual(_set_network_id(_get_config()), expected_config)

    @patch('builtins.input')
    @patch('traceforward.config._get_available_networks')
    def test__set_network_id_no_networks_returned(self, mock__get_available_networks, mock_input):
        expected_config = _get_config()
        expected_config['FORWARD_SERVER']['NETWORK_ID'] = "102"
        mock__get_available_networks.return_value = None
        mock_input.return_value = "102"
        self.assertEqual(_set_network_id(_get_config()), expected_config)

    @patch('traceforward.config.Path.is_file')
    def test_init_config_file_found(self, mock_path_is_file):
        mock_path_is_file.return_value = True
        init()
        mock_path_is_file.assert_called_once()
