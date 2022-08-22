# Проект парсинга документации Python
## Описание

Парсит спсиок PEP, в папку results в один файл сохраняет номер, название и статус
каждого PEP, во второй файл записывается статистика количества PEP'ов по категориям.

## Установка

- Клонировать репозиторий:

 ```
git clone https://github.com/firepanda70/scrapy_parser_pep
```

- Создать и активировать виртуальное окружение:

```
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

- Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

## Как запустить:

```
scrapy crawl pep
```

## Технологии:

- Python 3
- Scrapy
