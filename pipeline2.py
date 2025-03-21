# Exercise: Process store_sales.csv and calculate basic statistics
# Your task is to complete this outline with working code
#
# See ./Notes.md for some more instructions and explanations.
pass

# Import the csv module
# Import any other modules you need (e.g., collections for defaultdict)

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
