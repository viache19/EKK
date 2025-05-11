from flask import Flask, render_template, send_from_directory, request, abort
import os

app = Flask(__name__)

MEDIA_ROOT = "content"  # Carpeta raíz para los archivos multimedia

def get_items(path=""):
    abs_path = os.path.join(MEDIA_ROOT, path)
    if not os.path.exists(abs_path):
        return [], path
    items = []
    for name in sorted(os.listdir(abs_path)):
        full = os.path.join(abs_path, name)
        if os.path.isdir(full):
            items.append({"name": name, "type": "folder"})
        else:
            ext = os.path.splitext(name)[1].lower()
            if ext in [".jpg", ".jpeg", ".png", ".gif"]:
                ftype = "image"
            elif ext in [".mp4", ".webm", ".mov", ".mkv"]:
                ftype = "video"
            elif ext in [".mp3", ".wav", ".ogg"]:
                ftype = "audio"
            elif ext in [".pdf"]:
                ftype = "pdf"
            else:
                ftype = "file"
            items.append({"name": name, "type": ftype})
    return items, path

@app.route("/")
def index():
    rel_path = request.args.get("path", "").strip("/")
    items, path = get_items(rel_path)
    breadcrumbs = []
    if rel_path:
        parts = rel_path.split("/")
        for i in range(len(parts)):
            breadcrumbs.append({
                "name": parts[i],
                "path": "/".join(parts[:i+1])
            })
    return render_template("index.html", items=items, path=rel_path, breadcrumbs=breadcrumbs)

@app.route("/media/<path:filename>")
def media(filename):
    directory = os.path.join(MEDIA_ROOT, os.path.dirname(filename))
    fname = os.path.basename(filename)
    if not os.path.exists(os.path.join(directory, fname)):
        abort(404)
    return send_from_directory(directory, fname)

if __name__ == "__main__":
    os.makedirs(MEDIA_ROOT, exist_ok=True)
    app.run("0.0.0.0", 8080, debug=True) 