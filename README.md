Тестовое задание с сервисом для сокращения урлов


Создать виртаульное окружение через pyenv:

```bash
$ pyenv virtualenv 3.10.4 short_url
$ pyenv local short_url 
```
Установить необходимые пакеты:

```bash
$ pip install -U setuptools pip pipenv
$ pipenv install
$ pipenv install --dev
```

Важно: 
перед запуском внутри Docker, нужно обязательно выполнить команду `pipenv install`, 
чтобы сформировался Pipfile.lock, именно из этого файла должна браться информация о зависимостях при сборке докер образа. 
Также необходимо добавить этот файл в индекс git-а.

## Запуск внутри Docker

```bash
$ docker-compose up
```
