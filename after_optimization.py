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


def calculate_statistics_efficient(numbers):
    """Эффективный расчет статистики"""
    # Используем Counter для подсчета
    counter = Counter(numbers)
    stats = {}

    for number, count in counter.items():
        stats[f"pair_{number}"] = count * count  # n^2 пар для каждого числа

    return stats


def main_optimized():
    data = [random.randint(1, 100) for _ in range(1000)]

    start_time = time.time()

    profiler1 = cProfile.Profile()
    profiler1.enable()

    statistics = calculate_statistics_efficient(data)

    profiler1.disable()

    profiler2 = cProfile.Profile()
    profiler2.enable()

    processed_data = process_data_efficient(data)

    profiler2.disable()

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.7f} seconds")
    print(f"Processed {len(processed_data)} items")
    print(f"Statistics keys: {len(statistics)}")
    print("\n=== Profiling Results ===")
    profiler1.print_stats()
    profiler2.print_stats()


if __name__ == "__main__":
    main_optimized()
