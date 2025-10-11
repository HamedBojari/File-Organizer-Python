import os
import shutil

SOURCE_DRIVE = "D:\\"  
DEST_FOLDER = "D:\\OrganizedFiles" 

folders = {
    "photos": os.path.join(DEST_FOLDER, "Photos"),
    "movies": os.path.join(DEST_FOLDER, "Movies"),
    "music": os.path.join(DEST_FOLDER, "Music")
}

for path in folders.values():
    os.makedirs(path, exist_ok=True)

photo_ext = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".heic", ".webp")
movie_ext = (".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv")
music_ext = (".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a")


count = {"photos": 0, "movies": 0, "music": 0}

print("...")

for root, dirs, files in os.walk(SOURCE_DRIVE):
    for file in files:
        ext = file.lower().endswith
        src_path = os.path.join(root, file)
        try:
            if ext(photo_ext):
                shutil.move(src_path, folders["photos"])
                count["photos"] += 1
            elif ext(movie_ext):
                shutil.move(src_path, folders["movies"])
                count["movies"] += 1
            elif ext(music_ext):
                shutil.move(src_path, folders["music"])
                count["music"] += 1
        except Exception as e:
            
            print(f"⛔️ Eror {file}: {e}")

print("\n✅ Done!")
print(f"📸 : {count['photos']}")
print(f"🎬 : {count['movies']}")
print(f"🎵 : {count['music']}")
