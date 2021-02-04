### These are the things to be done with Controller Host, we'll try to automate this using shell scripting.
1. Installing Anisble using Python
2. Define Target Host etc.. to Anisble Inventory File.
3. Test connectivity.($ ansible -i ./ansible/inventory user1 -m ping).
4. Now making Configuration file to define Inventory etc. and run ($ ansible user1 -m ping)