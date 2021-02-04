### These are the things to be done with Target Host, we'll try to automate this using shell scripting.

1. Creating a host (Ec2 / VM / Docker Container)
2. Creating a user (say: anisbleuser)
3. Creating a ssh key at Local(Control) machine.
4. Paste generated public key to remote user (anisbleuser) in /home/anisbleuser/.ssh/authorized_keys file
5. Give ownership of above .ssh folder to anisbleuser ($ chown -R anisbleuser .ssh/)
6. Check with new ssh key to login to anisbleuser