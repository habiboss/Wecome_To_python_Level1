import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("front_door.txt"):
        src = path.realpath("front_door.txt")


        dst = src + ".bak"
        # lets make a backup copy by appending "bak" to the name
        shutil.copy(src, dst)

        #copy over the permission, modification times, and other info
        shutil.copy(src, dst)
        shutil.copystat(src, dst)

        #rename the original fine
        os.rename("front_door.txt", "newfile.txt")


        #now put things into a ZIP archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        #more fine-grained control over ZIP files
        with ZipFile("testZip.zip", "W") as newzip:
            newzip.write("front_door.txt")
            newzip.write("front_door.txt.bak")

if __name__ == "__main__":
    main()
