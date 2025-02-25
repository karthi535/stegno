Steganography with Image Encryption

This project implements a simple steganography tool using OpenCV in Python. It allows users to hide a secret message within an image and retrieve it using a password-based authentication system.

Features

Encrypts a text message into an image using pixel manipulation.

Decrypts and retrieves the message only if the correct password is provided.

Uses OpenCV (cv2) for image processing.

Supports dynamic image sizes.

Requirements

Ensure you have Python installed along with the following dependencies:

pip install opencv-python numpy

Usage

Encoding a Message

Run the script and provide an image path.

Enter a secret message to encode.

Set a password for security.

The encrypted image will be saved as encryptedImage.jpg.

Decoding a Message

Enter the correct password.

The message is retrieved only if authentication succeeds.

Running the Script

python steganography.py

Example

Enter image path: mypic.jpg
Enter secret message: Hello World!
Enter a passcode: mypassword
Message encoded successfully!
Enter passcode for Decryption: mypassword
Decryption message: Hello World!

If the password is incorrect:

YOU ARE NOT AUTHORIZED!

Contribution

Feel free to fork and improve the project. Open a pull request with your enhancements.

License

This project is licensed under the MIT License.

