# This code converts jpg files to pdf

# Install img2pdf using pip (assuming Python is installed and added to your system's PATH)

pip install img2pdf

# Choosing files manually and converting to pdf

img2pdf image1.jpg image2.jpg -o output.pdf


# You can convert all JPG files in the directory with a single command

img2pdf *.jpg -o output.pdf
