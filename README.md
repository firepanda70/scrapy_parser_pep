# Проект парсинга документации Python
## Описание
Парсит спсиок PEP, сохраняет их номер, название и статус в 
csv файл в папку results, а так же общее количество всех 
документов PEP по каждому отдельному статусу в отдельный файл

## Установка

- Клонировать репозиторий:

 ```
git clone https://github.com/firepanda70/scrapy_parser_pep
```

- Создать и активировать виртуальное окружение:

```
python -m venv env
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
