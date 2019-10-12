### Pre-requisite

1. [`curl`](http://manpages.ubuntu.com/manpages/trusty/man1/curl.1.html) should be installed. If not installed, install it using:

        sudo apt install curl
2. If you are using LTS version, it should be updated to latest point release. For example, at the time of writing this, 18.04.3 was released. So, you should be running the same since it's hard to find the manifest for 18.04, 18.04.1 or 18.04.2.
3. Internet connection is required to download the manifest.

### To run:

    wget https://raw.githubusercontent.com/kulfy1/remove-manually-installed-packages/master/script.py
    chmod +x script.py
    ./script.py

### Explanation: 

The above script will download the manifest file which contains the name of packages installed by default. A list will be created which contain those package names. Another list will be created which would contain currently installed package names. APT will remove the packages that were installed manually and are not in the earlier list. After removing the packages, the packages that were common in those lists would be installed, if removed due to some reasons. 

### Footnote:

The prompts of APT commands (such as password and confirmation to remove/install packages) are expected to be handled by the user and aren't being handled in the script since it may happen that user don't want to really remove those packages. Since script isn't run with sudo privileges, thus, no package would be removed by the script unless password and "Yes" are provided when prompted by the APT.
