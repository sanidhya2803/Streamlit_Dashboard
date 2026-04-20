# 📊 Interactive Data Dashboard

A no-code data visualization tool built with **Streamlit** and **Plotly Express**. Upload a dataset and instantly explore it through interactive charts and summary statistics.

Demo Link: https://appdashboard-abtguasbfzyzbpovozf26m.streamlit.app

---

## 🚀 Features

- 📁 **File Upload** — Supports CSV and Excel (`.xlsx`) files
- 📈 **6 Chart Types** — Bar, Histogram, Line, Scatter, Pie, Heatmap
- ⚙️ **Dynamic Controls** — Axis selectors auto-adjust based on chart type
- 🥧 **Pie Aggregations** — Count or Sum modes
- 🔥 **Correlation Heatmap** — Auto-detects numeric columns
- 🗂️ **Data Preview** — Head and Describe tabs for quick data inspection

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| Streamlit | UI & app framework |
| Plotly Express | Interactive charts |
| Pandas | Data handling |
| NumPy | Numerical support |

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/dashboard.git
cd dashboard

# Install dependencies
pip install streamlit plotly pandas numpy

# Run the app
streamlit run app.py
```

---

## 📖 Usage

1. Run the app and open it in your browser (`http://localhost:8501`)
2. Upload a **CSV** or **Excel** file using the file uploader
3. Select a **chart type** from the dropdown
4. Choose your **X** and **Y** axis columns
5. View the interactive chart and data preview side by side

---

## 📂 Project Structure

```
dashboard/
├── app.py        # Main Streamlit application
└── README.md     # Project documentation
```

---

## 📸 Preview

> Upload a CSV → Select a chart → Explore your data instantly.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
