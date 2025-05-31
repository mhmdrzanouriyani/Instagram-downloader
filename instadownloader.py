import instaloader
import os
import re

URL = input("Enter you instagram URL :").strip()

match = re.search("instagram\.com/(reel|p)/([A-Za-z0-9_-]+)",URL)

if not match :
    raise ValueError("Invalid url instagram ! ")

shortcode = match.group(2)

output_dir = r"D:\instagram dl"
os.makedirs ( output_dir , exist_ok=True)

L = instaloader.Instaloader(
    dirname_pattern=os.path.join(output_dir,"{target}"),
    download_video_thumbnails=False,
    save_metadata=False,
    post_metadata_txt_pattern="" 
)

try :
    post = instaloader.Post.from_shortcode(L.context,shortcode)
    L.download_post(post , target=f"{post.owner_username}_{shortcode}")
    print("✅ Download complete ✅ ")
except Exception as e :
    print("❌Error ❌:" , e)



