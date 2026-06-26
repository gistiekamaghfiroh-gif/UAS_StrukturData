# ==========================================
# DECODER
# Mengubah kode Huffman menjadi teks asli
# ==========================================

def decode(encoded, root):

    hasil = ""

    # Mulai dari root Huffman Tree
    current = root

    # Membaca setiap bit
    for bit in encoded:

        # Jika 0 pindah ke kiri
        if bit == "0":

            current = current.left

        # Jika 1 pindah ke kanan
        else:

            current = current.right

        # Jika sampai daun,
        # berarti ditemukan satu karakter
        if current.left is None and current.right is None:

            hasil += current.char

            # Kembali ke root
            current = root

    return hasil