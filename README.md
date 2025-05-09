# Biblioteca de Supervivencia

Una aplicación web ligera para Raspberry Pi Zero 2W que sirve como biblioteca de conocimiento de supervivencia.

## Características

- Reproducción de contenido multimedia (texto, imágenes, audio, video)
- Interfaz simple y ligera
- Organización por categorías
- Compatible con Raspberry Pi Zero 2W

## Estructura de Carpetas

El contenido se organiza en las siguientes carpetas:

- `content/books/` - Libros y documentos
- `content/audio/` - Archivos de audio
- `content/videos/` - Archivos de video
- `content/images/` - Imágenes
- `content/text/` - Archivos de texto

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

2. Crear las carpetas de contenido (se crearán automáticamente al iniciar la aplicación)

3. Iniciar la aplicación:
```bash
python app.py
```

4. Acceder a la aplicación desde un navegador web:
```
http://[IP-DE-TU-RASPBERRY-PI]:8080
```

## Uso

1. Coloca los archivos en las carpetas correspondientes según su tipo
2. Accede a la aplicación desde cualquier navegador web
3. Navega por las diferentes categorías
4. Haz clic en cualquier archivo para verlo o reproducirlo

## Formatos Soportados

- Texto: .txt, .pdf, .doc, .docx
- Imágenes: .jpg, .jpeg, .png, .gif
- Audio: .mp3, .wav, .ogg
- Video: .mp4, .webm

## Notas

- La aplicación está optimizada para funcionar en Raspberry Pi Zero 2W
- Se recomienda usar archivos de tamaño moderado para mejor rendimiento
- La interfaz es responsive y funciona en dispositivos móviles 