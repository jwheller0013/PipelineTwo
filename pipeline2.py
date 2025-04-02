# Exercise: Process store_sales.csv and calculate basic statistics
# Your task is to complete this outline with working code
#
# See ./Notes.md for some more instructions and explanations.
pass

# Import the csv module
# Import any other modules you need (e.g., collections for defaultdict)
import csv

# Initialize data structures to hold our results
# Hint: Consider using a dictionary with store_id as keys
# For each store, you'll need to track:
#   - Count of days
#   - Total items sold
#   - Total revenue
#   - Minimum revenue
#   - Maximum revenue

# Open the CSV file for reading
# Remember to use "with" to ensure the file gets closed properly

    # Create a CSV reader

    # Read the header row first

    # Loop through each row in the CSV file
        # Extract values from each row (date, store_id, items_sold, revenue)
        # Convert numerical values to the right data types (int, float)

        # Update the appropriate store's statistics:
        #   - Increment day count
        #   - Add to total items
        #   - Add to total revenue
        #   - Update min revenue if current is lower
        #   - Update max revenue if current is higher

# Calculate averages for each store
# For each store in your data structure:
    # Calculate average items per day (total_items / days)
    # Calculate average revenue per day (total_revenue / days)

# Determine which store had the highest average daily revenue
# Initialize variables to track best store and its revenue
# Loop through stores and compare average revenues

# Print a summary of statistics for each store
# Print which store had the highest average daily revenue
store_template = {
    "Days": 0,
    "items_sold": 0,
    "total_Revenue": 0,
    "min_Revenue": None,
    "max_Revenue": None,
    "transactions": 0
}

stores = {
}


with open('store_sales.csv', 'r', newline='') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    sum_of_items = 0
    lines = 0
    for line in csv_reader:
        print(line)
        if lines == 0:
            lines += 1
            continue
        sum_of_items += int(line[2])
        curstore = line[1]
        if stores.get(curstore) == None:
            stores[curstore] = store_template.copy()
        stores[curstore]["items_sold"] += int(line[2])
        stores[curstore]["Days"] += 1
        stores[curstore]['transactions'] += 1
        x = round(float(line[3]), 2)

        stores[curstore]["total_Revenue"] += x

        if stores[curstore]["min_Revenue"] is None or x < stores[curstore]["min_Revenue"] :
            stores[curstore]["min_Revenue"] = x

        if stores[curstore]["max_Revenue"] is None or x > stores[curstore]["max_Revenue"] :
            stores[curstore]["max_Revenue"] = x

        lines += 1

    print(f"Total number of items sold: {sum_of_items}")
    print(f"Total number of transactions: {lines}")
    print(stores)

store_averages = {}
for store_id, data in stores.items():
    days = data["Days"]
    if days > 0:
        avg_items = data['items_sold'] / days
        avg_revenue = data['total_Revenue'] / days
        store_averages[store_id] = {
            "avg_items_per_day": avg_items,
            "avg_rev_per_day": avg_revenue
        }
    else:
        store_averages[store_id] = {
            "avg_items_per_day": 0,
            "avg_rev_per_day": 0
        }
print(store_averages)

highest = 0
top_store = None
for store_id, average in store_averages.items():
    if average["avg_rev_per_day"] > highest:
        highest = average["avg_rev_per_day"]
        top_store = store_id

print(top_store)