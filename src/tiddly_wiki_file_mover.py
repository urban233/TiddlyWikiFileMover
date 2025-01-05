import os
import shutil
import sys

import toml
import re

# Define paths
# Determine the folder where the script or executable is located
if getattr(sys, 'frozen', False):  # Check if the script is running as a PyInstaller bundle
    script_folder = os.path.dirname(sys.argv[0])  # This gets the directory of the executable
else:
    script_folder = os.path.dirname(os.path.realpath(__file__))  # Use current script folder

config_file_path = os.path.join(script_folder, "config.toml")

# Load configuration from the TOML file
config = {}
try:
    config = toml.load(config_file_path)
except Exception as e:
    print(f"Error reading config file: {e}")
    print("Using default settings.")

# Get version information from the config
major_version = config.get('version', {}).get('major', 1)
minor_version = config.get('version', {}).get('minor', 0)

# Get folder paths from the config
download_folder = config.get('folders', {}).get('download_folder', os.path.join(os.path.expanduser("~"), "Downloads"))
target_folder = config.get('folders', {}).get('target_folder', os.path.join(script_folder, "old_versions"))

# Print version information
print(f"Using version: {major_version}.{minor_version}")

# Create the target folder if it doesn't exist
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Loop through all .html files in the script's directory
for filename in os.listdir(script_folder):
    if filename.endswith(".html"):
        filename_prefix = os.path.splitext(filename)[0]  # Extract prefix (filename without extension)

        print(f"Processing files with prefix: {filename_prefix}")

        # Create a subfolder for this prefix inside old_versions folder
        prefix_folder = os.path.join(target_folder, filename_prefix)
        if not os.path.exists(prefix_folder):
            os.makedirs(prefix_folder)

        # Initialize the counter for new filenames
        counter = 1

        # Flag to check if any files are found
        file_found = False

        # Loop through all matching files in the Downloads folder
        for file in os.listdir(download_folder):
            if file.startswith(filename_prefix) and file.endswith(".html"):
                file_found = True
                source_file = os.path.join(download_folder, file)

                # Generate the new filename with version info
                new_file_name = f"{filename_prefix}_v{major_version}.{minor_version}.{counter}.html"
                target_file = os.path.join(prefix_folder, new_file_name)

                # Ensure the new filename is unique (if the file exists in the target folder)
                while os.path.exists(target_file):
                    counter += 1
                    new_file_name = f"{filename_prefix}_v{major_version}.{minor_version}.{counter}.html"
                    target_file = os.path.join(prefix_folder, new_file_name)

                # Move and rename the file
                print(f"Moving file: {source_file} to {target_file}")
                shutil.move(source_file, target_file)

                # Increment the counter
                counter += 1

        # If no files were found for this prefix, inform the user
        if not file_found:
            print(f"No files found in the Downloads folder matching: {filename_prefix}*.html")

# Copy the latest version file into the parent directory
def copy_latest_version_file():
    # Version pattern (vX.Y.Z)
    version_pattern = re.compile(r'_v(\d+)\.(\d+)\.(\d+)')

    latest_version_file = None
    latest_version = None

    # Loop through all folders inside the target folder
    for folder in os.listdir(target_folder):
        folder_path = os.path.join(target_folder, folder)
        if os.path.isdir(folder_path):
            # Loop through all files in the subfolder
            for file in os.listdir(folder_path):
                if file.endswith(".html"):
                    match = version_pattern.search(file)
                    if match:
                        version = tuple(map(int, match.groups()))  # Convert to tuple of integers (X, Y, Z)
                        if latest_version is None or version > latest_version:
                            latest_version = version
                            latest_version_file = os.path.join(folder_path, file)

    if latest_version_file:
        # Copy the latest version file to the parent directory, without version in name
        file_name_without_version = os.path.splitext(os.path.basename(latest_version_file))[0].split('_v')[0]
        latest_version_copy = os.path.join(script_folder, f"{file_name_without_version}.html")
        print(f"Copying the latest version file: {latest_version_file} to {latest_version_copy}")
        shutil.copy2(latest_version_file, latest_version_copy)
    else:
        print("No version files found to copy.")

# Call the function to copy the latest version file
copy_latest_version_file()

print("All files have been processed.")
