import time
import random
from collections import Counter, defaultdict
import cProfile


def process_data_efficient(data):
    """Эффективная обработка данных"""
    result = []

    index_map = defaultdict(list)
    for i, value in enumerate(data):
        index_map[value].append(i)

    for value, indices in index_map.items():
        for i in indices:
            for j in indices:
                result.append((i, j))

    return result



def main_optimized():


if __name__ == "__main__":
    main_optimized()
