import matplotlib.pyplot as plt
from functools import reduce

nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

average = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)

label_mahasiswa = list(map(lambda x: f'{x+1}', range(len(nilai_mahasiswa))))

plt.bar(label_mahasiswa, nilai_mahasiswa, color='#6f03fc')
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.title('Diagram Batang Nilai Ujian Mahasiswa')
plt.axhline(average, color='red', linestyle='dashed', linewidth=1.4, label=f'Rata-rata: {average:.2f}')
plt.legend()
plt.show()