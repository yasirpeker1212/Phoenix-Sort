def benchmark():
    from phoenix_sort import phoenix_sort
    import timeit

    setup_code = '''
from __main__ import phoenix_sort
import random
arr1 = list(range(1000))
arr2 = list(range(1000, 0, -1))
arr3 = [random.randint(0, 1000) for _ in range(1000)]
'''

    tests = {
        "Sorted": "phoenix_sort(arr1)",
        "Reversed": "phoenix_sort(arr2)",
        "Random": "phoenix_sort(arr3)"
    }

    print("⏱ Benchmarking Phoenix Sort")
    for name, stmt in tests.items():
        t = timeit.timeit(stmt=stmt, setup=setup_code, number=10)
        print(f"{name:10}: {t:.4f} sec (10 runs)")
