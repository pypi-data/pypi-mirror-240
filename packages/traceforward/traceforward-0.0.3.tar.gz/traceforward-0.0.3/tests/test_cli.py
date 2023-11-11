import unittest
from unittest.mock import patch, MagicMock
from traceforward.cli import main as climain


class TestCli(unittest.TestCase):

    @patch('sys.exit')
    @patch('builtins.print')
    @patch(
        'traceforward.cli.get_arg_parser',
        MagicMock(side_effect=KeyboardInterrupt())
    )
    def test_main_raised_keyboard_interrupt(self, mock_print, mock_sys_exit):
        climain()
        mock_print.assert_called_once_with("\nInterrupted by user. Exiting...")
        mock_sys_exit.assert_called_once_with(0)

    @patch('traceforward.cli.run_command')
    @patch('traceforward.cli.config.init')
    @patch('traceforward.cli.get_arg_parser')
    def test_main_normal_action(
        self,
        mock_get_arg_parser,
        mock_config_init,
        mock_run_command
    ):
        climain()
        mock_get_arg_parser.assert_called_once()
        mock_config_init.assert_called_once()
        mock_run_command.assert_called_once()
