import subprocess

update_libc = "sudo sudo apt update && sudo apt install -y libc6"
check_libc = "dpkg -l | grep libc6"
try:
    libc = subprocess.run(update_libc, shell=True, check=True, stdout=subprocess.PIPE)
    check = subprocess.run(check_libc, shell=True, check=True, stdout=subprocess.PIPE)
    print(libc.stdout)
    print(check.stdout)
    
except subprocess.CalledProcessError as e:
    print(f"Error installing libc: {e}")
    
# Check if PortAudio19-Dev is installed
check_command = "dpkg -l | grep portaudio19-dev"

try:
    subprocess.run(check_command, shell=True, check=True, stdout=subprocess.PIPE)
    print("PortAudio19-Dev is already installed.")
except subprocess.CalledProcessError:
    # If the package is not found, install it
    installation_command = "apt-get update && apt-get install -y portaudio19-dev"
    try:
        subprocess.run(installation_command, shell=True, check=True)
        print("PortAudio19-Dev installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing PortAudio19-Dev: {e}")
