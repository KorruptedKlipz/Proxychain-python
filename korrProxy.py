import sys
import time
import random
import winreg

#Prerequisites
def usage():
    print("Argument Error")
    print("usage: py korrProxy.py [time between changes]")
    print("usage: py korrProxy.py random [min time between changes] [max time between changes]\n")

x = 0
file = open('proxies.txt', 'r+')
proxies = file.read().splitlines()
file.close()

#Regedit Defenitions
INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
    0, winreg.KEY_ALL_ACCESS)

def set_key(name, value):
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

#Detection and Proxy Changing
if len(sys.argv) < 2:
    try:
        usage()
        exit()

    except IndexError as e:
        usage()
        exit()

elif len(sys.argv) == 3:
    try:
        usage()
        exit()

    except IndexError as e:
        usage()
        exit()

elif len(sys.argv) > 4:
    try:
        usage()
        exit()

    except IndexError as e:
        usage()
        exit()

elif sys.argv[1] == "random":
    try:
        delay = random.randint(0, int(sys.argv[2]))
        while x < len(proxies):
            if x == len(proxies):
                break
            try:
                x += 1
                delay = random.randint(int(sys.argv[2]), int(sys.argv[3]))
                set_key('ProxyEnable', 1)
                set_key('ProxyServer', proxies[x])
                print(f'Changing to {proxies[x]} for {delay} seconds.')
                time.sleep(delay)

            except KeyboardInterrupt as e:
                set_key('ProxyEnable', 0)
                set_key('ProxyServer', "")
                print("Exiting...")
                exit()

            except:
                x += 1
                print("Dead: " + proxies[x])
                set_key('ProxyEnable', 0)
                set_key('ProxyServer', "")
    except IndexError as e:
        try:
            usage()
            exit()

        except IndexError as e:
            usage()
            exit()

else:
    delay = sys.argv[1]
    while x < len(proxies):
        if x == len(proxies):
            break
        try:
            set_key('ProxyEnable', 1)
            set_key('ProxyServer', proxies[x])
            print(f'Changing to {proxies[x]} for {delay} seconds.')
            time.sleep(int(delay))
            x += 1
        except KeyboardInterrupt as e:
            set_key('ProxyEnable', 0)
            set_key('ProxyServer', "")
            print("Exiting...")
            exit()
        except:
            x += 1
            print("Dead: " + proxies[x])
            set_key('ProxyEnable', 0)
            set_key('ProxyServer', "")

set_key('ProxyEnable', 0)
set_key('ProxyServer', "")
print("\nDone.")
