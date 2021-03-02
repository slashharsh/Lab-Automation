# File for installing necessary things for project (RPM based distro) 
yum install figlet -y
yum install python3-pip -y
yum install ansible -y
yum install -y openssh-server;
pip3 install -r requirements.txt
