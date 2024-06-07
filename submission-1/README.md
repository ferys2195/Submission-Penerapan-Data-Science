# Submission Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Salah satu perusahaan multinasional memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri, kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Permasalahan Bisnis

Tingkat attrition yang tinggi dan rendahnya retensi karyawan merupakan masalah bisnis yang perlu diselesaikan agar dapat meningkatkan stabilitas dan kesejahteraan perusahaan.

### Cakupan Proyek

Proyek ini dimulai dengan **Menyiapkan library yang dibutuhkan** serta **Menyiapkan data yang akan digunakan**, memastikan bahwa semua alat dan dataset yang diperlukan sudah tersedia dan siap untuk tahap-tahap selanjutnya.

Tahap berikutnya adalah _data understanding_, di mana saya mengidentifikasi sumber data, memahami konteks bisnis, dan melakukan analisis awal untuk menentukan kualitas serta relevansi data yang tersedia seperti mengecek **duplikasi data, data null, dll**.

Selanjutnya, saya melanjutkan ke tahap **data preparation**, dalam tahap ini saya hanya melakukan pembersihan data yaitu menghapus data yang memiliki nilai null / isNan sebelum data siap digunakan dalam analisis.

Setelah data siap, saya memasuki tahap **Eksplorasi Data Analisis (EDA)** di mana saya melakukan analisis deskriptif untuk mengidentifikasi pola dan korelasi dalam data, serta menggunakan visualisasi data untuk memberikan wawasan awal yang dapat membantu dalam pengambilan keputusan dan perencanaan tahap lanjut dalam proyek.

_Sayangnya, cakupan proyek yang saya lakukan tidak sampai pemodelan machine learning mengingat waktu pembelajaran saya yang semakin sedikit._

### Persiapan

Sumber data: [https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

Setup environment:

```
pipenv install

pipenv shell

jupyter notebook .
```

**Rekomendasi : Buka Notebook menggunakan [Google Colab](https://colab.research.google.com/)**

## Business Dashboard

Business dashboard yang dibuat dimaksudkan untuk memantau karyawan yang dibagi berdasarkan departemen tempat mereka bekerja, sehingga memudahkan analisis departemen mana yang memiliki tingkat attrition (dalam jumlah) yang tinggi. Dashboard ini lebih berfokus pada pemantauan tingkat attrisi berdasarkan usia, peran karyawan, status pernikahan, serta jenis kelamin karyawan.

Link Dashboard : [https://lookerstudio.google.com/s/iHZ5MYCVEhw](https://lookerstudio.google.com/s/iHZ5MYCVEhw)

## Conclusion

Tidak ada fitur spesifik yang menunjukkan korelasi langsung yang kuat dengan tingkat attrisi. Kemungkinan hal ini terjadi karena keputusan attrisi sangat bervariasi antara individu, sehingga setiap kasus perlu ditangani secara personal. Namun, ada beberapa poin yang dicatat mengenai tingkat attrisi:

- Faktor penyebab tingginya tingkat attrisi paling banyak terjadi pada karyawan yang **bekerja lembur (Overtime), berstatus single atau belum menikah**.
- Departemen yang memiliki tingkat attrition tertinggi adalah **Research & Development** dengan jumlah attrition sebanyak **107** karyawan, yang merupakan **59,78%** dari total karyawan yang meninggalkan perusahaan atau **15,26%** dari total seluruh karyawan yang bekerja pada department **Research & Development**.
- Karyawan yang meninggalkan perusahaan sebagian besar adalah karyawan yang jarang bepergian **(Travel Rarerly)**.

### Rekomendasi Action Items (Optional)

Berdasarkan Conclusion yang buat, berikut adalah beberapa rekomendasi action yang dapat dipertimbangkan perusahaan untuk mengurangi tingkat attrition:

1.  **Manajemen Kerja Lembur**:

    - Mengimplementasikan kebijakan kerja lembur yang lebih ketat untuk memastikan bahwa karyawan tidak terlalu banyak bekerja lembur. Misalnya, tentukan bahwa karyawan tidak boleh bekerja lebih dari 10 jam lembur dalam satu minggu.
    - Mendorong keseimbangan antara kerja dan kehidupan pribadi dengan menyediakan program kesejahteraan karyawan, seperti waktu istirahat yang cukup, fleksibilitas kerja, dan kegiatan yang mendukung kesehatan mental.

2.  **Pendekatan Khusus untuk Karyawan Single atau Belum Menikah**:

    - Menyediakan program sosial dan kegiatan untuk meningkatkan keterlibatan dan dukungan antar karyawan.
    - Memperkenalkan insentif atau program pengembangan karir yang menarik untuk karyawan single atau belum menikah, agar mereka merasa lebih terikat dengan perusahaan.

3.  **Fokus pada Departemen Research & Development**:

    - Melakukan tinjauan mendalam terhadap beban kerja, lingkungan kerja, dan manajemen di departemen Research & Development untuk mengidentifikasi dan menangani penyebab spesifik yang mendorong tingginya tingkat attrition.
    - Menyediakan pelatihan tambahan, sumber daya, dan dukungan untuk karyawan di departemen ini guna meningkatkan kepuasan dan retensi.

4.  **Kebijakan untuk Karyawan yang Jarang Bepergian**:

    - Mengembangkan program rotasi pekerjaan atau kesempatan perjalanan yang dapat memberikan variasi dan pengalaman baru bagi karyawan yang jarang bepergian.
    - Memperkenalkan kegiatan tim yang dapat meningkatkan keterlibatan dan kepuasan kerja bagi karyawan yang cenderung bekerja di satu tempat.

Demikian rekomendasi yang saya berikan, semoga dengan menerapkan rekomendasi action ini, perusahaan dapat mengurangi tingkat attrition dan meningkatkan kepuasan serta retensi karyawan secara keseluruhan.
