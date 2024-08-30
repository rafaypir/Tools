# This Python script renames image files in a specified directory, ensuring that filenames are zero-padded for correct numerical ordering. It specifically handles JPG files named in the format `imgX.jpg` (e.g., `img1.jpg`, `img2.jpg`, etc.). The script first identifies all JPG files, sorts them numerically, and then renames each file to include leading zeros (e.g., `img01.jpg`, `img02.jpg`). This process is useful for maintaining the correct sequence when processing or converting these images, such as when combining them into a PDF.


import os

# Directory containing your images
directory = 'path/to/your/images'

# List all JPG files
files = [f for f in os.listdir(directory) if f.endswith('.jpg')]

# Sort files numerically based on the digits in the filenames
files.sort(key=lambda f: int(f[3:-4]))

# Rename files with leading zeros
for i, filename in enumerate(files, start=1):
    new_name = f"img{i:02}.jpg"  # Adjust the number of zeros depending on total count
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
)
