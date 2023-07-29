# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.10.8

# Встановимо змінну середовища
ENV APP_HOME /assistant

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME


# Скопіюємо інші файли в робочу директорію контейнера
COPY pyproject.toml $APP_HOME/pyproject.toml
COPY poetry.lock $APP_HOME/poetry.lock

# Встановимо залежності всередині контейнера
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .


# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 5000

# Запустимо наш застосунок всередині контейнера
CMD ["python", "__main__.py"]