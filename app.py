from flask import Flask, request, render_template, send_file
import torch
import cv2
import os
from pathlib import Path
from datetime import datetime
from flask import send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load your trained YOLOv5 model once when the app starts
model_path = r"C:\Users\youss\Downloads\cancer_cell_project\ultralytics\yolov5\runs\train\cancer_experiment\weights\best.pt"
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

print("Modèle chargé avec succès")

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def find_latest_detected_image():
    """Trouve la dernière image générée dans le dossier results/exp_*."""
    exp_dirs = sorted(Path(RESULT_FOLDER).glob('exp*'), key=os.path.getmtime, reverse=True)
    print("Dossiers 'exp*' dans 'results':", exp_dirs)
    for exp_dir in exp_dirs:
        image_files = list(exp_dir.glob('*.jpg'))  # on cherche tous les fichiers image
        print(f"Contenu de {exp_dir} : {image_files}")
        if image_files:
            return image_files[0]  # on retourne le premier fichier détecté
    return None


@app.route('/', methods=['GET', 'POST'])
def index():
    detected_img_url = None
    uploaded_img_path = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)

            # Appliquer détection
            results = model(save_path)

            # Timestamp pour nommer le dossier
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            save_dir = os.path.join(RESULT_FOLDER, f'exp_{now}')
            os.makedirs(save_dir, exist_ok=True)

            # Récupérer l'image annotée (numpy array)
            img_annotated = results.render()[0]

            # Convertir RGB -> BGR
            img_annotated = cv2.cvtColor(img_annotated, cv2.COLOR_RGB2BGR)

            # Sauvegarder dans results/exp_<timestamp>/
            annotated_path = os.path.join(save_dir, filename)
            cv2.imwrite(annotated_path, img_annotated)

            # URL accessibles par Flask
            detected_img_url = f"/results/exp_{now}/{filename}"
            uploaded_img_path = f"/uploads/{filename}"

    return render_template('index.html', detected_img=detected_img_url, uploaded_img=uploaded_img_path)



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename))

@app.route('/results/<path:filename>')
def serve_detected_image(filename):
    return send_from_directory('results', filename)


if __name__ == '__main__':
    app.run(debug=True)
