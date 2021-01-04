import re
from collections import defaultdict
from itertools import permutations, combinations
v = 'https://www.airbnb.cosdfsdfwersdf/rooms/18520444?location=Cleveland xyz%2C%20TX'
ptrn = r'(location=)(.*)(%2C)'
mtch = re.search(ptrn,v)
print (mtch.group(2))

v='Here comes the boy said John.'
ptrn=re.compile(r'(.*) said')
print(f"'{ptrn.findall(v)[0]}'")
v='BE1  '
ptrn=re.compile(r'(.*) said')
print(f"'{ptrn.findall(v)}'")

v="Please sir, that's obviously a clip-on."
ptrn2 = re.compile('([a-zA-Z]+)(\'[a-zA-Z])?([a-zA-Z]*)')
ptrn = re.compile('[a-zA-Z]+(\'[a-zA-Z])?[a-zA-Z]*')
print(ptrn2.findall(v))
print([m.group(0) for m in ptrn.finditer(v)])

v="This costs $0.3 and this $784"
ptrn=re.compile("(\$\d*.\d*)")
print(ptrn.findall(v))

v='mani.shankar.raja@gmail.com'
#ptrn=re.compile("[a-z]+@[a-z]+.com")
ptrn2=re.compile(".+@\w+.com")
print(ptrn2.findall(v))

v='"uio" [ek3k 0die] 4229834'
ptrn=re.compile('"(\w+)"')
ptrn2=re.compile(r'\[(.+)\]')
print(ptrn.findall(v))
print(ptrn2.findall(v))

v="$100.00 • $10,000.00 • $1234 • $5000.00 • $1,000,000"
ptrn=re.compile(r'\$\d*,?.?\d*')
print(ptrn.findall(v))

v="olly olly in come free"
ptrn = re.compile(r'\w+')
d=defaultdict(int)
for x in ptrn.findall(v):
    d[x] += 1
print(d)

v="001---123--234-5678"
ptrn=re.compile(r'\-+')
print(ptrn.findall(v))
print(ptrn.sub('-',v))

v="CCIS-327E CCIS-227B CELS-112 SC-124B CCIS-328"
ptrn=re.compile(r'CCIS-\d+[A-Z]')
print(ptrn.findall(v))

v="Some man ate an apple from a tree in a glade at the edge of the town."
ptrn=re.compile(r'Some|an |a |the ')
print(ptrn.findall(v))
print(ptrn2.findall(v))

v='1234567'
ptrn=re.compile(r'\d{1,3}')
print(ptrn.findall(v))

v= """
Sed ut perspiciatis, unde omnis iste natus error sit
voluptatem accusantium doloremque laudantium, totam
rem aperiam eaque ipsa, quae ab illo inventore
veritatis et quasi architecto beatae vitae dicta
sunt, explicabo. Nemo enim ipsam voluptatem, quia
voluptas sit, aspernatur aut odit aut fugit, sed
quia consequuntur magni dolores eos, qui ratione
voluptatem sequi nesciunt, neque porro quisquam est,
qui dolorem ipsum, quia dolor sit amet consectetur
adipisci[ng] velit, sed quia non numquam [do] eius
modi tempora inci[di]dunt, ut labore et dolore
magnam aliquam quaerat voluptatem. Ut enim ad minima
veniam, quis nostrum exercitationem ullam corporis
suscipit laboriosam, nisi ut aliquid ex ea commodi
consequatur? Quis autem vel eum iure reprehenderit,
qui in ea voluptate velit esse, quam nihil molestiae
consequatur, vel illum, qui dolorem eum fugiat, quo
voluptas nulla pariatur?

At vero eos et accusamus et iusto odio dignissimos
ducimus, qui blanditiis praesentium voluptatum
deleniti atque corrupti, quos dolores et quas
molestias excepturi sint, obcaecati cupiditate non
provident, similique sunt in culpa, qui officia
deserunt mollitia animi, id est laborum et dolorum
fuga. Et harum quidem rerum facilis est et expedita
distinctio. Nam libero tempore, cum soluta nobis est
eligendi optio, cumque nihil impedit, quo minus id,
quod maxime placeat, facere possimus, omnis voluptas
assumenda est, omnis dolor repellendus. Temporibus
autem quibusdam et aut officiis debitis aut rerum
necessitatibus saepe eveniet, ut et voluptates
repudiandae sint et molestiae non recusandae. Itaque
earum rerum hic tenetur a sapiente delectus, ut aut
reiciendis voluptatibus maiores alias consequatur
aut perferendis doloribus asperiores repellat.
"""

ptrn = re.compile(r'([a-zA-Z]+[^\w+\s*]*[a-zA-Z]*)\s*')
ptrn2=re.compile(r'[^a-z0-0\s]')
x=ptrn.findall(re.sub('[^0-9a-zA-Z\s*]+', '', v).lower())
print(len(x))
print(x)

ptrnWhiteSpace = re.compile(r'[a-zA-Z]+')
y=ptrnWhiteSpace.findall(v.lower().replace("\n", ""))
print(len(y))
print(y)

def get_normalized_words (s):
    words = []
    temp = []
    for x in s:
        if x.isspace() and len(temp)>0:
            words.append("".join(temp))
            temp.clear()
        elif x.isalpha():
            temp.append(x.lower())
    return words
# Demo:
x=get_normalized_words(v)
print(len(x))
print(x)

x={'d', 'e', 's'}
print(list(permutations(x,2)))
print(list(combinations(x,2)))
y=permutations(x,2)
print(y)

r='adipisci[ng]'
r=re.sub('[^0-9a-zA-Z]+', '', r)
print(r)


sample_input = """
This film is based on Isabel Allende's not-so-much-better novel. I hate Meryl
Streep and Antonio Banderas (in non-Spanish films), and the other actors,
including Winona, my favourite actress and Jeremy Irons try hard to get over
such a terrible script.
"""

your_regex_pattern=r"\w+[\'-]?\w+|\w+"
sample_output_regex = re.findall(your_regex_pattern, sample_input.lower(), re.VERBOSE)
print(sample_output_regex)

'''
#Problem 14
match = re.search(r'var\s+approval\s*=\s*\[([^\]]*)\];', html)
pattern = r"\"date\":\"(\d{4}-\d{2}-\d{2})\",\"future\":(false|true),.*\"approve_estimate\":\"([^\"]*)\""
pattern = r"\"date\":\"(\d{4}-\d{2}-\d{2})\",\"future\":(false|true),.*\"disapprove_estimate\":\"([^\"]*)\""
'''
v="""
=== Excerpt from the book, '1984' ===
It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his 
breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not 
quickly enough to prevent a swirl of gritty dust from entering along with him. 
"""

print(''.join([c for c in v.lower() if c.isalpha() or c.isspace() or c.isnumeric()]))

l={1, 2, 3}
m={1, 4, 5}

print(l.union(m))
print(l|m)
m |= l
print(m)
print(l)

x='3140'
print(x[-3::-1][::-1]+'-'+x[-1:-3:-1][::-1])

e="cddev2privateacr.azurecr.io"
s=r'cd[dev\d*|qa\d*]*privateacr'
print(re.findall(s, e))
