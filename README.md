## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы независимые юнит-тесты для классов `Bun`, `Burger`, `Ingredient`,
`Database`. В тестах используются параметризация `pytest` и моки из
`unittest.mock`.

15 тестов проходят успешно. Покрытие целевых модулей — 100%.

### Структура проекта

- `bun.py`, `burger.py`, `ingredient.py`, `database.py` — код программы;
- `tests` — тесты, разделённые по тестируемым классам;
- `requirements.txt` — зависимости для запуска тестов и подсчёта покрытия.

### Запуск автотестов

**Установка зависимостей**

```shell
python -m pip install -r requirements.txt
```

**Запуск автотестов и создание HTML-отчета о покрытии**

```shell
python -m pytest tests --cov=bun --cov=burger --cov=ingredient --cov=database --cov-report=term-missing --cov-report=html
```

HTML-отчёт создаётся в `htmlcov/index.html`.
