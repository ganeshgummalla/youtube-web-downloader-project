# file: youtube_bulk_downloader/downloader.py

from pathlib import Path
from typing import List
import yt_dlp


OUTPUT_DIR = Path("downloads")


def prompt_urls() -> List[str]:
    print("Paste YouTube links (one per line).")
    print("Press ENTER on an empty line to start downloading.\n")

    urls: List[str] = []
    while True:
        line = input().strip()
        if not line:
            break
        urls.append(line)

    if not urls:
        raise ValueError("No YouTube links provided")

    return urls


def prepare_output_dir(path: Path) -> None:
    if path.exists() and not path.is_dir():
        raise RuntimeError(f"{path} exists but is not a directory")
    path.mkdir(parents=True, exist_ok=True)


def download_videos(urls: List[str], output_dir: Path) -> None:
    prepare_output_dir(output_dir)

    ydl_opts = {
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "ignoreerrors": True,
        "noplaylist": True,

        # ⭐ IMPORTANT CHANGE
        "restrictfilenames": False,

        # speed
        "concurrent_fragments": 5,
        "retries": 10,
        "fragment_retries": 10,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


def main() -> None:
    urls = prompt_urls()
    download_videos(urls, OUTPUT_DIR)


if __name__ == "__main__":
    main()
