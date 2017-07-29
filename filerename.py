import os
def filename():

    file_list = os.listdir(r"/Users/ashokjain/Desktop/prank")

    saved_path = os.getcwd()

    os.chdir("/Users/ashokjain/Desktop/prank")

    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"1234567890"))

    os.chdir(saved_path)

print(filename())