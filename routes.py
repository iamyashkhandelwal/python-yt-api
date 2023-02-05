from pytube import YouTube  
from pytube import Playlist

DOWNLOAD_PATH = "D:/Yash/youtube-downloads";
# PlaylistURL = 'https://youtube.com/playlist?list=PLC3y8-rFHvwiNfZK3QmKLnrPcSAX32INO';


def downloadPlaylistVideos(playlistUrl, downloadPath = DOWNLOAD_PATH):
    playlist = Playlist(playlistUrl)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    # Loop through all videos in the playlist and download them
    try:
      for video in playlist.videos:
          video.streams.filter(res="720p").first().download(downloadPath)
      print('Videos downloaded!')
      return True  
    except Exception as e:
      print('Error downloading - ' + str(e))
      return False


# downloadPlaylistVideos("https://www.youtube.com/watch?v=hGuwdn9mHnc&list=PLJUTYXGp-CH4zDSPpDgOvDHf2Q4XD-Zqu")

def downloadVideo(videoURL, downloadPath = DOWNLOAD_PATH):
    youtubeObject = YouTube(videoURL)
    # youtubeObject = youtubeObject.streams.get_highest_resolution()
    # youtubeObject = youtubeObject.streams.filter(res="1080")
    try:
        youtubeObject.streams.filter(resolution='720p', mime_type='video/mp4').first().download(downloadPath)
        # youtubeObject.download(downloadPath)
        print("Video downloaded!")
        return True
    except Exception as e:
        print("An error has occurred", str(e))
        return False

def downloadAudioOnly(videoURL, downloadPath = DOWNLOAD_PATH):
  youtubeObject = YouTube(videoURL)
  try:
    youtubeObject.streams.filter(only_audio=True).first().download(downloadPath)
    print("Audio downloaded!")
    return True
  except Exception as e:
    print("An error has occurred", str(e))
    return False


  youtubeObject = YouTube(videoURL)
  try:
    youtubeObject.streams.filter(only_video=True).first().download(downloadPath)
    print("Only Video downloaded!")
    return True
  except Exception as e:
    print("An error has occurred", str(e))
    return False

