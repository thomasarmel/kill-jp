# kill-jp
Fight more effectively against your annoying colleagues (MS Windows only)

If some of your colleagues do bad stuff when you forget to lock your workstation, this script is for you.

## How to use it ?

+ Install an OTP application on your smartphone (Google Authenticator, Authy...)
+ Install python >= 3 on your workstation
+ Run the command prompt as administrator and type `pip install keyboard pyotp qrcode`
+ Run the script on the command prompt, type your name and scan the QR code with your OTP application
+ When you leave your desk, simply run the script instead of locking your workstation (you can optionally hide it behind another application within the first 2 seconds)
+ Your workstation will automatically be locked if any interaction occurs with the mouse or the keyboard
+ The only way to stop the script is to type the 6 digits code given by the OTP application with the numeric keypad
