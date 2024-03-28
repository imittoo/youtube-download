import sys
import os
from pytube import YouTube

def download_progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    downloaded = size - bytes_remaining
    percent = (downloaded / size) * 100
    print(f"\rDownloading... {percent:.2f}%", end='', flush=True)

def download_video(url, filename=None):
    yt = YouTube(url, on_progress_callback=download_progress)
    #stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution='360p').first()
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first()

    if stream:
        download_path = os.path.join(os.getcwd(), 'video')
        os.makedirs(download_path, exist_ok=True)
        if filename:
            filepath = os.path.join(download_path, filename)
            stream.download(output_path=download_path, filename=filename)
        else:
            filepath = stream.download(output_path=download_path)
        print("\nDownload completed successfully.")
    else:
        print("\nNo suitable streams found for download.")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python main.py <YouTube_URL> [filename]")
    else:
        url = sys.argv[1]
        if len(sys.argv) == 3:
            filename = sys.argv[2]
            download_video(url, filename)
        else:
            download_video(url)
