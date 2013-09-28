serverconfig
============

The server configuration repo currently using ansible.

Still a work in progress. 


Install ansible
---------------
clone repo somewhere local on your machine then

$ mkvirtualenv ansible

$ pip install ansible

Run Playbook
------------
activate virtualenv then

    $ workon ansible
    
    $ cd to serverconfig root
    
    $ ansible-playbook dev.yml

If you have more then one server to install you can parallelize it.

    $ ansible-playbook dev.yml -f 5  # assuming you have 5 servers


dev.yml
========
This installs both worker and postgresql on the same server. 

Todo:
=====
Add the rest of the missing services.

1. redis
2. server monitoring software.
3. ?