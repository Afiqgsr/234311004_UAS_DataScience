## INFORMASI PROYEK

**Judul Proyek:** KLASIFIKASI PENYAKIT TANAMAN KEDELAI MENGGUNAKAN BASELINE MODEL, MACHINE LEARNING, DAN DEEP LEARNING

**Nama Mahasiswa:** [Isi Nama Lengkap Anda]  
**NIM:** [Isi NIM Anda]  
**Program Studi:** [Isi Prodi Anda]  
**Mata Kuliah:** Data Science  
**Dosen Pengampu:** [Isi Nama Dosen]  
**Tahun Akademik:** 2024/2025  
**Link GitHub Repository:** [Isi Link Repo GitHub Anda]  
**Link Video Pembahasan:** [Isi Link Video Anda]

---

## 1. LEARNING OUTCOMES
Pada proyek ini, mahasiswa diharapkan dapat:
1. Memahami konteks masalah dan merumuskan problem statement secara jelas
2. Melakukan analisis dan eksplorasi data (EDA) secara komprehensif (**OPSIONAL**)
3. Melakukan data preparation yang sesuai dengan karakteristik dataset
4. Mengembangkan tiga model machine learning yang terdiri dari (**WAJIB**):
   - Model baseline
   - Model machine learning / advanced
   - Model deep learning (**WAJIB**)
5. Menggunakan metrik evaluasi yang relevan dengan jenis tugas ML
6. Melaporkan hasil eksperimen secara ilmiah dan sistematis
7. Mengunggah seluruh kode proyek ke GitHub (**WAJIB**)
8. Menerapkan prinsip software engineering dalam pengembangan proyek

---

## 2. PROJECT OVERVIEW

### 2.1 Latar Belakang
Tanaman kedelai merupakan salah satu komoditas pangan utama dunia. Namun, penyakit pada tanaman kedelai seringkali menyebabkan gagal panen yang merugikan petani. Masalah utama yang dihadapi adalah kemiripan gejala visual antar penyakit (seperti bercak daun atau pembusukan akar), yang membuat identifikasi manual oleh petani menjadi sulit dan rentan kesalahan.

Proyek ini penting untuk mengembangkan sistem otomatis yang dapat membantu ahli agronomi dan petani dalam mendiagnosis penyakit secara cepat dan akurat berdasarkan ciri-ciri fisik tanaman.

**Referensi:**
> Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

## 3. BUSINESS UNDERSTANDING / PROBLEM UNDERSTANDING
### 3.1 Problem Statements
1. Petani kesulitan membedakan 19 jenis penyakit kedelai karena gejala visual yang mirip.
2. Dataset memiliki banyak *missing values* yang dapat menurunkan performa model jika tidak ditangani dengan benar.
3. Diperlukan perbandingan performa antara model sederhana, *ensemble*, dan *neural network* untuk menentukan pendekatan terbaik pada dataset kecil namun kompleks.

### 3.2 Goals
1. Membangun model klasifikasi *multiclass* yang mampu memprediksi penyakit dengan akurasi > 85%.
2. Mengimplementasikan strategi *data imputation* yang efektif untuk menangani data kosong.
3. Membandingkan performa tiga pendekatan model: Decision Tree (Baseline), Random Forest (Advanced), dan MLP (Deep Learning).

### 3.3 Solution Approach

#### **Model 1 – Baseline Model**
**Model:** Decision Tree Classifier  
**Alasan:** Model ini dipilih karena kemampuannya menghasilkan aturan "Jika-Maka" yang mudah diinterpretasi, sangat cocok sebagai standar dasar untuk melihat apakah pola data bisa dipelajari secara sederhana.

#### **Model 2 – Advanced / ML Model**
**Model:** Random Forest Classifier  
**Alasan:** Random Forest adalah metode *Ensemble* yang menggabungkan banyak pohon keputusan. Model ini dipilih karena lebih tahan terhadap *overfitting* dan sangat kuat menangani dataset tabular dengan banyak fitur kategori seperti data Soybean ini.

#### **Model 3 – Deep Learning Model (WAJIB)**
**Model:** Multilayer Perceptron (MLP) / Neural Network  
**Jenis:** A. Tabular Data  
**Alasan:** MLP mampu mempelajari hubungan non-linear yang kompleks antar fitur melalui *hidden layers*. Ini digunakan untuk melihat apakah arsitektur *Deep Learning* bisa mengungguli algoritma *Machine Learning* klasik pada dataset ini.

---

## 4. DATA UNDERSTANDING
### 4.1 Informasi Dataset
**Sumber Dataset:** UCI Machine Learning Repository (Soybean Large)  
**Deskripsi Dataset:**
- Jumlah baris (rows): 307
- Jumlah kolom (columns/features): 35 Fitur + 1 Target
- Tipe data: Tabular / Categorical
- Format file: .data (CSV structure)

### 4.2 Deskripsi Fitur
Dataset berisi 35 atribut kategorikal yang merepresentasikan kondisi fisik tanaman dan lingkungan.

| Nama Fitur | Tipe Data | Deskripsi | Contoh Nilai |
|------------|-----------|-----------|--------------|
| date | Categorical | Bulan pengamatan | april, may, etc. |
| plant-stand | Categorical | Kondisi tegakan | normal, lt-normal |
| precip | Categorical | Curah hujan | lt-norm, norm, gt-norm |
| temp | Categorical | Suhu lingkungan | lt-norm, norm, gt-norm |
| leaves | Categorical | Kondisi daun | norm, abnorm |
| class | Categorical | **Target (Jenis Penyakit)** | diaporthe-stem-canker, dll |

*(Tabel disederhanakan untuk laporan, dataset asli memiliki 35 fitur)*

### 4.3 Kondisi Data
- **Missing Values:** Ada (simbol '?'). Beberapa kolom memiliki banyak data kosong yang perlu diimputasi.
- **Outliers:** Tidak signifikan karena semua data bersifat kategori/nominal.
- **Imbalanced Data:** Ya, distribusi kelas penyakit tidak merata sepenuhnya.

### 4.4 Exploratory Data Analysis (EDA)
Visualisasi dilakukan untuk memahami karakteristik data.

#### Visualisasi 1: Distribusi Kelas Target
[Gambar disimpan di: images/eda_1_class_distribution.png]
**Insight:** Terdapat ketidakseimbangan jumlah sampel antar kelas penyakit, namun masih dalam batas wajar untuk dipelajari model.

#### Visualisasi 2: Peta Missing Values
[Gambar disimpan di: images/eda_2_missing_values.png]
**Insight:** Terdapat pola *missing values* yang signifikan pada beberapa baris tertentu, yang kemungkinan berasal dari kesalahan pengumpulan data atau fitur yang tidak relevan untuk penyakit tertentu.

---

## 5. DATA PREPARATION

### 5.1 Data Cleaning
**Aktivitas:** Handling Missing Values  
**Implementasi:**
- Mengubah simbol `?` menjadi `NaN`.
- Melakukan imputasi menggunakan **Modus (Most Frequent)**.
**Alasan:** Karena semua fitur bertipe kategori, penggunaan rata-rata (mean) tidak valid. Modus adalah pendekatan statistik terbaik untuk data nominal.

### 5.2 Data Transformation
**Aktivitas:** Encoding
**Implementasi:**
- **Fitur:** Menggunakan `LabelEncoder` untuk mengubah teks (misal: 'normal', 'abnormal') menjadi angka (0, 1).
- **Target:** - Untuk ML (DT & RF): Menggunakan `LabelEncoder`.
    - Untuk DL (MLP): Menggunakan `One-Hot Encoding` (`to_categorical`) agar sesuai dengan output layer softmax.

### 5.3 Data Splitting
**Strategi:** 80% Training, 20% Testing.
**Implementasi:** `train_test_split(test_size=0.2, random_state=42)`
**Alasan:** Proporsi 80/20 umum digunakan untuk menyeimbangkan jumlah data latih dan data uji yang representatif.

---
## 6. MODELING
#### 6.1.1 Deskripsi Model

**Nama Model:** Decision Tree Classifier

**Teori Singkat:**
Decision Tree adalah algoritma pembelajaran terawasi non-parametrik yang memprediksi nilai variabel target dengan mempelajari aturan keputusan sederhana yang disimpulkan dari fitur data. Model ini memecah data menjadi himpunan bagian yang lebih kecil hingga membentuk struktur pohon dengan simpul keputusan (*decision nodes*) dan simpul daun (*leaf nodes*). 

**Alasan Pemilihan:**
Dipilih sebagai baseline karena kemampuannya yang mudah diinterpretasi dan cepat dilatih. Ini menjadi standar dasar untuk melihat apakah pola pada data Soybean dapat dipelajari dengan aturan logika sederhana sebelum menggunakan model yang lebih kompleks.

**Keunggulan:**
- **Interpretabilitas Tinggi (White Box):** Alur keputusan model sangat mudah dipahami, divisualisasikan, dan dijelaskan logikanya, mirip dengan cara manusia mengambil keputusan.
- **Minim Preprocessing:** Tidak memerlukan penskalaan fitur (*feature scaling*) atau normalisasi data, sehingga cocok untuk data mentah.
- **Efektif untuk Data Kategorikal:** Sangat natural dalam menangani fitur kategorikal/diskrit seperti yang ada pada dataset Soybean ini.

**Kelemahan:**
- **Rawan Overfitting:** Cenderung membuat pohon yang terlalu kompleks (menghapal data latih), sehingga performanya bisa turun drastis pada data baru jika kedalaman pohon tidak dibatasi.
- **Instabilitas:** Sedikit perubahan pada data training dapat menghasilkan struktur pohon yang sangat berbeda (varian tinggi).