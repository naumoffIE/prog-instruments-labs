import time
import random
from collections import Counter


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

    # Медленные операции
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                key = f"pair_{numbers[i]}"
                if key not in stats:
                    stats[key] = 0
                stats[key] += 1

    return stats


def main():
    # Генерируем тестовые данные
    data = [random.randint(1, 100) for _ in range(1000)]

    start_time = time.time()

    # Вызываем неэффективные функции
    processed_data = process_data_inefficient(data)
    statistics = calculate_statistics(data)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    print(f"Processed {len(processed_data)} items")
    print(f"Statistics keys: {len(statistics)}")


if __name__ == "__main__":
    main()
