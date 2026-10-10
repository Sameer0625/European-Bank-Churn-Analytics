# 🇪🇺 Customer Segmentation & Churn Pattern Analytics in European Banking

An end-to-end data analytics and decision-support web application that analyzes customer churn patterns across retail banking operations in **France, Germany, and Spain**. Built with Python, Pandas, Matplotlib, Seaborn, and Streamlit.

---

## 📌 Project Overview
Customer attrition directly reduces customer lifetime value and increases operational costs. This project moves beyond high-level churn reporting to perform granular, multivariate segmentation across geography, age brackets, account balance tiers, credit scores, and customer engagement levels.

---

## 📊 Key Insights & Analytics Findings

* **Overall Baseline Churn Rate**: **20.37%** across the entire dataset (10,000 customers).
* **Geographic Risk Disparity**:
  * **France**: 16.15% churn rate (0.79x baseline risk)
  * **Spain**: 16.67% churn rate (0.82x baseline risk)
  * **Germany**: **32.44% churn rate** (**1.59x regional risk index**)
* **Demographic Vulnerability**: The **46–60 age bracket** exhibits an extreme churn spike of **51.12%**.
* **High-Value Customer Exposure**: **25.23%** of high-balance account holders have exited, signaling major revenue vulnerability.
* **Engagement Drop Correlation**: Inactive members (`IsActiveMember = 0`) churn at **26.85%**, compared to **14.27%** for active members.

---

## 🛠️ Tech Stack & Dependencies

* **Language**: Python 3.x
* **Data Processing**: Pandas, NumPy
* **Data Visualization**: Matplotlib, Seaborn
* **Web Framework**: Streamlit

---

## 📁 Repository Structure

```text
├── European_Bank.csv      # Source dataset (10,000 rows x 14 columns)
├── app.py                 # Streamlit interactive dashboard application
├── README.md              # Project documentation and summary