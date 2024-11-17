from time import perf_counter
from typing import Callable

import matplotlib.pyplot as plt

from funcs import *


REPEATS = 100_000
CORRECT = {
    1: '', 
    2: '', 
    3: 'fizz', 
    4: '', 
    5: 'buzz', 
    6: 'fizz', 
    7: '', 
    8: '', 
    9: 'fizz', 
    10: 'buzz', 
    11: '', 
    12: 'fizz', 
    13: '', 
    14: '', 
    15: 'fizzbuzz',
    16: '',
    17: '',
    18: 'fizz',
    19: '',
    20: 'buzz',
    21: 'fizz',
    22: '',
    23: '',
    24: 'fizz',
    25: 'buzz',
    26: '',
    27: 'fizz',
    28: '',
    29: '',
    30: 'fizzbuzz',
}


def run(func: Callable) -> tuple[float, float]:
    results = []
    for _ in range(REPEATS):
        dt0 = perf_counter()
        result = [func(i) for i in CORRECT.keys()]
        dt1 = perf_counter()
        results.append((dt1-dt0) * 10 ** 6)
    
    try:
        assert result == [*CORRECT.values()][:len(CORRECT)]
    except AssertionError:
        for key in CORRECT:
            if func(key) != CORRECT[key]:
                print(f'{func.__name__} produced an incorrect result for {key=}')
        return
    
    times_min = min(results)
    times_mean = sum(results) / len(results)
    print(f'{func.__name__:12}: Min={times_min:0.6f} µs, Avg={times_mean:0.6f} µs')

    return times_min, times_mean


def plot(results: list[tuple[Callable, float, float]]):

    width = 0.8
    plt.bar(
        [x for x in range(len(funcs))], 
        [result[2] for result in funcs], 
        label='min', 
        width=width,
        tick_label=[func[0].__name__.replace('fizzbuzz_', '') for func in funcs],
        alpha=1,
    )
    plt.bar(
        [x for x in range(len(funcs))], 
        [result[2]-result[1] for result in funcs], 
        label='mean', 
        width=width,
        bottom=[result[1] for result in funcs],
        tick_label=[func[0].__name__.replace('fizzbuzz_', '') for func in funcs],
        alpha=0.8,
    )
    plt.xlabel('Function', labelpad=-3)
    plt.xticks(rotation=-45)
    plt.ylabel('Execution time (micro-seconds)')
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.savefig('plot.png')
    plt.close('all')


if __name__ == '__main__':
    funcs = [func for name, func in locals().items() if name.startswith('fizzbuzz')]
    for i, func in enumerate(funcs):
        result = run(func)
        funcs[i] = (func, *result)

    # sort results before plotting
    funcs.sort(key=lambda x: x[2], reverse=True)

    plot(funcs)
