"""
Модуль для реализации алгоритма сортировки слиянием.

Сортировка слиянием - эффективный алгоритм сортировки с временной
сложностью O(n log n). Использует подход "разделяй и властвуй":
массив делится пополам, каждая половина рекурсивно сортируется,
затем отсортированные половины сливаются обратно.
"""

from typing import List, Any
import argparse
import random


def merge(
    left: List[Any],
    right: List[Any],
    reverse: bool = False
) -> List[Any]:
    """
    Сливает два отсортированных списка в один отсортированный.

    Args:
        left: Первый отсортированный список.
        right: Второй отсортированный список.
        reverse: Если True, сливает для сортировки по убыванию.

    Returns:
        Объединенный отсортированный список.
    """
    result = []
    i = j = 0

    # Сравниваем элементы из обоих списков и добавляем меньший
    # (или больший для reverse=True) в результат
    while i < len(left) and j < len(right):
        if reverse:
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    # Добавляем оставшиеся элементы из левого списка
    while i < len(left):
        result.append(left[i])
        i += 1

    # Добавляем оставшиеся элементы из правого списка
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(
    arr: List[Any],
    reverse: bool = False
) -> List[Any]:
    """
    Сортирует список методом слияния.

    Алгоритм работает за O(n log n) времени в любом случае.
    Использует дополнительную память O(n) для временных массивов.

    Args:
        arr: Список элементов для сортировки.
        reverse: Если True, сортирует по убыванию (по умолчанию False).

    Returns:
        Отсортированный список (новый список, исходный не изменяется).
    """
    # Базовый случай: массив из 0 или 1 элемента уже отсортирован
    if len(arr) <= 1:
        return arr.copy()

    # Разделяем массив пополам
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Рекурсивно сортируем каждую половину
    left_sorted = merge_sort(left, reverse)
    right_sorted = merge_sort(right, reverse)

    # Сливаем отсортированные половины
    return merge(left_sorted, right_sorted, reverse)


def merge_sort_with_steps(
    arr: List[Any],
    reverse: bool = False,
    depth: int = 0
) -> tuple:
    """
    Сортирует список с выводом промежуточных шагов.

    Полезно для демонстрации работы алгоритма и понимания рекурсии.

    Args:
        arr: Список элементов для сортировки.
        reverse: Если True, сортирует по убыванию.
        depth: Глубина рекурсии (для отступов в выводе).

    Returns:
        Кортеж (отсортированный список, количество операций).
    """
    indent = "  " * depth
    print(f"{indent}Сортировка: {arr}")

    # Базовый случай
    if len(arr) <= 1:
        print(f"{indent}  -> Базовый случай, возвращаем: {arr}")
        return arr.copy(), 0

    # Разделяем массив
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    print(f"{indent}  Разделяем: левая часть = {left}, правая часть = {right}")

    # Рекурсивно сортируем
    left_sorted, left_ops = merge_sort_with_steps(left, reverse, depth + 1)
    right_sorted, right_ops = merge_sort_with_steps(right, reverse, depth + 1)

    # Сливаем
    merged = merge(left_sorted, right_sorted, reverse)
    merge_ops = len(left_sorted) + len(right_sorted)

    print(
        f"{indent}  Сливаем {left_sorted} и {right_sorted} -> {merged}"
    )
    print(f"{indent}  Результат: {merged}")

    total_ops = left_ops + right_ops + merge_ops
    return merged, total_ops


def main():
    """Основная функция для работы программы из командной строки."""
    parser = argparse.ArgumentParser(
        description="Сортировка слиянием",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python merge_sort.py --list 5 2 8 1 9 3
  python merge_sort.py --list 5 2 8 1 9 3 --reverse
  python merge_sort.py --random 10
  python merge_sort.py --random 10 --steps
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
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        print("Используется пример по умолчанию")
        print(f"Массив: {arr}")

    print()

    # Выполняем сортировку
    if args.steps:
        print("Процесс сортировки:")
        print("=" * 50)
        sorted_arr, operations = merge_sort_with_steps(arr, args.reverse)
        print("=" * 50)
        print(f"\nИсходный массив: {arr}")
        print(f"Отсортированный массив: {sorted_arr}")
        print(f"Всего операций слияния: {operations}")
    else:
        sorted_arr = merge_sort(arr, args.reverse)
        print(f"Исходный массив: {arr}")
        print(f"Отсортированный массив: {sorted_arr}")


if __name__ == "__main__":
    main()

