import os
import time
#делаем список полных путей к файлам в указанной директории с условием созданные за последние сутки(86400сек).
spisok = []
for adress, dirs, files in os.walk('C:\\Users\Zver\Desktop\Music'):
    for file in files:  
        full = os.path.join(adress, file)
        if time.time()-os.path.getctime(full)<86400:
            spisok.append(full) 
        
print(spisok)
