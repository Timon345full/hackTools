import subprocess
import psutil
# import pygetwindow
# import psutil
# import time

# while True:
#     windows = pygetwindow.getAllTitles() # для получения названий всех процесов

#     for window in windows:
#         if 'браузер' in windows: # если в названии есть браузер то он будет его закрывать 
#             proces = psutil.process_iter([]) # для получения всех процесов
            
#             for proc in proces:
#                 if proc.info['name'] == "msedge.exe":
#                     proc.kill()
#     time.sleep(1) 

def showInfoCpuOzy(): # получения информаци о cpu и а оперативной памяти
    # получение оперотивной памяти
    print("System memory: ", psutil.virtual_memory()) # озу память
    print("System swap memory: ", psutil.swap_memory()) # swap память

    # cpu 
    for _ in range(3):
        info = psutil.cpu_percent(interval=1)
        print('CPU percent (interval=1, percpu=False): ', info) # практичный процесор

    print()
    for _ in range(3):
        info = psutil.cpu_percent(interval=1, percpu=True)
        print("CPU percent (interval=1, percpu=True): ", info)

    print()
    print("Logical CPUs: ", psutil.cpu_count()) # логические процесоры

def MemoryShow(Disk): # показывает информацию о памяти 
    free = psutil.disk_usage(Disk).free/(1024*1024*1024) # свободная память 
    used = psutil.disk_usage(Disk).used/(1024*1024*1024) # занятая память 
    total = psutil.disk_usage(Disk).total/(1024*1024*1024) # Обшее количество памяти
    procent = psutil.disk_usage(Disk).percent/(1024*1024*1024) # процент использования памяти
    
    print(f"Memory {Disk}: ")
    print(f"Total: {total:.4} gb")
    print(f"used: {used:.4} gb ")
    print(f"free: {free:.4} Gb ")
    print(f"Procent used memory: {procent:.4} gb")
