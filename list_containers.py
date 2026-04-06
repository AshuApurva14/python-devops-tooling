import subprocess

# Run the docker ps -a command and print all output
result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
output = result.stdout
print(output)

