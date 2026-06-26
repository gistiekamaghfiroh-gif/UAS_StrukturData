# ==========================================
# ENCODER
# Mengubah teks menjadi kode Huffman
# ==========================================

# Membuat kode Huffman dari Huffman Tree
def build_codes(node, code="", codes=None):

    if codes is None:
        codes = {}

    # Jika node kosong
    if node is None:
        return codes

    # Jika node merupakan daun,
    # simpan kode karakter
    if node.char is not None:
        codes[node.char] = code

    # Rekursif ke anak kiri
    build_codes(node.left, code + "0", codes)

    # Rekursif ke anak kanan
    build_codes(node.right, code + "1", codes)

    return codes


# Mengubah teks menjadi kode biner
def encode(text, codes):

    hasil = ""

    for ch in text:

        hasil += codes[ch]

    return hasil