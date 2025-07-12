# 🚀 SecuriLogX
SecuriLogX is a Flask-based cybersecurity log analysis web application.  
Upload your `.log` or `.txt` files, and the system will scan for suspicious activity, assign severity levels, and display clear, actionable results.

---

## ✨ Features
✅ Upload and analyze `.log` / `.txt` files  
✅ Detect suspicious keywords automatically  
✅ Assign severity levels (Low, Medium, High, Critical)  
✅ Clean web interface with easy navigation  
✅ Instant results summary in a readable table  
✅ Ready to extend for more advanced detection

---

## 📂 Project Structure
secLogX_clean/
├── run.py
├── app/
│ ├── init.py
│ ├── routes.py
│ └── templates/
│ ├── index.html
│ └── analysis.html


---

## ⚙️ Installation & Setup

1️⃣ **Clone this repository**
https://github.com/chahankar-arya04


2️⃣ **Create a virtual environment**
3️⃣ **Activate the environment**
- On Windows:

4️⃣ **Install dependencies**
5️⃣ **Run the app**
6️⃣ **Open in your browser**


## 🛡️ How It Works

1. Upload a `.log` or `.txt` file.
2. The app scans each line for suspicious keywords:
   - `error` → Low
   - `failed` → Medium
   - `unauthorized`, `admin` → High
   - `root` → Critical
3. Results display in a table showing:
   - Log Line
   - Severity Level with icons

---

## 🌟 Screenshots

*(Add screenshots here)*

---

## 🧩 Future Enhancements

✅ Export analysis results as CSV or PDF  
✅ Add user authentication  
✅ Integrate regex-based detection patterns  
✅ Create a dashboard with usage statistics  
✅ Style with Bootstrap for a professional UI  

---

## 🧑‍💻 Author

**Your Name Here**
- [LinkedIn](https://www.linkedin.com/in/arya-chahankar-27ba24262/)
- [GitHub](https://github.com/chahankar-arya04)


---

## 📝 License

This project is licensed for educational and demonstration purposes.






