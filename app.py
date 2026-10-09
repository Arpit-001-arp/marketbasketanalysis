import streamlit as st
import pandas as pd
from itertools import combinations
from collections import Counter

# Page configuration
st.set_page_config(
    page_title="Market Basket Analysis",
    page_icon="🛒",
    layout="wide"
)

# App Title & Description
st.title("🛒 Market Basket Analysis")
st.write(
    "A simple beginner-friendly project that analyzes shopping baskets "
    "to find popular items and products frequently bought together."
)

# 1. Sample Shopping Dataset (Created inside the project)
transactions = [
    ["Milk", "Bread", "Butter"],
    ["Bread", "Butter"],
    ["Milk", "Cookies", "Coffee"],
    ["Bread", "Butter", "Eggs"],
    ["Milk", "Bread", "Eggs"],
    ["Coffee", "Cookies"],
    ["Milk", "Bread", "Butter", "Eggs"],
    ["Bread", "Butter", "Coffee"],
    ["Milk", "Eggs"],
    ["Coffee", "Cookies", "Bread"],
    ["Milk", "Bread", "Butter"],
    ["Bread", "Butter", "Cookies"]
]

# Quick Summary Metrics
all_items = [item for basket in transactions for item in basket]
item_counts = pd.Series(all_items).value_counts()

col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("🧺 Total Baskets", len(transactions))
col_m2.metric("🛍️ Total Items Sold", len(all_items))
col_m3.metric("🏷️ Unique Products", len(item_counts))

# Display Sample Dataset
st.subheader("📋 Sample Shopping Dataset")
df_transactions = pd.DataFrame({
    "Basket ID": [f"Basket #{i+1}" for i in range(len(transactions))],
    "Items": [", ".join(basket) for basket in transactions]
})
st.dataframe(df_transactions, use_container_width=True)

# 2. Top 5 Most Purchased Products
top_5_products = item_counts.head(5).reset_index()
top_5_products.columns = ["Product", "Times Purchased"]

col1, col2 = st.columns(2)

with col1:
    st.subheader("⭐ Top 5 Most Purchased Products")
    st.dataframe(top_5_products, use_container_width=True)

# 3. Easy Bar Chart
with col2:
    st.subheader("📊 Product Popularity Chart")
    chart_data = top_5_products.set_index("Product")
    st.bar_chart(chart_data)

# 4. 3 Simple Examples of Products Bought Together
pair_counter = Counter()

for basket in transactions:
    # Sort items so ('Bread', 'Butter') and ('Butter', 'Bread') are counted as the same pair
    unique_items = sorted(list(set(basket)))
    for pair in combinations(unique_items, 2):
        pair_counter[pair] += 1

# Get the top 3 most common pairs
top_3_pairs = pair_counter.most_common(3)

st.subheader("🤝 3 Examples of Products Bought Together")
st.write("Here are the top 3 pairs of products most commonly found in the same basket:")

cols = st.columns(3)
for idx, (pair, count) in enumerate(top_3_pairs):
    with cols[idx]:
        st.metric(
            label=f"Example #{idx + 1}",
            value=f"{pair[0]} + {pair[1]}",
            delta=f"Bought together {count} times"
        )

# 5. Interactive Product Recommendation Finder
st.subheader("🔍 Interactive Recommendation Finder")
selected_product = st.selectbox(
    "Select a product to see what customers also buy with it:",
    options=sorted(list(set(all_items)))
)

# Find items that appear with the selected product
co_items = [item for basket in transactions if selected_product in basket for item in basket if item != selected_product]

if co_items:
    co_counts = pd.Series(co_items).value_counts().reset_index()
    co_counts.columns = ["Bought Together With", "Times Purchased Together"]
    top_co = co_counts.iloc[0]
    st.success(
        f"💡 Customers who bought **{selected_product}** most often also bought **{top_co['Bought Together With']}** "
        f"({top_co['Times Purchased Together']} times)!"
    )
    st.dataframe(co_counts, use_container_width=True)
