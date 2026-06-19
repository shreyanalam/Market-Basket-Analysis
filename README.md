# 🛒 Market Basket Analysis Dashboard

## 📌 Project Overview
This project performs Market Basket Analysis using the Apriori Algorithm and Association Rule Mining techniques. It analyzes customer purchase transactions to identify frequently bought product combinations and generate product recommendations.

The project is developed using Python and Streamlit, providing an interactive dashboard for data visualization and analysis.

---

## 🎯 Objectives
- Analyze customer purchasing behavior.
- Discover frequently purchased item combinations.
- Generate association rules between products.
- Recommend products based on purchase patterns.
- Visualize sales trends and product frequencies.

---

## 🚀 Features
- Interactive Streamlit Dashboard
- Top Selling Products Analysis
- Frequent Itemset Mining
- Association Rule Generation
- Product Recommendation System
- Data Visualization using Charts
- Easy-to-use User Interface

---

## 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib
- MLxtend
- NumPy

---

## 📂 Project Structure

```text
Market_Basket_Analysis/
│
├── app.py
├── dataset.csv
├── requirements.txt
└── README.md
```

## 📊 Methodology

### 1. Data Collection
Transaction data is loaded from the dataset.

### 2. Data Preprocessing
Transactions are converted into a suitable format for analysis.

### 3. Transaction Encoding
One-Hot Encoding is applied using TransactionEncoder.

### 4. Frequent Itemset Mining
The Apriori Algorithm is used to find frequently purchased itemsets.

### 5. Association Rule Mining
Rules are generated based on:
- Support
- Confidence
- Lift

### 6. Product Recommendation
Products are recommended based on generated association rules.

---

## ▶️ How to Run

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

If Streamlit is not recognized:

```bash
python -m streamlit run app.py
```

---

## 📈 Output
The dashboard provides:

- Top Selling Products
- Product Frequency Charts
- Frequent Itemsets
- Association Rules
- Product Recommendations
- Lift-based Rule Ranking

---

## 📚 Learning Outcomes
- Understanding Market Basket Analysis
- Implementing Apriori Algorithm
- Generating Association Rules
- Data Visualization
- Building Interactive Dashboards with Streamlit

---

## 👩‍💻 Author

Shreya Nalam

B.Tech Data Science

Intern ID : CITS2841
