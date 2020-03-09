from pathlib import Path
from collections import UserDict
from dataclasses import astuple, dataclass


def justify_columns(row, column_widths, alignments):
    aligners = [
        str.ljust if alignment == 'L' else str.rjust
        for alignment in alignments
    ]
    return [
        aligner(column, length)
        for column, length, aligner in zip(row, column_widths, aligners)
    ]

def format_fixed_width(rows, padding=2, widths=None, alignments=None):
    rows = [
        [str(x) for x in row]
        for row in rows
    ]
    if widths is None:
        widths = [
            max(len(cell) for cell in col)
            for col in zip(*rows)
        ]
    if alignments is None:
        alignments = ['L'] * len(widths)
    joiner = " " * padding
    return "\n".join(
        joiner.join(justify_columns(row, widths, alignments)).rstrip()
        for row in rows
    )

## Method 1

@dataclass
class Stat:
    files: float = 0
    lines: float = 0
    non_blank: float = 0

def count_lines(directory, extensions=['sql','ps1']):
    files = {}
    for ext in extensions:
        stat = Stat()
        for path in Path(directory).rglob(f'*.{ext}'):
            stat.files += 1
            with path.open() as f:
                for line in f:
                    stat.lines += 1
                    if line.strip():
                        stat.non_blank += 1
        if stat.files:
            files[ext] = stat
    print(files)
    return files

def Filestats(folder, extensions=['sql', 'ps1']):
    rows = sorted(
        (ext, stat.files, stat.lines, stat.non_blank)
        for ext, stat in count_lines(folder, extensions).items()
    )
    print(rows)

    total = Stat()
    for _, files, lines, non_blank in rows:
        total.files += files
        total.lines += lines
        total.non_blank += non_blank
    totals_row = ['Total', total.files, total.lines, total.non_blank]

    headers = ['Extension', 'Files', 'Lines', 'Non-blank']
    rows = [headers, *rows, totals_row]

    print(format_fixed_width(rows, padding=4, alignments=['L', 'R', 'R', 'R']))

## Method2
@dataclass
class Stat2:
    files: float = 0
    lines: float = 0
    non_blank: float = 0

    def __iter__(self):
        yield from astuple(self)

def count_lines2(*directories, extensions=['py', 'md', 'html', 'js','sql']):
    files = UserDict()
    files.totals = totals = Stat2()
    print(directories)

    for ext in extensions:
        stat = Stat2()
        for directory in directories:
            for path in Path(directory).rglob(f'*.{ext}'):
                stat.files += 1
                totals.files += 1
                with path.open() as f:
                    for line in f:
                        stat.lines += 1
                        totals.lines += 1
                        if line.strip():
                            stat.non_blank += 1
                            totals.non_blank += 1
            if stat.files:
                files[ext] = stat
    return files

def Filestats2(foldernames, extensions=['sql', 'ps1']):

    counts = count_lines2(*foldernames, extensions=extensions)
    rows = sorted(
        (ext, *stat)
        for ext, stat in counts.items()
    )
    rows = [
        ['Extension', 'Files', 'Lines', 'Non-blank'],
        *rows,
        ['Total', *counts.totals],
    ]

    print(format_fixed_width(rows, padding=4, alignments=['L', 'R', 'R', 'R']))

# Method3
def count_lines3(*directories, extensions):
    files = UserDict()
    files.totals = totals = Stat2()
    paths = {
        path
        for ext in extensions
        for directory in directories
        for path in Path(directory).rglob(f'*.{ext}')
    }
    for path in directories:
        if Path(path).is_file() and path.suffix.lstrip('.') in extensions:
            paths.add(path)
    for path in paths:
        stat = files.setdefault(path.suffix.lstrip('.'), Stat2())
        stat.files += 1
        totals.files += 1
        with path.open() as f:
            for line in f:
                stat.lines += 1
                totals.lines += 1
                if line.strip():
                    stat.non_blank += 1
                    totals.non_blank += 1
    return files

def Filestats3(foldernames, extensions=['sql', 'ps1']):

    counts = count_lines3(*foldernames, extensions=extensions)
    rows = sorted(
        (ext, *stat)
        for ext, stat in counts.items()
    )
    rows = [
        ['Extension', 'Files', 'Lines', 'Non-blank'],
        *rows,
        ['Total', *counts.totals],
    ]

    print(format_fixed_width(rows, padding=4, alignments=['L', 'R', 'R', 'R']))

Filestats('/Users/mrajagopal/Documents/git-utilitydb/UtilityDB/Utility/Table')
Filestats2(['/Users/mrajagopal/Documents/git-utilitydb/UtilityDB/Utility/Table',
            '/Users/mrajagopal/Documents/git-utilitydb/UtilityDB/Utility/schema',
            '/Users/mrajagopal/Documents/git-zarga/ZargaEndpoint/Code'])
Filestats3(['/Users/mrajagopal/Documents/git-utilitydb/UtilityDB/Utility/Table',
            '/Users/mrajagopal/Documents/git-utilitydb/UtilityDB/Utility/schema',
            '/Users/mrajagopal/Documents/git-zarga/ZargaEndpoint/Code'])