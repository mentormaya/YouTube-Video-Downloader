import os, subprocess

directory = 'C:\\Users\\Ajay\\Downloads\\SHAREit\\iPhone13,4\\photo'

for filename in os.listdir(directory):
    if filename.lower().endswith(".heic"): 
        print('Converting %s...' % os.path.join(directory, filename))
        subprocess.run(["magick", "%s" % directory + "\\" + filename, "%s" % (directory + "\\" + filename[0:-5] + '.jpg')])
        continue