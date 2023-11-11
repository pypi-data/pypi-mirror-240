import argparse
import string
import subprocess
import sys
from typing import List, Optional, Dict, Union
from traceforward.utils.helpers import \
    get_source_ip, \
    prepare_request_body, \
    print_green, \
    print_blue, \
    get_hop_index_from_line, \
    conditional_extend_or_append, \
    Action, \
    parse_ipv4_address_from_line
from traceforward.forward_server.client import \
    get_extended_traceroute_data, \
    TraceRouteHopData, \
    print_powered_by, \
    check_forward_sever_reachability


def process_traceroute_lines(
    traceroute_lines: List[str], args: argparse.Namespace
) -> None:
    source_ip_address = get_source_ip(args)
    current_traceroute_line = traceroute_lines[-1]
    current_last_hop = str(
        parse_ipv4_address_from_line(current_traceroute_line))
    # Skip getting extended traceroute data for the last hop since it will
    # be covered in the last request we do after traceroute is finished
    if current_last_hop == args.host:
        print_green(current_traceroute_line)
        return
    request_body = prepare_request_body(traceroute_lines, source_ip_address)
    extended_traceroute_data = \
        get_extended_traceroute_data(request_body) \
        if check_forward_sever_reachability() else None
    _output_traceroute_results(traceroute_lines, extended_traceroute_data)


def run_command(cmd: List[str], args: argparse.Namespace) -> None:
    print_green(f"Tracing route to {args.host}...")

    if args.virtual_only:
        _run_virtual_traceroute(args)
        print_green(f"Finished tracing to {args.host}")
        print_powered_by(src_ip=get_source_ip(args), dst_ip=args.host)
        sys.exit()

    if not check_forward_sever_reachability():
        print_blue(
            "Cannot connect to Forward Server, will run ordinary traceroute."
        )
    traceroute_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, text=True)
    traceroute_lines = []
    if traceroute_popen.stderr and traceroute_popen.stdout:
        while (line := traceroute_popen.stdout.readline()) != "":
            traceroute_lines.append(line.rstrip())
            process_traceroute_lines(traceroute_lines, args)
        if traceroute_popen.wait() != 0:
            sys.exit(f"Error: {traceroute_popen.stderr.readlines()}")

    # When traceroute finished, send additional request with full
    # list of 'traceRouteHops' and 'lastHopSuffix == True'
    request_body = prepare_request_body(
        traceroute_lines,
        get_source_ip(args),
        last_hop_suffix=True,
        set_last_ecmp_hop=False
    )
    extended_traceroute_data = \
        get_extended_traceroute_data(request_body) \
        if check_forward_sever_reachability() else None
    last_traceroute_index = [
        get_hop_index_from_line(traceroute_line) for traceroute_line
        in traceroute_lines if get_hop_index_from_line(traceroute_line)
    ][-1]
    if extended_traceroute_data:
        _print_virtual_traceroute_result(
            extended_traceroute_data,
            int(last_traceroute_index) + 1 if last_traceroute_index else 0
        )

    print_green(f"Finished tracing to {args.host}")
    print_powered_by(src_ip=get_source_ip(args), dst_ip=args.host)


def create_traceroute_command(args: argparse.Namespace) -> List[str]:
    command = ["traceroute"]
    # add optional args to traceroute here
    conditional_extend_or_append(Action.APPEND, command, args.as_lookup, "-a")
    conditional_extend_or_append(
        Action.EXTEND, command, args.as_server, ["-A", f"{args.as_server}"])
    conditional_extend_or_append(
        Action.APPEND, command, args.debug_socket, "-d")
    conditional_extend_or_append(
        Action.APPEND, command, args.firewall_evasion, "-e")
    conditional_extend_or_append(
        Action.EXTEND, command, args.first_ttl, ["-f", f"{args.first_ttl}"])
    conditional_extend_or_append(Action.APPEND, command, args.fragment, "-F")
    conditional_extend_or_append(
        Action.EXTEND, command, args.gateway, ["-g", f"{args.gateway}"])
    conditional_extend_or_append(Action.APPEND, command, args.icmp_echo, "-I")
    conditional_extend_or_append(
        Action.EXTEND, command, args.max_ttl, ["-m", f"{args.max_ttl}"])
    conditional_extend_or_append(
        Action.APPEND, command, args.numerically, "-n")
    conditional_extend_or_append(
        Action.EXTEND, command, args.port, ["-p", f"{args.port}"])
    conditional_extend_or_append(
        Action.EXTEND, command, args.protocol, ["-P", f"{args.protocol}"])
    conditional_extend_or_append(
        Action.EXTEND, command, args.nqueries, ["-q", f"{args.nqueries}"])
    conditional_extend_or_append(
        Action.EXTEND, command, args.source_addr, ["-s", f"{args.source_addr}"])
    conditional_extend_or_append(
        Action.EXTEND, command, args.tos, ["-t", f"{args.tos}"])
    conditional_extend_or_append(Action.APPEND, command, args.verbose, "-v")
    conditional_extend_or_append(
        Action.EXTEND, command, args.wait, ["-w", f"{args.wait}"])
    conditional_extend_or_append(
        Action.APPEND, command, args.ip_checksums, "-x")
    conditional_extend_or_append(
        Action.EXTEND, command, args.pausemsecs, ["-z", f"{args.pausemsecs}"])
    # add positional args to traceroute here
    command.append(args.host)
    command.append(str(args.packetzise))
    return command


def _output_traceroute_results(
    traceroute_lines: List[str],
    extended_traceroute_data: Optional[List[TraceRouteHopData]]
) -> None:
    current_traceroute_line = traceroute_lines[-1]
    current_hop_index = get_hop_index_from_line(current_traceroute_line)
    if not extended_traceroute_data:
        print_green(current_traceroute_line)
        return None
    if len(extended_traceroute_data) > 1 and current_hop_index:
        for index, hop_before in enumerate(extended_traceroute_data[:-1]):
            letter_for_index = string.ascii_lowercase[index]
            print_blue(
                hop_before.pretty_display(
                    display_index=f"{str(int(current_hop_index) - 1)}."
                                  f"{letter_for_index}"
                )
            )
    print_green(current_traceroute_line)
    print_blue(extended_traceroute_data[-1].pretty_display())
    return None


def _print_virtual_traceroute_result(
    virtual_traceroute_data: List[TraceRouteHopData], start_index: int = 0
):
    for index_enum, virtual_hop in enumerate(virtual_traceroute_data):
        index = index_enum if not start_index else index_enum + start_index
        print_blue(virtual_hop.pretty_display(f"{index}  "))


def _get_and_print_virtual_traceroute_result(
    source_ip: Optional[str] = None,
    dest_ip: Optional[str] = None,
    start_index: int = 0
) -> None:
    request_body: Dict[str, Optional[Union[str, List, bool]]] = {
        "srcIP": source_ip,
        "dstIP": dest_ip,
        "traceRouteHops": [['']],
        "lastHopSuffix": True
    }
    virtual_traceroute_data = get_extended_traceroute_data(request_body)
    if virtual_traceroute_data:
        _print_virtual_traceroute_result(virtual_traceroute_data, start_index)


def _run_virtual_traceroute(
    args: argparse.Namespace, start_index: int = 0
) -> None:
    if args.virtual_only and not args.source_addr:
        print_blue("Cannot run virtual-only traceroute without source IP")
        sys.exit()
    if not check_forward_sever_reachability():
        print_blue(
            "Cannot connect to Forward Server to run"
            " virtual-only traceroute"
        )
        sys.exit()
    _get_and_print_virtual_traceroute_result(
        get_source_ip(args),
        args.host,
        start_index
    )
