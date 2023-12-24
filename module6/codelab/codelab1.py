# #Lengkapi kode dibawah untuk menjawab soal diatas ya


# # TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont


# # TODO 1: Lakukan load image pada variabel berikut
# # hint: kalian bisa gunakan fungsi open()
gambarku = Image.open(r"C:\code\python\functional\module6\codelab\images\minion.png")


# # TODO 2: Ubah gambar menjadi hitam-putih
# # hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert('L')


# # TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype("arial.ttf", 24)
text = ""
text_width, text_height = draw.textsize(text, font)
text_x = (gambarku.width - text_width) // 2
text_y = 20
draw.text((text_x,text_y), u'Izza Ihsan Fathony, 202110370311297', 'black', font)


# # TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save(r"C:\code\python\functional\module6\codelab\images\minion_result.png")


# # TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()

