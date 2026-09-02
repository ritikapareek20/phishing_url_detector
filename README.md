🛡️ Phishing URL Detector
A simple Machine Learning + Streamlit project for detecting whether a URL is potentially phishing or safe.
This project uses a Random Forest Classifier to analyze URL-based features and predict whether a given website URL is Phishing or Safe. A simple Streamlit web interface allows users to enter a URL and instantly view the prediction.
✨ Features
🔍 Enter any URL through an easy-to-use interface
🤖 Uses a Random Forest Classifier
🧩 Extracts features from URLs before prediction
📊 Uses a labeled CSV dataset for model training
⚡ Provides instant prediction through Streamlit
🚨 Displays a warning for potentially phishing URLs
✅ Displays a success message for URLs classified as safe
🧪 Includes a small sample dataset for demonstration and testing
🖥️ Project Preview
The application provides a simple interface:
🔗 Phishing URL Detector

Enter URL:  https://example.com

[ Check ]

✅ Safe Website
If the model predicts a phishing URL:
⚠️ Phishing Website
🧠 How It Works
The project follows these main steps:
┌─────────────────┐
                 │   CSV Dataset   │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Feature         │
                 │ Extraction      │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Random Forest   │
                 │ Model Training  │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ User enters URL │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Extract URL     │
                 │ Features        │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Model Prediction│
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Safe / Phishing │
                 └─────────────────┘
Workflow
The application loads the URL dataset.
URL features are extracted from the dataset.
The data is divided into training and testing sets.
A Random Forest Classifier is trained using the training data.
The user enters a URL in the Streamlit interface.
Features are extracted from the entered URL.
The trained model predicts the URL's class.
The application displays either Phishing Website or Safe Website.
📁 Project Structure
phishing-url-detector/
│
├── app.py                 # Streamlit application and ML workflow
├── phishing_detector.py   # URL feature extraction / detection logic
├── phishing_simple.csv    # Labeled URL dataset
└── README.md              # Project documentation
Your exact file structure may vary depending on how the project is organized.
📊 Dataset
The project uses a CSV file named:
phishing_simple.csv
The dataset contains two main columns:
Column
Description
url
Website URL
label
Target class
The sample dataset contains examples of both safe and suspicious URLs.
Example:
url,label
https://www.google.com,0
https://www.amazon.in,0
https://www.wikipedia.org,0
http://secure-login-bank.com,1
http://verify-paypal-account.com,1
Where:
0 → Safe URL
1 → Phishing URL
⚠️ Important: This dataset is intended for learning and demonstration. A real-world phishing detector should use a much larger, diverse, regularly updated dataset.
🛠️ Technologies Used
Technology
Purpose
🐍 Python
Core programming language
🌲 Scikit-learn
Machine Learning
🤖 Random Forest
URL classification
📊 NumPy
Numerical data processing
🐼 Pandas
Dataset handling
🎨 Streamlit
Web interface
🚀 Getting Started
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/phishing-url-detector.git
2. Open the project
cd phishing-url-detector
3. Install dependencies
pip install pandas numpy scikit-learn streamlit
If your project contains a requirements.txt file, you can instead use:
pip install -r requirements.txt
4. Run the application
streamlit run app.py
Streamlit will provide a local address, usually similar to:
http://localhost:8501
Open that address in your browser.
🧪 Example URLs
Safe examples
https://www.google.com
https://www.wikipedia.org
https://www.github.com
https://www.linkedin.com
Demonstration phishing examples
http://secure-login-bank.com
http://verify-paypal-account.com
http://update-bank-details-now.com
These examples are part of the demonstration dataset. Do not visit suspicious URLs just to test a detector. You can enter them as text without opening them.
🔐 Security Note
This project is designed for educational and defensive cybersecurity purposes.
The application performs classification based on URL characteristics. It does not guarantee that a website is completely safe or malicious.
A prediction should therefore be treated as an indication rather than a definitive security verdict.
Never enter passwords, banking information, OTPs, or other sensitive information into unknown websites.
📌 Limitations
The model's accuracy depends heavily on the quality and size of the training dataset.
A small demonstration dataset cannot represent the full variety of real-world URLs.
Phishing techniques change over time.
A machine-learning prediction can produce false positives or false negatives.
The project does not replace professional browser, DNS, email, or security solutions.
🔮 Future Scope
Possible improvements include:
📚 Use a larger and more diverse phishing URL dataset
📈 Add model accuracy, precision, recall, and F1-score
🧠 Compare Random Forest with other ML algorithms
🔗 Add more URL and domain-based features
🗃️ Save and load a trained model instead of training on every application start
🌐 Add domain reputation and threat-intelligence checks
📊 Add visual analytics and prediction statistics
☁️ Deploy the Streamlit application online
🔄 Regularly update the training dataset
👩‍💻 Author
Ritika Pareek
Phishing URL Detection — Machine Learning & Cybersecurity Project
⭐ Acknowledgement
This project was created as an educational project to explore:
Machine Learning + URL Feature Extraction + Cybersecurity + Streamlit
If you found this project useful, consider giving the repository a ⭐ on GitHub!
⚠️ Disclaimer
This project is intended strictly for education, research, and defensive cybersecurity awareness. The predictions generated by the model should not be considered a guarantee of website safety.
