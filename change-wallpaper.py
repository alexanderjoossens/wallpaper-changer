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

def get_wallpaper_for_time(current_hour):
    """Select the appropriate wallpaper based on the current hour."""
    if 6 <= current_hour < 12:
        return 'morning.jpg'
    elif 12 <= current_hour < 18:
        return 'noon.jpg'
    elif 18 <= current_hour < 22:
        return 'evening.jpg'
    else:
        return 'night.jpg'
    
def set_wallpaper(image_path):
    """Set the specified image as the desktop wallpaper."""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def main():
    # Folder containing your wallpaper images
    folder_path = r"C:\Users\Alexander Joossens\Documents\Github\wallpaper-changer\images"
    
    # Get the current hour
    current_hour = datetime.now().hour
    
    # Determine the appropriate wallpaper based on the time of day
    wallpaper_filename = get_wallpaper_for_time(current_hour)
    wallpaper_path = os.path.join(folder_path, wallpaper_filename)
    
    if os.path.exists(wallpaper_path):
        # Set the selected image as the wallpaper
        set_wallpaper(wallpaper_path)
        print(f"Wallpaper set to: {wallpaper_path}")
    else:
        print(f"Wallpaper file not found: {wallpaper_path}")

if __name__ == "__main__":
    main()
