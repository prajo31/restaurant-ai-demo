import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Restaurant AI Demo", layout="wide")

# -----------------------------
# Sample Data
# -----------------------------
def create_sample_sales_data():
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
    sales = np.random.randint(1000, 3000, size=30)
    return pd.DataFrame({"date": dates, "sales": sales})

def create_sample_reviews():
    return pd.DataFrame({
        "review": [
            "Great food and service",
            "Service was slow",
            "Amazing experience",
            "Food was cold",
            "Loved the ambience",
            "Wait time too long"
        ]
    })

def create_sample_inventory():
    return pd.DataFrame({
        "item": ["Chicken", "Rice", "Tomatoes"],
        "stock": [10, 50, 5],
        "daily_use": [5, 10, 4]
    })

# -----------------------------
# App Title
# -----------------------------
st.title("🍽️ Restaurant AI Dashboard")

# -----------------------------
# Load Data
# -----------------------------
sales_df = create_sample_sales_data()
reviews_df = create_sample_reviews()
inventory_df = create_sample_inventory()

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3 = st.tabs(["📊 Sales Forecast", "⭐ Review Insights", "📦 Inventory Alert"])

# -----------------------------
# 1. Sales Forecast
# -----------------------------
with tab1:
    st.header("Sales Forecast")

    st.line_chart(sales_df.set_index("date"))

    avg_sales = sales_df["sales"].mean()
    prediction = avg_sales * np.random.uniform(0.9, 1.1)

    st.success(f"Predicted sales for tomorrow: ${prediction:.0f}")

# -----------------------------
# 2. Review Insights
# -----------------------------
with tab2:
    st.header("Customer Review Insights")

    st.dataframe(reviews_df)

    if st.button("Analyze Reviews"):
        st.write("Top issue: Slow service")
        st.write("Strength: Food quality")

# -----------------------------
# 3. Inventory Alert
# -----------------------------
with tab3:
    st.header("Inventory Alert")

    inventory_df["days_left"] = inventory_df["stock"] / inventory_df["daily_use"]
    st.dataframe(inventory_df)

    low_stock = inventory_df[inventory_df["days_left"] < 3]

    if not low_stock.empty:
        st.warning("Items running low:")
        st.write(low_stock["item"].tolist())
    else:
        st.success("Inventory levels are good")

# -----------------------------
# Footer
# -----------------------------
st.write("---")
st.write("AI helps turn restaurant data into decisions.")
