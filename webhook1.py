from flask import Flask, request
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/webhook', methods=['POST'])
def webhook():
    # Phase 1: List all Docker containers
    containers = client.containers.list(all=True)

    print(f"Found {len(containers)} container(s):")
    for container in containers:
        print(f"- {container.name}: {container.status}")

    return {"status": "success", "containers_found": len(containers)}, 200

if __name__ == "__main__":
    print("Flask webhook listening on port 5000...")
    app.run(host="0.0.0.0", port=5000)
