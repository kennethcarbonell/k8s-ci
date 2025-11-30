This file hosts a fastAPI webhook listener that listens for POSTs sent by Github.

When receiving a POST it triggers the listener to start the Ansible Playbook which runs the "update_fastapi.yml" file