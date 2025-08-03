from flask import Flask, render_template, request, send_from_directory
import os
from utils import generate_caption, categorize_caption
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the uploads folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    caption = None
    category = None
    image_path = None
    error = None

    if request.method == "POST":
        if 'image' not in request.files:
            error = "No image uploaded"
        else:
            file = request.files['image']
            if file.filename == '':
                error = "No selected file"
            elif file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                saved_filename = f"{timestamp}_{filename}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], saved_filename)
                file.save(filepath)

                caption = generate_caption(filepath)
                category = categorize_caption(caption)
                image_path = filepath
            else:
                error = "Invalid file type"

    return render_template(
        "index.html",
        caption=caption,
        category=category,
        image_path=image_path,
        error=error
    )

# Serve uploaded files if needed
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
