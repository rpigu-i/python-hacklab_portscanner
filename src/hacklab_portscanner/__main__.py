import argparse
from portscanner import PortScanner

def main():
    """
    Function to process
    command line input
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "host",
        nargs='?',
        const=None, 
        help="target host")
    parser.add_argument(
        "ip",
        nargs='?', 
        const=None, 
        help="target ip to use instead of host")
    parser.add_argument(
        "ports", 
        help="list of target ports to scan",
        type=list)

    args = parser.parse_args()
    scan = PortScanner(args.ports, args.host, args.ip)

