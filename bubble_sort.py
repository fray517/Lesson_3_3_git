"""
Модуль для реализации алгоритма пузырьковой сортировки.

Пузырьковая сортировка - простой алгоритм сортировки, который многократно
проходит по списку, сравнивает соседние элементы и меняет их местами,
если они находятся в неправильном порядке.
"""

from typing import List, Any
import argparse
import random


def bubble_sort(arr: List[Any], reverse: bool = False) -> List[Any]:
    """
    Сортирует список методом пузырьковой сортировки.

    Алгоритм работает за O(n²) времени в худшем случае.
    Проходит по массиву n раз, на каждой итерации "всплывает"
    наибольший (или наименьший) элемент в конец.

    Args:
        arr: Список элементов для сортировки.
        reverse: Если True, сортирует по убыванию (по умолчанию False).

    Returns:
        Отсортированный список (новый список, исходный не изменяется).
    """
    # Создаем копию списка, чтобы не изменять исходный
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    # Внешний цикл: количество проходов по массиву
    for i in range(n):
        # Флаг для оптимизации: если за проход не было обменов,
        # массив уже отсортирован
        swapped = False

        # Внутренний цикл: сравнение соседних элементов
        # После каждого прохода наибольший элемент "всплывает" в конец,
        # поэтому уменьшаем диапазон на i
        for j in range(0, n - i - 1):
            # Сравниваем соседние элементы
            if reverse:
                # Сортировка по убыванию
                if sorted_arr[j] < sorted_arr[j + 1]:
                    sorted_arr[j], sorted_arr[j + 1] = (
                        sorted_arr[j + 1], sorted_arr[j]
                    )
                    swapped = True
            else:
                # Сортировка по возрастанию
                if sorted_arr[j] > sorted_arr[j + 1]:
                    sorted_arr[j], sorted_arr[j + 1] = (
                        sorted_arr[j + 1], sorted_arr[j]
                    )
                    swapped = True

        # Если за проход не было обменов, массив отсортирован
        if not swapped:
            break

    return sorted_arr


def bubble_sort_with_steps(arr: List[Any], reverse: bool = False) -> tuple:
    """
    Сортирует список с выводом промежуточных шагов.

    Полезно для демонстрации работы алгоритма.

    Args:
        arr: Список элементов для сортировки.
        reverse: Если True, сортирует по убыванию.

    Returns:
        Кортеж (отсортированный список, количество шагов).
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    steps = 0

    print(f"Исходный массив: {sorted_arr}")
    print("-" * 50)

    for i in range(n):
        swapped = False
        print(f"Проход {i + 1}:")

        for j in range(0, n - i - 1):
            steps += 1
            if reverse:
                if sorted_arr[j] < sorted_arr[j + 1]:
                    sorted_arr[j], sorted_arr[j + 1] = (
                        sorted_arr[j + 1], sorted_arr[j]
                    )
                    swapped = True
                    print(
                        f"  Шаг {steps}: Обмен {sorted_arr[j + 1]} и "
                        f"{sorted_arr[j]} -> {sorted_arr}"
                    )
            else:
                if sorted_arr[j] > sorted_arr[j + 1]:
                    sorted_arr[j], sorted_arr[j + 1] = (
                        sorted_arr[j + 1], sorted_arr[j]
                    )
                    swapped = True
                    print(
                        f"  Шаг {steps}: Обмен {sorted_arr[j + 1]} и "
                        f"{sorted_arr[j]} -> {sorted_arr}"
                    )

        if not swapped:
            print(f"  Обменов не было, массив отсортирован!")
            break
        print()

    print("-" * 50)
    print(f"Результат: {sorted_arr}")
    print(f"Всего шагов: {steps}")

    return sorted_arr, steps


def main():
    """Основная функция для работы программы из командной строки."""
    parser = argparse.ArgumentParser(
        description="Пузырьковая сортировка",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python bubble_sort.py --list 5 2 8 1 9
  python bubble_sort.py --list 5 2 8 1 9 --reverse
  python bubble_sort.py --random 10
  python bubble_sort.py --random 10 --steps
        """
    )

    parser.add_argument(
        "-l", "--list",
        nargs="+",
        type=float,
        help="Список чисел для сортировки"
    )

    parser.add_argument(
        "-r", "--random",
        type=int,
        metavar="N",
        help="Сгенерировать случайный список из N элементов"
    )

    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Сортировать по убыванию"
    )

    parser.add_argument(
        "-s", "--steps",
        action="store_true",
        help="Показать промежуточные шаги сортировки"
    )

    args = parser.parse_args()

    # Определяем исходный массив
    if args.random:
        # Генерируем случайный список
        arr = [random.randint(1, 100) for _ in range(args.random)]
        print(f"Сгенерированный массив: {arr}")
    elif args.list:
        # Используем переданный список
        arr = args.list
    else:
        # Пример по умолчанию
        arr = [64, 34, 25, 12, 22, 11, 90]
        print("Используется пример по умолчанию")
        print(f"Массив: {arr}")

    print()

    # Выполняем сортировку
    if args.steps:
        sorted_arr, steps = bubble_sort_with_steps(arr, args.reverse)
    else:
        sorted_arr = bubble_sort(arr, args.reverse)
        print(f"Исходный массив: {arr}")
        print(f"Отсортированный массив: {sorted_arr}")


if __name__ == "__main__":
    main()

