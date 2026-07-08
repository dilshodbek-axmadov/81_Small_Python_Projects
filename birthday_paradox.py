import random
from datetime import datetime, date
import calendar


def generate_random_day_of_month():
    month = random.randint(1,12)
    year = random.choice([2022,2023,2024,2025,2026])
    # generate all the available days within a month
    weekday, max_days = calendar.monthrange(year,month)
    # generate a random month
    day = random.randint(1,max_days)
    random_date = date(year, month,day)
    return random_date.strftime('%b %d')

def generate_specified_number_of_random_days(n_days):
    return [generate_random_day_of_month() for i in range(n_days)]

def return_duplicate_values(nested_list):
    has_duplicates_dict = {}
    for  index, list_ in enumerate(nested_list):
        has_duplicates_dict[index] = {}
        has_duplicates_dict[index]["seen"] = set()
        has_duplicates_dict[index]["duplicates"] = []
        for item in list_:
            if item not in has_duplicates_dict[index]["seen"]:
                has_duplicates_dict[index]["seen"].add(item)
            else:
                if item not in has_duplicates_dict[index]["duplicates"]:
                    has_duplicates_dict[index]["duplicates"].append(item)
    return has_duplicates_dict

def calculate_duplicates_count(duplicates_dict):
    count = 0
    total = len(duplicates_dict)
    for i in duplicates_dict:
        if duplicates_dict[i]["duplicates"]:
            count += 1
    percentage = round(count/total*100,2)
    return [total,count,percentage]

def main():
    user_output = int(input("How many birthdays should I generate? (max 100)\n> "))
    print(f"Here are {user_output} birthdays")
    generate_specified_number_of_random_days(user_output)

    total_random_days = []
    for i in range(100_000):
        total_random_days.append(generate_specified_number_of_random_days(user_output))
        if i%10_000==0:
            print(f"{i} simulations run...")

    duplicates_list = return_duplicate_values(total_random_days)
    result = calculate_duplicates_count(duplicates_list)

    print(f"Out of 100,000 simulations of {user_output} people, there was a\n"
    f"matching birthday in that group {result[1]} times. This means\n" +
    f"that 23 people have a {result[2]} % chance of\n" +
    f"having a matching birthday in their group.\n" +
    f"That's probably more than you would think!\n")

if __name__ == "__main__":
    main()