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

    # run long test, wait for it and gather reports
    - name: "Execute smart report"
      import_role:
        name: "ansible-smartctl-reports"
      vars:
        smartctl_test_type: "long"
        
    # run short test, wait for it and gather reports
    - name: "Execute smart report"
      import_role:
        name: "ansible-smartctl-reports"
      vars:
        smartctl_test_type: "short"
        
    # gather reports only
    - name: "Execute smart report"
      import_role:
        name: "ansible-smartctl-reports"
      vars:
        smartctl_test_type: "long"
        
    # save report as file on localhost
    - name: "save reports"
      local_action: copy content={{ smartctl_reports }} dest="./smartctl_reports.txt"
        
License
-------

BSD
