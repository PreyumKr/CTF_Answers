import os
import shutil
path = "./xhdjdagubiojmeae"

for root, d_name, f_name in os.walk(path):
    print (root,d_name,f_name)
    rel_path = root + "/" + "".join(f_name)

# os.chdir(rel_path)
print(rel_path)
shutil.copy(rel_path, "./")