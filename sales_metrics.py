def calculate_daily_sales(sales):
    """
    Calculates the total sales for the day.
    :param sales: list of numerical sales values
    :return: total sales sum
    """
    return sum(sales)

if __name__ == "__main__":
    sample_sales = [100, 200, 150]
    print("Total Sales:", calculate_daily_sales(sample_sales))

def filter_sales(sales, threshold=100):
    """
    Filters out sales below a given threshold.
    :param sales: list of numerical sales values
    :param threshold: minimum sale value to keep
    :return: filtered list of sales
    """
    return [sale for sale in sales if sale >= threshold]

if __name__ == "__main__":
    sample_sales = [50, 100, 200, 75, 150]
    filtered = filter_sales(sample_sales, threshold=100)
    print("Filtered Sales:", filtered)
    print("Total Filtered Sales:", calculate_daily_sales(filtered))
