import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('../simpleDemographicDataAnalyze/adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the
    # index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(np.average(df.age[df['sex'] == 'Male']), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df.education[df['education'] == 'Bachelors'].count()
    edu_total = df['education'].count()
    percentage_bachelors = round((bachelors * 100) / edu_total, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # Numbers of people who make more than 50K
    df_gt50 = df[df['salary'] == '>50K']
    total_num_gt50 = df_gt50.shape[0]
    doctorates_gt50 = df_gt50.education[df_gt50['education'] == 'Doctorate'].count()
    masters_gt50 = df_gt50.education[df_gt50['education'] == 'Masters'].count()
    bachelors_gt50 = df_gt50.education[df_gt50['education'] == 'Bachelors'].count()
    higher_education = doctorates_gt50 + masters_gt50 + bachelors_gt50
    lower_education = total_num_gt50 - higher_education

    # percentage with salary >50K
    higher_education_rich = round((higher_education / total_num_gt50) * 100, 1)
    lower_education_rich = round((lower_education / total_num_gt50) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].values.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    num_rich_min_workers = df_gt50[df_gt50['hours-per-week'] == min_work_hours].shape[0]

    rich_percentage = round((num_rich_min_workers / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df_gt50['native-country'].value_counts().index[0]
    highest_earning_country_percentage = round((df_gt50['native-country'].value_counts()[0] / df.shape[0]) * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df_gt50['occupation'][df_gt50['native-country'] == 'India'].value_counts().index[0]

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
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()
