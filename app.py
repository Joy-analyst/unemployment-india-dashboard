# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Unemployment in India Dashboard", layout="wide")

@st.cache_data
def load_data(path="Unemployment in India.csv"):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[%\(\)\.]", "", regex=True)
    # rename if trailing underscores
    df.rename(columns={
        'estimated_unemployment_rate_': 'estimated_unemployment_rate',
        'estimated_labour_participation_rate_': 'estimated_labour_participation_rate'
    }, inplace=True)
    # parse dates
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    # numeric conversion
    for c in ['estimated_unemployment_rate','estimated_employed','estimated_labour_participation_rate']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    df = df.dropna(subset=['date'])
    df = df.sort_values('date').reset_index(drop=True)
    return df

df = load_data()

st.title("📊 Unemployment in India — Dashboard")
st.markdown("Interactive exploration of the `Unemployment_in_India.csv` dataset.")

# Sidebar controls
st.sidebar.header("Filters")
min_date = df['date'].min()
max_date = df['date'].max()

date_range = st.sidebar.date_input("Date range", [min_date.date(), max_date.date()])
start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
mask = (df['date'] >= start_date) & (df['date'] <= end_date)
df_filtered = df.loc[mask].copy()

# Area filter if present
if 'area' in df.columns:
    areas = df['area'].dropna().unique().tolist()
    sel_areas = st.sidebar.multiselect("Area", options=areas, default=areas)
    if sel_areas:
        df_filtered = df_filtered[df_filtered['area'].isin(sel_areas)]

# Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Data points", len(df_filtered))
with col2:
    avg_unemp = df_filtered['estimated_unemployment_rate'].mean()
    st.metric("Avg Unemployment Rate (%)", f"{avg_unemp:.2f}")
with col3:
    if 'estimated_employed' in df_filtered.columns:
        st.metric("Avg Employed (est.)", f"{df_filtered['estimated_employed'].mean():.0f}")

# Main charts
st.subheader("Unemployment Rate Over Time")
fig, ax = plt.subplots()
ax.plot(df_filtered['date'], df_filtered['estimated_unemployment_rate'], marker='o', linewidth=1)
ax.set_xlabel("Date")
ax.set_ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
st.pyplot(fig)

# Area comparison
if 'area' in df_filtered.columns:
    st.subheader("Unemployment by Area")
    fig2, ax2 = plt.subplots()
    for area in df_filtered['area'].unique():
        sub = df_filtered[df_filtered['area'] == area]
        ax2.plot(sub['date'], sub['estimated_unemployment_rate'], label=area)
    ax2.legend()
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Unemployment Rate (%)")
    st.pyplot(fig2)

# Show data table and download
st.subheader("Filtered Data")
st.dataframe(df_filtered.reset_index(drop=True))

csv = df_filtered.to_csv(index=False).encode('utf-8')
st.download_button("Download filtered data as CSV", csv, "unemployment_filtered.csv", "text/csv")

# Optional: simple forecast using linear regression on time index
st.subheader("Simple Time Regression Forecast (short horizon)")
from sklearn.linear_model import LinearRegression
df_lr = df[['date','estimated_unemployment_rate']].dropna().copy()
df_lr['time_idx'] = (df_lr['date'] - df_lr['date'].min()).dt.days
if len(df_lr) > 10:
    X = df_lr[['time_idx']]
    y = df_lr['estimated_unemployment_rate']
    model = LinearRegression().fit(X, y)
    # forecast next 6 months
    last_date = df_lr['date'].max()
    future_dates = [last_date + pd.DateOffset(months=i) for i in range(1,7)]
    future_idx = np.array([(d - df_lr['date'].min()).days for d in future_dates]).reshape(-1,1)
    preds = model.predict(future_idx)
    future_df = pd.DataFrame({'date': future_dates, 'predicted_unemployment_rate': preds})
    st.table(future_df)
else:
    st.write("Not enough data for forecasting (need >10 rows).")

st.markdown("---")
st.caption("Built with Streamlit. For more advanced forecasting consider SARIMA/Prophet.")
