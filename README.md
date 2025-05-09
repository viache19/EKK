# Emergency Knowledge Kit (EKK)

Una biblioteca multimedia visual y responsive, diseñada para funcionar de manera eficiente en una Raspberry Pi Zero 2W. Permite navegar y visualizar archivos y carpetas multimedia desde cualquier dispositivo (PC, tablet, móvil) conectado a la red local.

## Características
- Navegación sencilla y visual por carpetas y archivos multimedia (videos, imágenes, audio, PDF, etc.)
- Interfaz moderna y responsive basada en Tailwind CSS
- Compatible con ordenadores, tablets y móviles
- Breadcrumbs para navegación rápida entre carpetas
- Botón Home destacado junto al título para volver a la raíz
- Visualización directa de imágenes y videos, y apertura de archivos en nueva pestaña
- Sin dependencias pesadas: solo Flask y Tailwind CDN
- Optimizado para bajo consumo de recursos y uso en Raspberry Pi Zero 2W

## Estructura de carpetas
Coloca todo tu contenido multimedia dentro de la carpeta `content` en la raíz del proyecto. Puedes crear subcarpetas libremente.

```
content/
├── Peliculas/
│   ├── pelicula1.mp4
│   └── portada.jpg
├── Libros/
│   └── libro1.pdf
├── Musica/
│   └── cancion.mp3
└── ...
```

## Instalación y uso
1. **Instala Flask:**
   ```bash
   pip install flask
   ```
2. **Estructura básica:**
   - `app.py` (servidor Flask)
   - `templates/index.html` (interfaz visual tipo galería)
   - `content/` (tu carpeta multimedia)

3. **Ejecuta la app:**
   ```bash
   python app.py
   ```
   Accede a [http://localhost:8080](http://localhost:8080) desde cualquier dispositivo en tu red local.

## Personalización
- Cambia el título editando la línea correspondiente en `templates/index.html`.
- Puedes modificar los colores y estilos fácilmente usando Tailwind.

## Compatibilidad
- Probado en Chrome, Firefox, Edge, Safari (PC y móvil)
- Navegación táctil y con teclado
- Visualización óptima en todos los tamaños de pantalla
- Especialmente optimizado para Raspberry Pi Zero 2W

## Créditos
- UI basada en Tailwind CSS CDN

---
¡Disfruta de tu Emergency Knowledge Kit visual, ligero y accesible en cualquier dispositivo conectado a tu Raspberry Pi Zero 2W! 