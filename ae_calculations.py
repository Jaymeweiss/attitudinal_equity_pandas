DEFAULT_RANK_SUM = 1
s_values = (0, 2.33, 1.69, 1.32, 0.88)


def get_s_value(number_of_ratings):
    if number_of_ratings > 5:
        return s_values[4]
    else:
        return s_values[int(number_of_ratings) - 1]


def calculate_rank_sum(number_of_ratings, s):
    if number_of_ratings > 1:
        rank_sum = 0
        for i in range(number_of_ratings):
            rank_sum += (1 / pow(i + 1, s))
        return rank_sum
    else:
        return DEFAULT_RANK_SUM


def calculate_rank_to_power_of_s(rank, number_of_ratings):
    if rank > 0:
        return 1 / pow(rank, get_s_value(number_of_ratings))
    else:
        return 0


def calculate_attitudinal_equity(number_of_ratings, rank, rank_sum):
    if rank != 0:
        return 1 / (pow(rank, get_s_value(number_of_ratings)) * rank_sum)
    else:
        return 0
