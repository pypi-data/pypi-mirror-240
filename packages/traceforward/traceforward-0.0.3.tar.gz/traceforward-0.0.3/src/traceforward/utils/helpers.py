import argparse
import re
from ipaddress import ip_address, IPv4Address, IPv6Address
from typing import Optional, Union, Dict, List
from enum import Enum
import subprocess
import sys

IPV4_ADDRESS = re.compile(r'(?P<ip_address>\d+\.\d+\.\d+\.\d+)')
LINUX_SRC_IPV4_ADDRESS = re.compile(r'src\s(?P<ip_address>\d+\.\d+\.\d+\.\d+)')
HOP_INDEX = re.compile(r'^\s(?P<hop_index>\d+)\s')
FWD_TRACE_SERVER_URL = 'FWD_TRACE_SERVER_URL'


class Action(Enum):
    APPEND = 'append'
    EXTEND = 'extend'


def print_green(line_to_print: str) -> None:
    print(f"\033[92m{line_to_print}\033[0m")


def print_blue(line_to_print: str) -> None:
    print(f"\033[94m{line_to_print}\033[0m")


def parse_ipv4_address_from_line(
    traceroute_line: str, ipaddr_regexp: re.Pattern = IPV4_ADDRESS
) -> Optional[Union[IPv4Address, IPv6Address]]:
    match = ipaddr_regexp.search(traceroute_line)
    if match and match.groupdict()['ip_address']:
        try:
            return ip_address(match.groupdict()['ip_address'])
        except ValueError:
            pass
    return None


def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="""
            ForwardNetworks traceroute command.
            """,
    )

    # add optional arguments
    # Forward Networks specific

    parser.add_argument("--virtual-only", action='store_true',
                        help='Only run virtual traceroute on Forward Server')

    # traceroute arguments
    parser.add_argument("-a", dest='as_lookup', action='store_true',
                        help='Turn on AS# lookups for each hop encountered')
    parser.add_argument("-A", dest='as_server', type=str,
                        help='Turn  on  AS#  lookups  and  use the given'
                        ' server instead of the default')
    parser.add_argument("-d", dest='debug_socket', action='store_true',
                        help='Enable socket level debugging')
    parser.add_argument("-e", dest='firewall_evasion', action='store_true',
                        help='Firewall evasion mode. '
                        'Use fixed destination ports for UDP and TCP probes')
    parser.add_argument("-f", "-M", dest='first_ttl', type=str,
                        help='Set the initial time-to-live used in the first'
                        ' outgoing probe packet')
    parser.add_argument("-F", dest='fragment', action='store_true',
                        help='Do not fragment probe packets')
    parser.add_argument("-g", dest='gateway', type=str,
                        help='Specify a loose source route gateway')
    parser.add_argument("-I", dest='icmp_echo', action='store_true',
                        help='Use ICMP ECHO instead of UDP datagrams')
    parser.add_argument("-m", dest='max_ttl', type=int,
                        help='Set the max time-to-live (max number of hops)'
                        ' used in outgoing probe packets')
    parser.add_argument("-n", dest='numerically', action='store_true',
                        help='Print hop addresses numerically rather than'
                        ' symbolically')
    parser.add_argument("-p", dest='port', type=int,
                        help='Choose the destination port base traceroute '
                        'will use')
    parser.add_argument("-P", dest='protocol', type=str,
                        help='Use raw packet of specified protocol for '
                        'tracerouting')
    parser.add_argument("-q", dest='nqueries', type=str,
                        help='Set the number of probes per ttl')
    parser.add_argument("-s", dest='source_addr', type=str,
                        help='Choose an alternative source address')
    parser.add_argument("-t", dest='tos', type=int,
                        help='Set the type-of-service in probe packets'
                        ' to the following value')
    parser.add_argument("-v", dest='verbose', action='store_true',
                        help='Verbose output')
    parser.add_argument("-w", dest='wait', type=int,
                        help='Set the time (in seconds) to wait for a'
                        ' response to a probe')
    parser.add_argument("-x", dest='ip_checksums', action='store_true',
                        help='Toggle IP checksums. Normally, this prevents '
                        'traceroute from calculating IP checksums.')
    parser.add_argument("-z", dest='pausemsecs', type=int,
                        help='Set the time (in milliseconds) to pause '
                        'between probes')

    # add positional arguments
    parser.add_argument(
        "host", type=str, help='Destination host for traceroute')
    parser.add_argument("packetzise", type=int, nargs='?',
                        default=60, help='Size of the probing packet')

    return parser


def _get_system() -> str:
    return sys.platform.lower()


def get_source_ip(args: argparse.Namespace) -> Optional[str]:
    if args.source_addr:
        return args.source_addr
    if _get_system() == 'darwin':
        return str(_get_osx_source_ip(args.host))
    elif _get_system() == 'linux' or _get_system() == 'linux2':
        return str(_get_linux_source_ip(args.host))
    return None


def _get_osx_outgoing_interface(target_host_addr: str) -> Optional[str]:
    route_lookup_command = f"route -n get {target_host_addr}"
    interface_grep = "grep interface"
    route_lookup_sub = subprocess.Popen(
        route_lookup_command.split(), stdout=subprocess.PIPE, text=True
    )
    interface_sub = subprocess.Popen(
        interface_grep.split(),
        stdin=route_lookup_sub.stdout,
        stdout=subprocess.PIPE,
        text=True
    )
    try:
        outgoint_interface, _ = interface_sub.communicate(timeout=15)
        return outgoint_interface.split()[-1]
    except subprocess.TimeoutExpired:
        interface_sub.kill()
    return None


def _get_interface_ip(
    interface_name: Optional[str]
) -> Optional[Union[IPv4Address, IPv6Address]]:
    ifconfig_command = f"ifconfig {interface_name}"
    inet_grep = "grep inet"
    ifconfig_sub = subprocess.Popen(
        ifconfig_command.split(), stdout=subprocess.PIPE, text=True
    )
    inet_sub = subprocess.Popen(
        inet_grep.split(),
        stdin=ifconfig_sub.stdout,
        stdout=subprocess.PIPE,
        text=True
    )
    try:
        interface_ip_lines, _ = inet_sub.communicate(timeout=15)
        return parse_ipv4_address_from_line(interface_ip_lines, IPV4_ADDRESS)
    except subprocess.TimeoutExpired:
        inet_sub.kill()
    return None


def _get_osx_source_ip(
    target_host_addr: str
) -> Optional[Union[IPv4Address, IPv6Address]]:
    osx_outgoing_interface = _get_osx_outgoing_interface(target_host_addr)
    osx_outgoing_interface_ip = _get_interface_ip(osx_outgoing_interface)
    return osx_outgoing_interface_ip


def _get_linux_source_ip(
    target_host_addr: str
) -> Optional[Union[IPv4Address, IPv6Address]]:
    ip_route_get_command = f"ip route get {target_host_addr}"
    ip_route_get_sub = subprocess.Popen(
        ip_route_get_command.split(),
        stdout=subprocess.PIPE,
        text=True
    )
    try:
        interface_ip_lines, _ = ip_route_get_sub.communicate(timeout=15)
        return parse_ipv4_address_from_line(
            interface_ip_lines, LINUX_SRC_IPV4_ADDRESS
        )
    except subprocess.TimeoutExpired:
        ip_route_get_sub.kill()
    return None


def get_hop_index_from_line(line: str) -> Optional[str]:
    hop_index_match = HOP_INDEX.search(line)
    if hop_index_match and hop_index_match.groupdict()['hop_index']:
        return hop_index_match.groupdict()['hop_index']
    return None


def _get_traceroute_index_to_hops_map(
    traceroute_lines: List[str]
) -> Dict:
    traceroute_hops: Dict[int, List[str]] = {}
    current_hop_index = 0
    for line in traceroute_lines:
        if get_hop_index_from_line(line):
            current_hop_index += 1
        hop_ip = parse_ipv4_address_from_line(line, IPV4_ADDRESS)
        if current_hop_index in traceroute_hops.keys():
            traceroute_hops[current_hop_index].append(
                str(hop_ip) if hop_ip else '*')
        else:
            traceroute_hops[current_hop_index] = [str(hop_ip)] \
                if hop_ip else ['*']
    return traceroute_hops


def _set_last_ecmp_hop(trace_route_hops: List[List[str]]) -> List[List[str]]:
    if len(trace_route_hops[-1]) <= 1:
        return trace_route_hops
    hops_before_last = trace_route_hops[:-1]
    last_hop_last_ecmp_host = trace_route_hops[-1][-1]
    hops_before_last.append([last_hop_last_ecmp_host])
    return hops_before_last


def prepare_request_body(
    traceroute_lines: List[str],
    source_ip: Optional[str],
    last_hop_suffix: bool = False,
    set_last_ecmp_hop: bool = True
) -> Dict:
    index_to_hops = _get_traceroute_index_to_hops_map(
        traceroute_lines
    )
    return {
        "srcIP": source_ip,
        "dstIP": str(
            parse_ipv4_address_from_line(traceroute_lines[-1], IPV4_ADDRESS)
        ),
        "traceRouteHops": _set_last_ecmp_hop(
            [value for _, value in index_to_hops.items()]
        ) if set_last_ecmp_hop else [value for _, value in index_to_hops.items()],
        "lastHopSuffix": last_hop_suffix
    }


def conditional_extend_or_append(
    action: Action,
    list_to_modify: List[str],
    conditional_element: Optional[str],
    value: Union[List, str]
) -> None:
    if conditional_element:
        if action == Action.EXTEND:
            list_to_modify.extend(value)
        if action == Action.APPEND:
            list_to_modify.append(str(value))
