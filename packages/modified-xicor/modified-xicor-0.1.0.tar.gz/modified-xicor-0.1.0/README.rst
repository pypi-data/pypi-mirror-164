# Xi Correlation by Chatterjee, modified

It detects non-linear correlations including parabolas and waves.

Here's the paper I used. https://arxiv.org/pdf/1909.10140.pdf
Here's the github gist: https://gist.github.com/mandrewstuart/e1c584a36ca5394cc934542731b4d8c2

I modified the unordered equation because the boundaries weren't working I expected. They are now 'unordered': 1 + (len(Y)*numerator)/(4*denominator)
