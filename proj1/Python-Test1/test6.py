import threading, time, datetime

async def sleeping():
    time.sleep(5)
    L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
    with open("data/threading.txt", "w") as file1:
        # Writing data to a file
        file1.write("Hello \n")
        file1.writelines(L)
    print("Done")

print("Before Threading")
thread2=threading.Thread(target=sleeping())
thread2.daemon = True
thread2.start()
print("After threading")


'''
class TestThreading(object):
    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # More statements comes here
            print(datetime.datetime.now().__str__() + ' : Start task in the background')
            time.sleep(self.interval)
            L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
            with open("data/threading.txt", "w") as file1:
                # Writing data to a file
                file1.write("Hello \n")
                file1.writelines(L)

tr = TestThreading()
#time.sleep(1)
#print(datetime.datetime.now().__str__() + ' : First output')
#time.sleep(2)
#print(datetime.datetime.now().__str__() + ' : Second output')
'''

x="12xx"
print("".join(i) for i in x if str(x).isnumeric())

x="magister-db2.postgres.database.azure.com"
y = 'pkiuser@'
db_settings={"host":"magister-db2.postgres.database.azure.com","user":"pkiuser"}

if f'@{db_settings["host"].split(".")[0]}' not in db_settings["user"]:
    print (f"{y}@{x.split('.')[0]}")
else:
    print(y)
print(y.split('@')[0])

d={'auth_type': 'azure_uami'}

if d['auth_type'] in ('azure_uami', 'azure_password'):
    print('azure')