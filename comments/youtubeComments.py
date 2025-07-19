# import json
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# import pandas as pd

# # Replace with your API key
# API_KEY = ""
# youtube = build("youtube", "v3", developerKey=API_KEY)

# def get_video_comments(video_id):
#     comments = []
#     next_page_token = None

#     try:
#         while True:
#             response = youtube.commentThreads().list(
#                 part="snippet",
#                 videoId=video_id,
#                 maxResults=100,  # Max allowed per request
#                 pageToken=next_page_token,
#                 textFormat="plainText"
#             ).execute()

#             for item in response["items"]:
#                 top_comment = item["snippet"]["topLevelComment"]["snippet"]
#                 comment_data = {
#                     "video_id": video_id,
#                     "text": top_comment["textDisplay"],
#                     "timestamp": top_comment["publishedAt"]
#                 }
#                 comments.append(comment_data)

#             next_page_token = response.get("nextPageToken")
#             if not next_page_token:
#                 break

#     except HttpError as e:
#         print(f"An HTTP error occurred: {e}")
    
#     return comments

# def save_to_json(data, filename="youtube_comments.json"):
#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)

# def save_to_excel(data, filename="youtube_comments.xlsx"):
#     df = pd.DataFrame(data)
#     df.to_excel(filename, index=False, engine="openpyxl")

# # === Run ===
# video_id = "p-7c0gADuIc"
# comments = get_video_comments(video_id)

# # Optional: print comments
# for c in comments:
#     print(f"{c['timestamp']} — {c['text']}")

# # Save to JSON
# save_to_json(comments)
# print("✅ Saved comments to youtube_comments.json")

# # Save to Excel
# save_to_excel(comments)
# print("✅ Saved comments to youtube_comments.xlsx")

import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd

# Replace with your API key
API_KEY = ""
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_video_comments(video_id, max_comments=100):
    comments = []
    next_page_token = None

    try:
        while len(comments) < max_comments:
            response = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=min(100, max_comments - len(comments)),  # Fetch only needed comments
                pageToken=next_page_token,
                textFormat="plainText"
            ).execute()

            for item in response["items"]:
                top_comment = item["snippet"]["topLevelComment"]["snippet"]
                comment_data = {
                    "video_id": video_id,
                    "text": top_comment["textDisplay"],
                    "timestamp": top_comment["publishedAt"]
                }
                comments.append(comment_data)

            next_page_token = response.get("nextPageToken")
            if not next_page_token or len(comments) >= max_comments:
                break

    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
    
    return comments[:max_comments]  # Ensure exactly max_comments are returned

def save_to_json(data, filename="youtube_comments.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def save_to_excel(data, filename="youtube_comments.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, engine="openpyxl")

# === Run ===
video_id = "UrWZVJkvFpI"
comments = get_video_comments(video_id, max_comments=100)

# Optional: print comments
for c in comments:
    print(f"{c['timestamp']} — {c['text']}")

# Save to JSON
save_to_json(comments)
print("✅ Saved comments to youtube_comments.json")

# Save to Excel
save_to_excel(comments)
print("✅ Saved comments to youtube_comments.xlsx")
