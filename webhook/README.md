This file hosts a fastAPI webhook listener that listens for POSTs sent by Github.

When receiving a POST it triggers the listener to start the Ansible Playbook which runs the "update_fastapi.yml" file.

Ensure that you are in python venv and run these commands to launch the webhook listener:

sourece venv/bin/activate

python3 -m uvicorn webhook_listener:app --host 0.0.0.0 --port 9000