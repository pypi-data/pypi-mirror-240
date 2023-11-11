"""CLI endpoint for traceforward"""
import sys
from traceforward.command.traceroute import \
    run_command,\
    create_traceroute_command
from traceforward.utils.helpers import \
    get_arg_parser
from traceforward import config


def main():
    """Main endpoint to the application"""
    try:
        parser = get_arg_parser()
        args = parser.parse_args()
        config.init()
        run_command(create_traceroute_command(args), args)

    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
        sys.exit(0)
