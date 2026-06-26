# ==========================================
# NODE HUFFMAN TREE
# Setiap node menyimpan karakter dan frekuensinya
# ==========================================

class Node:

    # Constructor
    def __init__(self, char, freq):

        # Karakter
        self.char = char

        # Frekuensi karakter
        self.freq = freq

        # Anak kiri
        self.left = None

        # Anak kanan
        self.right = None

    # Mengecek apakah node merupakan daun
    def is_leaf(self):

        return self.left is None and self.right is None