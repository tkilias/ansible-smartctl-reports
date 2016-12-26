ansible-smartctl-reports
=========

Gathers with pySMART smart reports for each disks and stores them in the fact smartctl_reports

Requirements
------------

- python
- pip
- smartmontools


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: "ansible-smartctl-reports" }
      tasks:
        - debug:
            msg: "{{ smartctl_reports }}"

License
-------

BSD
