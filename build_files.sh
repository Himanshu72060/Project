# Define variables for commands
PIP_INSTALL_CMD=pip install -r requirement.txt
COLLECTSTATIC_CMD=python3.10 manage.py collectstatic

# Execute the commands
$PIP_INSTALL_CMD
$COLLECTSTATIC_CMD
