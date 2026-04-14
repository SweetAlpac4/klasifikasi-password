from pathlib import Path

content = """# 🔐 Password Strength Classifier  
**Machine Learning Project using Random Forest**

Sebuah proyek klasifikasi kekuatan password berbasis machine learning yang mampu mengkategorikan password menjadi **Weak**, **Medium**, atau **Strong** berdasarkan karakteristiknya.

---

## ✨ Overview

Di era digital, kekuatan password menjadi garis pertahanan pertama terhadap keamanan data. Proyek ini membangun model klasifikasi sederhana menggunakan **Random Forest** untuk mengevaluasi kekuatan password berdasarkan pola dan struktur karakter.

---

## 🧠 Methodology

### 📥 Data Processing
- Dataset dibaca dari file CSV
- Data tidak valid atau kosong dihapus
- Kolom distandarisasi menjadi:
  - `password`
  - `strength`

---

### ⚙️ Feature Engineering

Password dikonversi menjadi fitur numerik:

| Fitur | Deskripsi |
|------|--------|
| Length | Panjang password |
| Lowercase | Jumlah huruf kecil |
| Uppercase | Jumlah huruf besar |
| Digits | Jumlah angka |
| Special Characters | Jumlah simbol |

---

### 🌲 Model

Menggunakan:
`RandomForestClassifier`

Konfigurasi:
- `n_estimators = 100`
- `random_state = 42`

---

### 🔀 Data Split

- 80% Training
- 20% Testing

---

### 📊 Evaluation Metrics

- Accuracy Score  
- Precision, Recall, F1-score (Classification Report)

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install pandas scikit-learn
