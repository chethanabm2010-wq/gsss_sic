import pandas as pd

# Load original call records
df = pd.read_csv("call_records.csv")

# Ensure column names are consistent
df.columns = [c.strip() for c in df.columns]

# Convert call times to datetime
df['CallStartTime'] = pd.to_datetime(df['CallStartTime'], dayfirst=True)
df['CallEndTime'] = pd.to_datetime(df['CallEndTime'], dayfirst=True)

# Calculate call duration in minutes (override if needed)
df['CallDuration'] = (df['CallEndTime'] - df['CallStartTime']).dt.total_seconds() / 60

# ----------------- Customer Summary -----------------
customer_summary = df.groupby("CustomerID").agg(
    NumberOfCalls=("CallID", "count"),
    TotalDuration=("CallDuration", "sum"),
    AverageDuration=("CallDuration", "mean")
).reset_index()

customer_summary.to_csv("customer_summary.csv", index=False)

# ----------------- Call Type Summary -----------------
def categorize_call(call_type):
    call_type = str(call_type).strip().lower()
    if call_type in ["local", "domestic"]:
        return "Local"
    elif call_type in ["std", "isd", "international"]:
        return "International"
    else:
        return "Other"

df['CallTypeCategory'] = df['CallType'].apply(categorize_call)

call_type_summary = df.groupby("CallTypeCategory").agg(
    NumberOfCalls=("CallID", "count"),
    TotalDuration=("CallDuration", "sum")
).reset_index()

call_type_summary.to_csv("call_type_summary.csv", index=False)

# ----------------- Daily Summary -----------------
df['CallDate'] = df['CallStartTime'].dt.date

daily_summary = df.groupby("CallDate").agg(
    NumberOfCalls=("CallID", "count"),
    TotalDuration=("CallDuration", "sum")
).reset_index()

daily_summary.to_csv("daily_call_summary.csv", index=False)

print("All summary CSVs generated successfully!")
