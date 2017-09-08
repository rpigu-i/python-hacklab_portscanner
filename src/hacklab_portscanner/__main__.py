import argparse
from portscanner import PortScanner

def main():
    """
    Function to process
    command line input
    """

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument(
        "--ports", 
        help="list of target ports to scan",
        nargs='+', 
        type=int)
    group.add_argument(
        "--ip",
        nargs='?', 
        const=None, 
        help="target ip to use instead of host")
    group.add_argument(
        "--host",
        nargs='?',
        const=None, 
        help="target host to use instead of ip")

    args = parser.parse_args()

    if args.host == None:
        flag = "ip"
        target = args.ip
    else:
        flag = "host"
        target = args.host

    scan = PortScanner(args.ports, target, flag)

if __name__ == "__main__":
    main()
