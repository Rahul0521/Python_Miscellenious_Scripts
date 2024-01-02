import easyocr


def scan_image(image_path):
    # Create an OCR reader using the language of your choice
    reader = easyocr.Reader(['en'])

    # Perform OCR on the image
    result = reader.readtext(image_path)

    # Extract and print the recognized text
    for detection in result:
        text = detection[1]
        print(text)


if __name__ == "__main__":
    image_path = r"C:\Users\RAHUL\PycharmProjects\GooglePDFChatBot\t1.jpg"  # Replace with the actual path to your image
    scan_image(image_path)
