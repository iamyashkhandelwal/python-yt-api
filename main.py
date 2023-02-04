from flask import Flask, jsonify, request
from routes import  downloadVideo, downloadAudioOnly, downloadVideoOnly, downloadPlaylistVideos
app = Flask(__name__)

@app.route('/')
def index():
  print('request-data -> ', request.get_json()['link'])
  videoURL = request.get_json()['link']
  return 'Welcome to Home Page!'

@app.route('/about')
def about():
  res = {
    "page": "about",
    "Server IP": "127.0.0.1",
    "test": True,
  }
  return jsonify(res)

@app.route('/downloadYoutubeVideo')
def downloadYoutubeVideo():
  videoURL = request.get_json()['videoLink']
  # downloadPath = request.get_json()['path']
  response = downloadVideo(videoURL)
  # response = downloadAudioOnly(videoURL)
  
  if response:
    return jsonify({
      "code": 200,
      "message": "Your video has been downloaded successfully"
    })
  else:
    return jsonify({
      "code": 404,
      "message": "Couldn't download video"
    })

@app.route('/downloadPlaylist')
def downloadYoutubePlaylist():
  playlistURL = request.get_json()['playlistLink']
  response = downloadPlaylistVideos(playlistURL)
  if response:
    print("Downloaded")
    return jsonify({
      "code": 200,
      "message": "Your playlist downloaded successfully"
    })
  else:
    return jsonify({
      "code": 404,
      "message": "Couldn't download playlist"
    })




if __name__ == '__main__':
  app.run(debug=True)