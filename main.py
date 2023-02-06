from flask import Flask, jsonify, request
from routes import  downloadVideo, downloadAudioOnly, downloadPlaylistVideos
import os

app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to Home Page!'

@app.route('/downloadYoutubeVideo')
def downloadYoutubeVideo():
  videoURL = request.get_json()['videoLink']
  # downloadPath = request.get_json()['path']
  response = downloadVideo(videoURL)
  # response = downloadAudioOnly(videoURL)
  if response["downloadUrl"] is not None:
    return jsonify({
      "code": 200,
      "downloadUrl": response["downloadUrl"],
      "message": "Video download URL generated successfully"
    })
  else:
    return jsonify({
      "code": 404,
      "message": "Couldn't generate video download URL"
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
  app.run(debug=True, port=os.getenv("PORT", default=5000))