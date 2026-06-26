# ==========================================
# HASH TABLE
# Digunakan untuk menghitung frekuensi setiap karakter
# ==========================================

class HashTable:

    # Constructor
    def __init__(self):
        # Dictionary digunakan sebagai tempat penyimpanan data
        self.table = {}

    # Menambahkan karakter ke Hash Table
    def insert(self, char):

        # Jika karakter sudah ada,
        # maka frekuensinya ditambah 1
        if char in self.table:
            self.table[char] += 1

        # Jika belum ada,
        # maka dibuat dengan nilai awal 1
        else:
            self.table[char] = 1

    # Mengembalikan seluruh data frekuensi
    def get_frequency(self):
        return self.table