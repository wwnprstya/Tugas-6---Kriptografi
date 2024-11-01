def enkripsi_subtitusi_dengan_modulus(plaintext, kunci):
    # Hilangkan spasi, konversi ke huruf besar, dan buang huruf yang berulang
    plaintext = "".join(dict.fromkeys(plaintext.replace(" ", "").upper()))
    kunci = "".join(dict.fromkeys(kunci.replace(" ", "").upper()))
    
    # Panjang teks dan kunci
    panjang_plaintext = len(plaintext)
    panjang_kunci = len(kunci)
    
    # Perpanjang kunci hingga panjangnya sama dengan plaintext
    kunci_ulang = (kunci * ((panjang_plaintext // panjang_kunci) + 1))[:panjang_plaintext]
    
    # Alphabet untuk referensi indeks
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # List untuk menyimpan hasil substitusi
    hasil_substitusi = []
    
    # Lakukan enkripsi substitusi
    for i in range(panjang_plaintext):
        indeks_plaintext = alphabet.index(plaintext[i])  # Indeks karakter plaintext
        indeks_kunci = alphabet.index(kunci_ulang[i])    # Indeks karakter kunci
        indeks_enkripsi = (indeks_plaintext + indeks_kunci) % 26  # Operasi modulus 26
        hasil_substitusi.append(alphabet[indeks_enkripsi])  # Tambahkan karakter hasil enkripsi
    
    # Gabungkan hasil substitusi menjadi ciphertext
    ciphertext = ''.join(hasil_substitusi)
    return ciphertext

# Input data
plaintext = "TECHNIQUSARYPOG"
kunci = "ANWRBDULH"

# Hasil enkripsi
print("Plaintext: ", plaintext)
ciphertext = enkripsi_subtitusi_dengan_modulus(plaintext, kunci)
print("Ciphertext:", ciphertext)