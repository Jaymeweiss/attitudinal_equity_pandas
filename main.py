import time

import pandas as pd

from ae_calculations import calculate_attitudinal_equity, calculate_rank_to_power_of_s


def display_brand_level_attitudinal_equity(brand_names_list, total_number_of_rows):
    for brand_name in brand_names_list:
        brand_ae = ranked_df[f"{brand_name}:AE"].sum() / total_number_of_rows
        print(f'Attitudinal Equity for {brand_name}: {brand_ae}')


brand_names = ['Facebook', 'Twitter', 'Google+', 'LinkedIn', 'Tumblr', 'Instagram']

start = time.time()

df = pd.read_csv('survey_data_original.csv')[
    ['Response ID', 'Facebook:performance_rating', 'Twitter:performance_rating',
     'Google+:performance_rating', 'LinkedIn:performance_rating', 'Tumblr:performance_rating',
     'Instagram:performance_rating']].rename(
    columns={'Facebook:performance_rating': 'Facebook', 'Twitter:performance_rating': 'Twitter',
             'Google+:performance_rating': 'Google+', 'LinkedIn:performance_rating': 'LinkedIn',
             'Tumblr:performance_rating': 'Tumblr',
             'Instagram:performance_rating': 'Instagram'})

# Rank the ratings
ranked_df = df[['Facebook', 'Twitter', 'Google+', 'LinkedIn', 'Tumblr', 'Instagram']].rank(axis=1, ascending=False)

# Determine the number of ratings supplied
ranked_df['Number of ratings'] = ranked_df.count(axis=1)
total_rows = ranked_df['Number of ratings'].count()

# Filter and clean responses
ranked_df = ranked_df[ranked_df['Number of ratings'] > 0].fillna(0)

# Calculate rank to inverse s
for brand in brand_names:
    ranked_df[f'{brand}:Rank_S'] = ranked_df.apply(
        lambda x: calculate_rank_to_power_of_s(x[f'{brand}'], int(x['Number of ratings']), ), axis=1)

# Calculate sum rank to inverse s
for brand in brand_names:
    ranked_df['Sum Rank S'] = ranked_df[
        ['Facebook:Rank_S', 'Twitter:Rank_S', 'Google+:Rank_S', 'LinkedIn:Rank_S', 'Tumblr:Rank_S',
         'Instagram:Rank_S']].sum(axis=1)

# Calculate attitudinal equity
for brand in brand_names:
    ranked_df[f'{brand}:AE'] = ranked_df.apply(
        lambda x: calculate_attitudinal_equity(int(x['Number of ratings']), x[f'{brand}'], x['Sum Rank S']), axis=1)

print(ranked_df)

display_brand_level_attitudinal_equity(brand_names, total_rows)

end = time.time()
print('Execution time', end - start)
