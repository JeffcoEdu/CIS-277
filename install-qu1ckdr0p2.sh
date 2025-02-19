#!/bin/bash
# Path to the script
# Get the absolute path of the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Define the relative path to serv.py
SERV_SCRIPT="$SCRIPT_DIR/qu1ckdr0p2/qu1ckdr0p2/serv.py"

# install in pipx env
pipx install cookiecutter
pipx runpip cookiecutter install -r "qu1ckdr0p2/qu1ckdr0p2/requirements.txt"

# pipx install "qu1ckdr0p2/"

# Detect current shell
CURRENT_SHELL=$(basename "$SHELL")

# Determine the correct shell profile file
case "$CURRENT_SHELL" in
    bash)
        SHELL_PROFILE="$HOME/.bashrc"
        ;;
    zsh)
        SHELL_PROFILE="$HOME/.zshrc"
        ;;
    *)
        echo "Unsupported shell: $CURRENT_SHELL"
        exit 1
        ;;
esac

# Define the alias line
ALIAS_LINE="alias serv='python3 \"$SERV_SCRIPT\"'"

# Check if the alias already exists
if grep -qF "$ALIAS_LINE" "$SHELL_PROFILE"; then
    echo "Alias already exists in $SHELL_PROFILE"
else
    echo "$ALIAS_LINE" >> "$SHELL_PROFILE"
    echo "Added alias to $SHELL_PROFILE"
fi

# Reload shell configuration
case "$CURRENT_SHELL" in
    bash)
        source "$HOME/.bashrc"
        ;;
    zsh)
        source "$HOME/.zshrc"
        ;;
esac

echo "Now you can run 'serv' from anywhere."
echo "if you get halo errors, run: pip install --user halo --break-system-packages"