import os
#делаем список полных путей к файлам в указанной директории.
spisok = []
for adress, dirs, files in os.walk('C:\\Users\Zver\Desktop\Music'):
    for file in files:  
        spisok.append(os.path.join(adress,file))
print(spisok)



