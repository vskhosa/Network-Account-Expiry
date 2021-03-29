$s = New-PSSession -ComputerName t8pdcp2 -Credential(Get-Credential)
Copy-Item -Path \\t8appp2\c$\Scripts\Network_Account_Expiry\Account_ExpiryNEW.csv -Destination \\t8pdcp2\c$\Temp\Network_Account_Expiry\
Invoke-Command -Session $s -FilePath C:\Scripts\Network_Account_Expiry\UpdateUsersCsv.ps1