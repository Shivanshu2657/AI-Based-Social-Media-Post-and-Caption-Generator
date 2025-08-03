Social Media Post & Caption Generator (AI-Powered)

This is a Flask-based web application that automatically generates captions for uploaded images using an AI image captioning model (BLIP). It categorizes the caption into tags like `Travel`, `Food`, `Pets`, etc., to help with social media content creation.

----------------------------------------------------------------------

 Features

- 🖼️ Upload an image and get a smart AI-generated caption
- 📂 Offline Hugging Face BLIP model support
- 🔖 Auto-categorize content into lifestyle topics
- 🧠 Powered by `transformers`, `torch`, and `Pillow`
- 🎨 Fully functional in a single-page HTML frontend
- 📁 Uploads saved in `static/uploads/`

------------------------------------------------------------------------

🗂️ Project Structure
Social_Media_Post_Generator/
├── static/
│ └── uploads/ # Uploaded images saved here
├── templates/
│ └── index.html # Main HTML frontend
├── utils.py # Caption generation & categorization logic
├── app.py # Flask backend application
├── requirements.txt # Python dependencies
└── README.md
-------------------------------------------------------------------------

 Setup Instructions

1. Create Virtual Environment:
    python -m venv venv
    source venv/bin/activate     # On Linux/Mac
    venv\Scripts\activate        # On Windows
  
2. Install Dependencies
   pip install -r requirements.txt

3. Download & Place Offline BLIP Model
Download the BLIP model from Hugging Face: https://huggingface.co/Salesforce/blip-image-captioning-base

4. 🏃 Run the Flask App
   python app.py
Important:
Hugging Face Model is Loaded Locally
This project uses the Salesforce/blip-image-captioning-base model from Hugging Face via a local directory, not downloaded at runtime.
To ensure the app runs correctly:

Make sure the model files are located at:
hf_model/Salesforce/blip-image-captioning-base/

This folder must include files like:

config.json
preprocessor_config.json
ytorch_model.bin
etc.

If deploying the project (e.g. on Render), ensure the hf_model/ folder is included in the repository and accessible.

⚠️ Do not rely on internet access to fetch the model dynamically. This project loads the model strictly from disk.
---------------------------------------------------------------------------

Technologies Used:
 1. Frontend Technologies
    HTML
    CSS
    JavaScript
    Canvas API
    Audio API
 2.AI / ML Components
     BLIP (Salesforce)
     Image Categorization
 3.Flask (Python Web Framework)
 4.Hugging Face Transformers (BLIP model)
 5.PyTorch (for model execution)
 6.Pillow (image preprocessing)
-----------------------------------------------------------------------------

Example Usage:

1.Upload an image
2.AI generates a caption like:
3."A dog running on the beach during sunset"
4.Category: Pets, Travel
5.Use this for social media posts or inspiration!
------------------------------------------------------------------------------

Working Images:-
<img width="1366" height="768" alt="Screenshot (79)" src="https://github.com/user-attachments/assets/3bfdadae-89c2-4e09-b643-cbc01ec89442" />
<img width="1366" height="768" alt="Screenshot (80)" src="https://github.com/user-attachments/assets/7ed026e5-5b13-4a55-a977-df8571f4aa45" />

-------------------------------------------------------------------------------

 Notes:
 
=>This app runs fully offline once the BLIP model is cached locally.
=>All uploads are stored in /static/uploads — clean regularly if needed.
=>Works best with clear, well-lit images.
------------------------------------------------------------------------------

Author:-
Shiavnshu Kumar Chaubey - built for learning AI + Web Development

