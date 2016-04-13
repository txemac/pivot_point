__author__ = 'josebermudez'


def find_pivot_points(array):
    if not array:
        raise ValueError('error in parameter.')

    result = []

    for index in xrange(len(array)):
        if sum(array[:index]) == sum(array[index+1:]):
            result.append(index)

    return result if result else -1
