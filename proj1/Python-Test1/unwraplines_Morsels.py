import re
def unwrapline(randomstr):
    outstr = ""
    previous="1"
    test=[]
    n = re.compile(r'(\d+\.\s.*\n?)+')
    LIST_ITEMS = re.compile(r'^ ( - | \d [.] \s )', re.VERBOSE)
    randomlist=randomstr.split('\n')
    for l in randomlist:
        if l[:2] == '  ':
            outstr += '\n'
            outstr += l
        elif LIST_ITEMS.search(l):
            outstr += '\n'
            outstr += l
        elif l == '':
            outstr += '\n'
            if previous != '':
                outstr += '\n'
        else:
            outstr += ' '+l
        previous=l
    print(outstr)

def unwrap_lines_solution(text):
    unwrapped = ""
    lines = []
    for line in text.split('\n'):
        if line[:2] == "  ":

            unwrapped += " ".join(lines) + "\n"
            unwrapped += line
            lines=[]
        elif line:
            lines.append(line)
        elif lines:
            unwrapped += " ".join(lines) + "\n\n"
            lines = []
        else:
            unwrapped += "\n\n"
    unwrapped += " ".join(lines)
    return unwrapped + "\n"

def unwrap_lines_solution2(text):
    paragraphs = [""]
    for line in text.splitlines():
        if line:
            paragraphs[-1] += " " + line
        else:
            paragraphs.append("")
    return "\n\n".join(p.strip() for p in paragraphs)

wrappedtext="""\
This is test
  you should print 12

A second paragraph
1.  test
2.  test"""

unwrapline(wrappedtext)

print(unwrap_lines_solution(wrappedtext))

print(unwrap_lines_solution2(wrappedtext))