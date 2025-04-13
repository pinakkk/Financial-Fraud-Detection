# 💰 AI-Based Financial Fraud Detection Web App

This Streamlit-powered web application uses anomaly detection techniques and Google's **Gemini AI** to help users analyze financial transactions and detect potential fraudulent activity.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue" />
  <img src="https://img.shields.io/badge/Streamlit-1.x-brightgreen" />
  <img src="https://img.shields.io/badge/Gemini%20API-integrated-orange" />
</div>

---

## 🚀 Features

- ✅ **AI-Powered Fraud Detection** using anomaly detection algorithms
- 🧠 **Gemini AI Integration** to explain why a transaction might be suspicious
- 📁 **CSV Upload** to analyze your own transaction data
- 📊 **Dynamic Filtering & Sorting** of transactions
- 🔍 **Detailed Transaction View** with on-demand explanations
- 📄 **PDF Report Generation** with one-click download

---

## 📸 Demo Screenshot

![Demo](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZHBfCPzwgumLb1qzpZoapU7l5_c2pcVuTyHjFFHsgzYbtbpKwEzfZG-7rXrqRI85yw0ibVs3zDk07k47BxSNtML4FQHDOcfZ9M_ZwMy7qKsCh-2pPlmNgPs60SMppimoRe3UcZ9uLHKo-APOAV7c_A-mHXrza9srAfSTt-2mCLnZ1rLbLmzkQSeW0aCQ/s1918/Screenshot%202025-04-07%20210819.png)

![Demo](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHmFVeo7EyHDVCfL7GFKaqx-45sjf-s55ACchCV3U4rGBwzPUP8AeorqyRuYSvtvphhFzOEGHPyrasjH0d1vpKN3xA9oPRucjU5tavPvZjvX5ko04bDfc9XKL9hr0NaYFsZRRfVKE_YQ30IwMBKx2n2JzRG4RYPQVtyeqUl5Z6grAZ1H4wQavpaAsoAbw/s1919/Screenshot%202025-04-07%20211002.png)

![Demo](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitDZfj2NCDzgR6nT-pZfPeEGtC-_jP_SzC4E9NK_pZ_L5QZBeJbtH8VsauahUrCrxhx4LlDja_mNaphb5vg4Cfju36A9cwddYJq6VXqYZuXRmT_XFVxHK3KRNlwbTp1Crvbhe2TiKqhZ_RGJR6TmrDb-rhEXo8VElzlJEFlPqmBvC0v5XOKilNB6kPpg8/s1919/Screenshot%202025-04-07%20211034.png)

![Demo](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUyYcs9hOnWHx5IkiSd2zd3vg7zisPcpGvQSTvj1gM6SnzQ-vYPe5CzMm5e6Zt_Pc5mc8VRvV97zjaJ45HOTFjeGjTgOsQXVaMGG4RAiADdCglEO7dBvcUrIqEMJ7siRx2-FWAeGT7BnQ-WFKqUOa_JOlc_Zj-DGcMURfjvU1xDxvTw217G1SoUiA6mD8/s1919/Screenshot%202025-04-07%20211119.png)

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python (Pandas, FPDF)
- **AI Engine**: Google Gemini API
- **Anomaly Detection**: Isolation Forest

---

## 📂 Project Structure

```
ai-fraud-detector/ 
├── app/ 
│ └── streamlit_app.py # Main Streamlit app 
├── src/ 
│ ├── anomaly_detection.py # Anomaly detection logic 
│ ├── gemini_integration.py # Gemini API logic 
│ └── utils.py # Helper functions 
├── data/ 
│ └── transactions.csv # Sample transaction data 
├── .streamlit/ 
│ └── config.toml # App settings for deployment 
├── requirements.txt # Python dependencies 
├── .gitignore # Files and folders to ignore in git 
└── README.md # You are here!
```


## 🔧 Setup Instructions

### 1. Clone the Repo
```
git clone https://github.com/your-username/ai-fraud-detector.git
cd ai-fraud-detector
```

### 2. Install Dependencies
```
pip install -r [requirements.txt](http://_vscodecontentref_/2)
```

### 3. Set Gemini API Key
Create a .env file in the root directory:
```
GEMINI_API_KEY=your_api_key_here
```
For deployment (e.g., on Streamlit Cloud), add this to the Secrets tab instead.

### 4. Run Locally
```
streamlit run [streamlit_app.py](http://_vscodecontentref_/3)
```

## 🌐 Deployment (Streamlit Cloud)
- Push this project to a GitHub repo.
- Go to Streamlit Cloud.
- Connect your GitHub and select the repo.

## 📤 Upload CSV Format
Ensure your CSV has the following columns (can be more):
```
TransactionID,Date,Amount,Description,Merchant,Category
```

## 📎 Sample Data
The app includes a preloaded dataset in data/transactions.csv so you can try it without uploading your own.

## 🧠 Gemini Integration
When you select a transaction, click the "Generate Gemini Explanation" button to get an AI-driven analysis explaining if it's suspicious and why.

## 📄 PDF Report
Click "Generate Report" to download a professional PDF summary of your analysis, including anomalies and metadata.

## 🙌 Contributing
Pull requests are welcome! If you’d like to contribute or suggest a new feature, open an issue or submit a PR.

## 📜 License
MIT License. Feel free to use and adapt.

## 🔗 Connect
Made with ❤️ by Pinak Kundu# Financial-Fraud-Detection
