import pandas as pd
import csv

df = pd.read_csv(
    "../data/password_data.csv",
    sep=",",
    on_bad_lines='skip',
    engine='python'
)

print("Data loaded:")
print(df.head())
print(df.info())


# drop data kosong
df = df.dropna()

# pastikan kolom sesuai
df.columns = ["password", "strength"]

def extract_features(pw):
    return [
        len(pw),
        sum(c.islower() for c in pw),
        sum(c.isupper() for c in pw),
        sum(c.isdigit() for c in pw),
        sum(not c.isalnum() for c in pw)
    ]

X = [extract_features(p) for p in df["password"]]
y = df["strength"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred))

def predict_password(pw):
    features = [extract_features(pw)]
    result = model.predict(features)[0]
    
    label_map = {
        0: "Weak ",
        1: "Medium ",
        2: "Strong "
    }
    
    return label_map.get(result, result)

# coba test
while True:
    user_input = input("\nMasukkan password (atau 'exit'): ")
    if user_input.lower() == "exit":
        break
    
    print("Hasil:", predict_password(user_input))