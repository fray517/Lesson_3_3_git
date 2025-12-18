"""
Модуль для генерации безопасных паролей.

Предоставляет функционал для создания паролей с настраиваемыми параметрами:
длина, использование различных типов символов (буквы, цифры, спецсимволы).
"""

import secrets
import string
import argparse
import sys


def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_special: bool = True
) -> str:
    """
    Генерирует случайный безопасный пароль.

    Использует криптографически стойкий генератор случайных чисел
    (secrets модуль) для создания паролей.

    Args:
        length: Длина пароля (по умолчанию 16).
        use_uppercase: Использовать заглавные буквы (A-Z).
        use_lowercase: Использовать строчные буквы (a-z).
        use_digits: Использовать цифры (0-9).
        use_special: Использовать специальные символы.

    Returns:
        Сгенерированный пароль.

    Raises:
        ValueError: Если не выбран ни один тип символов или длина <= 0.
    """
    if length <= 0:
        raise ValueError("Длина пароля должна быть больше 0")

    # Формируем набор символов на основе параметров
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not characters:
        raise ValueError(
            "Необходимо выбрать хотя бы один тип символов для пароля"
        )

    # Генерируем пароль используя криптографически стойкий генератор
    password = "".join(
        secrets.choice(characters) for _ in range(length)
    )

    return password


def main():
    """Основная функция для работы программы из командной строки."""
    parser = argparse.ArgumentParser(
        description="Генератор безопасных паролей",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python password_generator.py
  python password_generator.py --length 20
  python password_generator.py --length 12 --no-special
  python password_generator.py --length 8 --only-digits
        """
    )

    parser.add_argument(
        "-l", "--length",
        type=int,
        default=16,
        help="Длина пароля (по умолчанию: 16)"
    )

    parser.add_argument(
        "--no-uppercase",
        action="store_true",
        help="Не использовать заглавные буквы"
    )

    parser.add_argument(
        "--no-lowercase",
        action="store_true",
        help="Не использовать строчные буквы"
    )

    parser.add_argument(
        "--no-digits",
        action="store_true",
        help="Не использовать цифры"
    )

    parser.add_argument(
        "--no-special",
        action="store_true",
        help="Не использовать специальные символы"
    )

    parser.add_argument(
        "-n", "--count",
        type=int,
        default=1,
        help="Количество паролей для генерации (по умолчанию: 1)"
    )

    args = parser.parse_args()

    try:
        # Генерируем указанное количество паролей
        for i in range(args.count):
            password = generate_password(
                length=args.length,
                use_uppercase=not args.no_uppercase,
                use_lowercase=not args.no_lowercase,
                use_digits=not args.no_digits,
                use_special=not args.no_special
            )
            print(password)

    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

