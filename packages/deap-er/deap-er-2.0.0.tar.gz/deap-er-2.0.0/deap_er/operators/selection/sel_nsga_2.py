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
from deap_er.utilities.sorting import *
from .sel_helpers import assign_crowding_dist
from operator import attrgetter
from itertools import chain


__all__ = ['sel_nsga_2']


# ====================================================================================== #
def sel_nsga_2(individuals: list, sel_count: int,
               sorting: str = 'standard') -> list:
    """
    Selects the next generation of individuals using the NSGA-II algorithm.
    Usually, the size of **individuals** should be larger than the **sel_count**
    parameter. If the size of **individuals** is equal to **sel_count**, the
    population will be sorted according to their pareto fronts.

    :param individuals: A list of individuals to select from.
    :param sel_count: The number of individuals to select.
    :param sorting: The algorithm to use for non-dominated
        sorting. Can be either 'log' or 'standard' string literal.
    :return: A list of selected individuals.
    """
    if sorting == 'standard':
        pareto_fronts = sort_non_dominated(individuals, sel_count)
    elif sorting == 'log':
        pareto_fronts = sort_log_non_dominated(individuals, sel_count)
    else:
        raise RuntimeError(
            f'selNSGA2: The choice of non-dominated '
            f'sorting method \'{sorting}\' is invalid.'
        )

    for front in pareto_fronts:
        assign_crowding_dist(front)

    chosen = list(chain(*pareto_fronts[:-1]))
    sel_count = sel_count - len(chosen)
    if sel_count > 0:
        attr = attrgetter("fitness.crowding_dist")
        sorted_front = sorted(pareto_fronts[-1], key=attr, reverse=True)
        chosen.extend(sorted_front[:sel_count])

    return chosen
