import tkinter as tk
from tkinter import filedialog
import csv
import pandas as pd
import datetime
import subprocess
import sys

root = tk.Tk()
root.withdraw()

#Input file from user
file1 = filedialog.askopenfilename(title = "Select Account Expiry File")

#file1 = 'Soon-to-expire User Accounts.csv'

df=pd.read_csv(file1,encoding='ISO-8859-1')

#Renamed first column for the powershell script to work
df.rename(columns = {'sAMAccountName':'UserID'}, inplace=True)

#Delete rows where user is Disabled or lognHours are none
df = df[df.userAccountControl != "Disabled"]
df = df[df.logonHours != '0']

#Convert accountExpires column to date data type
df["accountExpires"]= pd.to_datetime(df["accountExpires"])

#Add 30 days to date
df['accountExpires'] = df['accountExpires'] + pd.DateOffset(days=30)
#Convert date to LDAP 18-digit timestamp
df['accountExpires'] = df['accountExpires'].apply(lambda x: (((x-datetime.datetime(1970,1,1)).total_seconds())+11644473600)*10000000)

#Drop unwanted columns
df.drop(df.columns[0], axis=1, inplace=True)
df.drop(['userAccountControl', 'logonHours'], axis=1, inplace=True)

#Write file to a csv. Using float format to avoid scientific notation for LDAP date
df.to_csv('Account_ExpiryNEW.csv',index=False,float_format='%.0f')

p = subprocess.Popen(["powershell.exe", "C:\\Temp\\Network Account Expiry\\UpdateUsersCsv.ps1"], stdout=sys.stdout)
p.communicate()
