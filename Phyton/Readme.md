Что бы получить список пакетов в проекте

```python
pip freeze
````

Для записи вывода в requirements.txt дополняем следующим образом:

```python
pip freeze > requirements.txt
````

Запуск иницилизации библиотек из requirements.txt:

```python
pip install -r requirements.txt
````