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




def main():



if __name__ == "__main__":
    main()
