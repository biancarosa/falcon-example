# app.py
import falcon
import json
import middlewares

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

api = falcon.API(middleware=[
    middlewares.require_json.RequireJSONMiddleware(),
    middlewares.json_translator.JSONTranslatorMiddleware(),
    middlewares.auth.AuthMiddleware()
])
api.add_route('/songs', SongsResource())
api.add_route('/song', SongResource())