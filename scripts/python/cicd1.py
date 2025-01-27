import subprocess
import os

def run_command(command, cwd=None):
    """Run a shell command and capture its output."""
    try:
        result = subprocess.run(
            command, shell=True, check=True, text=True, cwd=cwd,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e.stderr}")
        return False

# Define paths and commands
vagrantfile_dir = os.path.abspath(".")  # Directory containing your Vagrantfile
inventory_file = os.path.join(vagrantfile_dir, "inventory.ini")
playbooks = ["ubuntu-vm.yml", "k3s.yml"]

# Step 1: Bring up the Vagrant VMs
print("\n[INFO] Starting Vagrant VMs...")
if run_command("vagrant up", cwd=vagrantfile_dir):
    print("\n[INFO] Vagrant VMs started successfully!")
else:
    print("\n[ERROR] Failed to start Vagrant VMs. Exiting.")
    exit(1)

# Step 2: Run Ansible playbooks
for playbook in playbooks:
    print(f"\n[INFO] Running Ansible playbook: {playbook}...")
    command = f"ansible-playbook -i {inventory_file} {playbook}"
    if run_command(command):
        print(f"[INFO] Playbook {playbook} ran successfully!")
    else:
        print(f"[ERROR] Playbook {playbook} failed. Exiting.")
        exit(1)

# Step 3: Verify the processes
print("\n[INFO] Verifying processes on VMs...")
verification_commands = [
    "kubectl get nodes",
    "docker --version",
]
for command in verification_commands:
    print(f"\n[INFO] Running verification command: {command}...")
    if run_command(f"vagrant ssh ubuntu-vm1 -c \"{command}\"", cwd=vagrantfile_dir):
        print(f"[INFO] Verification command '{command}' succeeded on ubuntu-vm1!")
    else:
        print(f"[ERROR] Verification command '{command}' failed on ubuntu-vm1!")

print("\n[INFO] All steps completed. Your environment is set up and verified!")

