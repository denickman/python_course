def validate_password(password):
    """Проверяет пароль и возвращает СЛОВАРЬ с ошибками"""
    errors = {}

    # Проверка 1: Длина
    if len(password) < 8:
        errors['length'] = "❌ Минимум 8 символов"
    else:
        print("✅ Длина пароля: OK")

    # Проверка 2: Цифры
    if not any(i.isdigit() for i in password):
        errors['digits'] = "❌ Должна быть хотя бы одна цифра (0-9)"
    else:
        print("✅ Цифры: OK")

    if not any(i.islower() for i in password):
        errors['lowercase'] = "❌ Должна быть хотя бы одна маленькая буква"
    else:
        print("✅ Заглавные буквы: OK")

    if not any(i.isupper() for i in password):
        errors['uppercase'] = "❌ Должна быть хотя бы одна заглавная буква"
    else:
        print("✅ Маленькие буквы: OK")

    return errors



while True:
    password = input("\n🔐 Введите пароль: ")
    print("\n" + "=" * 50)

    allErrors = validate_password(password)

    if not allErrors:
        print("\n✨ Пароль СИЛЬНЫЙ! Все требования выполнены.")
        print(f"Ваш пароль: {password}")
        break
    else:
        print("\n⚠️  ОБНАРУЖЕНЫ ОШИБКИ:")
        print("-" * 50)

    # Показываем содержимое dictionary
    for k, v in allErrors.items():
        print(f"{k}: {v}")

    print("-"*50)
    print(f"total errors: {len(allErrors)}")
    print("try again...")



















