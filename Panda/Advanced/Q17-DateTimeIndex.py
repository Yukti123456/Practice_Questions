#Q17- Create arolling 7-day average of sales data with datetime index .

import pandas as pd

# Create date range
dates = pd.date_range(start="2024-01-01", periods=15, freq="D")

# Create sales data
df = pd.DataFrame({
    "Sales": [200, 220, 250, 240, 260, 270, 300,
              310, 290, 280, 350, 360, 370, 390, 400]
}, index=dates)

print(df)
df["7_day_avg"] = df["Sales"].rolling(window=7).mean()

print(df)
