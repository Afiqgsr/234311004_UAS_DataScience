# 📘 Judul Proyek
*ANALISIS KLASIFIKASI PENYAKIT TANAMAN KEDELAI MENGGUNAKAN BASELINE MODEL, MACHINE LEARNING, DAN DEEP LEARNING*

## 👤 Informasi
- **Nama:** Afiq Galuh Setya Ramadhani
- **Repo:** https://github.com/Afiqgsr/234311004_UAS_DataScience
- **Video:** [...]

---

# 1. 🎯 Ringkasan Proyek
- Mengklasifikasikan 19 jenis penyakit pada tanaman kedelai berdasarkan fitur fisik dan kondisi lingkungan.
- Melakukan data preparation (handling missing values, encoding, splitting).
- Membangun 3 pendekatan model:
  (1) Baseline – Decision Tree Classifier
  (2) Advanced ML – Random Forest Classifier
  (3) Deep Learning – MLP Neural Network
- Melakukan evaluasi menggunakan metrik Accuracy, Precision, Recall, dan F1-Score.
- Menentukan model terbaik dan memberikan insight dari hasil pemodelan.

---

# 2. 📄 Problem & Goals
**Problem Statements:**
- Petani sering kesulitan mengidentifikasi jenis penyakit kedelai secara dini karena kemiripan gejala visual pada daun, batang, dan akar.
- Diperlukan sistem otomatis yang dapat mendiagnosis penyakit berdasarkan ciri-ciri fisik tanaman dengan akurasi tinggi.
- Dataset memiliki banyak nilai yang hilang (*missing values* disimbolkan dengan '?') yang harus ditangani agar tidak merusak performa model.
- Belum ada analisis yang membandingkan secara langsung kinerja model sederhana (*Baseline*), *Ensemble* (ML), dan *Deep Learning* untuk kasus penyakit kedelai ini.

**Goals:**
- Membangun model klasifikasi multiclass yang mampu memprediksi 19 kelas penyakit kedelai.
- Melakukan data cleaning yang efektif untuk menangani missing values dengan metode imputasi.
- Membandingkan performa tiga pendekatan model—Baseline (Decision Tree), Machine Learning (Random Forest), dan Deep Learning (Neural Network).
- Memberikan output berupa pipeline analisa yang *reproducible*, mencakup preprocessing, pelatihan model, dan evaluasi.
- Memberikan wawasan mengenai gejala fisik apa yang paling berpengaruh dalam penentuan penyakit.

---
## 📁 Struktur Folder
```text
project/
│
├── data/                   # Dataset (tidak di-commit, download manual)
│
├── notebooks/              # Jupyter notebooks
│   └── soybean_analysis.ipynb
│
├── src/                    # Source code
│   
├── models/                 # Saved models
│   ├── model_baseline.pkl
│   ├── model_rf.pkl
│   └── model_dl.h5
│
├── images/                 # Visualizations
│   └── accuracy_plot.png
│
├── requirements.txt        # Dependencies
├── .gitignore
└── README.md

# 3. 📊 Dataset
- **Sumber:** UCI Machine Learning Repository (Soybean Large)
- **Jumlah Data:** 307 baris, 35 fitur dan 1 target
- **Tipe:** Kategorikal / Multivariat

### Fitur Utama
Dataset ini memiliki **35 fitur**, berikut adalah tabel **10 fitur utama** yang digunakan untuk mendeteksi penyakit:

| **Nama Fitur** | **Deskripsi** |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **date** | Bulan saat pengamatan dilakukan (April - Oktober), indikator musim tanam. |
| **plant-stand** | Kondisi tegakan tanaman (normal / di bawah normal). |
| **precip** | Curah hujan (rendah / normal / tinggi), mempengaruhi kelembaban jamur. |
| **temp** | Suhu lingkungan (rendah / normal / tinggi). |
| **leaves** | Kondisi daun secara umum (normal / abnormal). |
| **leafspots-halo** | Keberadaan lingkaran halo pada bercak daun (gejala spesifik virus/bakteri). |
| **stem-cankers** | Keberadaan kanker/luka pada batang tanaman. |
| **fruit-pods** | Kondisi polong buah (normal / berpenyakit / sedikit / hilang). |
| **roots** | Kondisi akar (normal / busuk / ada kista). |
| **class** | **Target** – Jenis penyakit kedelai (19 kelas, misal: Diaporthe stem canker, Charcoal rot, dll). |

---

# 4. 🔧 Data Preparation
- **Cleaning**: Mengganti simbol `?` dengan `NaN`, kemudian melakukan imputasi menggunakan **Modus** (*most_frequent*) karena data bersifat kategori.
- **Feature Selection**: Menggunakan seluruh fitur yang tersedia karena setiap gejala fisik pada bagian tanaman (akar, batang, daun) berkontribusi terhadap diagnosa.
- **Encoding**: Mengubah data teks menjadi angka. Fitur menggunakan `LabelEncoder`, target Deep Learning menggunakan `One-Hot Encoding`.
- **Scaling**: Tidak diperlukan scaling numerik berat karena data hasil encoding berupa label kategori.
- **Splitting**: Pembagian dataset menjadi 80% train dan 20% test menggunakan `train_test_split` dengan `random_state = 42`.
- **Balancing**: Dataset dibiarkan alami (*imbalanced*) untuk melihat kemampuan model menangani kelas minoritas.

---

# 5. 🤖 Modeling
- **Model 1 – Baseline:** [Decision Tree Classifier]
- **Model 2 – Advanced ML:** [Random Forest Classifier]
- **Model 3 – Deep Learning:** [Neural Network / MLP]

---

# 6. 🧪 Evaluation
**Metrik:** Accuracy

| Model | Akurasi (Test) | Keterangan | Training Time |
|------------------------------|----------------|-------------------|----------------|
| Baseline (Decision Tree) | [Isi %] | Cukup baik sebagai standar minimal | ~0.1 detik |
| Advanced (Random Forest) | [Isi %] | Lebih stabil dan akurat | ~0.5 detik |
| Deep Learning (MLP) | [Isi %] | Mampu menangkap pola kompleks | ~3 detik |

*(Catatan: Silakan isi angka hasil running notebook Anda di kolom Akurasi)*

---

# 7. 🏁 Kesimpulan

- **Model terbaik:** [Sebutkan Model Terbaik, misal: Random Forest / MLP]
- **Alasan:**
  - Mampu mempelajari pola hubungan antar atribut gejala yang kompleks (non-linear).
  - (Jika RF): Ensemble method membuatnya lebih stabil dan tahan terhadap *overfitting* dibanding Decision Tree tunggal.
  - (Jika MLP): Arsitektur neural network mampu memisahkan 19 kelas penyakit dengan loss yang minim pada fase testing.

- **Insight penting:**
  - Gejala pada daun (*leaves*, *leafspot*) menjadi indikator paling dominan dalam membedakan penyakit.
  - Faktor lingkungan (*temp*, *precip*) sangat membantu model membedakan penyakit yang gejalanya mirip tapi muncul di musim berbeda.
  - Deep Learning memerlukan data yang cukup banyak, sehingga pada dataset kecil/menengah ini, Random Forest seringkali memberikan hasil yang sangat kompetitif.

---

# 8. 🔮 Future Work

## 📌 Data Improvements
- [x] Menggunakan dataset standar UCI
- [ ] Mengumpulkan lebih banyak data sampel untuk penyakit langka
- [ ] Menambah variasi data gambar daun (untuk project Computer Vision)

## 🤖 Model Enhancements
- [x] Mencoba arsitektur deep learning (MLP)
- [x] Hyperparameter tuning sederhana
- [x] Mencoba ensemble methods (Random Forest)
- [ ] Menerapkan Cross-Validation (K-Fold)

## 🚀 Deployment & System
- [ ] Membuat API (Flask / FastAPI)
- [ ] Membuat web app (Streamlit / Gradio)
- [ ] Containerization dengan Docker
- [ ] Deploy ke cloud

## ⚙️ Optimization
- [ ] Model compression
- [x] Improving inference speed (menggunakan model ringan)
- [ ] Reducing model size

---

# 9. 🔁 Reproducibility
Gunakan environment:
**Python Version:**
- Python 3.10 / 3.12

**Main Libraries & Versions:**
- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn

**Deep Learning Framework:**
- tensorflow
- keras