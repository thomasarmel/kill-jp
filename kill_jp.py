import win32api
import ctypes
from time import sleep
import keyboard
import sys
import pyotp
from winreg import *
import qrcode
import io

if __name__ != "__main__":
    print("This script has to be launched directly", file=sys.stderr)
    sys.exit(2)


regKeyToRead = r'SOFTWARE\kill_jp'
reg = ConnectRegistry(None, HKEY_CURRENT_USER)

otpPassword = ""

try:
    key = OpenKey(reg, regKeyToRead)
    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        DeleteKey(key, "otp_key")
    otpPassword = QueryValue(key, "otp_key") # Raise exception if key has been deleted previously
except:
    print("You have not configured your OTP application yet")
    username = input("Please enter your name: ")
    otpPassword = pyotp.random_base32()
    otpURL = pyotp.totp.TOTP(otpPassword).provisioning_uri(name='Thomas', issuer_name='KILL JP')
    qr = qrcode.QRCode()
    qr.add_data(otpURL)
    qr.print_ascii(invert=True)
    print("Scan this QR code with your OTP application or alternatively enter the following code:", otpPassword)
    input("Press enter to save your data and exit the program")
    key = CreateKey(reg, regKeyToRead)
    SetValue(key, "otp_key", REG_SZ, otpPassword)
    CloseKey(key)
    sys.exit(0)

misteryKey = "f"

jpIsHackingMe = False
imTheLegitimUser = False
otpEnteredKey = ""

def keyboardCallback(event):
    global jpIsHackingMe
    global imTheLegitimUser
    global otpEnteredKey
    totp = pyotp.TOTP(otpPassword)
    pressedKey = event.name
    if not pressedKey.isnumeric() or len(otpEnteredKey) > 5:
        jpIsHackingMe = True
        return False
    otpEnteredKey += pressedKey
    if len(otpEnteredKey) != 6:
        return False
    if totp.verify(otpEnteredKey):
        imTheLegitimUser = True
        return False
    else:
        jpIsHackingMe = True
        return False

sleep(2)
count = 0
savedpos = win32api.GetCursorPos()
keyboard.on_release(callback=keyboardCallback)
while (not jpIsHackingMe) and (not imTheLegitimUser):
    curpos = win32api.GetCursorPos()
    if savedpos != curpos:
        print("moved to " + str(savedpos))
        jpIsHackingMe = True
    sleep(0.05)

if not imTheLegitimUser:
    print("JP is hacking me !!!")
    ctypes.windll.user32.LockWorkStation()
else:
    print("Authenticated user")
