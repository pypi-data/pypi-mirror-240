import pywaybackup.archive as archive 
import argparse
import os
__version__ = "0.2"

parser = argparse.ArgumentParser(description='Download from wayback machine (archive.org)')
parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__, help='Show version')
required = parser.add_argument_group('required')
required.add_argument('-u', '--url', type=str, help='URL to use')
exclusive_required = required.add_mutually_exclusive_group(required=True)
exclusive_required.add_argument('-c', '--current', action='store_true', help='Download the latest version of each file snapshot')
exclusive_required.add_argument('-f', '--full', action='store_true', help='Download snapshots (optional range in years)')
optional = parser.add_argument_group('optional')
optional.add_argument('-l', '--list', action='store_true', help='Only list available snapshots (optional range in years)')
optional.add_argument('-r', '--range', type=int, default=1, help='Range in years to search')
optional.add_argument('-o', '--output', type=str, help='Output folder')
special = parser.add_argument_group('special')
special.add_argument('-m', '--mimetype', action='store_true', help='Guess mimetype for each file and add file extension if not present')

args = parser.parse_args()

if args.output is None:
    args.output = os.path.join(os.getcwd(), "pywaybackup_snapshots")
if args.list:
    cdxResult_list = archive.query_list(args.url, args.range)
    archive.print_result(cdxResult_list)
if not args.list:
    if args.full:
        cdxResult_list = archive.query_list(args.url, args.range)
        archive.download_full(cdxResult_list, args.output)
    archive.remove_empty_folders(args.output)
