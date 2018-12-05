import pandas as pd
from email_sum import summarize


if __name__ == "__main__":


    companies_reviews = pd.read_csv('companies_100_reviews.csv', sep='|', names=["id", "company_name", "pros", "cons"])

    companies_reviews_count = companies_reviews.groupby(['id'], as_index=False)["company_name"].count()

    companies_reviews_count = companies_reviews_count.sort_values(by='company_name', ascending=False)
    companies_high_reviews = list(companies_reviews_count["id"][:1])

    companies_reviews = companies_reviews[companies_reviews["id"].isin(companies_high_reviews)]

    summarize(list(companies_reviews["pros"][:1000]))

    print()