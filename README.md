# Шаблон Aiogram 3.18.0

Шаблон для Telegram-ботов на базе Aiogram 3.18.0 с поддержкой асинхронных баз данных, интернационализацией (i18n) и развертыванием через Docker. Обеспечивает основу для разработки масштабируемых ботов с чистой и поддерживаемой архитектурой.

## Особенности

- Aiogram 3.18.0: Последняя стабильная версия фреймворка для Telegram-ботов.
- SQLAlchemy 2.0.39: ORM для работы с запросами и миграциями.
- Поддержка баз данных:
  - Asyncpg 0.30.0: Асинхронный драйвер для PostgreSQL.
  - Aiosqlite 0.21.0: Асинхронный драйвер для SQLite (по умолчанию для локальной разработки).
- Alembic 1.15.1: Управление миграциями базы данных.
- Babel 2.17.0: Поддержка интернационализации (i18n) и локализации.

## Требования

- Python: 3.8 или выше
- Docker: Установлен для развертывания в контейнерах (опционально для локальной разработки)
- Git: Для клонирования репозитория

## Установка

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/zhandos256/templateaiogram
    ```
  
2. Откройте файл `docker-compose.yml` и замените `YOUR_BOT_TOKEN` на токен, полученный от `@BotFather`

3. Выберите тип базы данных, отредактировав `docker-compose.yml`:

   - Для PostgreSQL: `DB_TYPE=postgres`
   - Для SQLite: `DB_TYPE=sqlite`

   > *Драйверы для обоих типов баз данных уже установлены и настроены, поэтому вам нужно просто выбрать нужный вариант.*

4. Соберите и запустите проект:

    ```bash
    docker-compose build
    docker compose up
    ```

> *Автоматическая инициализация: Docker автоматически запускает скрипт `run.sh`, который создаёт необходимые директории (`migrations/versions`, `locales`, `logs`) и накатывает начальную миграцию базы данных через Alembic. Если миграции уже существуют, скрипт их пропускает; если нет — создаёт и применяет миграцию `initial`. Ничего дополнительно запускать не нужно — всё выполняется автоматически.*

## Настройка интернационализации (i18n)

Шаблон поддерживает многоязычность через Babel и aiogram.utils.i18n. Чтобы настроить локализацию:

1. Импорт функции перевода: В файлах, где используются переводимые строки, добавьте импорт:

    ```python
    from aiogram.utils.i18n import gettext as _
    ```

    Затем оберните текст в функцию _(), например:

    ```python
    await message.answer(_("Привет, пользователь!"))
    ```

2. Извлечение строк для перевода: Выполните команду для создания файла шаблона переводов:

    ```bash
    pybabel extract --input-dirs=. -o locales/messages.pot
    ```

3. Создание файла перевода: Инициализируйте переводы для нужного языка (например, казахский kk):

      ```bash
      pybabel init -i locales/messages.pot -d locales -D messages -l kk
      ```

      > *Выбирайте код языка из стандарта ISO 639-1 (двухбуквенный код).
      Список доступных кодов можно посмотреть здесь: [Список кодов ISO 639-1](https://ru.wikipedia.org/wiki/Список_кодов_ISO_639-1)*

4. Редактирование перевода: Откройте файл `locales/kk/LC_MESSAGES/messages.po` и добавьте переводы для извлечённых строк.

5. Обновление переводов после изменений

    Если вы добавили или изменили строки, выполните обновление файлов перевода:

    ```bash
    pybabel update -d locales -D messages -i locales/messages.pot
    ```

6. Компиляция переводов

    Скомпилируйте переводы в бинарный формат:

    ```bash
    pybabel compile -d locales -D messages
    ```

## Пример использования

1. После запуска бота отправьте команду `/start` в Telegram для получения приветственного сообщения.
2. Используйте `/help` для списка доступных команд.

## Структура проекта

```bash
├── Dockerfile              # Конфигурация для сборки Docker-образа приложения
├── LICENSE                 # Файл с лицензией проекта
├── README.md               # Документация: описание проекта, инструкции по установке и запуску
├── docker-compose.yml      # Конфигурация для запуска приложения и зависимостей через Docker Compose
├── requirements.txt        # Список Python-зависимостей для установки через pip
├── run.sh                  # Скрипт для запуска приложения (например, миграции + запуск бота)
└── src/                    # Основная директория с исходным кодом приложения
├── __init__.py         # Пустой файл, делающий src Python-пакетом
├── alembic.ini         # Конфигурация Alembic для миграций базы данных
├── config/             # Модуль для хранения настроек приложения
│   ├── __init__.py     # Инициализация модуля config
│   ├── const.py        # Константы (например, тексты сообщений, коды ошибок)
│   ├── routers.py      # Регистрация роутеров для обработчиков Aiogram
│   └── settings.py     # Основные настройки (токен бота, URL базы данных и т.д.)
├── database/           # Модуль для работы с базой данных
│   ├── __init__.py     # Инициализация модуля database
│   ├── models.py       # Определение моделей базы данных (SQLAlchemy)
│   ├── queries.py      # Функции для выполнения запросов к базе данных
│   └── session.py      # Настройка сессий для работы с базой данных
├── filters/            # Пользовательские фильтры для Aiogram
│   ├── __init__.py     # Инициализация модуля filters
│   └── admin_filter.py # Фильтр для проверки прав администратора
├── handlers/           # Обработчики событий (команд и callback-запросов)
│   ├── __init__.py     # Инициализация модуля handlers
│   ├── admin/          # Обработчики для админ-функционала
│   │   ├── __init__.py # Инициализация подмодуля admin
│   │   └── admin.py    # Логика админ-команд (например, бан, статистика)
│   └── users/          # Обработчики для пользовательских команд
│       ├── __init__.py # Инициализация подмодуля users
│       ├── about.py    # Обработчик команды "О боте"
│       ├── cancel.py   # Обработчик команды отмены действия
│       ├── echo.py     # Обработчик для эхо-ответов (повторение текста)
│       ├── help.py     # Обработчик команды "Помощь"
│       ├── lang.py     # Обработчик смены языка
│       ├── menu.py     # Обработчик команды вызова меню
│       ├── settings.py # Обработчик настроек пользователя
│       └── start.py    # Обработчик команды /start
├── keyboards/          # Модуль для создания клавиатур
│   ├── __init__.py     # Инициализация модуля keyboards
│   └── inline/         # Подмодуль для инлайн-клавиатур
│       ├── __init__.py # Инициализация подмодуля inline
│       ├── cancel.py   # Клавиатура для отмены действия
│       ├── lang.py     # Клавиатура для выбора языка
│       ├── menu.py     # Клавиатура основного меню
│       └── settings.py # Клавиатура настроек
├── locales/            # Файлы переводов для интернационализации (i18n)
├── main.py             # Точка входа: запуск бота, инициализация
├── middleware/         # Промежуточные обработчики (middleware) для Aiogram
│   ├── __init__.py     # Инициализация модуля middleware
│   ├── i18n_middleware.py      # Middleware для поддержки локализации
│   └── last_action_middleware.py # Middleware для отслеживания активности
├── migrations/         # Директория для миграций базы данных (Alembic)
│   ├── README          # Описание миграций или инструкции
│   ├── env.py          # Настройки окружения для Alembic
│   ├── script.py.mako  # Шаблон для генерации миграций
│   └── versions/       # Папка с версиями миграций
├── services/           # Бизнес-логика приложения (пока пусто)
│   └── init.py     # Инициализация модуля services
└── utils/              # Вспомогательные утилиты
├── __init__.py     # Инициализация модуля utils
└── notify.py       # Функции для отправки уведомлений
```

## Лицензия

Проект распространяется под лицензией MIT.
