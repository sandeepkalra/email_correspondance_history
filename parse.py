import os
from email import policy
from email.parser import BytesParser
import glob

pwd_full = os.environ["PWD"]
pwd = pwd_full.split("_with_")[1]
file_list = glob.glob('*.eml')  # returns list of files
for file in file_list:
    with open(file, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
        fnm = os.path.splitext(file)[0] + '.txt'
        oldFnm = "[\""+pwd+"/"+file+"\"]\r\n"
        fnm = fnm.replace(" ", "_")
        content = msg.get_body(preferencelist=('plain')).get_content()
        content = content.replace('\r', '')
        content = f"Filename: {oldFnm}, Content\n {content}"
        with open(fnm, 'w', newline="\n") as f:
            f.write(content)
