from sanic import Sanic
from sanic.response import file, json
import yt_dlp
import hashlib
import os.path

app = Sanic("simple-ytdl-server")


@app.route("/")
async def download(request):
    url = request.args.get("url")

    if url is None:
        return json({"error": "no url provided"}, status=400)

    filename = hashlib.md5(url.encode("utf-8")).hexdigest() + ".mp4"
    path = f"./files/{filename}"

    if os.path.isfile(path):
        return await file(path)

    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "outtmpl": path
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
        return await file(path, filename=filename)
    except yt_dlp.utils.DownloadError:
        return json({"error": "could not download file"}, status=400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
