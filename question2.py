from PIL import Image
import os

def compress_lossless(input_path, output_path):
    with Image.open(input_path) as img:
        print("Original size:", img.size)
        print("Original mode:", img.mode)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(output_path, format='WEBP', lossless=True, method=6)

        print("Compressed size:", os.path.getsize(output_path), "bytes")

compress_lossless("original_10x10.png", "compressed.webp")
