Labs Stats
==========

This role installs mongodb on the host and updates labs demo stats after each successful run.

Requirements
------------

The control machine SSH key must be on the `authorized_keys` of the DB server machine. To install mongodb, sudo access is required hence the `become: true` in `prep-demo.yml`. If mongodb is already installed you can comment out that line.

Role Variables
--------------

- `labs_username`: The labs username that we want to record in the database (currently pulled from `demo_username`).

Running the Playbook
--------------------

`$ ansible-playbook playbooks/prep-demo.yml --ask-become-pass` if become is enabled