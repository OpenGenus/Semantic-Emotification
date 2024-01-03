# Semantic-Emotification
## Semantic Emotification with OCR and NLTK

This Python script utilizes EasyOCR, emoji, difflib, and OpenCV to perform Optical Character Recognition (OCR) on an image and then map detected words to a predefined list of emojis. The goal is to identify and display emojis corresponding to the words found in the image.

## Prerequisites
Before running the script, make sure you have the required Python libraries installed. You can install them using the following commands:

```
pip install easyocr emoji difflib matplotlib opencv-python-headless nltk
```

Additionally, download the NLTK data by running the following commands:

```
python -m nltk.downloader stopwords punkt
```

## Usage
* Clone the repository or download the script:

```
git clone https://github.com/AgnivaMaiti/Semantic-Emotification.git
cd emoji-ocr
```

* Place the image you want to analyze in the same directory as the script.

* Open the script in a text editor and modify the image_path variable to point to your image file.

```image_path = 'your_image.jpg'```

* Run the script:

python emoji_ocr.py

## Output
The script will print the detected text, preprocessed text, closest keywords, and corresponding emojis. If OCR does not detect any text in the image, a message stating so will be displayed.

## Notes
* The script uses a small list of predefined keywords for emoji mapping. You can expand the keywords list with more emojis according to your needs.
* Ensure that the image is clear and contains text for accurate OCR results.
