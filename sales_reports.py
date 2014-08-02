from myarray import myArray
from myarray import MultiArray

# Compute the total sales of all items for all months in a given store.
def totalSalesByStore( salesData, store):
    # Subtract 1 from the store #  since the array indices are 1 less
    # than the given store #
    s = store - 1
    # Accumulate the total sales for the given store.
    total = 0.0

    # Iterate over item.
    for i in range( salesData.length(2) ):
        # Iterator over each month of the i item
        for m in range( salesData.length(3) ):
            total += salesData[s, i, m]

    return total

# Compute the total sales of all item in all stores for a given month.
def totalSalesByMonth( salesData, month ):
    # The month number must be offset by 1.
    m = month - 1
    # Accumulate the total sales for the given month.
    total = 0.0

    # Iterate over each store.
    for s in range( salesData.length(1) ):
        # Iterate over each item of the s store.
        for i in range( salesData.length(2) ):
            total += salesData[s, i, m]

    return total

# Compute the total sales of a single item in all stores over months.
def totalSalesByItem( salesData, item):
    m = item - 1
    total = 0.0
    for s in range( salesData.length(1) ):
        for m in range( salesData.length(3) ):
            total += salesData[s, i, m]
    return total

# Compute the total sales per month for a given store. A 1-D array is
# returned that contains the totals for each month.
def totalSalesPerMonth( salesData, store ):
    # The store number must be offset by 1
    s = store - 1
    # The totals will be returned in a 1-D array.
    totals = myArray( 12 )
    # Iterate over the sales of each month.
    for m in range( salesData.length(3) ):
        sum = 0.0
        # Iterate over the sales of each item sold during the m month.
        for i in range( salesData.length(2) ):
            sum += salesData[s, i, m]
        totals[m] = sum
    return totals

salesData = MultiArray( 8, 100, 12)
for i in range(8):
    for j in range(100):
        for k in range(12):
            salesData[i, j, k] = i + 0.0

print totalSalesByStore( salesData, 2)
print totalSalesByMonth( salesData, 2)
print totalSalesByItem( salesData, 3)

salesPerMonth = totalSalesPerMonth( salesData, 1)
for i in range(12):
    print salesPerMonth[i],
print ''
