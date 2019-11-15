import re

with open('data/jobs.sql','r') as f:
    jobs=[]
    for line in f:
        if re.search(r'select\s+@jobname',line.lower()) is not None:
            jobs.append(line.lstrip())
            #print(re.search(r'select\s+@Job',line).group())
    print(*sorted(jobs))


