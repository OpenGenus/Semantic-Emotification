import easyocr
import emoji
import difflib
import matplotlib.pyplot as plt
import cv2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

keywords = [
    "grinning_face", "grinning_face_with_smiling_eyes", "grinning_face_with_big_eyes",
    "pick", "grinning_squinting_face", "grinning_face_with_sweat",
    "rolling_on_the_floor_laughing", "guitar", "slightly_smiling_face",
    "cloud_with_lightning", "camera", "fog", "wind_face", "droplet",
    "sweat_droplets", "ocean"]

# I have used a very small list of keywords here, a full list of available emojis can be used instead.

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    return filtered_words

def find_closest_keywords(input_words):
    closest_matches = [difflib.get_close_matches(word, keywords, n=1) for word in input_words]
    closest_keywords = [match[0] if match else None for match in closest_matches]
    return closest_keywords

def get_emojis(keywords):
    emojis = [emoji.emojize(f":{keyword}:") for keyword in keywords]
    return [e for e in emojis if e != ':None:']

def perform_ocr(image_path):
    reader = easyocr.Reader(['en'])
    image = cv2.imread(image_path)
    results = reader.readtext(image)
    detected_text = ' '.join([result[1] for result in results])
    return detected_text

def main():
    print("Available keywords: {}".format(", ".join(keywords)))

    image_path = r'C:\Users\KIIT\Downloads\WhatsApp Image 2023-12-31 at 10.29.51_128afb29.jpg'

    detected_text = perform_ocr(image_path)

    if detected_text:
        preprocessed_text = preprocess_text(detected_text)
        closest_keywords = find_closest_keywords(preprocessed_text)
        emojis = get_emojis(closest_keywords)

        print(f"Detected Text: {detected_text}")
        print(f"Preprocessed Text: {preprocessed_text}")
        print(f"Closest Keywords: {closest_keywords}")
        print("Emojis: {}".format(emojis))
    else:
        print("OCR did not detect any text in the image.")

if __name__ == "__main__":
    main()
