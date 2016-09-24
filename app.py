# app.py
import falcon
import json


class SongsResource:
    def on_get(self, req, resp):
        songs = [
            {
                "title": "Your Song", "artist": "Elton John"
            },
            {
                "title": "I Want To Break Free", "artist": "Queen"
             }
        ]
        resp.body = json.dumps(songs)

class SongResource:
    def on_get(self, req, resp):
        song = {
            "title": "Your Song", "artist": "Elton John"
        }
        resp.body = json.dumps(song)

api = falcon.API()
api.add_route('/songs', SongsResource())
api.add_route('/song', SongResource())