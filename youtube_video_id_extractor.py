import re
def video_id(url: str) -> str:
    regex = re.compile(r"(?:v=|\/)([0-9A-Za-z_-]{11})")
    match = regex.search(url)
    if match:
        return match.group(1)
    else:
        raise ValueError(f"Invalid YouTube URL: {url}")
