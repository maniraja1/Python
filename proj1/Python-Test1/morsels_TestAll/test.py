from glob import glob
import os.path
import sys
print(__file__)
print(os.path.basename(__file__))

test_filename = os.path.basename(__file__)
print(test_filename)
module_name = test_filename[len("test_"):-len(".py")]
print(f"Module Name: {module_name}")
directory = os.path.abspath(module_name)
print(f"Directory: {directory}")
for filename in glob(os.path.join(directory, "*.py")):
    print("SOLUTION", os.path.relpath(filename))
