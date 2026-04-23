import cv2
import numpy as np

def preprocess_image(image_path):
    # load the image using opencv
    img = cv2.imread(image_path)
    
    # convert to grayscale because color doesn't matter for reading text
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # resize the image to make the text bigger, helps OCR read it better
    # multiplying width and height by 2
    resized = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
    # apply thresholding to make the text pure black and background pure white
    # this removes shadows and weird lighting
    _, thresh = cv2.threshold(resized, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # returning the processed image so we can pass it to tesseract later
    return thresh
