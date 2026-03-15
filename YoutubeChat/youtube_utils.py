from langchain_community.document_loaders import YoutubeLoader
from urllib.parse import urlparse, parse_qs


def get_video_id(url):

    parsed = urlparse(url)

    if parsed.hostname == "youtu.be":
        return parsed.path[1:]

    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        if parsed.path == "/watch":
            return parse_qs(parsed.query)["v"][0]

    raise ValueError("Invalid YouTube URL")


def fetch_transcript(url):

    video_id = get_video_id(url)

    loader = YoutubeLoader.from_youtube_url(
        f"https://www.youtube.com/watch?v={video_id}",
        add_video_info=False
    )

    docs = loader.load()

    transcript = " ".join(doc.page_content for doc in docs)

    return transcript