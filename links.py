import re
import glob
import os

final_links = []
links = []
pwd = os.environ["PWD"]
# pwd = pwd_full.split("_with_")[1]
file_list = glob.glob('*.txt')  # returns list of files
for file in file_list:
    with open(file, 'rb') as fp:
        for line in fp:
            if b"drive.google.com" in line and b"sharing" in line:
                result = re.findall(b'drive.google.com(.*?)sharing', line)
                links.append(result)


for s in links:
    for r in s:
        r = r.replace(b"/file/d/", b"")
        r = r.replace(b"%2Ffile%2Fd%2F", b"")
        r = r.replace(b"/view?usp=", b"")
        r = r.replace(b"%2Fview%3Fusp%3D", b"")
        r = r.replace(b"/view?usp", b"")
        r = r.replace(b"%2Fview%3Fusp", b"")
        # print(r, end='\n')
        final_links.append(r)

myset = list(set(final_links))
print("unique set: ", len(myset))
for s in myset:
    print(s)
