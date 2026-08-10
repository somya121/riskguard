from .generator import generate_credit_portfolio


df = generate_credit_portfolio(
    n_customers=10000,
    n_months=24,
    random_state=42
)

output_path = (
    "data/raw/credit_portfolio.csv"
)

df.to_csv(
    output_path,
    index=False
)

print("Dataset created successfully.")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(
    f"Default rate: "
    f"{df['default_flag'].mean():.2%}"
)