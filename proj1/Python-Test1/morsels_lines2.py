import os
import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("foldernames", nargs='+', help="Folder Names to search. You can enter multiple folders here")
parser.add_argument("--ext", help="Folder Names to search. You can enter multiple folders here")
args = parser.parse_args()
foldernames = args.foldernames
ext = args.ext
print(*args.foldernames)
print(foldernames)
print(*foldernames)

def lines2 (foldernames, ext=None):
    extension_stats = dict()
    for foldername in foldernames:
        for root, dire, files in os.walk(foldername):
            for file in files:
                filename, extension = os.path.splitext(file)
                if ".DS_Store" not in filename and (ext is None or extension.replace('.', '') in ext.split(",")):
                    try:
                        row = extension_stats.get(extension.replace('.', ''), (0, 0, 0, 0))
                        num_lines = row[1]
                        blank = row[2]
                        nonblank = row[3]
                        with open(f"{root}/{file}", 'r') as f:
                            for line in f:
                                num_lines += 1
                            if line.strip():
                                nonblank += 1
                            else:
                                blank += 1
                        # filecount = ext.get(extension.replace('.','')[0], 0)+1
                        filecount = row[0] + 1
                        extension_stats[extension.replace('.', '')] = (filecount, num_lines, blank, nonblank)
                    except:
                        pass
                        #print(f"FileName {filename}{extension} had errors when reading this file")

    print("Extension    Files     Lines    Non-blank")
    for key, value in extension_stats.items():
        print(key, str(value[0]).rjust(17-len(key),' '), str(value[1]).rjust(9,' '), str(value[2]).rjust(11,' '))

lines2(foldernames, ext)
