import os
import sys
from distutils.sysconfig import get_python_lib
import site
from setuptools import setup

def print_progress(message):
    """Prints a progress message to the standard output."""
    sys.stdout.write(f"{message}\n")
    sys.stdout.flush()

# Determine if we should allow editable install into the user site directory.
print_progress("Checking for user site directory installation option...")
site.ENABLE_USER_SITE = "--user" in sys.argv

# Flag to indicate if we should display a warning about potential overlay issues
overlay_warning = False

if "install" in sys.argv:
    print_progress("Installation detected. Checking for existing Django installations...")

    # List of possible library paths to check for existing installations
    lib_paths = [get_python_lib()]

    # Add /usr/local to the list of paths to handle custom Debian installations
    if lib_paths[0].startswith("/usr/lib/"):
        lib_paths.append(get_python_lib(prefix="/usr/local"))

    # Check each library path for existing Django installations
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "django"))
        if os.path.exists(existing_path):
            # Flag to display warning if Django is already installed
            overlay_warning = True
            print_progress(f"Existing Django installation found at: {existing_path}")
            break

# Set up the package using setuptools
print_progress("Setting up the package with setuptools...")
setup()

# Display a warning if an existing Django installation was detected
if overlay_warning:
    sys.stderr.write(
        """
========
WARNING!
========

You have just installed Django over an existing installation without removing it first.
This may result in your install containing outdated or extraneous files from a previous version, which can lead to various issues.

To resolve this, manually remove the following directory and then reinstall Django:

%(existing_path)s

"""
        % {"existing_path": existing_path}
    )
    print_progress("Warning issued. Please follow the instructions above to avoid potential issues.")
else:
    print_progress("Installation completed successfully.")
