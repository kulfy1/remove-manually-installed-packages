#!/usr/bin/env python3
import os
import subprocess
def main():
    #Find release number
    a=str(subprocess.check_output("lsb_release -sr", shell=True))[2:7]

    #Check if it is LTS
    if(a[3:5]=='04' and int(a[0:2])%2==0):
        print("Since you are using LTS release, is your Ubuntu up to date? Enter 'yes' to continue.", end=" ")
        b=input()
        if(b!='yes'):
            return
        b=str(subprocess.check_output("lsb_release -sd", shell=True))[9:16]

        #Download manifest and extract the package names by removing architecture and version string
        l = os.system('curl -s http://releases.ubuntu.com/' + a + '/ubuntu-' + b + '-desktop-amd64.manifest > 1.txt; sed -i "s/\t.*//g" 1.txt; sed -i "s/:.*//g" 1.txt')
    else:
        l= os.system('curl -s http://releases.ubuntu.com/' + a + '/ubuntu-' + a + '-desktop-amd64.manifest > 1.txt; sed -i "s/\t.*//g" 1.txt; sed -i "s/:.*//g" 1.txt')

    #Get default packages in a set
    packages_initial={line.strip() for line in open("1.txt", 'r')}
    l=os.system('apt list --installed > 2.txt 2> /dev/null; sed -i "s/\/.*//g" 2.txt')

    #Get currently installed packages in a set
    packages_installed={line.strip() for line in open("2.txt", 'r')}

    #Packages that are manually installed
    l=packages_installed-packages_initial

    #Converting list into a string separated by space to pass to APT commands
    to_be_removed=' '.join(l)

    #Package count to be removed
    print(len(l), "packages will be removed.")

    #Removing those packages
    os.system('sudo apt purge '+ to_be_removed+'; sudo apt autoclean; sudo apt autoremove')

    #Install any default package that might have been deleted because of dependencies
    os.system('sudo apt install '+' '.join(packages_initial.intersection(packages_installed)))

    #Cleanup
    os.system('rm 1.txt 2.txt')
main()
