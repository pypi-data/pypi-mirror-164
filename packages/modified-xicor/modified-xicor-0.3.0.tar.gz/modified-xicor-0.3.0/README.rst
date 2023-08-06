# Xi Correlation by Chatterjee, modified

It detects non-linear correlations including parabolas and waves. The longer the series, the better the results.

Here's the paper I used. https://arxiv.org/pdf/1909.10140.pdf
Here's the github gist: https://gist.github.com/mandrewstuart/e1c584a36ca5394cc934542731b4d8c2

I modified the unordered equation because the boundaries weren't working I expected. They are now 'unordered': 1 + (len(Y)*numerator)/(4*denominator)


Usage:


>> import modified_xicor as mx

>> x = [1, 2, 3, 4, 5]

>> y = [1, 3, 5, 7, 9]

>> mx.xicor(x, y)

{'ordered': float, 'unordered': float, 'len': int}
