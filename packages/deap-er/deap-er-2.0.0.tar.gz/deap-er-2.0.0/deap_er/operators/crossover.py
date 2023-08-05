# ====================================================================================== #
#                                                                                        #
#   MIT License                                                                          #
#                                                                                        #
#   Copyright (c) 2022 - Mattias Aabmets, The DEAP Team and Other Contributors           #
#                                                                                        #
#   Permission is hereby granted, free of charge, to any person obtaining a copy         #
#   of this software and associated documentation files (the "Software"), to deal        #
#   in the Software without restriction, including without limitation the rights         #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell            #
#   copies of the Software, and to permit persons to whom the Software is                #
#   furnished to do so, subject to the following conditions:                             #
#                                                                                        #
#   The above copyright notice and this permission notice shall be included in all       #
#   copies or substantial portions of the Software.                                      #
#                                                                                        #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR           #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,             #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE          #
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER               #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,        #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE        #
#   SOFTWARE.                                                                            #
#                                                                                        #
# ====================================================================================== #
from __future__ import annotations
from deap_er.base.dtypes import *
from collections.abc import Sequence
from itertools import repeat
import random


__all__ = [
    'cx_one_point', 'cx_messy_one_point',
    'cx_two_point', 'cx_two_point_copy',
    'cx_es_two_point', 'cx_es_two_point_copy',
    'cx_partially_matched', 'cx_uniform_partially_matched',
    'cx_blend', 'cx_es_blend',
    'cx_simulated_binary', 'cx_simulated_binary_bounded',
    'cx_uniform', 'cx_ordered'
]


# ====================================================================================== #
def _slicer(ind1: Individual, ind2: Individual,
            start: int, stop: int = None, copy: bool = False) -> Mates:
    if stop is None:
        s1 = slice(start, len(ind1))
        s2 = slice(start, len(ind2))
    else:
        s1 = slice(start, stop)
        s2 = slice(start, stop)

    temp_1 = ind1[s1] if not copy else ind1[s1].copy()
    temp_2 = ind2[s2] if not copy else ind2[s2].copy()
    ind1[s1] = temp_2
    ind2[s2] = temp_1
    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def _two_point(ind1: Individual, ind2: Individual,
               copy: bool = False, strategy: bool = False) -> tuple:
    size = min(len(ind1), len(ind2))
    cxp1 = random.randint(1, size)
    cxp2 = random.randint(1, size - 1)
    if cxp2 >= cxp1:
        cxp2 += 1
    else:
        cxp1, cxp2 = cxp2, cxp1
    ind1, ind2 = _slicer(ind1, ind2, cxp1, cxp2, copy)
    if strategy:
        _slicer(
            ind1.strategy,
            ind2.strategy,
            cxp1, cxp2
        )
    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def _match(ind1: Individual, ind2: Individual,
           p1: list, p2: list, i: int) -> None:
    temp1, temp2 = ind1[i], ind2[i]
    ind1[i], ind1[p1[temp2]] = temp2, temp1
    ind2[i], ind2[p2[temp1]] = temp1, temp2
    p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
    p2[temp1], p2[temp2] = p2[temp2], p2[temp1]


# -------------------------------------------------------------------------------------- #
def cx_one_point(ind1: Individual, ind2: Individual) -> Mates:
    """
    Executes a one-point crossover on the two
    individuals, who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    size = min(len(ind1), len(ind2))
    cxp = random.randint(1, size - 1)
    ind1, ind2 = _slicer(ind1, ind2, cxp)
    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_messy_one_point(ind1: Individual, ind2: Individual) -> Mates:
    """
    Executes a messy one-point crossover on the two
    individuals, who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    cxp1 = random.randint(0, len(ind1))
    cxp2 = random.randint(0, len(ind2))
    ind1, ind2 = _slicer(ind1, ind2, cxp1, cxp2)
    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_two_point(ind1: Individual, ind2: Individual) -> Mates:
    """
    Executes a two-point crossover on the two
    individuals, who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    ind1, ind2 = _two_point(ind1, ind2)
    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_two_point_copy(ind1: Individual, ind2: Individual) -> Mates:
    """
    Executes a two-point crossover on the copies of the two
    individuals. This should be used instead of the regular
    :func:`cx_two_point` operator when the individuals are
    based on numpy arrays to avoid incorrect mating behavior
    due to the specifics of the numpy array datatype.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    ind1, ind2 = _two_point(ind1, ind2, copy=True)
    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_es_two_point(ind1: Individual, ind2: Individual) -> Mates:
    """
    Executes a two-point crossover on the two
    individuals and their evolution strategies,
    who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    ind1, ind2 = _two_point(ind1, ind2, strategy=True)
    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_es_two_point_copy(ind1: Individual, ind2: Individual) -> Mates:
    """
    Executes a two-point crossover on the copies of the two individuals
    and their evolution strategies. This should be used instead of the
    regular :func:`cx_es_two_point` operator when the individuals are
    based on numpy arrays to avoid incorrect mating behavior due to
    the specifics of the numpy array datatype.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    ind1, ind2 = _two_point(ind1, ind2, copy=True, strategy=True)
    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_partially_matched(ind1: Individual, ind2: Individual) -> Mates:
    """
    Executes a partially matched crossover on the
    two individuals, who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    size = min(len(ind1), len(ind2))
    p1, p2 = [0] * size, [0] * size

    cxp1 = random.randint(0, size)
    cxp2 = random.randint(0, size - 1)

    if cxp2 >= cxp1:
        cxp2 += 1
    else:
        cxp1, cxp2 = cxp2, cxp1

    for i in range(size):
        p1[ind1[i]] = i
        p2[ind2[i]] = i

    for i in range(cxp1, cxp2):
        _match(ind1, ind2, p1, p2, i)

    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_uniform_partially_matched(ind1: Individual, ind2: Individual,
                                 cx_prob: float) -> Mates:
    """
    Executes a uniform partially matched crossover on
    the two individuals, who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :param cx_prob: The probability of swapping any two traits.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    size = min(len(ind1), len(ind2))
    p1, p2 = [0] * size, [0] * size

    for i in range(size):
        p1[ind1[i]] = i
        p2[ind2[i]] = i

    for i in range(size):
        if random.random() < cx_prob:
            _match(ind1, ind2, p1, p2, i)

    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_blend(ind1: Individual, ind2: Individual, alpha: float) -> Mates:
    """
    Executes a blend crossover on the two
    individuals, who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :param alpha: Extent of the interval in which the
        new values can be drawn for each attribute
        on both sides of the parents' attributes.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    for i, (x1, x2) in enumerate(zip(ind1, ind2)):
        gamma = (1. + 2. * alpha) * random.random() - alpha
        ind1[i] = (1. - gamma) * x1 + gamma * x2
        ind2[i] = gamma * x1 + (1. - gamma) * x2

    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_es_blend(ind1: Individual, ind2: Individual, alpha: float) -> Mates:
    """
    Executes a blend crossover on the two
    individuals and their strategies, who
    are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :param alpha: Extent of the interval in which the
        new values can be drawn for each attribute
        on both sides of the parents' attributes.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    zipper = zip(ind1, ind1.strategy, ind2, ind2.strategy)
    for i, (x1, s1, x2, s2) in enumerate(zipper):

        gamma = (1. + 2. * alpha) * random.random() - alpha
        ind1[i] = (1. - gamma) * x1 + gamma * x2
        ind2[i] = gamma * x1 + (1. - gamma) * x2

        gamma = (1. + 2. * alpha) * random.random() - alpha
        ind1.strategy[i] = (1. - gamma) * s1 + gamma * s2
        ind2.strategy[i] = gamma * s1 + (1. - gamma) * s2

    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_simulated_binary(ind1: Individual, ind2: Individual, eta: float) -> Mates:
    """
    Executes a simulated binary crossover on the
    two individuals, who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :param eta: The crowding degree of the crossover.
        Higher values produce children more similar to
        their parents, while smaller values produce
        children more divergent from their parents.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    for i, (x1, x2) in enumerate(zip(ind1, ind2)):
        rand = random.random()

        if rand <= 0.5:
            beta = 2. * rand
        else:
            beta = 1. / (2. * (1. - rand))

        beta **= 1. / (eta + 1.)
        ind1[i] = 0.5 * (((1 + beta) * x1) + ((1 - beta) * x2))
        ind2[i] = 0.5 * (((1 - beta) * x1) + ((1 + beta) * x2))

    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_simulated_binary_bounded(ind1: Individual, ind2: Individual, eta: float,
                                low: NumOrSeq, up: NumOrSeq) -> Mates:
    """
    Executes a simulated binary bounded crossover on
    the two individuals, who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :param eta: The crowding degree of the crossover.
        Higher values produce children more similar to
        their parents, while smaller values produce
        children more divergent from their parents.
    :param low: The lower bound of the search space.
    :param up: The upper bound of the search space.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :type low: :ref:`NumOrSeq <datatypes>`
    :type up: :ref:`NumOrSeq <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    def check_bounds(name: str, var: NumOrSeq) -> Sequence:
        if not isinstance(var, Sequence):
            var = repeat(var, size)
        elif isinstance(var, Sequence) and len(var) < size:
            raise ValueError(
                f'{name} must be at least the size of the '
                f'shorter individual: {len(var)} < {size}'
            )
        return var

    def calc_c(diff: float) -> float:
        beta = 1.0 + (2.0 * diff / (x2 - x1))
        alpha = 2.0 - beta ** -(eta + 1)
        if rand <= 1.0 / alpha:
            beta_q = (rand * alpha) ** (1.0 / (eta + 1))
        else:
            beta_q = (1.0 / (2.0 - rand * alpha)) ** (1.0 / (eta + 1))
        c = 0.5 * (x1 + x2 - beta_q * (x2 - x1))
        return c

    size = min(len(ind1), len(ind2))
    low = check_bounds('low', low)
    up = check_bounds('up', up)

    for i, xl, xu in zip(list(range(size)), low, up):
        if random.random() <= 0.5:
            if abs(ind1[i] - ind2[i]) > 1e-14:
                x1 = min(ind1[i], ind2[i])
                x2 = max(ind1[i], ind2[i])
                rand = random.random()

                c1 = calc_c(x1 - xl)
                c1 = min(max(c1, xl), xu)

                c2 = calc_c(xu - x2)
                c2 = min(max(c2, xl), xu)

                if random.random() <= 0.5:
                    ind1[i] = c2
                    ind2[i] = c1
                else:
                    ind1[i] = c1
                    ind2[i] = c2

    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_uniform(ind1: Individual, ind2: Individual, cx_prob: float) -> Mates:
    """
    Executes a uniform crossover on the two
    individuals, who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :param cx_prob: The probability of swapping any two traits.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    size = min(len(ind1), len(ind2))
    for i in range(size):
        if random.random() < cx_prob:
            _slicer(ind1, ind2, i, i + 1)
    return ind1, ind2


# -------------------------------------------------------------------------------------- #
def cx_ordered(ind1: Individual, ind2: Individual) -> Mates:
    """
    Executes an ordered crossover on the two
    individuals, who are modified in-place.

    :param ind1: The first individual.
    :param ind2: The second individual.
    :return: Two mated individuals.

    :type ind1: :ref:`Individual <datatypes>`
    :type ind2: :ref:`Individual <datatypes>`
    :rtype: :ref:`Mates <datatypes>`
    """
    size = min(len(ind1), len(ind2))
    a, b = random.sample(list(range(size)), 2)
    if a > b:
        a, b = b, a

    holes1, holes2 = [True] * size, [True] * size
    for i in range(size):
        if i < a or i > b:
            holes1[ind2[i]] = False
            holes2[ind1[i]] = False

    temp1, temp2 = ind1, ind2
    k1, k2 = b + 1, b + 1

    for i in range(size):
        if not holes1[temp1[(i + b + 1) % size]]:
            ind1[k1 % size] = temp1[(i + b + 1) % size]
            k1 += 1

        if not holes2[temp2[(i + b + 1) % size]]:
            ind2[k2 % size] = temp2[(i + b + 1) % size]
            k2 += 1

    for i in range(a, b + 1):
        _slicer(ind1, ind2, i, i + 1)

    return ind1, ind2
