# 📘 Judul Proyek
*ANALISIS KLASIFIKASI PENYAKIT TANAMAN KEDELAI MENGGUNAKAN BASELINE MODEL, MACHINE LEARNING, DAN DEEP LEARNING*

## 👤 Informasi
- **Nama:** Afiq Galuh Setya Ramadhani
- **Repo:** https://github.com/Afiqgsr/234311004_UAS_DataScience
- **Video:** https://youtu.be/7qS1b6vCJuo

---

# 1. 🎯 Ringkasan Proyek
- Mengklasifikasikan 19 jenis penyakit pada tanaman kedelai berdasarkan fitur fisik dan kondisi lingkungan.
- Melakukan data preparation yang meliputi *handling missing values*, *encoding*, dan *splitting*.
- Membangun 3 pendekatan model sesuai standar komparasi:
  1. **Baseline** – Decision Tree Classifier
  2. **Advanced ML** – Random Forest Classifier
  3. **Deep Learning** – MLP Neural Network
- Melakukan evaluasi menggunakan metrik *Accuracy* dan visualisasi performa model.
- Menentukan model terbaik dan memberikan insight mengenai fitur (gejala) yang paling dominan.

---

# 2. 📄 Problem & Goals
**Problem Statements:**
- Petani sering kesulitan mengidentifikasi jenis penyakit kedelai secara dini karena kemiripan gejala visual pada daun, batang, dan akar.
- Diperlukan sistem otomatis yang dapat mendiagnosis penyakit berdasarkan ciri-ciri fisik tanaman dengan akurasi tinggi.
- Dataset memiliki banyak nilai yang hilang (*missing values* disimbolkan dengan '?') yang harus ditangani agar tidak merusak performa model.
- Belum ada analisis yang membandingkan secara langsung kinerja model sederhana (*Baseline*), *Ensemble* (ML), dan *Deep Learning* untuk kasus penyakit kedelai ini.

**Goals:**
- Membangun model klasifikasi multiclass yang mampu memprediksi 19 kelas penyakit kedelai.
- Melakukan data cleaning yang efektif untuk menangani missing values dengan metode imputasi (Modus).
- Membandingkan performa tiga pendekatan model—Baseline (Decision Tree), Machine Learning (Random Forest), dan Deep Learning (Neural Network).
- Memberikan output berupa pipeline analisa yang *reproducible*, mencakup preprocessing, pelatihan model, dan evaluasi.
- Memberikan wawasan mengenai gejala fisik apa yang paling berpengaruh dalam penentuan penyakit.

---
## 📁 Struktur Folder
Struktur folder proyek ini disusun agar rapi dan mudah direproduksi:

```text
project/
│
├── data/                   # Dataset (berisi soybean-large.data)
│
├── notebooks/              # Jupyter notebooks (Eksperimen Utama)
│   └── soybean_analysis.ipynb
│
├── src/                    # Source code Python
│   └── soybean_training.py # Script training otomatis (versi .py)
│   
├── models/                 # Saved models (Hasil Training)
│   ├── model_baseline.pkl  # Model Decision Tree
│   ├── model_rf.pkl        # Model Random Forest
│   ├── model_dl.keras      # Model Deep Learning (Format Tensorflow Terbaru)
│   ├── le_features.pkl     # Encoder untuk fitur input
│   └── le_target.pkl       # Encoder untuk label target
│
├── images/                 # Visualizations (Grafik & Plot)
│   ├── 1_accuracy_comparison.png
│   ├── 2_decision_tree_viz.png
│   ├── 3_deep_learning_history.png
│   └── 4_rf_detailed_analysis.png
│
├── requirements.txt        # Dependencies library
├── .gitignore              # Daftar file yang diabaikan git
└── README.md               # Dokumentasi Proyek
```
---
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
- **Encoding**: Mengubah data teks menjadi angka. Fitur menggunakan `LabelEncoder`, target Deep Learning menggunakan `One-Hot Encoding`.
- **Scaling**: Tidak diperlukan scaling numerik berat karena data hasil encoding berupa label kategori.
- **Splitting**: Pembagian dataset menjadi 80% train dan 20% test menggunakan `train_test_split` dengan `random_state = 42`.
- **Balancing**: Dataset dibiarkan alami (*imbalanced*) untuk melihat kemampuan model menangani kelas minoritas.

---

# 5. 🤖 Modeling
- **Model 1 – Baseline:** Decision Tree Classifier (Model pohon keputusan tunggal).
- **Model 2 – Advanced ML:** Random Forest Classifier (Ensemble Learning yang menggabungkan banyak pohon).
- **Model 3 – Deep Learning:** Neural Network / MLP (Arsitektur Sequential dengan Dense Layers dan Dropout).

---

# 6. 🧪 Evaluation
**Metrik:** Accuracy

| Model | Akurasi (Test) | Keterangan | Training Time |
|------------------------------|----------------|-------------------|----------------|
| Baseline (Decision Tree) | 90.32% | Cukup baik sebagai standar minimal | ~0.1 detik |
| Advanced (Random Forest) | 91.94% | Lebih stabil dan akurat (Ensemble) | ~0.5 detik |
| Deep Learning (MLP) | 88.71% | Mampu menangkap pola kompleks | ~3 detik |

---

# 7. 🏁 Kesimpulan

- **Model terbaik:** **Random Forest Classifier (91.94%)**

- **Alasan:**
  - Metode *ensemble* (menggabungkan banyak pohon keputusan) membuat Random Forest lebih stabil dan tahan terhadap *overfitting* dibandingkan Decision Tree tunggal.
  - Random Forest terbukti lebih efektif menangani dataset berukuran kecil hingga menengah (seperti dataset Soybean ini) dibandingkan Deep Learning.
  - Deep Learning (MLP) sedikit tertinggal (88.71%) kemungkinan karena jumlah data yang terbatas (<500 baris), sehingga jaringan syaraf tiruan belum bisa mempelajari fitur secara optimal dibandingkan algoritma berbasis pohon.

- **Insight penting:**
  - Berdasarkan *Feature Importance*, gejala fisik pada **daun** (*leaves*, *leafspot-halo*) menjadi indikator paling dominan dalam membedakan penyakit.
  - Faktor lingkungan seperti **suhu** (*temp*) dan **hujan** (*precip*) sangat membantu model membedakan penyakit yang memiliki gejala fisik mirip namun muncul di musim berbeda.
  - Hasil ini membuktikan bahwa untuk data tabular dengan jumlah sampel terbatas, algoritma *Machine Learning* klasik (seperti Random Forest) seringkali lebih efisien dan akurat dibandingkan arsitektur *Deep Learning* yang kompleks.

---

# 8. 🔮 Future Work

## 📌 Data Improvements
- [x] Menggunakan dataset standar UCI
- [ ] Mengumpulkan lebih banyak data sampel untuk penyakit langka
- [ ] Menambah variasi data gambar daun (untuk project Computer Vision masa depan)

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
Gunakan environment berikut untuk menjalankan proyek:

**Python Version:**
- Python 3.12.12

**Main Libraries & Versions:**
- numpy==2.0.2
- pandas==2.2.2
- scikit-learn==1.6.1
- matplotlib==3.10.0
- seaborn==0.13.2

**Deep Learning Framework:**
- tensorflow==2.19.0