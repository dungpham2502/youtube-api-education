# youtube-api-education

# Project Description
This Python project uses the YouTube Data API to search for videos related to specific queries (e.g., "Children Education", "Education Technology") and saves important information about these videos to a CSV file. The output includes video title, description, video ID, view count, channel title, channel ID, and thumbnail URL.

# Prerequisites
Before running this script, ensure you have the following requirements installed:

Python 3.x
google-api-python-client
python-dotenv

# Installation
To run this script, you need to install necessary Python libraries. You can install these using pip:

`pip install google-api-python-client python-dotenv`

 # Setting Up Your Environment
1. YouTube API Key: You need a YouTube API key to fetch data from YouTube. Follow these steps to obtain it:

* Go to Google Cloud Console.
* Create a new project or select an existing one.
* Enable the YouTube Data API for your project.
* Create credentials (API key) for the project.

2. Environment Variables: Store your API key in a .env file at the root of your project:
* Create a file named .env.
* Add your YouTube API key to it like this:

`API_KEY=your_youtube_api_key
`


# Running the Script
Open your terminal or command prompt.
Navigate to the directory where the script is located.
Run the script:

`python main.py`  # Replace 'main.py' with the name of your script if different

# Output
The script will create a CSV file named youtube_edu_videos.csv in the same directory, containing the fetched video data.