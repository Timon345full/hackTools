import subprocess
import socket
import os 

def wifiProfiles():
    try:
        data = subprocess.check_output("netsh wlan show profiles").decode('cp866').split('\n') # для получениях даных о всех беспроводных сетях
        profiles = [i.split(":")[1][1: -1] for i in data if "все профили пользовотельских" in i]
        pass_wifi = ''

        for i in profiles:
            results = subprocess.check_output(['netch', 'wlan', 'show', 'profile', i, "key=clear"]).decode('cp866').split('\n')
            
            for j in results:
                if "Содержание ключа" in j:
                    pass_wifi += f"{i} -- {j.split(':')[1][1:-1]}\n"
        
        print(pass_wifi)

    except Exception as e:
        print("Ошибка", e)

def ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def udateIp():
    os.system("uvicorn ipUdate:app --reload")
    