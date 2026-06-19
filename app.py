import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Market Basket Analysis",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Market Basket Analysis Dashboard")
st.markdown("---")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("dataset.csv")

transactions = []

for items in df["Items"]:
    transactions.append(items.split(","))

# --------------------------------------------------
# TOP SELLING PRODUCTS
# --------------------------------------------------

all_items = []

for transaction in transactions:
    all_items.extend(transaction)

item_counts = Counter(all_items)

product_df = pd.DataFrame(
    item_counts.items(),
    columns=["Product", "Frequency"]
)

product_df = product_df.sort_values(
    by="Frequency",
    ascending=False
)

st.subheader("📊 Top Selling Products")

col1, col2 = st.columns([1, 1])

with col1:
    st.dataframe(product_df)

with col2:
    fig, ax = plt.subplots(figsize=(6,4))

    ax.bar(
        product_df["Product"],
        product_df["Frequency"]
    )

    ax.set_title("Top Products")
    ax.set_xlabel("Products")
    ax.set_ylabel("Frequency")

    st.pyplot(fig)

# --------------------------------------------------
# ENCODING
# --------------------------------------------------

encoder = TransactionEncoder()

encoded = encoder.fit(transactions).transform(transactions)

basket = pd.DataFrame(
    encoded,
    columns=encoder.columns_
)

# --------------------------------------------------
# APRIORI
# --------------------------------------------------

frequent_itemsets = apriori(
    basket,
    min_support=0.20,
    use_colnames=True
)

st.subheader("📈 Frequent Itemsets")

st.dataframe(frequent_itemsets)

# --------------------------------------------------
# ASSOCIATION RULES
# --------------------------------------------------

rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.50
)

st.subheader("🔗 Association Rules")

show_rules = rules[
    [
        "antecedents",
        "consequents",
        "support",
        "confidence",
        "lift"
    ]
]

st.dataframe(show_rules)

# --------------------------------------------------
# RECOMMENDATION SYSTEM
# --------------------------------------------------

st.subheader("🎯 Product Recommendation")

products = sorted(list(item_counts.keys()))

selected_product = st.selectbox(
    "Select a Product",
    products
)

recommendations = []

for _, row in rules.iterrows():

    antecedent = list(row["antecedents"])

    consequent = list(row["consequents"])

    if selected_product in antecedent:

        recommendations.extend(consequent)

if recommendations:

    st.success(
        "Customers who buy '{}' also buy: {}".format(
            selected_product,
            ", ".join(set(recommendations))
        )
    )

else:

    st.warning(
        "No recommendation found."
    )

# --------------------------------------------------
# BEST RULES
# --------------------------------------------------

st.subheader("🏆 Top Rules by Lift")

top_rules = rules.sort_values(
    by="lift",
    ascending=False
)

st.dataframe(
    top_rules[
        [
            "antecedents",
            "consequents",
            "confidence",
            "lift"
        ]
    ].head(10)
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")
st.markdown(
    "Developed using Python, Streamlit, Apriori Algorithm and Association Rule Mining."
)
