import os, shutil
path=r"C:/Users/HP/Downloads/"
file_name=os.listdir(path)
folder_names=['PDF Files']
for loop in range(0,1):
    if not os.path.exists(path+folder_names[loop]):
        print(path+folder_names[loop])
        os.makedirs(path+folder_names[loop])

for file in file_name:
    if ".pdf" in file and not os.path.exists(path+"PDF Files/"+file):
        shutil.move(path+file,path+"PDF Files/"+file)