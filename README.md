### Hexlet tests and linter status:
[![Actions Status](https://github.com/tarvarrs/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/tarvarrs/python-project-50/actions)

[![Test Coverage](https://api.codeclimate.com/v1/badges/63b6dcb1b16fefbeefe3/test_coverage)](https://codeclimate.com/github/tarvarrs/python-project-50/test_coverage)

# Вычислитель отличий: утилита для сравнения двух конфигурационных файлов

## Проект в рамках курса «Python-разработчик»

Создан для отработки навыков работы с деревьями, слабоструктурированными форматами данных (JSON и YAML), написания тестов и непрерывной интеграции (CI).

## Установка

Склонируйте и установите репозиторий, используя UV:

```sh
git clone https://github.com/tarvarrs/python-project-50
cd gendiff
make install
```

## Использование

Вывести информацию об использовании

```sh
uv run gendiff -h
```

Пример сравнения двух файлов:

```sh
uv run gendiff filepath1.json filepath2.json
```

Вывод:

```json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

## Опции

- `-h, --help` — show this help message and exit.
- `f {stylish,plain,json}, --format {stylish,plain,json}` - set format of output
                        
## Форматы вывода

### Stylish

Форматирование по умолчанию. Отображает изменения в древовидной структуре.

### Plain

Человекочитаемый формат.

### JSON

Вывод в формате JSON.


