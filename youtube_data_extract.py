from env import youtube_api_key
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd

api_service_name = "youtube"
api_version = "v3"
output_file = "yt_edmunds_id4.csv"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version,developerKey = youtube_api_key
)

request = youtube.commentThreads().list(
    part="snippet",
    videoId = "UvCtq0u3wrU",
    maxResults = 1000000
)
response = request.execute()

comments = []


for item in response['items']:
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    comment = item['snippet']['topLevelComment']['snippet']
    comments.append([
        comment['authorDisplayName'],
        comment['publishedAt'],
        comment['updatedAt'],
        comment['likeCount'],
        comment['textDisplay']
        ]
    )


df = pd.DataFrame(comments, columns=['author','published_at','updated_at','like_count','text'])
df.to_csv(output_file)





