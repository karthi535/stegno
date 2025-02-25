import cv2
import os

def encode_message(image_path, output_path, message, password):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found!")
        return
    
    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}
    
    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = d[char]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    
    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")  # Open the image on Windows
    print("Message encoded successfully!")

def decode_message(image_path, password, original_password, message_length):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found!")
        return
    
    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}
    
    if password == original_password:
        message = ""
        n, m, z = 0, 0, 0
        for _ in range(message_length):
            message += c[img[n, m, z]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % 3
        print("Decryption message:", message)
    else:
        print("YOU ARE NOT AUTHORIZED!")

if __name__ == "__main__":
    image_path = input("Enter image path: ")
    output_path = "encryptedImage.jpg"
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    encode_message(image_path, output_path, message, password)
    
    pas = input("Enter passcode for Decryption: ")
    decode_message(output_path, pas, password, len(message))
