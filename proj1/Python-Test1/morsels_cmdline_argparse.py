from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('old_file',help="input the current file")
parser.add_argument('new_file', help="input the new file")
parser.add_argument('--update', action='store_true', help="update if a match is found")
args = parser.parse_args()

print(f"Old File: {args.old_file}")
print(f"New File: {args.new_file}")
print(f"Update: {args.update}")
