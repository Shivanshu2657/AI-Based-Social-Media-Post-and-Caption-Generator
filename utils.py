from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load BLIP model and processor from local Hugging Face cache path
processor = BlipProcessor.from_pretrained(
    r"C:\Users\HP\.cache\huggingface\hub\models--Salesforce--blip-image-captioning-base\snapshots\82a37760796d32b1411fe092ab5d4e227313294b"
)
model = BlipForConditionalGeneration.from_pretrained(
    r"C:\Users\HP\.cache\huggingface\hub\models--Salesforce--blip-image-captioning-base\snapshots\82a37760796d32b1411fe092ab5d4e227313294b"
)

def generate_caption(image_path):
    """Generate a caption from an image file path."""
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def categorize_caption(caption):
    """Simple rule-based categorization from caption text."""
    caption = caption.lower()
    if "dog" in caption or "cat" in caption:
        return "Pets"
    elif "beach" in caption or "mountain" in caption:
        return "Travel"
    elif "food" in caption or "pizza" in caption:
        return "Food"
    elif "car" in caption or "bike" in caption:
        return "Automobile"
    else:
        return "Lifestyle"
