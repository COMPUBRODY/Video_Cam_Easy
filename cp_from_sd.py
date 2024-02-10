import os
import shutil

def copy_videos_and_photos(source_directory, videos_directory, photos_directory):
    # Ensure destination directories exist, create them if not
    for directory in [videos_directory, photos_directory]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Iterate through files in the source directory
    for filename in os.listdir(source_directory):
        source_path = os.path.join(source_directory, filename)

        # Check if it's a video file (.mp4) and copy to videos directory
        if filename.lower().endswith('.mp4') and os.path.isfile(source_path):
            destination_path = os.path.join(videos_directory, filename)
            shutil.copy2(source_path, destination_path)
            print(f"Video file '{filename}' copied to '{videos_directory}'")

        # Check if it's a photo file (.jpg) and copy to photos directory
        elif filename.lower().endswith('.jpg') and os.path.isfile(source_path):
            destination_path = os.path.join(photos_directory, filename)
            shutil.copy2(source_path, destination_path)
            print(f"Photo file '{filename}' copied to '{photos_directory}'")

if __name__ == "__main__":
    # Replace these paths with your actual directory paths
    source_directory = "/media/duguid/8765-4321/DCIM/100GOPRO"
    videos_directory = "/media/duguid/GoPro/VIAJES/Los Cabos- La Paz/videos"
    photos_directory = "/media/duguid/GoPro/VIAJES/Los Cabos- La Paz/photos"

    copy_videos_and_photos(source_directory, videos_directory, photos_directory)
