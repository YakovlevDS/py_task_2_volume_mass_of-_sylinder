import os
#делаем список полных путей к файлам в указанной директории c расширением txt.
spisok = []
for adress, dirs, files in os.walk('C:\\Users\Zver\Desktop\Music'):
    for file in files:  
        full = os.path.join(adress, file)
        if '.txt' in full:
            spisok.append(full) 
        
print(spisok)
