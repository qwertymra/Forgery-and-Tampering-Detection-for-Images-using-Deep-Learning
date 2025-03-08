import os

# Define the directory path
directory_path = 'CASIA2/masks/'

# Check if the directory exists
if not os.path.exists(directory_path):
    print(f"The directory {directory_path} does not exist.")
else:
    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # If the file does not end with "_gt.png"
        if not filename.endswith("_gt.png"):
            # Split the filename into name and extension
            name, extension = os.path.splitext(filename)
            # Create a new filename with "_gt.png" at the end
            new_filename = name + "_gt.png"
            # Rename the file
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))

    print("All files in the directory have been renamed to end with _gt.png.")
