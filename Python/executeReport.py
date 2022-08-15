#!/usr/bin/env python3

import subprocess, smtplib

def sendMail(emailAdd, emailPass, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(emailAdd, emailPass)
	server.sendmail(emailAdd, emailAdd, message)