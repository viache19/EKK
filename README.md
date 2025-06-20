# Emergency Knowledge Kit (EKK)

A visual and responsive multimedia library, designed to run efficiently on a Raspberry Pi Zero 2W. It allows browsing and viewing multimedia files and folders from any device (PC, tablet, mobile) connected to the local network.

## Features
- Simple and visual navigation through multimedia folders and files (videos, images, audio, PDFs, etc.)
- Modern, responsive interface built with Tailwind CSS
- Compatible with desktops, tablets, and mobile devices
- Breadcrumbs for quick folder navigation
- Highlighted Home button next to the title to return to the root directory
- Direct preview of images and videos, with option to open files in a new tab
- No heavy dependencies: only Flask and Tailwind CDN
- Optimized for low resource consumption and ideal for use on Raspberry Pi Zero 2W

## Folder Structure
Place all your multimedia content inside the `content` folder at the root of the project. You can freely create subfolders. The code will process them automatically without needing any changes.


```
content/
├── Movies/
│   ├── movie1.mp4
│   └── cover.jpg
├── Books/
│   └── book1.pdf
├── Music/
│   └── song.mp3
└── ...
```

## Supported File Formats
- Images: ".jpg", ".jpeg", ".png", ".gif"
- Video: ".mp4", ".webm", ".mov", ".mkv"
- Audio: ".mp3", ".wav", ".ogg"
- Documents: ".pdf"

Note: Support for these files depends on the browser. Most modern browsers can display the formats listed above without issues.

## Instalation & Usage
1. **Install Flask:**
   ```bash
   pip install flask
   ```
2. **Basic structure:**
   - `app.py` (Flask Server)
   - `templates/index.html` (gallery-style visual interface)
   - `content/` (your multimedia folder)

3. **Run the app:**
   ```bash
   python app.py
   ```
   Access [http://localhost:8080](http://localhost:8080)

## Customization (manual)
- Change the title by editing the corresponding line in  `templates/index.html`.
- You can easily tweak colors and styles using Tailwind.

## Compatibility
- Tested on Chrome, Firefox, Edge, Safari (desktop and mobile)
- Optimized display across all screen sizes
- Specifically optimized for Raspberry Pi Zero 2W

## Credits
- UI based on Tailwind CSS CDN

----
"README generated by AI"🤖💡
