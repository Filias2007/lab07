# Online Shop — persistence layer

Лабораторна робота №7 «Робота з базами даних у Python», курс «Професійний Python», варіант №3 — «Інтернет-магазин».
Проєкт продовжує структуру попередніх лабораторних робіт (src-layout, `pyproject.toml`, `tests/`).

## Що реалізовано

- SQLite + SQLAlchemy 2.0 ORM, таблиці `categories`, `products`, `purchases` (PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK)
- Repository Pattern: `CategoryRepository`, `ProductRepository`, `PurchaseRepository`
- CRUD, пошук, фільтрація за категорією, сортування, пагінація, зміна ціни та кількості
- Service layer: вартість залишків (`SUM`), середня ціна (`AVG`), `GROUP BY` за категоріями, найдорожчий товар
- Python DB-API (`sqlite3`) з параметризованими запитами: `src/shop/dbapi.py`
- Транзакція `purchase_product()` (commit/rollback) та `purchase_many()`
- Alembic: міграція `0002` додає поле `description` до `products`
- Integration tests на окремій тестовій SQLite-базі

## Структура

```
LAB_07/
├── pyproject.toml
├── README.md
├── alembic.ini
├── sql/schema.sql
├── migrations/            # Alembic (env.py, versions/0001, versions/0002)
├── src/shop/
│   ├── __init__.py
│   ├── database.py        # engine, SessionLocal, PRAGMA foreign_keys=ON
│   ├── models.py          # ORM-моделі
│   ├── repositories.py    # Repository Pattern
│   ├── services.py        # бізнес-логіка, транзакції
│   ├── dbapi.py           # sqlite3 DB-API, parameterized queries
│   ├── exceptions.py
│   └── main.py
└── tests/
    ├── conftest.py
    ├── test_repositories.py
    ├── test_services.py
    ├── test_constraints.py
    ├── test_dbapi.py
    └── test_migrations.py
```

## Встановлення

```bash
python -m venv .venv
.venv\Scripts\activate          # Linux/macOS: source .venv/bin/activate
python -m pip install -e ".[test]"
```

## Запуск

```bash
python -m shop.main
```

## Міграції

```bash
alembic upgrade head            # створює/оновлює shop.db
alembic current
alembic downgrade 0001          # відкат міграції з description
```

## Тести

```bash
python -m pytest -v
```
