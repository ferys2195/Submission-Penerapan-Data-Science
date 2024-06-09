# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Salah satu institusi pendidikan yang telah berdiri sejak tahun 2000 telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat juga banyak siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah besar bagi sebuah institusi pendidikan. Oleh karena itu, institusi pendidikan tersebut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberikan bimbingan khusus.

### Permasalahan Bisnis

Banyak siswa tidak menyelesaikan pendidikan mereka, yang menyebabkan tingginya angka dropout di institusi tersebut serta berdampak negatif terhadap reputasi institusi, sehingga dapat mengurangi daya tarik bagi calon siswa dan orang tua.

### Cakupan Proyek

Proyek ini dimulai dengan **Menyiapkan library yang dibutuhkan** serta **Menyiapkan data yang akan digunakan**, memastikan bahwa semua alat dan dataset yang diperlukan sudah tersedia dan siap untuk tahap-tahap selanjutnya.

Tahap berikutnya adalah _data understanding_, di mana saya mengidentifikasi sumber data, memahami konteks bisnis, dan melakukan analisis awal untuk menentukan kualitas serta relevansi data yang tersedia seperti mengecek **duplikasi data, data null, dll**.

Selanjutnya, saya melanjutkan ke tahap **data preparation**, dalam tahap ini saya hanya melakukan pembersihan data yaitu mengubah nilai **Graduated, Enrollment dan Dropout** menjadi **1 (Dropout), 0 (Non-Dropout)** sebelum data siap digunakan dalam analisis.

Setelah data siap, saya memasuki tahap **Eksplorasi Data Analisis (EDA)** di mana saya melakukan analisis deskriptif untuk mengidentifikasi pola dan korelasi dalam data, serta menggunakan visualisasi data untuk memberikan wawasan awal yang dapat membantu dalam pengambilan keputusan dan perencanaan tahap lanjut dalam proyek.

Pada tahap modeling saya menyeleksi fitur-fitur yang memiliki nilai relevan, mengatasi _imbalance data_ menggunakan teknik _oversampling_, lalu melakukan _hyperparameter tuning_ menggunakan **GridSearchCv** kemudian menerapkannya pada algoritma **RandomForestClassifier**

### Persiapan

Sumber data: [https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:

```
conda create --name proyek-akhir-penerapan-data-science python=3.11

conda activate proyek-akhir-penerapan-data-science

pip install -r requirements.txt

jupyter notebook .
```

## Business Dashboard

Business dashboard yang dibuat berfungsi untuk memonitoring siswa yang dropout, dengan visualisasi yang lebih terfokus pada fitur-fitur yang memiliki nilai relevan seperti pada tahap Exploratory Data Analysis. Selain itu, juga ditambahkan fitur-fitur lainnya yang ada di institusi pendidikan.

Link Dashboard : [https://lookerstudio.google.com/s/om1A_PByNOY](https://lookerstudio.google.com/s/om1A_PByNOY)

## Menjalankan Sistem Machine Learning

```
streamlit run app.py
```

Link Prototype : [https://submission-penerapan-data-science-mazafathi.streamlit.app](https://submission-penerapan-data-science-mazafathi.streamlit.app)

## Conclusion

- Mahasiswa yang gagal menyelesaikan banyak mata kuliah dan mendapatkan nilai rendah di semester pertama dan kedua lebih rentan terhadap risiko dropout. Hal ini menunjukkan bahwa performa akademis awal sangat mempengaruhi kemungkinan mahasiswa untuk berhenti dari studi.
- Mahasiswa yang memiliki hutang juga cenderung lebih rentan terhadap risiko dropout sedangkan Penerima beasiswa cenderung memiliki risiko dropout yang lebih rendah, menunjukkan bahwa tekanan finansial merupakan faktor penting lainnya.
- Mahasiswa yang lebih muda pada saat pendaftaran cenderung memiliki risiko dropout yang lebih tinggi. Hal ini mungkin disebabkan oleh kurangnya persiapan dalam menghadapi tantangan akademis dan kehidupan kampus.
- Jurusan Manajemen, baik kelas malam maupun siang, merupakan penyumbang terbesar dalam jumlah mahasiswa yang dropout. Hal ini menunjukkan bahwa mahasiswa dalam jurusan ini memiliki tantangan tertentu yang perlu diatasi untuk mengurangi angka dropout.
- Pada Application Mode di kategori **over 23 years old** memiliki jumlah mahasiswa dropout tertinggi. Ini menunjukkan bahwa mahasiswa yang mendaftar melalui jalur ini lebih rentan terhadap risiko dropout.

### Rekomendasi Action Items

- Membuat/Menjalankan program konseling akademis oleh Dosen PA (Pembimbing Akademis) yang dapat membantu mahasiswa mengatasi tantangan dalam menyelesaikan mata kuliah dan meningkatkan kemampuan belajar mereka.
- Meningkatkan informasi tentang opsi beasiswa dan bantuan keuangan yang tersedia bagi mahasiswa untuk mengurangi tekanan finansial.
- Mengembangkan program orientasi khusus dan dukungan sosial untuk mahasiswa yang lebih muda, membantu mereka menyesuaikan diri dengan tantangan akademis dan kehidupan kampus, contohnya dengan menyelenggarakan seminar keterampilan belajar dan manajemen waktu serta pembentukan kelompok mentoring antar-mahasiswa.
- **Khusus pada jurusan manajemen**, mungkin diadakan kerja sama antara dosen, staf akademis, dan mahasiswa dalam menemukan solusi untuk tantangan yang spesifik dalam jurusan Manajemen.
- Menyediakan bimbingan karir dan dukungan khusus untuk mahasiswa yang kembali ke perguruan tinggi, khususnya pada kategori **over 23 years old**, untuk membantu mereka menemukan motivasi dan tujuan dalam menyelesaikan pendidikan mereka.
