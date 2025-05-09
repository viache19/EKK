from flask import Flask, render_template, send_from_directory, Response
import os
from werkzeug.serving import run_simple
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

# Configuración de las carpetas de contenido
CONTENT_FOLDERS = {
    'books': 'content/books',
    'audio': 'content/audio',
    'videos': 'content/videos',
    'images': 'content/images',
    'text': 'content/text'
}

# Crear las carpetas si no existen
for folder in CONTENT_FOLDERS.values():
    os.makedirs(folder, exist_ok=True)

# Cache de archivos para mejorar el rendimiento
file_cache = {}

def get_files(category):
    if category not in file_cache:
        try:
            files = os.listdir(CONTENT_FOLDERS[category])
            file_cache[category] = files
        except Exception:
            file_cache[category] = []
    return file_cache[category]

@app.route('/')
def index():
    content = {category: get_files(category) for category in CONTENT_FOLDERS}
    return render_template('index.html', content=content)

@app.route('/content/<category>/<filename>')
def serve_content(category, filename):
    if category in CONTENT_FOLDERS:
        response = send_from_directory(CONTENT_FOLDERS[category], filename)
        # Configurar headers para mejor rendimiento
        response.headers['Cache-Control'] = 'public, max-age=31536000'
        return response
    return "Archivo no encontrado", 404

if __name__ == '__main__':
    # Usar run_simple en lugar de app.run para mejor rendimiento
    run_simple('0.0.0.0', 8080, app, 
               use_reloader=False,  # Desactivar reloader en producción
               use_debugger=False,  # Desactivar debugger en producción
               threaded=True)       # Habilitar threading para mejor rendimiento 