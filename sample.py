import csv
import os
import googleapiclient.discovery 
from dotenv import load_dotenv
load_dotenv()


def youtube_search(api_key, query, max_results):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    
    request = youtube.search().list(
        q=query,
        maxResults = max_results,
        part="id,snippet"
    )
    
    video_list = []
    
    responses = request.execute()
    
    for response in responses.get("items"):
        if response["id"]["kind"] == "youtube#video":
            video_title = response["snippet"]["title"]
            video_description = response["snippet"]["description"]
            channel_title = response["snippet"]["channelTitle"]
            video_id = response["id"]["videoId"]
            channel_id = response["snippet"]["channelId"]
            thumbnail_url = response["snippet"]["thumbnails"]["default"]["url"]

            video_statistics = youtube.videos().list(
                part = 'statistics',
                id = video_id
            ).execute()
            
            view_count = video_statistics["items"][0]["statistics"]["viewCount"]
            video_list.append([video_title, video_description, video_id, view_count, channel_title, channel_id, thumbnail_url])

    print(video_list)
    return video_list

    
# Function to save results to a CSV file
def save_to_csv(videos, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Video_Title', 'Video_Description', 'Video_Id', 'View_Count', 'Channel_Title', 'Channel_Id', 'Thumbnail_Url'])
        for video in videos:
            writer.writerow(video)

# Main script
def main():
    api_key = os.getenv('API_KEY')
    queries = ['Children Education', 'Education Technology']
    max_results = 100
    
    video_list = []
    
    for query in queries:
        videos = youtube_search(api_key, query, max_results)
        video_list.extend(videos)
        
    save_to_csv(video_list, 'youtube_edu_videos.csv')

if __name__ == '__main__':
    main()
