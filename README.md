# Market Basket Analysis (Beginner Project)

A simple, beginner-friendly Python project that demonstrates **Market Basket Analysis** using **Pandas** and **Streamlit**.

This project analyzes a built-in sample of grocery shopping transactions to uncover customer buying patterns—identifying the most popular items, frequently co-purchased product pairs, and interactive product recommendations—without complex algorithms or external databases.

---

## 🌟 Features

* **Built-in Sample Dataset**: Realistic shopping baskets created directly inside the project code.
* **Summary KPI Metrics**: Quick cards showing Total Baskets, Total Items Sold, and Unique Products.
* **Top 5 Most Purchased Products**: Summary table showing which items are bought the most.
* **Interactive Bar Chart**: Clean visual representation of product sales frequencies using Streamlit's built-in chart.
* **Co-occurrence Analysis**: 3 straightforward examples of items frequently bought together (e.g., Bread & Butter).
* **Interactive Recommendation Finder**: Select any product to instantly see which items customers also buy with it.
* **Beginner-Friendly Code**: Written cleanly in Python using standard libraries (`itertools`, `collections`) and `pandas`.

---

## 📁 Project Structure

```text
Market_Basket_Basic/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies (pandas, streamlit)
└── README.md           # Instructions and documentation
```

---

## 🚀 How to Run on Windows

Follow these simple steps in **Command Prompt (CMD)** or **PowerShell**:

### Step 1: Open Terminal in the Project Folder
Open PowerShell or Command Prompt and navigate to the project directory:
```powershell
cd d:\Internship\Market_Basket_Basic
```

### Step 2: (Recommended) Create & Activate a Virtual Environment
```powershell
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install the Required Packages
Install **Pandas** and **Streamlit** using `pip`:
```powershell
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application
Launch the app with Streamlit:
```powershell
streamlit run app.py
```

### Step 5: View the App in Your Browser
Streamlit will automatically open your default browser. If it doesn't, navigate to:
```text
http://localhost:8501
```

To stop the application, press `Ctrl + C` in your terminal window.

---

## 💡 How It Works

1. **Transaction Data**: Baskets are represented as lists of items (e.g., `["Milk", "Bread", "Butter"]`).
2. **Frequency Counting**: All basket items are tallied to rank the top 5 most popular products.
3. **Product Pairing**: Standard Python `itertools.combinations` pairs every combination of two items within each basket. A counter tallies these pairs to reveal which items customers buy together most often.
4. **Interactive Recommendations**: Filters transactions containing a chosen product to rank companion items.
