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



if __name__ == "__main__":
    main()
