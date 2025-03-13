#!/usr/bin/env python3

import os
import subprocess
import click

# Directory for cloning tools
TOOLS_DIR = os.path.expanduser("./AD_Tools")  # or any other directory you want

# List of tools to install (pipx supported and non-pipx)
TOOLS = {
    "AutoRecon": "https://github.com/Tib3rius/AutoRecon.git",
    "bloodyAD": "https://github.com/CravateRouge/bloodyAD.git",
    "impacket": "https://github.com/ThePorgs/impacket.git",
    "NetExec": "https://github.com/Pennyw0rth/NetExec",
    "powerview.py": "https://github.com/aniqfakhrul/powerview.py.git",
    "pywerview": "https://github.com/the-useless-one/pywerview.git",
    "pywhisker": "https://github.com/ShutdownRepo/pywhisker.git",
    "targetedKerberoast": "https://github.com/ShutdownRepo/targetedKerberoast.git",
    "Coercer": "https://github.com/p0dalirius/Coercer.git",
    "certipy": "https://github.com/ly4k/Certipy.git",
    "GPOditty": "https://github.com/synacktiv/GPOddity.git",
    "GoldenCopy": "https://github.com/Dramelac/GoldenCopy.git",
    "dploot": "https://github.com/zblurx/dploot.git",
    "DonPAPI": "https://github.com/login-securite/DonPAPI.git",
    "ASRepCatcher": "https://github.com/Yaxxine7/ASRepCatcher.git", 
    "enum4linux-ng": "https://github.com/cddmp/enum4linux-ng.git",
    "ADcheck": "https://github.com/CobblePot59/ADcheck.git",
    "aclpwn.py": "https://github.com/fox-it/aclpwn.py.git",
    "abuseACL": "https://github.com/AetherBlack/abuseACL.git",
    "wafw00f": "https://github.com/EnableSecurity/wafw00f",
    "smbclient-ng": "https://github.com/p0dalirius/smbclient-ng.git",
    "BloodHound.py": "https://github.com/dirkjanm/BloodHound.py.git",
    "dirsearch": "https://github.com/maurosoria/dirsearch.git",
    "tldr": "https://github.com/tldr-pages/tldr.git",
    "autobloody": "https://github.com/CravateRouge/autobloody.git",
    "pypykatz": "https://github.com/skelsec/pypykatz.git"

}

def run_command(command):
    """Executes a shell command and returns the result."""
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0

def ensure_pipx():
    """Ensures pipx is installed and configured."""
    click.secho("🔍 Checking pipx installation...", fg="cyan")
    if not run_command("command -v pipx"):
        click.secho("⚠️  pipx not found. Installing it now...", fg="yellow")
        run_command("sudo apt update && sudo apt install -y pipx python3-venv")
    run_command("pipx ensurepath")
    click.secho("✅ pipx is ready!", fg="green")

def clone_or_update_repo(name, url, update):
    """Clones or updates a git repository."""
    repo_path = os.path.join(TOOLS_DIR, name)
    
    if os.path.exists(repo_path):
        if update:
            click.secho(f"🔄 Updating {name}...", fg="yellow")
            run_command(f"git -C {repo_path} pull")
        else:
            click.secho(f"⚡ {name} already cloned. Skipping...", fg="blue")
    else:
        click.secho(f"📥 Cloning {name}...", fg="cyan")
        run_command(f"git clone {url} {repo_path}")

    return repo_path

def install_tool(name, repo_path, update):
    """Installs a tool using pipx if possible, otherwise installs its requirements."""
    click.secho(f"🚀 Installing {name}...", fg="green")
    
    if update:
        run_command(f"pipx install --force {repo_path}")
    else:
        run_command(f"pipx install {repo_path}")

    # If there's a requirements.txt, install dependencies using pipx runpip
    req_file = os.path.join(repo_path, "requirements.txt")
    if os.path.exists(req_file):
        click.secho(f"📦 Installing dependencies for {name}...", fg="magenta")
        run_command(f"pipx runpip {name} install -r {req_file}")

@click.command()
@click.option('--update-tools', is_flag=True, help="Update/reinstall all tools.")
def install_tools(update_tools):
    """Clones, installs, and updates tools as needed."""
    
    ensure_pipx()

    # Ensure TOOLS_DIR exists
    os.makedirs(TOOLS_DIR, exist_ok=True)

    for name, url in TOOLS.items():
        repo_path = clone_or_update_repo(name, url, update_tools)
        install_tool(name, repo_path, update_tools)

    click.secho("\n🎉 All tools installed successfully!", fg="bright_green")

if __name__ == "__main__":
    install_tools()
