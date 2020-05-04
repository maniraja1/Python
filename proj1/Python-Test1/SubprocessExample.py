import subprocess
import sys
import asyncio

async def Task():
    p = subprocess.Popen(['pwsh', '/Users/mrajagopal/Documents/hostname.ps1'])
    out, err = p.communicate()
    print(f"Error: {err}")

async def Task2():

    p = subprocess.Popen(['pwsh', '/Users/mrajagopal/Documents/hostname.ps1'],stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, universal_newlines=True)
    out, err = p.communicate()

    return out, err
'''
    print(f"{out}")

    if err:
        print(f"Error: {err}")
'''

    #subprocess.check_output(['pwsh', '/Users/mrajagopal/Documents/hostname.ps1'])

    '''
    process = subprocess.run(['pwsh', '/Users/mrajagopal/Documents/hostname.ps1'],stdout=subprocess.PIPE,
                             check=True, universal_newlines=True,stderr=subprocess.PIPE)
    output = process.stderr
    print(f"{output}")
    '''
async def main():
    try:
        out = Task()
        await out
    except:
        print("Unexpected error:")
        raise


asyncio.run(main())
#Task2()
#Task()

'''
p = subprocess.Popen(['pwsh', '/Users/mrajagopal/Documents/hostname.ps1'],stdout=sys.stdout)
p.communicate()
'''

