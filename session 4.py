def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not a leap year"

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def calculate_total_payment(total_purchase):
    if total_purchase > 100000:
        discount = 0.10
    elif total_purchase > 50000:
        discount = 0.05
    else:
        discount = 0
    total_payment = total_purchase - (total_purchase * discount)
    return total_payment

def check_graduation(math, science, english):
    average = (math + science + english) / 3
    below_70_count = sum(1 for score in [math, science, english] if score < 70)
    if average > 75 or below_70_count == 1 or any(score == 100 for score in [math, science, english]):
        return "Pass"
    else:
        return "Fail"

# Example usage
print(leap_year(2024))
print(check_number(-5))
print(calculate_total_payment(120000))
print(check_graduation(80, 65, 90))