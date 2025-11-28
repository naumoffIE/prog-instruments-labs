import time
import random
import cProfile


def process_data_inefficient(data):
    """Неэффективная обработка данных"""
    result = []

    for i in range(len(data)):
        temp_list = []
        for j in range(len(data)):
            if data[i] == data[j]:
                temp_list.append((i, j))

        processed = temp_list.copy()
        for item in processed:
            result.append(item)

    return result


def calculate_statistics(numbers):
    """Неэффективный расчет статистики"""
    stats = {}

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                key = f"pair_{numbers[i]}"
                if key not in stats:
                    stats[key] = 0
                stats[key] += 1

    return stats


def main():
    data = [random.randint(1, 100) for _ in range(1000)]

    start_time = time.time()

    profiler1 = cProfile.Profile()
    profiler1.enable()

    statistics = calculate_statistics(data)

    profiler1.disable()

    profiler2 = cProfile.Profile()
    profiler2.enable()

    processed_data = process_data_inefficient(data)

    profiler2.disable()

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.7f} seconds")
    print(f"Processed {len(processed_data)} items")
    print(f"Statistics keys: {len(statistics)}")
    print("\n=== Profiling Results ===")
    profiler1.print_stats()
    profiler2.print_stats()


if __name__ == "__main__":
    main()
