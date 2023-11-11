import unittest
import re
import argparse
from ipaddress import ip_address
from unittest.mock import patch, MagicMock, Mock
from traceforward.utils.helpers import \
    print_green,\
    print_blue,\
    parse_ipv4_address_from_line,\
    get_arg_parser,\
    get_source_ip, \
    _get_osx_source_ip, \
    _get_linux_source_ip,\
    prepare_request_body,\
    _get_traceroute_index_to_hops_map,\
    get_hop_index_from_line, \
    _set_last_ecmp_hop, \
    conditional_extend_or_append, \
    Action


class TestHelpers(unittest.TestCase):

    @patch('builtins.print')
    def test_print_green(self, mock_print):
        print_green("test_string")
        mock_print.assert_called_once_with(f"\033[92mtest_string\033[0m")

    @patch('builtins.print')
    def test_print_blue(self, mock_print):
        print_blue("test_string")
        mock_print.assert_called_once_with(f"\033[94mtest_string\033[0m")

    def test_parse_ipv4_address_from_line_parses(self):
        test_regexp = re.compile(r'(?P<ip_address>\d+\.\d+\.\d+\.\d+)')
        test_line_with_ip_addr = \
            "	inet 192.168.1.22 netmask 0xffffff00 broadcast 192.168.1.255"
        self.assertEqual(
            '192.168.1.22',
            str(
                parse_ipv4_address_from_line(
                    test_line_with_ip_addr,
                    test_regexp
                )
            )
        )

    def test_parse_ipv4_address_from_line_fails_to_parse(self):
        test_regexp = re.compile(r'(?P<ip_address>\d+\.\d+\.\d+\.\d+)')
        test_line_with_ip_addr = "this is a line without any IPv4 address"
        self.assertIsNone(
            parse_ipv4_address_from_line(
                test_line_with_ip_addr,
                test_regexp
            )
        )

    def test_get_arg_parser_returns_parser(self):
        self.assertEqual(type(get_arg_parser()), argparse.ArgumentParser)

    @patch(
        'traceforward.utils.helpers._get_system',
        MagicMock(return_value='linux')
    )
    @patch('traceforward.utils.helpers._get_linux_source_ip')
    @patch('traceforward.utils.helpers._get_osx_source_ip')
    def test_get_source_ip_linux(
        self,
        mock_get_osx_source_ip,
        mock_get_linux_source_ip
    ):
        parser = get_arg_parser()
        args = parser.parse_args(['1.1.1.1'])
        get_source_ip(args)
        self.assertEqual(args.source_addr, None)
        mock_get_osx_source_ip.assert_not_called()
        mock_get_linux_source_ip.assert_called_once_with('1.1.1.1')

    @patch(
        'traceforward.utils.helpers._get_system',
        MagicMock(return_value='darwin')
    )
    @patch('traceforward.utils.helpers._get_linux_source_ip')
    @patch('traceforward.utils.helpers._get_osx_source_ip')
    def test_get_source_ip_osx(
        self,
        mock_get_osx_source_ip,
        mock_get_linux_source_ip
    ):
        parser = get_arg_parser()
        args = parser.parse_args(['1.1.1.1'])
        get_source_ip(args)
        self.assertEqual(args.source_addr, None)
        mock_get_osx_source_ip.assert_called_once_with('1.1.1.1')
        mock_get_linux_source_ip.assert_not_called()

    @patch('traceforward.utils.helpers._get_linux_source_ip')
    @patch('traceforward.utils.helpers._get_osx_source_ip')
    def test_get_source_ip_with_source_addr(
        self, mock_get_osx_source_ip, mock_get_linux_source_ip
    ):
        parser = get_arg_parser()
        args = parser.parse_args(['1.1.1.1', '-s2.2.2.2'])
        get_source_ip(args)
        self.assertEqual(args.source_addr, '2.2.2.2')
        mock_get_osx_source_ip.assert_not_called()
        mock_get_linux_source_ip.assert_not_called()

    @patch(
        'traceforward.utils.helpers._get_osx_outgoing_interface',
        MagicMock(return_value='en0')
    )
    @patch(
        'traceforward.utils.helpers._get_interface_ip',
        MagicMock(return_value=ip_address('2.2.2.2'))
    )
    def test__get_osx_source_ip(self):
        expected_source_ip = ip_address('2.2.2.2')
        actual_source_ip = _get_osx_source_ip('1.1.1.1')
        self.assertEqual(actual_source_ip, expected_source_ip)

    @patch('traceforward.utils.helpers.parse_ipv4_address_from_line')
    @patch('subprocess.Popen')
    def test__get_linux_source_ip(
        self,
        mock_subprocess_popen,
        mock_parse_ipv4_address_from_line
    ):
        process_mock = Mock()
        attrs = {"communicate.return_value": ("output", "error")}
        process_mock.configure_mock(**attrs)
        mock_subprocess_popen.return_value = process_mock
        mock_parse_ipv4_address_from_line.return_value = ip_address('2.2.2.2')
        expected_source_ip = ip_address('2.2.2.2')
        actual_source_ip = _get_linux_source_ip('1.1.1.1')
        self.assertEqual(actual_source_ip, expected_source_ip)

    def test_prepare_request_body(self):
        traceroute_lines = [
            ' 1  1.1.1.10 (1.1.1.10)  2.254 ms  1.349 ms  1.193 ms',
            ' 2  undefined.hostname.localhost (2.2.2.1)  44.339 ms',
            '    undefined.hostname.localhost (2.2.2.2)  44.123 ms',
            ' 3  192.168.11.1 (192.168.11.1)  48.050 ms  43.593 ms  47.848 ms'
        ]
        source_ip = '1.1.1.1'
        self.assertEqual(
            prepare_request_body(traceroute_lines, source_ip),
            {
                "srcIP": '1.1.1.1',
                "dstIP": '192.168.11.1',
                "traceRouteHops": [
                    ['1.1.1.10'], ['2.2.2.1', '2.2.2.2'], ['192.168.11.1']
                ],
                'lastHopSuffix': False
            }
        )

    def test__get_traceroute_index_to_hops_map(self):
        traceroute_lines = [
            ' 1  192.168.1.1 (192.168.1.1)  2.254 ms  1.349 ms  1.193 ms',
            ' 2  undefined.hostname.localhost (172.16.11.12)  44.339 ms',
            '    undefined.hostname.localhost (172.16.100.1)  44.123 ms',
            ' 3  192.168.11.1 (192.168.11.1)  48.050 ms  43.593 ms  47.848 ms'
        ]
        expected_index_to_hops = {
            1: ['192.168.1.1'],
            2: ['172.16.11.12', '172.16.100.1'],
            3: ['192.168.11.1']
        }
        result_index_to_hops = _get_traceroute_index_to_hops_map(
            traceroute_lines
        )
        self.assertEqual(expected_index_to_hops, result_index_to_hops)

    def test_get_hop_index_from_line(self):
        line_with_index = ' 1  192.168.1.1 (192.168.1.1)  2.254 ms  1.349 ms'
        self.assertEqual('1', get_hop_index_from_line(line_with_index))
        line_without_index = '    undefined.hostname.localhost (172.16.100.1)'
        self.assertEqual(None, get_hop_index_from_line(line_without_index))

    def test_set_last_ecmp_hop(self):
        hops_with_ecmp = [
            ["1.1.1.1"],
            ["2.2.2.2", "3.3.3.3"],
            ["4.4.4.4", "5.5.5.5"]
        ]
        expected_hops_with_ecmp = [
            ["1.1.1.1"],
            ["2.2.2.2", "3.3.3.3"],
            ["5.5.5.5"]
        ]
        self.assertEqual(
            expected_hops_with_ecmp, _set_last_ecmp_hop(hops_with_ecmp)
        )
        hops_without_ecmp = [
            ["1.1.1.1"],
            ["2.2.2.2"]
        ]
        self.assertEqual(
            hops_without_ecmp, _set_last_ecmp_hop(hops_without_ecmp)
        )

    def test_conditional_extend_or_append(self):
        test_list1 = ["1","2"]
        conditional_extend_or_append(Action.EXTEND, test_list1, "test", ["3","4"])
        self.assertEqual(["1","2","3","4"], test_list1)
        test_list2 = ["1","2"]
        conditional_extend_or_append(Action.EXTEND, test_list2, None, ["3","4"])
        self.assertEqual(["1","2"], test_list2)
        test_list3 = ["1","2"]
        conditional_extend_or_append(Action.APPEND, test_list3, "test", "3")
        self.assertEqual(["1","2","3"], test_list3)
        test_list4 = ["1","2"]
        conditional_extend_or_append(Action.APPEND, test_list3, "test", "3")
        self.assertEqual(["1","2"], test_list4)
