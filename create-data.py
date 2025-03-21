import csv
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)

# Create date range for 20 days (resulting in 60 rows - 20 days × 3 stores)
end_date = datetime.now().date()
start_date = end_date - timedelta(days=20)
dates = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(20)]

# Store information
stores = ["Store1", "Store2", "Store3"]

# Open the CSV file for writing
with open('store_sales.csv', 'w', newline='') as file:
    # Create a CSV writer
    csv_writer = csv.writer(file)

    # Write the header row
    csv_writer.writerow(['date', 'store_id', 'items_sold', 'revenue'])

    # Generate 60 records (20 days × 3 stores)
    for date in dates:
        for store in stores:
            # Generate random data for each store on each date
            # Each store has a different sales pattern
            if store == "Store1":
                items = random.randint(20, 50)
                price_per_item = random.uniform(10, 20)
            elif store == "Store2":
                items = random.randint(30, 70)
                price_per_item = random.uniform(8, 15)
            else:  # Store3
                items = random.randint(15, 40)
                price_per_item = random.uniform(15, 25)

            # Calculate revenue (with some randomness)
            revenue = round(items * price_per_item * random.uniform(0.9, 1.1), 2)

            # Write the row
            csv_writer.writerow([date, store, items, revenue])

print("Created store_sales.csv with 60 records")
