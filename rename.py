import os
def rename_files(path):
    file_list = os.listdir(path)
    print(file_list)
    for file in file_list:
        new_file = file.translate(None,"0123456789")
        source = path+"/"+file
        dest = path+"/"+new_file
        os.rename(source,dest)
        print(dest)

path = "/Users/moazmansour/Downloads/prank"
rename_files(path)
