
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_soybean_model():
    print("🚀 Memulai proses training dari script Python...")

    # --- 1. SETUP PATH ---
    # Asumsi script dijalankan dari root project
    dataset_path = '/content/data/soybean-large.data'
    model_save_path = '/content/models/model_rf_script.pkl'
    
    # Cek dataset
    if not os.path.exists(dataset_path):
        print(f"❌ Error: Dataset tidak ditemukan di {dataset_path}")
        return

    # --- 2. LOAD DATA ---
    col_names = [
        'class', 'date', 'plant-stand', 'precip', 'temp', 'hail', 'crop-hist', 
        'area-damaged', 'severity', 'seed-tmt', 'germination', 'plant-growth', 
        'leaves', 'leafspots-halo', 'leafspots-marg', 'leafspot-size', 
        'leaf-shread', 'leaf-malf', 'leaf-mild', 'stem', 'lodging', 
        'stem-cankers', 'canker-lesion', 'fruiting-bodies', 'external-decay', 
        'mycelium', 'int-discolor', 'sclerotia', 'fruit-pods', 'fruit-spots', 
        'seed', 'mold-growth', 'seed-discolor', 'seed-size', 'shriveling', 'roots'
    ]
    
    print("📂 Loading dataset...")
    df = pd.read_csv(dataset_path, names=col_names, header=None)
    
    # --- 3. CLEANING ---
    df.replace('?', np.nan, inplace=True)
    imputer = SimpleImputer(strategy='most_frequent')
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    
    # --- 4. ENCODING ---
    X = df_imputed.drop('class', axis=1)
    y = df_imputed['class']
    
    X_encoded = X.copy()
    for col in X_encoded.columns:
        le = LabelEncoder()
        X_encoded[col] = le.fit_transform(X_encoded[col])
        
    le_target = LabelEncoder()
    y_encoded = le_target.fit_transform(y)
    
    # --- 5. SPLITTING ---
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)
    
    # --- 6. TRAINING (Random Forest) ---
    print("🌲 Training Random Forest Model...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # Evaluasi Singkat
    acc = rf_model.score(X_test, y_test)
    print(f"✅ Training Selesai! Akurasi: {acc*100:.2f}%")
    
    # --- 7. SAVING ---
    if not os.path.exists('/content/models'):
        os.makedirs('/content/models')
        
    joblib.dump(rf_model, model_save_path)
    print(f"💾 Model berhasil disimpan ke: {model_save_path}")

if __name__ == "__main__":
    train_soybean_model()
