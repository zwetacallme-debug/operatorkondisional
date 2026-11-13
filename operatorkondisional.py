pasien = input("jenis pasien : ")

status = "Pasien Opname" if pasien in ["anak", "dewasa", "lansia", "ibu hamil", "jantung", "bedah", "saraf", "ortopedi", "penyakit dalam", "pascaoperasi"] else "Bukan Pasien Opname"

print(status)