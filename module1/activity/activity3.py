def countGrade(uts, uas):
    return (uts + uas) / 2

def countGradeAll(dataMahasiswa):
    nilaiAkhir = {}
    for index in dataMahasiswa:
        nilaiAkhir[index] = countGrade(dataMahasiswa[index]["uts"], dataMahasiswa[index]["uas"]) 
    return nilaiAkhir


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa: ")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        "Izza": {
            "uts": 90,
            "uas": 81
        },
        "Rangga": {
            "uts": 90,
            "uas": 85
        }
    }
 
    data_nilai_akhir = countGradeAll(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()