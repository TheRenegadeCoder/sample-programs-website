To run the Fizz Buzz script, launch a PowerShell console, grab a copy of the
Fizz Buzz script from the repository (or copy/paste the code from above 😉),
and then execute it.

NOTE: If you have a secure Execution Policy, you'll have to set it to unrestricted
before executing this script.

```console
$Url = "https://raw.githubusercontent.com/TheRenegadeCoder/sample-programs/main/archive/p/powershell/FizzBuzz.ps1"
$CurrPath = (Get-Location).Path
$FilePath = "$CurrPath\FizzBuzz.ps1"
$WebClient = New-Object System.Net.WebClient
$WebClient.DownloadFile($Url, $FilePath)
# Only use option 2 if you're unable to execute the script due to an ExecutionPolicy restriction.
# Afterward, reconfigure your policy to something more secure, such as options 2 or 3.
#
# Option 1:
# Set-ExecutionPolicy Unrestricted
#
# Option 2:
# Set-ExecutionPolicy AllSigned
#
# Option 3:
# Set-ExecutionPolicy RemoteSigned
.\FizzBuzz.ps1
# Output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
```
