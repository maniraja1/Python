from glob import glob
import re


def scan(pattern, filename):
    letters = re.findall(r'%(\w)', pattern)
    regex = re.sub(r'%(\w)', r'(.+)', pattern)
    match = re.fullmatch(regex, filename)
    if match:
        return dict(zip(letters, match.groups()))
    else:
        return None


def format(pattern, data):
    format_string = re.sub(r'%(\w)', r'%(\1)s', pattern)
    return format_string % data


def find_files(pattern):
    pattern = re.sub(r'\*', r'\*', pattern)
    return glob(re.sub(r'%(\w)', r'*', pattern))


def main(from_pattern, to_pattern):
    for filename in find_files(from_pattern):
        parts = scan(from_pattern, filename)
        if parts is not None:
            destination = format(to_pattern, parts)
            print("Moving", f'"{filename}"', "to", f'"{destination}"')


if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])