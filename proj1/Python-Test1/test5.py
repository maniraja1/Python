from sys import getsizeof
from collections import defaultdict
'''
# Swap arrays to move even and od values to one side
from array import array
l = [1,2,3,4,5]
m=array('i',l)
print(type(m))
print(m)
print(len(m))
even, odd = 0, len(m)-1
while even < odd:
    if m[even] %2 ==0:
        even += 1
    else:
        m[even], m[odd]=m[odd], m[even]
        odd -= 1
print(m)

# Append to end
l.append(42)
print(l)

# Insert to a specific index
l.insert(1,100)
print(l)
l.insert(1,100)
print(l)

# remove the first occurrence of a value
l.remove(100)
print(l)
print(100 in l)
print(200 in l)

# shallow copy vs deep copy
l = [1,2,3,4,5,[1,2,3]]
m = l
print(m)
n = list(l)
print(n)
l[0]=100
print(l)
print(m)
print(n)



# Rotate list at a certain axis
l = [1,2,3,4,5]
print(l[3:]+l[:3])


# list comprehension with multiple loops. cross join
x = [1,2,3]
y = ['a','b','c']
z = [(a,b) for a in x for b in y]
print(z)

# List comprehension for flattening 2D arrays
l = [[1,2,3],[4,5,6]]
print(list(x for y in l for x in y))
print(list((x**2 for x in y) for y in l))

l = [1]*10
l[0:8:3]=[0]*4
print(l)
'''
'''
x={'DKillian7': None, 'snelluri': None, 'acollaguazo': 'Adriana Collaguazo Jaramillo', 'YYCJag': 'Jag Badh',
'yvemeng': None, 'lelelena': None, 'shuoooooooooo': 'shuo li', 'bduja': None}
print(type(x.keys()))
print('shuo li' in x.values())
'''
'''
N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

# Initialize an array t of size len(N) to all zeroes.
t = [0.0] * len(N)

# Your code should do the experiment described above for
# each problem size N[i], and store the computed sum in t[i].

for i,z in enumerate(N):
    x=[0.1]*z
    oldsum=0.0
    delta = 0.0
    for z2 in x:
        y = z2-delta
        newsum = oldsum+y
        delta=(newsum-oldsum)-y
        oldsum = newsum
    t[i]=newsum
print(t)

'''




'''
import psycopg2
from psycopg2 import pool
from requests import Session, exceptions as requests_exceptions
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from psycopg2 import OperationalError
import time
import os
from datetime import datetime

def _getazure_uami_token(retry_attempt = 3):
    try:
        retry_strategy = Retry(
        total=retry_attempt,
        status_forcelist=[429, 500,  503, 504, 502],
        method_whitelist=["HEAD", "GET", "OPTIONS"]
        )
        _adapter = HTTPAdapter(max_retries=retry_strategy)
        _url = "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fossrdbms-aad.database.windows.net"
        if _url is not None:
            _session = Session()
            _session.mount("https://", _adapter)
            _session.mount("http://", _adapter)

            _response = _session.get(_url)
            return _response.json()['access_token']
        else:
            raise RuntimeError(f"Config value for azure_uami_url has not been set in config.toml and db_authtype is set to azure_uami")
    except requests_exceptions.RequestException as e:
        _logger.debug(e)
        raise RuntimeError(f"Error Occurred when generating user assigned managed identity from azure for resource [https%3A%2F%2Fossrdbms-aad.database.windows.net]")

db_settings={
    "minconn": 1,
    "maxconn": 100,
    "host": 'magister-db2.postgres.database.azure.com',
    "port": 5432,
    "database": "magister",
    "user": "pkiuser@magister-db2",
}

db_settings["password"] = _getazure_uami_token()

_pool = psycopg2.pool.ThreadedConnectionPool(**db_settings)
filename = 'postgres-log.txt'
if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if no

logwriter = open(filename,append_write)
i = 0

while i <= 3000:
    try:
        connection = _pool.getconn()
        with connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                    "SELECT * from templates"
                )
            row = cursor.fetchone()
        _pool.putconn(conn=connection)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        logwriter.write(f"{dt_string}    Postgres Query Successfull \n")
        print(f"{dt_string}    Postgres Query Successfull")
        time.sleep(60)
    except Exception as e:
        logwriter.write(f"{dt_string}    Postgres Query Failed \n")
        logwriter.write(str(e))
        print(f"{dt_string}    Postgres Query Failed")
        print(e)
        time.sleep(60)

logwriter.close()
_pool.closeall()
'''
'''

'''
x=[0,1,2,3,4,5,6]
print('#'*50)
print(f"Max Array index: {len(x)-1}")
for i in range(0,len(x)):
    print(i)
print('#'*50)
print(f"Max Array index: {len(x)-1}")
for i in range(0,len(x)-1,2):
    print(i)
print('#'*50)
print(f"Max Array index: {len(x)-1}")
for i in range(1,len(x)-1,2):
    print(i)
print('#'*50)
print(f"Max Array index: {len(x)-1}")
for i in range(2,len(x)-1,2):
    print(i)

[2, 10, 12]
[-12, -10, 2]
print('#'*50)
import functools
x=[1,2,3,4,5,6,7,8,9,10,1]


y1 = functools.reduce(lambda v, i: v^i[1], enumerate(x), 0)
print(y1)
y2 = functools.reduce(lambda v, i: v^i, range(0,11), 0)
print(y2)
print(y1^y2)
print('#'*50)
x=10
print(x)
print(~(x-1))
print(x & ~(x-1))
print(bin(x).lstrip('0b'))
print(bin(~(x)).lstrip('-0b'))
print('#'*50)
print(4&1)
print(2^1)
print('#'*50)
x=[0,1,2,3,5,3]
y=0
for i in x:
    y ^= i
print(y)
for i in range(6):
    y ^= i
print(y)
z = y & ~(y-1)
print(z)
x=9
print(bin(~(x-1)))
print(bin(x))

d={1: 1, 2:1, 3:1}
print(1 in d)
print(4 in d)