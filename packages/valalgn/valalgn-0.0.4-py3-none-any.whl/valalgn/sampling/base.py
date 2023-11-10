import numpy as np

from copy import deepcopy
from itertools import combinations
from math import factorial
from mesa import Model
from mealpy.optimizer import Optimizer
from mealpy.evolutionary_based.GA import BaseGA
from pathos.multiprocessing import cpu_count, ProcessPool

from typing import Any, Callable, Iterable, Type


def evaluate_path(
    model_cls: Type[Model],
    model_args: list[Any],
    model_kwargs: dict[str, Any],
    norms: dict[str, dict[str, float]],
    value: Callable[[Model], float],
    path_length: int
) -> float:
    """Evaluate the outcome of a path in terms of a value.

    Parameters
    ----------
    model_cls : Type[Model]
        The class of the ABM, a subclass of ``mesa.Model``.
    model_args : list[Any]
        Model initilization arguments.
    model_kwargs : dict[str, Any]
        Model initialization keyword arguments.
    norms : dict[str, dict[str, float]]
        The set of norms governing the evolution of the model.
    value : Callable[[Model], float]
        The value semantics function that evaluates the final state of a path.
    path_length : int
        The number of steps in the path to evaluate.

    Returns
    -------
    float
    """
    mdl = model_cls(*model_args, **model_kwargs)
    for _ in range(path_length):
        mdl.step(norms)
    return value(mdl)


def alignment(
    model_cls: Type[Model],
    model_args: list[Any],
    model_kwargs: dict[str, Any],
    norms: dict[str, dict[str, float]],
    value: Callable[[Model], float],
    path_length: int = 10,
    path_sample: int = 100
) -> float:
    """Compute the alignment from a sample of paths.

    Parameters
    ----------
    model_cls : Type[Model]
        The class of the ABM, a subclass of ``mesa.Model``.
    model_args : list[Any]
        Model initilization arguments.
    model_kwargs : dict[str, Any]
        Model initialization keyword arguments.
    norms : dict[str, dict[str, float]]
        The set of norms governing the evolution of the model.
    value : Callable[[Model], float]
        The value semantics function that evaluates the final state of a path.
    path_length : int, optional
        The length of the evolution path used to compute the alignment, by
        default 10.
    path_sample : int, optional
        The number of paths to sample when computing the alignment, by
        default 100.

    Returns
    -------
    float
    """
    # prepare pool
    num_nodes = cpu_count()
    if path_sample <= num_nodes:
        num_nodes = path_sample
    pool = ProcessPool(nodes=num_nodes)
    # compute alignment
    algn =  __alignment(
        model_cls, model_args, model_kwargs, norms, value,
        path_length, path_sample, pool
    )
    pool.terminate()
    return algn


def __alignment(
    model_cls: Type[Model],
    model_args: list[Any],
    model_kwargs: dict[str, Any],
    norms: dict[str, dict[str, float]],
    value: Callable[[Model], float],
    path_length: int,
    path_sample: int,
    pool: ProcessPool
) -> float:
    args = [
        [model_cls] * path_sample,
        [model_args] * path_sample,
        [model_kwargs] * path_sample,
        [norms] * path_sample,
        [value] * path_sample,
        [path_length] * path_sample
    ]
    pool.restart()
    algn = 0.
    for res in pool.map(evaluate_path, *args):
        algn += res
    pool.close()
    pool.terminate()
    return algn / path_sample


def optimize_norms(
    model_cls: Type[Model],
    model_args: list[Any],
    model_kwargs: dict[str, Any],
    norms: dict[str, Iterable[str]],
    value: Callable[[Model], float],
    lower_bounds: dict[str, dict[str, float]],
    upper_bounds: dict[str, dict[str, float]],
    const: Iterable[Callable[[dict[str, dict[str, float]]], float]] = [],
    lambda_const: float = 1.,
    opt_cls: type[Optimizer] = BaseGA,
    opt_args = [],
    opt_kwargs = {},
    term_dict = {"max_epoch": 100},
    path_length: int = 10,
    path_sample: int = 100,
) -> tuple[dict[str, dict[str, float]], float]:
    """Optimize a set of norms with respect to a value of interest.

    This optimization relies on the algorithms for metaheuristics search
    implemented in the `mealpy
    <https://mealpy.readthedocs.io/en/latest/index.html>`__ package. It takes in
    data in a more intuitive format (as dictionaries of norms, normative
    parameters and their bounds) and manages the transformation of format into
    numpy arrays suitable for the mealpy optimizers.

    Parameters
    ----------
    model_cls : Type[Model]
        The model (e.g. an agent-based model) governed by a set of norms.
    model_args : list[Any]
        Initialization arguments for the model.
    model_kwargs : dict[str, Any]
        Initialization keyword arguments for the model.
    norms : dict[str, Iterable[str]]
        The identifies of the norms and their parameters that determine the
        evolution of the model.
    value : Callable[[Model], float]
        The value semantics function with respect to whom the alignment of the
        norms is optimized.
    lower_bounds : dict[str, dict[str, float]]
        The lower bounds for the normative parameters.
    upper_bounds : dict[str, dict[str, float]]
        The upper bounds for the normative parameters.
    const : Iterable[Callable[[dict[str, dict[str, float]]], float]], optional
        Any constraints that should be respeted by the normative parameters, by
        default []. These are a set of function that take as input a norm
        dictionary and output a real number. The closer the output is to 0, the
        more respectful of the constraints is the normative system.
    lambda_const : float, optional
        The penalty to the fitness of violating the constraints, by default 1.
    opt_cls : type[Optimizer], optional
        The mealpy optimizer class used for the search, by default BaseGA.
    opt_args : list, optional
        The mealpy optimizer initialization arguments, by default [].
    opt_kwargs : dict, optional
        The mealpy optimizer initialization keyword arguments, by default [].,
        by default {}.
    term_dict : dict, optional
        The dictionary for termination condition for the optimization search, by
        default {"max_epoch": 100}. For details, see the mealpy page.
    path_length : int, optional
        The length of the evolution path used to compute the alignment, by
        default 10.
    path_sample : int, optional
        The number of paths to sample when computing the alignment, by
        default 100.

    Returns
    -------
    tuple[dict[str, dict[str, float]], float]
        _description_
    """
    
    # prepare pool for parallelization
    num_nodes = cpu_count()
    if path_sample <= num_nodes:
        num_nodes = path_sample
    pool = ProcessPool(nodes=num_nodes)
    
    def __array_to_norms(arr: np.ndarray) -> dict[str, dict[str, float]]:
        slt_norms = {n_id: {} for n_id in norms.keys()}
        for n_id in norms_to_array.keys():
            for param, i in norms_to_array[n_id].items():
                slt_norms[n_id][param] = arr[i]
        return slt_norms

    def __fitness_function(slt_array: np.ndarray) -> float:
        # turn the candidate array into a norm dictionary
        slt_norms = __array_to_norms(slt_array)
        # compute alignment (pool is already initialized)
        algn = __alignment(
            model_cls, model_args, model_kwargs, slt_norms, value,
            path_length, path_sample, pool
        )
        # add penalties for constraint violation
        const_penalty = [f(slt_norms) for f in const]
        fitness = algn - lambda_const*sum(const_penalty)
        return fitness
    
    # Step 1. Build a mapping (two dictionaries) to go from normative systems to
    # arrays
    norms_to_array = {}
    array_to_norms = {}
    i = 0
    for n_id in norms:
        norms_to_array[n_id] = {}
        for param in norms[n_id]:
            norms_to_array[n_id][param] = i
            array_to_norms[i] = (n_id, param)
            i += 1
    tot_norms = i

    # Step 2. Translate lower and upper bound dictionaries into arrays
    lb = np.zeros(tot_norms)
    ub = np.zeros(tot_norms)
    for i in range(tot_norms):
        n_id, param = array_to_norms[i]
        lb[i] = lower_bounds[n_id][param]
        ub[i] = upper_bounds[n_id][param]

    # Step 3. Prepare and run optimizer
    problem_dict = {
        "fit_func": __fitness_function,
        "lb": lb,
        "ub": ub,
        "minmax": "max"
    }
    optimizer = opt_cls(*opt_args, **opt_kwargs)
    best_position, best_fitness = optimizer.solve(
        problem_dict,
        termination=term_dict,
        mode="single"
    )
    pool.terminate()
    best_norms = __array_to_norms(best_position)
    return best_norms, best_fitness


def shapley_value(
    model_cls: Type[Model],
    model_args: list[Any],
    model_kwargs: dict[str, Any],
    baseline_norms: dict[str, dict[str, float]],
    normative_system: dict[str, dict[str, float]],
    norm: str,
    value: Callable[[Model], float],
    path_length: int = 10,
    path_sample: int = 100
) -> float:
    """Compute the Shapley value of a norm in a normative system.

    This calculator computes the Shapley value of individual norms in a
    normative system with respect to some value. For a complete
    formalization of the Shapley values of norms in a normative system, see
    [1]_.

    Parameters
    ----------
    model_cls : Type[Model]
        The class of the ABM, a subclass of ``Model``.
    model_args : list[Any]
        Model initilization arguments.
    model_kwargs : dict[str, Any]
        Model initialization keyword arguments.
    baseline_norms : dict[str, dict[str, float]]
        The baseline norms causing no evolution of the ABM.
    normative_system : dict[str, dict[str, float]]
        The complete normative system, as a mapping of norm IDs (the keys)
        to a dictionary of its normative parameters.
    norm : str
        The ID of the norm whose Shapley value is computed.
    value : Callable[[Model], float]
        The value with respect to which the Shapley value is computed. It is
        passed as a function taking as input a model instance and returning
        the evaluation of the value semantics function given the state of
        the model.
    path_length : int, optional
        The length of the evolution path used to compute the alignment, by
        default 10.
    path_sample : int, optional
        The number of paths to sample when computing the alignment, by
        default 100.

    Returns
    -------
    float
        The Shapley value of ``norm`` in ``normative_system`` with respect
        to ``value``.

    References
    ----------
    .. [1] Montes, N., & Sierra, C. (2022). Synthesis and properties of
        optimally value-aligned normative systems. Journal of Artificial
        Intelligence Research, 74, 1739–1774.
        https://doi.org/10.1613/jair.1.13487
    """
    # check that norms match
    assert normative_system.keys() == baseline_norms.keys(), \
        "normative system must have identical norms to the baseline normative system"
    for norm_id, params in normative_system.items():
        assert params.keys() == baseline_norms[norm_id].keys(), \
        f"norm {norm_id} does not have the same params in the normative \
            system and in the baseline normative system"
        
    # prepare list of norms id's for the subsets of norms
    all_norms_ids = list(baseline_norms.keys())
    all_norms_except_n = deepcopy(all_norms_ids)
    all_norms_except_n.remove(norm)

    N = len(all_norms_ids)
    combo_max_size = len(all_norms_except_n)
    shapley = 0.

    # prepare pool for parallelization
    num_nodes = cpu_count()
    if path_sample <= num_nodes:
        num_nodes = path_sample
    pool = ProcessPool(nodes=num_nodes)

    for N_prime in range(combo_max_size + 1):
        factor = factorial(N_prime) * factorial(N - N_prime - 1) / factorial(N)

        for norms_prime in combinations(all_norms_except_n, N_prime):
            normative_system_prime = {}
            for n_id in all_norms_ids:
                if n_id in norms_prime:
                    normative_system_prime[n_id] = normative_system[n_id]
                else:
                    normative_system_prime[n_id] = baseline_norms[n_id]

            normative_system_prime_union = deepcopy(normative_system_prime)
            normative_system_prime_union[norm] = normative_system[norm]

            algn1 = __alignment(
                model_cls, model_args, model_kwargs,
                normative_system_prime_union, value, path_length,
                path_sample, pool
            )
            algn2 = __alignment(
                model_cls, model_args, model_kwargs,
                normative_system_prime, value, path_length, 
                path_sample, pool
            )

            shapley += factor*(algn1 - algn2)

    pool.terminate()
    return shapley


def value_compatibility(
    model_cls: Type[Model],
    model_args: list[Any],
    model_kwargs: dict[str, Any],
    normative_system: dict[str, dict[str, float]],
    values: Iterable[Callable[[Model], float]],
    path_length: int = 10,
    path_sample: int = 100
) -> float:
    """Compute the compatibility between two values under a normative system.

    Parameters
    ----------
    model_cls : Type[Model]
        The class of the ABM, a subclass of ``Model``.
    model_args : list[Any]
        Model initilization arguments.
    model_kwargs : dict[str, Any]
        Model initialization keyword arguments.
    normative_system : dict[str, dict[str, float]]
        The complete normative system, as a mapping of norm IDs (the keys)
        to a dictionary of its normative parameters.
    values : Iterable[Callable[[Model], float]]
        An iterable of the value semantics functions capturing the values whose
        compatibility is computed.
    path_length : int, optional
        The length of the evolution path used to compute the alignment, by
        default 10.
    path_sample : int, optional
        The number of paths to sample when computing the alignment, by
        default 100.
    
    Returns
    -------
    float
    """
    # prepare pool
    num_nodes = cpu_count()
    if path_sample <= num_nodes:
        num_nodes = path_sample
    pool = ProcessPool(nodes=num_nodes)
    # compute alignments
    algns = []
    for v in values:
        algn_v =  __alignment(
            model_cls, model_args, model_kwargs, normative_system, v,
            path_length, path_sample, pool
        )
        algns.append(algn_v)
    pool.terminate()
    return min(algns)
