from datetime import timedelta

# Spot USD/INR rate (example)
spot_rate = 83.20  

# Interest rates (annualized, example values)
usd_rate = 0.05   # 5% USD interest rate
inr_rate = 0.07   # 7% INR interest rate

# Define tenors in days
tenors = {
    "TDY": 0,   # Today
    "TOM": 1,   # Tomorrow
    "SPOT": 2,  # Spot (T+2)
    "ON": 1,    # Overnight
    "TN": 2,    # Tomorrow Next
    "SN": 3,    # Spot Next
    "1D": 1,
    "5D": 5,
    "1W": 7,
    "1M": 30,
    "2M": 60,
    "3M": 90,
    "6M": 180,
    "1Y": 365,
    "2Y": 730,
    "3Y": 1095,
    "5Y": 1825,
    "10Y": 3650
}

def forward_rate(spot, usd_rate, inr_rate, days):
    T = days / 365.0  # convert days to years
    return spot * (1 + inr_rate * T) / (1 + usd_rate * T)

# Calculate rates for all tenors
for tenor, days in tenors.items():
    rate = forward_rate(spot_rate, usd_rate, inr_rate, days)
    print(f"{tenor}: {rate:.4f}")
