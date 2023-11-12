# -*- coding: utf-8 -*-

import cv2
import easyocr
import time
import argparse

def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    return cv2.resize(image, (width, height))

def detect_currency_symbol(image_path, list_symbols, languages,image_rescale):
    try:
        image = cv2.imread(image_path)
        resized_image = resize_image(image,image_rescale)
        gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        reader = easyocr.Reader(languages)
        results = reader.readtext(gray)

        detected_symbols = [symbol for symbol in list_symbols if any(symbol in result[1] for result in results)]

        return detected_symbols

    except Exception as e:
        raise e

def main():
    parser = argparse.ArgumentParser(description='Detect currency symbols in an image using EasyOCR.')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--symbols', nargs='+', default=['$', '€', '£', '¥', '₹','د.ك','₣','AED', 'INR','USD','CAD'],help='List of currency symbols to detect')
    parser.add_argument('--languages', nargs='+', default=['en', 'ar'], help='List of OCR languages')
    parser.add_argument('--image_rescale',nargs='+', default=50,help='Rescalable Image size')
    args = parser.parse_args()

    detected_symbols = detect_currency_symbol(args.image_path, args.symbols, args.languages, args.image_rescale)

    if detected_symbols:
        print(detected_symbols)
    else:
        print("No currency symbols detected.")

if __name__ == '__main__':
    main()
