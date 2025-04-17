import numpy as np
import pandas as pd
from faker import Faker

# Инициализация генератора случайных данных
fake = Faker('ru_RU')
np.random.seed(42)

# Параметры для генерации
N = np.random.randint(30, 46)  # Количество строк (от 30 до 45)

# Создание DataFrame
df = pd.DataFrame()

# 1 столбец - номер
df['№'] = range(1, N+1)

# 2 столбец - Фамилия Имя (заполняем последним)
df['ФИО'] = [fake.name() for _ in range(N)]

# 3 столбец - год рождения (водители от 18 до 70 лет)
birth_years = np.random.normal(loc=1985, scale=10, size=N).astype(int)
df['Год рождения'] = np.clip(birth_years, 1953, 2005)  # Ограничиваем разумные значения

# 4 столбец - пол (70% мужчин, 30% женщин)
genders = np.random.choice(['м', 'ж'], size=N, p=[0.7, 0.3])
df['Пол'] = genders

# 5 столбец - вес (разный для мужчин и женщин)
male_mask = df['Пол'] == 'м'
df['Вес, кг'] = 0
df.loc[male_mask, 'Вес, кг'] = np.random.normal(loc=85, scale=10, size=male_mask.sum()).astype(int)
df.loc[~male_mask, 'Вес, кг'] = np.random.normal(loc=65, scale=8, size=(~male_mask).sum()).astype(int)

# 6 столбец - рост (разный для мужчин и женщин)
df['Рост, см'] = 0
df.loc[male_mask, 'Рост, см'] = np.random.normal(loc=178, scale=7, size=male_mask.sum()).astype(int)
df.loc[~male_mask, 'Рост, см'] = np.random.normal(loc=165, scale=6, size=(~male_mask).sum()).astype(int)

# 7 столбец - 1 качественный признак (марка автомобиля)
brands = ['ВАЗ', 'Renault', 'VolksVagen', 'Hynday', 'Kia']
brand_probs = [0.4, 0.1, 0.2, 0.25, 0.05]
df['Марка'] = np.random.choice(brands, size=N, p=brand_probs)

# 8 столбец - 2 качественный признак (категория автомобиля)
categories = ['Эконом', 'Средний', 'Престиж']
category_probs = [0.75, 0.2, 0.05]
df['Категория'] = np.random.choice(categories, size=N, p=category_probs)

# 9 столбец - количественный признак (закредитованность)
df['Закредитованность'] = np.random.normal(loc=150000, scale=80000, size=N).astype(int)
df['Закредитованность'] = df['Закредитованность'].apply(lambda x: max(x, 0))  # Не может быть отрицательной

# Переупорядочиваем столбцы
df = df[['№', 'ФИО', 'Год рождения', 'Пол', 'Вес, кг', 'Рост, см', 
         'Марка', 'Категория', 'Закредитованность']]

# Сохраняем исходные данные
df.to_csv('ishodVar.csv', index=False)
df.to_excel('ishodVar.xlsx', index=False)


