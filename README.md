# LSB Watermarking scheme
A simple python code that lets you insert and extract a watermark inside an image using the LSB scheme.

## Implementation
This implementation uses randomized pixel mapping. This adds a layer of obfuscation: even if someone knows steganography was used, they cannot easily retrieve the message without the specific coordinate map used during embedding.

# How it Works
Bit Conversion: The input string is converted into a binary stream (8 bits per character).
Random Selection: For every bit in the message, the algorithm selects a random coordinate (x,y) that hasn't been used yet.

Embedding: The LSB of the blue channel (pixel[0]) is modified using bitwise operations:
  `pixel[0]=(pixel[0] & 254) ∣ bit`

Extraction: To retrieve the message, the algorithm visits the pixels in the exact order stored in the map_list and extracts the LSB:
  `bit=pixel[0] & 1`

# Getting Started
Prerequisites:
- Python 3.x
- OpenCV (opencv-python)
- NumPy

# Installation
`pip install opencv-python numpy`

# Usage Example
```
from LSB_encoding import embed_watermark, extract_watermark

mappa = []
secret_text = "Hidden Message 2026"

# Embed the message
embed_watermark(mappa, secret_text)

# Extract the message (Requires the map and the original string length)
retrieved = extract_watermark(mappa, len(secret_text))
print(f"Decoded Message: {retrieved}")
```
