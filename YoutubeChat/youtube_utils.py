from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

from urllib.parse import urlparse, parse_qs

def get_video_id(url):

    parsed_url = urlparse(url)

    # Case 1: youtu.be short link
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    # Case 2: youtube.com/watch?v=
    if parsed_url.hostname in ("www.youtube.com", "youtube.com"):
        if parsed_url.path == "/watch":
            return parse_qs(parsed_url.query)["v"][0]

        # Case 3: youtube.com/shorts/VIDEO_ID
        if parsed_url.path.startswith("/shorts/"):
            return parsed_url.path.split("/")[2]

        # Case 4: youtube.com/embed/VIDEO_ID
        if parsed_url.path.startswith("/embed/"):
            return parsed_url.path.split("/")[2]

    raise ValueError("Invalid YouTube URL")

    
def fetch_transcript(url):

    video_id = get_video_id(url)

    transcript_list = YouTubeTranscriptApi().fetch(video_id)

    transcript = " ".join(chunk.text for chunk in transcript_list)

    return transcript