import os
import shutil

raw_ext = str(input("What is the extension of the RAW file? (include dot before extension and hyphens before and after!!!) "))
jpg_ext = '.JPG'

workingDir = str(input("Where would you like to delete 'unused' RAW files? (include hyphens before and after the path!!!) "))
os.chdir(workingDir)
destination = os.getcwd() + "/deleted"

#print(destination)

for filename in os.listdir('.'):
    (shortname, extension) = os.path.splitext(filename)

    if extension == raw_ext:
        if not os.path.isfile(shortname + jpg_ext):
            print 'Moving ' + shortname + raw_ext + '...'

            if not os.path.exists(destination):
                os.makedirs(destination)
            shutil.move(shortname + raw_ext, destination)
