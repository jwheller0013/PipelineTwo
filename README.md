# PipelineTwo - Basic CSV Processing with Python

## Exercise: Simple Data Analysis Without Pandas

**Objective:** Read a small CSV file using Python's built-in CSV module, and calculate basic statistics (min, max, sum, average) for each numerical column.

**Dataset:** `store_sales.csv` (60 lines) with the following columns:
- `date` (string): Sales date in YYYY-MM-DD format
- `store_id` (string): Store identifier ("Store1", "Store2", or "Store3")
- `items_sold` (integer): Number of items sold that day
- `revenue` (float): Total revenue for that day in dollars

**Tasks:**
0. read the file `pipeline2.py` for a psuedo-code outline of what needs to be done.
1. Read the CSV file using Python's built-in `csv` module
2. For each store, calculate:
   - Total items sold
   - Average items sold per day
   - Minimum daily revenue
   - Maximum daily revenue
   - Total revenue
3. Print a summary of the statistics for each store
4. Determine which store had the highest average daily revenue


## Sample Data Generation

Here's a Python script to generate the sample dataset for this exercise:

```python
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

print(f"Created store_sales.csv with 60 records")
```

This exercise will help you practice basic file I/O operations and data processing
in Python without relying on pandas or other external libraries.
It focuses on essential programming concepts like reading files, data structures, and basic calculations.

Remember with `age` you should have faith that **zipcoderocks**.
