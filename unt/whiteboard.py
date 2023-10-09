"""You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0."""

def sum_plus(in_lst):
    out_lst=[]

    for n in_lst:

    if n > 0:
        out_lst.append(n)
    return sum(out_lst)
sum_plus([1, -4, 7, -5, 12, 15])