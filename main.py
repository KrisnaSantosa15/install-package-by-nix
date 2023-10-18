import subprocess

# Check if PortAudio19-Dev is installed
check_command = "nix-env -q portaudio19-dev"

try:
    subprocess.run(check_command, shell=True, check=True, stdout=subprocess.PIPE)
    print("PortAudio19-Dev is already installed.")
except subprocess.CalledProcessError:
    print("PortAudio19-Dev is not installed. Installing...")
    # If the package is not found, install it using Nix
    installation_command = "nix-env -iA nixpkgs.portaudio19-dev"
    try:
        subprocess.run(installation_command, shell=True, check=True)
        print("PortAudio19-Dev installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing PortAudio19-Dev: {e}")
