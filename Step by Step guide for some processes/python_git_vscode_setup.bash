sudo apt update

sudo apt -y upgrade

sudo apt install software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update

sudo apt install python3.11

python3

which python3

sudo apt install python3.11-dev python3.11-venv python3.11-distutils python3.11-gdbm python3.11-tk python3.11-lib2to3



vscode setup - 
open extensions (ctrl+shift+x) - install "Remote-SSH" 

go to Remote Explorer pane 
C:\Users\prabh\.ssh\config


sudo apt-get update
sudo apt-get install git

git --version

cd /home/userver/python_100_day
git init

git config --global user.name "prabh8331"
git config --global user.email "prabh8331@gmail.com"



echo "# Python_projects" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/prabh8331/Python_projects.git

https://github.com/settings/tokens
generate tokken from this 
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

git push -u origin main



ssh git and github setup
cd ~/.ssh
ssh-keygen -t rsa -b 4096 -C "prabh8331@gmail.com"
ssh-keygen -t ed25519 -C "prabh8331@gmail.com"

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat id_ed25519.pub (copy)
go to github>settings>ssh and GPG keys > new ssh key > paste the key

ssh -T git@github.com



vscode automatically recgonise it is git and show it has the changes, 
we can like git hub from there and link to git hub



windows ssh setup 
-- ubuntu server part 
cd ~/.ssh
ssh-keygen -t ed25519
     name the key as vscode
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/vscode

cat vscode.pub (copy key from here)
nano authorized_keys (paste here)

--- now copy this vscode (privte key to C:\Users\prabh\.ssh location)
or open vscode and edit ssh config file (which is in location C:\Users\prabh\.ssh\config)

Host ubuntu_server
  HostName 192.168.1.111
  User userver
  IdentityFile C:\Users\prabh\.ssh\vscode



Putty ssh setup with puttykeygen
1. open putty key generator 
2. type of key to generate - RSA 
3. click generate (move mouse for randomness)
4. save public & private key 
5. Copy from public key from first option in key generator " Public key for passting into OpenSSH authorized_keys files
6. go to ubuntu server inside /home/userver/.ssh (or ~/.ssh) and open authorized keys and in end (in new line) paste the key
7. also paste the public key which we generate to this location of userver
8. setup with putty 
	1. and give the private key location to connetion>ssh>auth>credentials in Private key file for authentication 
        2. now go to session and put userver@192.168.1.111
3. save the session and open 





#####Vs code setup 
vscode setup - 
open extensions (ctrl+shift+x) - install "Remote-SSH" 



# Functionalities
1. Spell Check - 
  Extenxion -> code spell checker
2. More space - split screen 
3. Built-in linter 
  Extenxion for pyton to apply PEP 8 style guide --> 