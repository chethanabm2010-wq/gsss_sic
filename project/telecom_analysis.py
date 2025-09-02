import pandas as pd

# Step 1: Load data
df = pd.read_csv("call_records.csv")
print("Initial Data:\n", df.head(), "\n")

# Step 2: Normalize column names to lowercase for consistency
df.columns = [col.lower() for col in df.columns]

# Step 3: Data cleaning

df['callduration'] = df['callduration'].fillna(0)  # fill missing durations
df.drop_duplicates(subset='call id', inplace=True)  # drop duplicates
df['callstarttime'] = pd.to_datetime(df['callstarttime'])
df['callendtime'] = pd.to_datetime(df['callendtime'])

# Step 4: Derive columns
df['call_duration_minutes'] = (df['callendtime'] - df['callstarttime']).dt.total_seconds() / 60

def categorize_call(call_type):
    if pd.isna(call_type):
        return 'Other'
    call_type = call_type.lower()
    if call_type in ['local', 'domestic']:
        return 'Domestic'
    elif call_type in ['std', 'isd', 'international']:
        return 'International'
    else:
        return 'Other'

df['call_type_category'] = df['calltype'].apply(categorize_call)
df['call_duration_minutes'] = df['call_duration_minutes'].round(2)

# Step 5: Filtering
long_calls = df[df['call_duration_minutes'] > 10]
cust_calls = df[df['customerid'] == 'C001']
intl_long_calls = df[(df['call_type_category'] == 'International') & (df['call_duration_minutes'] > 30)]

print("Calls > 10 minutes:\n", long_calls[['call id','customerid','calltype','call_duration_minutes']], "\n")
print("Calls by C001:\n", cust_calls[['call id','calltype','call_duration_minutes']], "\n")
print("International calls > 30 minutes:\n", intl_long_calls[['call id','customerid','calltype','call_duration_minutes']], "\n")

# Step 6: Grouping & Aggregation
customer_summary = df.groupby('customerid').agg(
    total_call_duration=('call_duration_minutes', 'sum'),
    average_call_duration=('call_duration_minutes', 'mean'),
    number_of_calls=('call id', 'count')
).reset_index()

call_type_summary = df.groupby('call_type_category').agg(
    total_call_duration=('call_duration_minutes', 'sum'),
    average_call_duration=('call_duration_minutes', 'mean'),
    number_of_calls=('call id', 'count')
).reset_index()

df['call_date'] = df['callstarttime'].dt.date
daily_call_summary = df.groupby('call_date').agg(
    total_call_duration=('call_duration_minutes', 'sum')
).reset_index()

top_customers = customer_summary.sort_values(by='total_call_duration', ascending=False).head(5)

print("Customer Summary:\n", customer_summary, "\n")
print("Call Type Summary:\n", call_type_summary, "\n")
print("Daily Call Summary:\n", daily_call_summary, "\n")
print("Top 5 Customers:\n", top_customers, "\n")

# Step 7: Export results
customer_summary.to_csv("customer_summary.csv", index=False)
call_type_summary.to_csv("call_type_summary.csv", index=False)
daily_call_summary.to_csv("daily_call_summary.csv", index=False)

print("CSV files exported successfully!")

