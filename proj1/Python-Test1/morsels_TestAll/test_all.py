from argparse import ArgumentParser
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time


TEST_FILENAME_RE = re.compile(r'^ test_ (.+) \. py $', flags=re.VERBOSE)
TEST_COUNT_RE = re.compile(r'test_ .* [ ][.]{3}[ ](ok|\w+)', flags=re.VERBOSE)
print("#"*50, 'Starting tests', '#'*50)

def main(test_filename):
    stats = {}
    module_name = TEST_FILENAME_RE.search(test_filename).group(1)
    print(f"Module_name: {module_name}")
    test_filename = Path(test_filename).resolve()
    print(f"test_filename: {test_filename}")
    directory = Path(module_name).resolve()
    print(f"directory: {directory}")
    module_path = directory / f"{module_name}.py"
    cwd = Path.cwd()
    print(f"cwd: {cwd}")
    os.chdir(module_name)
    new_test_filename = directory / test_filename.name
    print(time.sleep(2))
    print('#'*50)

    for path in directory.glob("*.py"):
        print(f"Path: {path}")
        print(f"Module_path: {module_path}")
        print("SOLUTION", path.relative_to(cwd))
        print()
        shutil.copy(test_filename, new_test_filename)
        shutil.copy(path, module_path)
        print("Copied Files")
        try:
            process = subprocess.run([sys.executable, new_test_filename], capture_output=True)
            output = process.stderr.decode()
            print(output)
            results = TEST_COUNT_RE.findall(output)
            successes, total = results.count('ok'), len(results)
            stats[path.relative_to(cwd)] = (successes, total)
            for filename, (successes, total) in stats.items():
                if total == 0:
                    print(f"{filename}: error")
                else:
                    print(f"{filename}: {successes}/{total} passed")
        finally:
            new_test_filename.unlink()
            module_path.unlink()
        print('#' * 50)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('test_filename', metavar='TEST_FILE')
    args = parser.parse_args()
    main(args.test_filename)

