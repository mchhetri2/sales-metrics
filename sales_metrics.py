def calculate_daily_sales(sales):
    """
    Calculates the total sales for the day.
    :param sales: list of numerical sales values
    :return: total sales sum
    """
    return sum(sales)

def filter_sales(sales, threshold=100):
    """
    Filters out sales below a given threshold.
    :param sales: list of numerical sales values
    :param threshold: minimum sale value to keep
    :return: filtered list of sales
    """
    return [sale for sale in sales if sale >= threshold]

def apply_discount(sales, discount_rate=0.1):
    """
    Applies a discount to each sale.
    :param sales: list of numerical sales values
    :param discount_rate: decimal discount rate to apply (e.g., 0.1 for 10%)
    :return: list of discounted sales
    """
    return [round(sale * (1 - discount_rate), 2) for sale in sales]

if __name__ == "__main__":
    sample_sales = [50, 100, 200, 75, 150]

    filtered = filter_sales(sample_sales, threshold=100)
    print("Filtered Sales:", filtered)

    discounted = apply_discount(filtered, discount_rate=0.1)
    print("Discounted Sales:", discounted)

    total = calculate_daily_sales(discounted)
    print("Total Sales after Discount:", total)

