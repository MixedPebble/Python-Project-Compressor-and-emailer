import re
from sets import Set
from zipfile import ZipFile
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
'''
Project from 2014
this project finds several projects I made, including this one then compresses them into a single .zip file.
Included in the .zip file is an HTML page with links to the downloaded projects as well as each projects line count
The .zip file is then sent as an email attachment.
Note: The file locations are hard coded because I knew where they were being saved.
Note: I did not add any catches to the files because I wanted the program to fail if something went wrong. 
'''

symbols = open("/Users/Dan/Documents/Programming/CSC-344/Assignment5/csc344/symbols.txt", "w")

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

for i in range(1,6):
    # I did not add catch statements here because
    directory = "a" + str(i)
    pathname = '/Users/Dan/Documents/Programming/CSC-344/Assignment5/csc344/' + directory + "/Assignment" + str(i)
    if i == 1:
        pathname = pathname + ".c"
        c = open(pathname, 'r')
    elif i == 2:
        pathname = pathname + ".lisp"
        lisp = open(pathname, 'r')
    elif i == 3:
        pathname = pathname + ".scala"
        scala = open(pathname, 'r')
    elif i == 4:
        pathname = pathname + ".pl"
        prolog = open(pathname, 'r')
    else:
        pathname = pathname + ".py"
        python = open(pathname, 'r')


csymbols = []
clines = 0
for line in c:
    csymbols.extend(re.findall(r'[_a-zA-Z][_a-zA-Z0-9]*',line))
    clines = clines + 1
csym = Set(csymbols)

lispsymbols = []
lisplines = 0
for line in lisp:
    lispsymbols.extend(re.findall(r'[^ ( | ) | " | , | \' | ` | : | ; | # | \s | \d]+',line))
    lisplines = lisplines + 1
lispsym = Set(lispsymbols)

scalasymbols = []
scalalines = 0
for line in scala:
    scalasymbols.extend(re.findall(r'[_a-zA-Z][_a-zA-Z0-9]*',line))
    scalalines = scalalines + 1
scalasym = Set(scalasymbols)

plsymbols = []
prologlines = 0
for line in prolog:
    plsymbols.extend(re.findall(r'[_a-zA-Z][_a-zA-Z0-9]*',line))
    prologlines = prologlines + 1
plsym = Set(plsymbols)

pysymbols = []
pythonlines = 0
for line in python:
    pysymbols.extend(re.findall(r'[_a-zA-Z][_a-zA-Z0-9]*',line))
    pythonlines = pythonlines + 1
pysym = Set(pysymbols)

for identifier in csym:
    symbols.write("C : " + identifier + '\n')

for identifier in lispsym:
    symbols.write("Lisp : " + identifier + '\n')

for identifier in scalasym:
    symbols.write("Scala : " + identifier + '\n')

for identifier in plsym:
    symbols.write("Prolog : " + identifier + '\n')

for identifier in pysym:
    symbols.write("Python : " + identifier + '\n')



contents = '''<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<html> 
<head>
<title>CSC344 Assignments</title>
</head>

<body>
<h1>Final Project</h1>

<ul>
<p><img src="http://www.clker.com/cliparts/Y/Y/O/y/Z/6/green-c-md.png" width="50" height ="50"></p>
  <h2 href = "C project">C project</h2>
  	<li><a href='Assignment1.c'>Assignment 1</A> : Linecount: ''' + str(clines) + '''
<p><img src="http://common-lisp.net/static/imgs/lisplogo.png" width="50" height ="50"></p>
  <h2 href = "lisp project">lisp project</h2>
  	<li><a href='Assignment2.lisp'>Assignment 2</A> : Linecount: ''' + str(lisplines) + '''
<p><img src="http://www.scala-lang.org/resources/img/smooth-spiral.png" width="50" height ="50"></p>
  <h2 href = "Scala Project">Scala Project</h2>
  	<li><a href='Assignment3.scala'>Assignment 3</A> : Linecount: ''' + str(scalalines) + '''  	
<p><img src="http://www.swi-prolog.org/icons/swipl.png" width="50" height ="50"></p>
  <h2 href = "Prolog Project">Prolog Project Project</h2>
  	<li><a href='Assignment4.pl'>Assignment 4</A> : Linecount: ''' + str(prologlines) + '''
<p><img src="https://www.python.org/static/img/python-logo.png" width="50" height ="50"></p>
  <h2 href = "Python project">Python project</h2>
  	<li><a href='Assignment5.py'>Assignment 5</A> : Linecount: ''' + str(pythonlines) + '''
  <h2 href = "symbols">symbols</h2>
  	<li><a href='symbols.txt'>symbols</a>
</ul>

<hr>
</body> </html>
'''
    

webpage = open('/Users/Dan/Documents/Programming/CSC-344/Assignment5/csc344/csc344.html','w')
webpage.write(contents)
webpage.close()

with ZipFile('csc344.zip', 'w') as myzip:
    myzip.write('/Users/Dan/Documents/Programming/CSC-344/Assignment5/csc344/a1/Assignment1.c','Assignment1.c')
    myzip.write('/Users/Dan/Documents/Programming/CSC-344/Assignment5/csc344/a2/Assignment2.lisp','Assignment2.lisp')
    myzip.write('/Users/Dan/Documents/Programming/CSC-344/Assignment5/csc344/a3/Assignment3.scala','Assignment3.scala')
    myzip.write('/Users/Dan/Documents/Programming/CSC-344/Assignment5/csc344/a4/Assignment4.pl','Assignment4.pl')
    myzip.write('/Users/Dan/Documents/Programming/CSC-344/Assignment5/csc344/a5/Assignment5.py','Assignment5.py')
    myzip.write('/Users/Dan/Documents/Programming/CSC-344/Assignment5/csc344/symbols.txt','symbols.txt')
    myzip.write('/Users/Dan/Documents/Programming/CSC-344/Assignment5/csc344/csc344.html','csc344.html')
    
#myzip.close()
symbols.close()

sender = raw_input('\nEnter your email\n')
pwd = raw_input('Enter your password\n')#Plaintext password
receiver = raw_input('Enter recepient email\n')

msg = MIMEMultipart(
        From=sender,
        To=receiver,
        Date=formatdate(localtime=True),
        Subject='Assignment 5'
    )
    
msg.attach(MIMEText('344 Final Docs'))
part = MIMEBase('application', "csc344.zip")
part.set_payload(open("csc344.zip", "rb").read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename=csc344.zip')
msg.attach(part)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender,pwd)

s.sendmail(sender, receiver, msg.as_string())

s.quit()
