import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(page_title="European Banking Churn Analytics", layout="wide")

st.title("🇪🇺 Customer Segmentation & Churn Pattern Analytics in European Banking")
st.markdown("Interactive Decision-Support Dashboard for European Banking Stakeholders.")

# Load Data function
@st.cache_data
def load_data():
    df = pd.read_csv('European_Bank.csv')
    df = df.drop(columns=['CustomerId', 'Surname', 'Year'], errors='ignore')
    
    # Derived Segmentation Fields
    df['Age_Group'] = pd.cut(df['Age'], bins=[0, 29, 45, 60, 100], labels=['<30', '30-45', '46-60', '60+'])
    df['CreditScore_Band'] = pd.qcut(df['CreditScore'], q=3, labels=['Low', 'Medium', 'High'])
    df['Tenure_Group'] = pd.cut(df['Tenure'], bins=[-1, 2, 6, 10], labels=['New', 'Mid-term', 'Long-term'])
    df['Balance_Segment'] = pd.cut(df['Balance'], bins=[-1, 1, 100000, 300000], labels=['Zero-balance', 'Low-balance', 'High-balance'])
    return df

try:
    df_cleaned = load_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Segment Filters")
selected_geo = st.sidebar.multiselect("Select Geography", options=df_cleaned['Geography'].unique(), default=df_cleaned['Geography'].unique())
selected_gender = st.sidebar.multiselect("Select Gender", options=df_cleaned['Gender'].unique(), default=df_cleaned['Gender'].unique())

# Filter Data safely
filtered_df = df_cleaned[
    (df_cleaned['Geography'].isin(selected_geo)) & 
    (df_cleaned['Gender'].isin(selected_gender))
]

# --- KPIS ---
st.markdown("### 📊 Key Performance Indicators")
total_cust = len(filtered_df)
if total_cust > 0:
    churn_rate = (filtered_df['Exited'].sum() / total_cust) * 100
    high_bal_churn = filtered_df[filtered_df['Balance_Segment'] == 'High-balance']['Exited'].mean() * 100
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Filtered Customers", f"{total_cust:,}")
    col2.metric("Overall Churn Rate", f"{churn_rate:.2f}%")
    col3.metric("High-Balance Churn Rate", f"{high_bal_churn:.2f}%" if not pd.isna(high_bal_churn) else "0.00%")
else:
    st.warning("No customers match the selected filter criteria.")

st.markdown("---")

# --- TABS ---
tab1, tab2 = st.tabs(["🌍 Geography & Regional Risk", "💰 High-Value Churn Explorer"])

with tab1:
    st.subheader("Geography-wise Churn Distribution")
    if not filtered_df.empty:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.data = filtered_df.groupby('Geography')['Exited'].mean().reset_index()
        sns.barplot(data=filtered_df, x='Geography', y='Exited', ax=ax, palette='Blues_d')
        ax.set_ylabel("Churn Rate")
        st.pyplot(fig)
    else:
        st.info("No data to display.")

with tab2:
    st.subheader("High-Value Customer Churn Explorer")
    high_val_subset = filtered_df[filtered_df['Balance_Segment'] == 'High-balance']
    st.write(f"Showing high-balance customer records ({len(high_val_subset)} found):")
    st.dataframe(high_val_subset[['CreditScore', 'Geography', 'Gender', 'Age', 'Balance', 'EstimatedSalary', 'Exited']].head(10))