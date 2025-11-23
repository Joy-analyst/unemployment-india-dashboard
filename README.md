# Unemployment in India Dashboard  
By Joy Uko  

<img width="2733" height="1604" alt="Streamlit" src="https://github.com/user-attachments/assets/51cda7c9-8122-4ddc-b994-f9829d3ebf71" />


**Live App:** [Open the Dashboard](https://unemployment-india-dashboard-rrelcusszzwheb4xs7z79t.streamlit.app/)  

---

##  Project Overview  
This project is an **interactive dashboard** built with [Streamlit](https://streamlit.io) that explores and visualises unemployment trends in India. The dashboard allows users to filter by date range, analyse unemployment rates over time, compare across areas, and even run a simple regression‑based forecast for short‑term prediction.

---

##  Key Features  
- Load and clean the dataset `Unemployment in India.csv`, including handling missing values, normalising column names, and converting types (dates / numeric).  
- Sidebar filters: select date range and area (if available) for custom subsets.  
- Metrics panel: display number of data points, average unemployment rate, and average employed estimate.  
- Time‑series plot of unemployment rate.  
- Comparison chart by area (if area column exists).  
- Data table view and CSV download for filtered data.  
- Simple linear regression for forecasting the unemployment rate for the next 6 months.  
- Clean UI set to “wide” mode for enhanced display.


## Findings / Insights

The analysis from the dataset reveals:

- The estimated unemployment rate shows fluctuations over time, with certain periods experiencing noticeable increases.

- Regional differences are evident: some states/regions consistently report higher unemployment rates than others.

- Labour participation rates vary by area, indicating differences in workforce engagement between urban and rural areas.

- Estimated employment trends align inversely with unemployment trends, reflecting the shifts in workforce availability over time.

<img width="1868" height="973" alt="Unemployment rate" src="https://github.com/user-attachments/assets/5c84e9fb-335a-4c1e-bc6d-3f9cf38dec62" />

---

##  Technologies & Libraries  
- Python 3.x  
- [Streamlit](https://streamlit.io) for the web interface  
- pandas & numpy for data processing  
- matplotlib for static plots  
- scikit‑learn for the regression model  
- seaborn / plotly (optional) for enhanced visualisation  

---
## Linkedin: https://www.linkedin.com/in/joy-uko
## Website: https://sites.google.com/view/joy-uko/portfolio

