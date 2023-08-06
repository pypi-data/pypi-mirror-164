__version__ = '0.3.0'

# https://arxiv.org/pdf/1909.10140.pdf
# https://gist.github.com/mandrewstuart/e1c584a36ca5394cc934542731b4d8c2


def xicor(X, Y):
    """Expects two lists as arguments,
    outputs a dict with ordered, unordered, and len.
    """
    # sort Y based on X
    new_vars = []
    for i in range(len(X)):
        new_vars.append([X[i], Y[i]])
    new_vars.sort()
    Y = [i[1] for i in new_vars]

    # calculate rank of Ys when X is ordered
    top_ranks = []
    for index in range(len(Y)):
        rank = len([item for item in Y if item <= Y[index]])
        top_ranks.append(rank)

    # calculate sum of abs diffs of ranks
    numerator = 0
    for index in range(1, len(top_ranks)):
        numerator += abs(top_ranks[index] - top_ranks[index - 1])

    # calculations for denominator
    bottom_ranks = []
    for index in range(len(Y)):
        count = len([item for item in Y if item >= Y[index]])
        bottom_ranks.append(count)

    # calculation product for denominator
    denominator = 0
    for index in range(len(Y)):
        denominator += bottom_ranks[index] * \
            (1 + index - bottom_ranks[index])

    output = {
        'ordered': 1 - (3*numerator)/(len(Y)**2 - 1),
        # for whatever reason, the below modification gave better results... 🤷‍♂️
        'unordered': 1 + (len(Y)*numerator)/(4*denominator),
        'length': len(Y)
    }
    return output
