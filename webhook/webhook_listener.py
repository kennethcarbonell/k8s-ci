from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

# Listens for a post on /webhook endpoint
@app.post("/webhook")
# Receives a json that sends the SHA
async def webhook(req: Request):
    data = await req.json()
    sha = data.get("sha")

    # Conditional to check for SHA
    if not sha:
        return {"status": "error", "msg": "missing sha"}

    # If SHA is received, run this playbook with this directory
    result = subprocess.run(
        ["ansible-playbook", "/home/kenneth/github/k8s-ci/update_fastapi.yml", "--extra-vars", f"sha={sha}"],
        capture_output=True,
        text=True
    )

    # print result or print error
    print(result.stdout)
    print(result.stderr)

    # Status return
    return {"status": "ok"}