import os
import ctypes
import random
from datetime import datetime

def get_random_image(folder_path):
    """Select a random image from the specified folder."""
    images = [img for img in os.listdir(folder_path) if img.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
    if images:
        return os.path.join(folder_path, random.choice(images))
    return None

def set_wallpaper(image_path):
    """Set the specified image as the desktop wallpaper."""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def main():
    # Folder containing your wallpaper images
    folder_path = r"C:\Users\Alexander Joossens\Documents\Github\wallpaper-changer\images"
    
    # Get a random image from the folder
    image_path = get_random_image(folder_path)
    
    if image_path:
        # Set the selected image as the wallpaper
        set_wallpaper(image_path)
        print(f"Wallpaper set to: {image_path}")
    else:
        print("No images found in the folder.")

if __name__ == "__main__":
    main()
