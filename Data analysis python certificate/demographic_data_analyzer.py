import pandas as pd

data = pd.read_csv(r'C:\Users\barba\Downloads\adult_data.csv')
df = pd.DataFrame(data)

print('VALUES COUNTS', df['race'].value_counts())
print('AGE MEAN', round(df['age'].mean(), 2))
print('DF COLUMNS', df.columns)
print('DF DESCRIBE', df.describe())
print('DF SHAPE', df.shape)
print('DF INFO', df.info())
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df['race'].value_counts()
df = df.set_index('race')

# What is the average age of men?
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 2)

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / len(df) * 100, 2)
print(f"\nPercentage of people who have a Bachelor's degree: {percentage_bachelors}%")

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
percentage_advanced_education = round(len(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')])/len(df)*100, 2)
print(f"\nWhat percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?, {percentage_advanced_education:.2f}%")

# What percentage of people without advanced education make more than 50K?
percentage_no_advanced_education = round(len(df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')])/len(df)*100, 2)
print(f"\nWhat percentage of people without advanced education make more than 50K?, {percentage_no_advanced_education:.2f}%")

# with and without `Bachelors`, `Masters`, or `Doctorate`
higher_education =  round(len(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))])*100/len(df), 2)
print(f"\nWith `Bachelors`, `Masters`, or `Doctorate`, {higher_education:.2f}%")
lower_education = round(len(df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))])*100/len(df), 2)
print(f"\nWithout `Bachelors`, `Masters`, or `Doctorate`, {lower_education:.2f}%")

# percentage with salary >50K
higher_education_rich = round(len(df[df['salary'] == '>50K'])/len(df)*100, 2)
print(f"\npercentage with salary >50K: {higher_education_rich:.2f}%")
lower_education_rich = round(len(df[df['salary'] != '>50K'])/len(df)*100, 2)
print(f"\npercentage with salary <=50K: {lower_education_rich:.2f}%")



# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()
print(f"\nMinimum number of hours a person works per week: {min_work_hours}")

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = round(len(df[(df['hours-per-week'] == min_work_hours)])/len(df)*100,2)
print(f"\nPercentage of the people who work the minimum number of hours per week: {num_min_workers}%")

rich_percentage = round(len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])/len(df)*100,2)
print(f"\nPercentage of the people who work the minimum number of hours per week have a salary of >50K: {rich_percentage}%")

# What country has the highest percentage of people that earn >50K?
highest_earning_country = df['native-country'].value_counts().idxmax()
print(f"\nCountry with the highest percentage of people that earn >50K: {highest_earning_country}")
highest_earning_country_percentage = round(len(df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')])/len(df)*100,2)
print(f"\nHighest percentage of rich people in country: {highest_earning_country_percentage}%")

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
print(f"\nMost popular occupation for those who earn >50K in India: {top_IN_occupation}")



def calculate_demographic_data(print_data=True):
    # Read data from file
    data = pd.read_csv('adult_data.csv')
    df = pd.DataFrame(data)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    df = df.set_index('race')

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean())

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / len(df) * 100)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    percentage_advanced_education = round(len(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')])/len(df)*100)
    # What percentage of people without advanced education make more than 50K?
    percentage_no_advanced_education = round(len(df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')])/len(df)*100)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education =  round(len(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))])*100/len(df))
    lower_education = round(len(df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))])*100/len(df))

    # percentage with salary >50K
    higher_education_rich = round(len(df[df['salary'] == '>50K'])/len(df)*100)
    lower_education_rich = round(len(df[df['salary'] != '>50K'])/len(df)*100)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = round(len(df[(df['hours-per-week'] == min_work_hours)])/len(df)*100   )

    rich_percentage = round(len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])/len(df)*100)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df['native-country'].value_counts().idxmax()
    highest_earning_country_percentage = round(len(df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')])/len(df)*100)
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation}

