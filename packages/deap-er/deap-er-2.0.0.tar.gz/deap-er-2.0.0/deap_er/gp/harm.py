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
from deap_er.records.dtypes import *
from deap_er.records import Logbook
from deap_er.base import Toolbox
from typing import Callable
import random
import math


__all__ = ['harm']


# ====================================================================================== #
def harm(toolbox: Toolbox,
         population: list,
         generations: int,
         cx_prob: float,
         mut_prob: float,
         alpha: float = 0.05,
         beta: float = 10.0,
         gamma: float = 0.25,
         rho: float = 0.9,
         nb_model: int = -1,
         min_cutoff: int = 20,
         hof: Hof = None,
         stats: Stats = None,
         verbose: bool = False) -> AlgoResult:
    """
    Implements population bloat control by an evolution algorithm for a genetic
    program. The default parameter values are recommended for most use-cases.

    :param toolbox: A Toolbox which contains the evolution operators.
    :param population: A list of individuals to evolve.
    :param generations: The number of generations to compute.
    :param cx_prob: The probability of mating two individuals.
    :param mut_prob: The probability of mutating an individual.
    :param alpha: The half-life of the exponential, which is linearly
        proportional to the cutoff point, optional. Higher values
        increase the chance of accepting larger individuals.
    :param beta: The minimal value of the half-life, which ensures that
        reasonably sized growth is always possible even during the
        first few generations, when sizes can be small, optional.
    :param gamma: The percentage of individuals that are allowed after
        the cutoff point, optional. Sets the proportion of the
        population that is allowed to grow in size.
    :param rho: Controls the position of the cutoff point by setting the
        range of fitness in which to search for the smallest individual,
        optional. Higher values of 'rho' can be used to search more
        aggressively for slightly better solutions with the potential
        downside of increasing the risk of over-fitting.
    :param nb_model: The number of individuals to generate in order to
        model the natural distribution, optional. The default value
        of -1 sets the 'nb_model' to max(2000, len(population)).
    :param min_cutoff: The absolute minimum value for the cutoff point,
        optional. It ensures that the algorithm does not shrink the
        population too much at the beginning of the evolution.
    :param hof: A HallOfFame or a ParetoFront object, optional.
    :param stats: A Statistics or a MultiStatistics object, optional.
    :param verbose: Whether to print debug messages, optional.
    :return: The final population and the logbook.

    :type hof: :ref:`Hof <datatypes>`
    :type stats: :ref:`Stats <datatypes>`
    :rtype: :ref:`AlgoResult <datatypes>`
    """
    # -------------------------------------------------------- #
    def _harm_target_func(x: int) -> float:
        half_life = x * float(alpha) + beta
        hl_1 = gamma * len(population) * math.log(2) / half_life
        hl_2 = math.exp(-math.log(2) * (x - cutoff_size) / half_life)
        return hl_1 * hl_2

    # -------------------------------------------------------- #
    def _harm_accept_func(s: int) -> bool:
        prob_hist = [t / n if n > 0 else t for n, t in zip(natural_hist, target_hist)]
        prob = prob_hist[s] if s < len(prob_hist) else _harm_target_func(s)
        return random.random() <= prob

    # -------------------------------------------------------- #
    def _harm_gen_pop(n: int, pick_from: list = None,
                      accept_func: Callable = lambda s: True) -> tuple:

        if pick_from is None:
            pick_from = list()

        produced_pop = list()
        produced_pop_sizes = list()

        while len(produced_pop) < n:
            if len(pick_from) > 0:
                aspirant = pick_from.pop()
                if accept_func(len(aspirant)):
                    produced_pop.append(aspirant)
                    produced_pop_sizes.append(len(aspirant))
            else:
                op_random = random.random()
                if op_random < cx_prob:
                    aspirant1, aspirant2 = toolbox.mate(
                        *map(toolbox.clone, toolbox.select(population, 2))
                    )
                    del aspirant1.fitness.values, aspirant2.fitness.values
                    if accept_func(len(aspirant1)):
                        produced_pop.append(aspirant1)
                        produced_pop_sizes.append(len(aspirant1))

                    if len(produced_pop) < n and accept_func(len(aspirant2)):
                        produced_pop.append(aspirant2)
                        produced_pop_sizes.append(len(aspirant2))
                else:
                    aspirant = toolbox.clone(toolbox.select(population, 1)[0])
                    if op_random - cx_prob < mut_prob:
                        aspirant = toolbox.mutate(aspirant)[0]
                        del aspirant.fitness.values
                    if accept_func(len(aspirant)):
                        produced_pop.append(aspirant)
                        produced_pop_sizes.append(len(aspirant))

        return produced_pop, produced_pop_sizes

    # -------------------------------------------------------- #
    logbook = Logbook()
    logbook.header = ['gen', 'nevals'] + (stats.fields if stats else [])

    invalid_ind = [ind for ind in population if not ind.fitness.is_valid()]
    fitness = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitness):
        ind.fitness.values = fit

    if hof is not None:
        hof.update(population)

    record = stats.compile(population) if stats else {}
    logbook.record(gen=0, nevals=len(invalid_ind), **record)

    if verbose:
        print(logbook.stream)

    if nb_model == -1:
        nb_model = max(2000, len(population))

    for gen in range(1, generations + 1):
        natural_pop, natural_pop_sizes = _harm_gen_pop(n=nb_model)
        natural_hist = [0] * (max(natural_pop_sizes) + 3)

        for ind_size in natural_pop_sizes:
            natural_hist[ind_size] += 0.4
            natural_hist[ind_size - 1] += 0.2
            natural_hist[ind_size + 1] += 0.2
            natural_hist[ind_size + 2] += 0.1
            if ind_size - 2 >= 0:
                natural_hist[ind_size - 2] += 0.1

        natural_hist = [val * len(population) / nb_model for val in natural_hist]
        sorted_natural = sorted(natural_pop, key=lambda ind: ind.fitness)
        cutoff_candidates = sorted_natural[int(len(population) * rho - 1):]
        cutoff_size = max(min_cutoff, len(min(cutoff_candidates, key=len)))

        target_hist = list()
        for bin_idx in range(len(natural_hist)):
            if bin_idx <= cutoff_size:
                target_hist.append(natural_hist[bin_idx])
            else:
                target = _harm_target_func(bin_idx)
                target_hist.append(target)

        offspring, _ = _harm_gen_pop(
            n=len(population),
            pick_from=natural_pop,
            accept_func=_harm_accept_func
        )

        invalid_ind = [ind for ind in offspring if not ind.fitness.is_valid()]
        fitness = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitness):
            ind.fitness.values = fit

        if hof is not None:
            hof.update(offspring)

        population[:] = offspring
        record = stats.compile(population) if stats else {}
        logbook.record(gen=gen, nevals=len(invalid_ind), **record)

        if verbose:
            print(logbook.stream)

    return population, logbook
