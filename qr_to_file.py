import cv2
from pyzbar.pyzbar import decode
import os
import base64
import numpy as np

def decode_and_combine(qr_code_folder, num_images):
    decoded_data = ""

    for i in range(1, num_images + 1):
        # Load the QR code image
        qr_code_path = os.path.join(qr_code_folder, f'example_qr_{i}.png')
        img = cv2.imread(qr_code_path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale

        # Decode the QR code
        decoded_objects = decode(img)
        if decoded_objects:
            decoded_data += decoded_objects[0].data.decode('utf-8')

    # Decode base64 data
    binary_data = base64.b64decode(decoded_data)

    # Convert binary data to a numpy array
    binary_array = np.frombuffer(binary_data, dtype=np.uint8)

    # Decode the numpy array as an image
    combined_image = cv2.imdecode(binary_array, cv2.IMREAD_UNCHANGED)

    if combined_image is not None:
        # Save the combined image
        output_file_path = 'combined_output.png'
        cv2.imwrite(output_file_path, combined_image)
        return output_file_path
    else:
        print("Error: Combined image is empty.")
        return None

# Replace this with the actual path to your folder and the total number of images
qr_code_folder = 'test1_output'
num_images = 41
output_file_path = decode_and_combine(qr_code_folder, num_images)

if output_file_path:
    print(f"Combined image saved to: {output_file_path}")
else:
    print("Failed to save the combined image.")
