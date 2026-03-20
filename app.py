
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv('phishing_simple.csv')

# Feature extraction
def extract_features(url):
    return [
        len(url),
        url.count('.'),
        url.count('-'),
        url.count('/'),
        1 if 'https' in url else 0,
        1 if '@' in url else 0
    ]

# Prepare data
X = []
for url in df['url']:
    X.append(extract_features(url))

X = np.array(X)
y = df['label']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# UI
st.title("🔍 Phishing URL Detector")

url = st.text_input("Enter URL")

if st.button("Check"):
    if url == "":
        st.write("❌ Please enter a URL")
    else:
        features = np.array(extract_features(url)).reshape(1, -1)
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.error("⚠️ Phishing Website")
        else:
            st.success("✅ Safe Website")