from PIL import Image

def convert_png_to_ico(png_path, ico_path):
    """
    Convert a PNG image to an ICO file.
    :param png_path:
    :param ico_path:
    :return:
    """
    img = Image.open(png_path)
    img.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print(f"Converted {png_path} to {ico_path} successfully.")
    img.close()

def convert_jpg_to_ico(jpg_path, ico_path):
    """
    Convert a JPG image to an ICO file.
    :param jpg_path:
    :param ico_path:
    :return:
    """
    img = Image.open(jpg_path)
    img.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print(f"Converted {jpg_path} to {ico_path} successfully.")
    img.close()

if __name__ == "__main__":
    # png_file = "example.png"  # Replace with your PNG file path
    jpg_file = "profile.jpg"  # Uncomment if you want to convert a JPG file
    ico_file = "favicon.ico"  # Replace with your desired ICO file path
    # convert_png_to_ico(png_file, ico_file)  # Uncomment to convert PNG to ICO
    convert_jpg_to_ico(jpg_file, ico_file)  # Convert JPG to ICO
    # convert_png_to_ico("example.png", "example.ico")  # Uncomment to convert PNG to ICO
