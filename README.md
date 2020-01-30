# HTB Scripts
Here the scripts that I developed for some specific tasks during the pentesting process in some of the HackTheBox boxes and challenges that I pwned. I do not guarantee that these scripts work for your purposes or that they are free of bugs.

NOTE: All **scripts of still active boxes and challenges are protected** by the root flag for the boxes, and the flag in the format *HTB{challenge_flag}* for the challenges.

## List of scripts
- **Mango_cracker.py**: Mango script to retrieve the passwords of the existing users thru the NoSQL injection technique
- **Json_injector.py**: Allows to inject arbitrary commands due to a exploitable Json.Net API via .NET deserialization
- **ezpz_injector.py**: Script to perform the SQL injection needed in this challenge
- **USB-Ripper.py**: For forensics USB-Ripper challenge. Parses manufacturers and serial numbers from syslog and compares with those in auth.log retrieving the one/s that were removed
- **Craft_exploit.py**: Craft box exploit to inject arbitrary code into the exploitable API and get a reverse shell
- **Fortune_shell.py**: Script that acts as a shell in the machine, exploiting the RCE vulnerability that this machine has at the web service

<p align="center">
<a href="https://www.hackthebox.eu/home/users/profile/91096"><img src="https://www.hackthebox.eu/badge/image/91096" alt="Hack The Box XMA"></a>
</p>
