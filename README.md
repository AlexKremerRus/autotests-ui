# Автоматизированные тесты для UI курса

Этот проект реализует автоматизированные тесты для [Тестового приложения UI курса](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login). Тесты написаны с использованием **Python**, **Pytest**, **Allure** и **Playwright**. Исходный код тестового приложения доступен на [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course).  
**Allure** отчет можно посмотреть по ссылке - https://alexkremerrus.github.io/autotests-ui  
Связь со мной 👉 [@Al_Star](https://t.me/Al_Star)

## Обзор проекта

Цель проекта - автоматизация тестирования приложения UI курса. Автоматизированные тесты проверяют различные функции приложения, чтобы гарантировать его стабильность и корректность. Структура проекта соответствует лучшим практикам организации тестового кода с понятными и поддерживаемыми скриптами.

## Начало работы

### Клонирование репозитория

Для начала клонируйте репозиторий проекта с помощью Git:

```bash
git clone https://github.com/AlexKremerRus/autotests-ui.git
cd autotests-ui
```

### Создание виртуального окружения

Рекомендуется использовать виртуальное окружение для управления зависимостями проекта. Следуйте инструкциям для вашей операционной системы:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей

После активации виртуального окружения установите зависимости проекта, перечисленные в `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Дополнительная настройка Playwright (если необходимо)

Если вы запускаете Playwright впервые, может потребоваться установка необходимых браузеров:

```bash
playwright install
```

### Запуск тестов с генерацией отчета Allure

Для запуска тестов и генерации отчета Allure используйте следующую команду:

```bash
pytest -m "regression" --alluredir=./allure-results
```

Эта команда выполнит все тесты проекта и отобразит результаты в терминале.

### Просмотр отчета Allure

После выполнения тестов вы можете сгенерировать и просмотреть отчет Allure с помощью:

```bash
allure serve allure-results
```

Эта команда откроет отчет Allure в вашем веб-браузере по умолчанию.

