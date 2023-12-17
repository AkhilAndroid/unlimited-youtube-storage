import qrcode
import base64

def file_to_qr(file_path, qr_code_prefix):
    chunk_size = 500  # Set your desired chunk size

    with open(file_path, 'rb') as file:
        binary_data = file.read()

    # Encode binary data to base64
    base64_data = base64.b64encode(binary_data).decode('utf-8')

    # Calculate the number of chunks
    num_chunks = (len(base64_data) + chunk_size - 1) // chunk_size

    for i in range(num_chunks):
        # Get a chunk of data
        start = i * chunk_size
        end = (i + 1) * chunk_size
        chunk = base64_data[start:end]

        # Create a QR code for the chunk
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(chunk)
        qr.make(fit=True)

        # Save the QR code with a unique filename
        qr_code_path = f'{qr_code_prefix}_{i+1}.png'
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(qr_code_path)

# Example usage
file_path = 'test.png'
qr_code_prefix = 'example_qr'
file_to_qr(file_path, qr_code_prefix)
