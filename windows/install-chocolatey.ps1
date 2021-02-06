#!/usr/bin/env powershell

#Requires -RunAsAdministrator

function Test-Command {
    param($Command)

    $found = $false
    $match = [Regex]::Match($Command, "(?<Verb>[a-z]{3,11})-(?<Noun>[a-z]{3,})", "IgnoreCase")
    if($match.Success) {
        if(Get-Command -Verb $match.Groups["Verb"] -Noun $match.Groups["Noun"]) {
            $found = $true
        }
    }
    $found
 }

# First let's install chocolatey.
$chocoInstalled = Test-Command -Command "choco"
if (-Not $chocoInstalled) {
    $chocolateyInstallUrl = "https://chocolatey.org/install.ps1"
    $tempDir = $Env:userprofile + "\appdata\local\temp\"
    $scriptOutputFile = $tempDir + "install_chocolatey.ps1"
    Invoke-Webrequest -Uri $chocolateyInstallUrl -Outfile $scriptOutputFile

    & $scriptOutputFile
}
