# Not fixed anymore

# Forcegrief 
### PRE-RELEASE
Forcegrief is a Python program that automates a server login request. It comes along with goblin, a powerful wordlist generator made by UndeadSec and Sam Junior:@un00mz.
Forcegrief is Licensed under Apache 2.0 license. You can find it in the LICENSE file.

## Requirements
1. Python 3.8 or later;
2. The REQUESTS module for Python. Install it with PIP : "sudo pip install requests" on Linux or "pip install requests" on Windows.

## Installing
### Linux
1. Clone the repo using (Git)[https://git-scm.com/download], using :
* SSH : "git clone git@github:DiamondsBattle/Forcegrief.git"
* HTTPS : "git clone https://github.com/DiamondsBattle/Forcegrief.git

### Windows
1. Download the ZIP file using : 
 * [Direct Download](https://github.com/DiamondsBattle/Forcegrief/archive/master.zip)
 * [Git](https://git-scm.com/download), using :
   * SSH : "git clone git@github.com:DiamondsBattle/Forcegrief.git"
   * HTTPS :  "git clone https://github.com/DiamondsBattle/Forcegrief.git"
2. Open cmd.exe and move to the directory you installed it in.
3. Then type "python3 forcegrief.py"

### Usage
#### If you have a wordlist : 
1. Enter the "forcegrief" command;
2. Then enter the file containing the password's name;
3. Then enter the Username field's Name (Returned to the server when trying to login);
4. Then enter the Password field's Name (Returned to the server when trying to login);
5. Then enter the site's login form URL;
6. Then enter the Username;
6. Let the program run.
#### If you don't have a wordlist : 
* Create the wordlist : 
1. Enter "goblin", and follow the instruction on the screen.
