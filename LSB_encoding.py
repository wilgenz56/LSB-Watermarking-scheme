import cv2
import numpy as np

map_pixels = [] 

def embed_watermark(map_list, watermark):
    byte_data = watermark.encode('utf-8')
    watermark_binario = "".join(f"{b:08b}" for b in byte_data)

    # Carichiamo l'immagine 
    img = cv2.imread('img.jpg')
    if img is None:
        print("Errore: Immagine non trovata!")
        return

    for bit in watermark_binario:
        while True:
            x = np.random.randint(0, img.shape[0])
            y = np.random.randint(0, img.shape[1])
            if (x, y) not in map_list:
                map_list.append((x, y))
                break
        
        pixel = img[x, y].copy()
        
        pixel[0] = (int(pixel[0]) & 254) | int(bit)

        img[x, y] = pixel

    # Salviamo l'immagine con il watermark
    cv2.imwrite('img_watermarked.png', img)
    print("Watermark inserito con successo in img_watermarked.png")

def extract_watermark(map_list, length):
    # Leggiamo l'immagine salvata in PNG
    img = cv2.imread('img_watermarked.png')
    bits = ""
    
    for i in range(length * 8):
        x, y = map_list[i]
        pixel = img[x, y]
        # Estraiamo solo l'ultimo bit
        bit = pixel[0] & 1
        bits += str(bit)

    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        byte_array.append(int(byte, 2))

    try:
        return byte_array.decode('utf-8')
    except UnicodeDecodeError:
        return "Errore di decodifica: i dati estratti sono corrotti."

# Test
mappa = []
testo = "c"
embed_watermark(mappa, testo)
estratto = extract_watermark(mappa, len(testo))

print(f"Mappe usate per l'embedding: {mappa}")

print(f"Originale: {testo}")
print(f"Estratto:  {estratto}")