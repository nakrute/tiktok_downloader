import json
import requests

with open('# TODO', 'r') as f:
    data = json.load(f)

video_list = [v["Link"] for v in data["Video"]["Videos"]["VideoList"]]
output_folder = # TODO

video_list = video_list[:2]
for video_url in video_list:
    video_file_name = f"{output_folder}/{video_url[-27:]}.mp4"
    try:
        # Send a GET request to the URL
        response = requests.get(video_url, stream=True)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    
        # Save the video to a file
        with open(video_file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    
        print(f"Video downloaded successfully and saved as '{video_file_name}'")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
