This script allows multiple AD accounts to be renewed with a single action.
--------------------------------------------------------------------------------

Process:

1. Donwload the latest report received via email at supportservices@ca.panasonic.com and extract its contents

2. Copy the csv file named "Soon-to-expire User Accounts.csv" and paste/replace the file in t8appp2 server at C:\Scripts\Network_Account_Expiry folder

3. Run the batch script names "~RUNME"

4. Provide domain admin credentials when prompted

5. Wait for the script to finish

6. Close the command prompt window once completed


-------------------------------------------------------------------------------
More Information:

Account_Expiry.py - The python script formats the raw csv file and prepares it to be read by the powershell script

Account_ExpiryNEW.csv - The csv file generated by the python script (Account_Expiry.py)

UpdateUsersCsv.ps1 - Powershell script to modify AD user attributes

RemoteScript.ps1 - Powershell script to invoke UpdateUsersCsv.ps1 to run remotely on t8pdcp2 and modify attributes

~RUNME.bat - Combines Python and Powershell script to make it convenient for administrators
