import os
import email
from email import policy
from email.parser import BytesParser
import glob

file_list = glob.glob('*.eml') # returns list of files
for file in file_list:
    with open(file, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
        fnm = os.path.splitext(file)[0] + '.txt'
        fnm = fnm.replace(" ", "_")
        txt = msg.get_body(preferencelist=('plain')).get_content()
        with open(fnm, 'w') as f:
            print('Filename:', txt, file = f, end="")

