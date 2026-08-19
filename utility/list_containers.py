import subprocess

# Run the docker ps -a command and print all output
result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
output = result.stdout
print(output)

"""
import subprocess

# Run the docker ps -a command and print all output
result = subprocess.run(["docker", "ps", "-a", "--format", "{{.Names}}\t{{.Status}}"], capture_output=True, text=True)

lines = result.stdout.strip().split('\n')
for line in lines:
    name, status = line.split('\t', 1)
    print(f"{name} - {status}")




"""

