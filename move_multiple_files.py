import shutil
import os

# You can specify the specific extension you want to move
file_extensions = ['jpg']

for root, dirs, files in os.walk(r"<Enter your path here - dir 1>", topdown=True):
    for name in files:
        if name.split('.')[-1] in file_extensions:
            shutil.move(os.path.join(root, name), os.path.join(r"<Enter your path here - dir 2>", name))
