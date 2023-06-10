import os
from PIL import Image

def convert_image(input_path, output_folder):
    with Image.open(input_path) as im:
        jpeg_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".jpeg")
        im.save(jpeg_path, format="JPEG", quality=100)

def main():
    print("Welcome to JPG to JPEG Converter!")
    while True:
        jpg_folder = input("Enter the path to the folder containing JPG images: ")
        if os.path.exists(jpg_folder):
            break
        else:
            print("The folder does not exist.")
    while True:
        jpeg_folder = input("Enter the path to the folder where converted JPEG images will be saved: ")
        if os.path.exists(jpeg_folder):
            break
        else:
            print("The folder does not exist.")
    # Create the JPEG folder if it doesn't exist yet
    if not os.path.exists(jpeg_folder):
        os.makedirs(jpeg_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            convert_image(input_path, jpeg_folder)
    print("All images converted successfully to JPEG format and saved in the chosen folder!")

if __name__ == "__main__":
    main()

# softy_plug