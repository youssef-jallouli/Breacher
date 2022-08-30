import requests
import hashlib
import colorama
import sys


def fetch(hashpwd):
    url = "https://api.pwnedpasswords.com/range/"+hashpwd
    try:
        response = requests.get(url)
    except Exception as e:
        print("Could not fetch data for " + hashpwd + ". \nerror: "+e)
    return response.text


def treat(restext, pwdlo, pwd):
    lines = restext.splitlines()
    for line in lines:
        lineComp = line.split(":")
        try:
            fullHash = lineComp[0]
            occ = lineComp[1]
        except IndexError:
            pass
        if fullHash == pwdlo:
            if int(occ) <= 1:
                t = "time"
            else:
                t = "times"
            return colorama.Fore.LIGHTYELLOW_EX + "\nYour password has been breached and is currently vulnerable. \n" + colorama.Fore.RED + pwd + " appears " + occ + " " + t + " in data breaches."
    return colorama.Fore.GREEN + "\nYour password " + pwd + " seems safe, but it could still be vulnerable to bruteforce if it is weak."


if len(sys.argv) <= 1:
    password = input("password >>>")
    passlist = password.split(";")
    for pwd in passlist:
        hashinp = hashlib.sha1(pwd.encode("utf-8")).hexdigest().upper()
        pwdHashHead = hashinp[:5]
        pwdHashTail = hashinp[5:]
        data = fetch(pwdHashHead)
        result = treat(data, pwdHashTail, pwd)
        print(result)
else:
    for pwd in sys.argv:
        hashinp = hashlib.sha1(pwd.encode("utf-8")).hexdigest().upper()
        pwdHashHead = hashinp[:5]
        pwdHashTail = hashinp[5:]
        data = fetch(pwdHashHead)
        result = treat(data, pwdHashTail, pwd)
        print(result)


print(colorama.Fore.RESET+"")
