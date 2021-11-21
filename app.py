import os, sys
from pytube import YouTube, Search, Playlist


PATH_TO_SAVE = "./downloads"

def main():
    
    if not os.path.isdir(PATH_TO_SAVE):
        os.mkdir(PATH_TO_SAVE)
    url = input("Digite a URL do video ou playlist desejada.\n")
    
    YouTube(url, on_progress_callback=progress_function , use_oauth=False, allow_oauth_cache=True).streams.filter(progressive=True, file_extension='mp4').order_by("resolution").desc().first().download(PATH_TO_SAVE)

def progress_function(stream, chunk, bytes_remaining):
    
    print("Downloaded: " + str(percent(bytes_remaining, stream.filesize)) + "%")
    
def percent(partial, total):
    perc = (float(partial) / float(total)) * float(100)
    return 100 - round(perc , 2)
    
if __name__ == "__main__":
    main()