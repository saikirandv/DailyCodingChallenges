#Calculate the total size of files in a directory in bytes
#There is a set of files in the "deps" directory, which is at the same directory level that your code is running in. There are no subdirectories within this "deps" folder.
#Your task: Calculate and return the total number of bytes of the text file sizes within the "deps" directory. Only include text files that end with ".txt" in your calculation. Other files should be ignored.
#Parameters
#No parameters are passed to your function.

import os

def calculate_total_text_file_size():
    # Specify the directory path where the text files are located
    directory_path = "deps"  # Update this to the actual path of the "deps" directory

    # Initialize a variable to store the total size in bytes
    total_size_bytes = 0

    # Iterate through the files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file has a ".txt" extension
        if filename.endswith(".txt"):
            # Get the full file path
            file_path = os.path.join(directory_path, filename)
            
            # Get the file size in bytes
            file_size_bytes = os.path.getsize(file_path)
            
            # Add the file size to the total size
            total_size_bytes += file_size_bytes

    # Return the total size in bytes
    return total_size_bytes

# Call the function to calculate the total size of text files
total_size = calculate_total_text_file_size()
print("Total Size of Text Files in 'deps' Directory:", total_size, "bytes")
