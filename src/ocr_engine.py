import pytesseract
from PIL import Image

def extract_text_from_image(processed_img_array):
    # pytesseract expects a PIL image, but opencv gives us a numpy array
    # so we need to convert it first
    pil_img = Image.fromarray(processed_img_array)
    
    # run tesseract on the image. 
    # config '--psm 6' means assume a single uniform block of text.
    # it works best for reading single words or short phrases like a prescription
    raw_text = pytesseract.image_to_string(pil_img, config='--psm 6')
    
    # clean up the text by removing extra spaces or newlines at the end
    clean_text = raw_text.strip()
    
    return clean_text
