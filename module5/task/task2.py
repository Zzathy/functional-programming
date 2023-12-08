import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

harga_produk = [item[1] for item in data_transaksi]
jumlah_terjual = [item[2] for item in data_transaksi]

total_pendapatan = [item[1] * item[2] for item in data_transaksi]

produk_labels = [item[0] for item in data_transaksi]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

ax1.scatter(harga_produk, jumlah_terjual, color='red')
ax1.set_xlabel('Harga Produk')
ax1.set_ylabel('Jumlah Produk Terjual')
ax1.set_title('Scatter Plot Hubungan Harga dan Jumlah Terjual')

ax2.bar(produk_labels, total_pendapatan, color='blue')
ax2.set_xlabel('Produk')
ax2.set_ylabel('Total Pendapatan')
ax2.set_title('Diagram Balok Total Pendapatan Produk')

plt.tight_layout()
plt.show()