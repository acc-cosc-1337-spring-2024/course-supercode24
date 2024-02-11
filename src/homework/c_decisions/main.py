from decisions import get_options_ratio, get_faculty_rating

options = float(input("enter options:"))
total = float(input("Enter total:"))

result = get_options_ratio(options, total)
print("Faculty Rating:", get_faculty_rating(result))