# 2.1. Чтение данных и базовые операции
import pandas as pd

work_df = pd.read_excel('ishodVar.xlsx')
print("Первые 5 записей:")
print(work_df.head())

# Сохраняем рабочую копию
work_df.to_excel('WorkVar.xlsx', index=False)

# Выделение серий
print("\nСерии (столбцы):", work_df.columns.tolist())

# Сортировка
sorted_asc = work_df.sort_values('Закредитованность')
#sorted_desc = work_df.sort_values('Закредитованность', ascending=False)

print("\nСортировка по возрастанию закредитованности:")
print(sorted_asc[['ФИО', 'Закредитованность']].head())

# Фильтрация
filtered = work_df[(work_df['Пол'] == 'м') & (work_df['Категория'] == 'Престиж')]
print("\nМужчины с автомобилями престижной категории:")
print(filtered[['ФИО', 'Марка', 'Категория']])

# 2.2. Формирование новых словарей
# Словарь с ключами из качественных признаков
dict_brand = work_df.groupby('Марка').apply(lambda x: list(zip(x['ФИО'], x['Год рождения'], x['Закредитованность'])), include_groups=False).to_dict()

dict_category = work_df.groupby('Категория').apply(lambda x: list(zip(x['ФИО'], x['Марка'], x['Закредитованность'])), include_groups=False).to_dict()

# Словарь с ключами из кортежей двух качественных признаков
dict_brand_category = work_df.groupby(['Марка', 'Категория']).apply(lambda x: list(zip(x['ФИО'], x['Год рождения'], x['Закредитованность'])), include_groups=False).to_dict()

print("\nПример словаря по маркам автомобилей (первые 2 элемента):")
for brand, values in list(dict_brand.items())[:2]:
    print(f"{brand}: {values[:2]}")

# 2.3. Фильтрация словарей
# Фильтрация по полу (мужчины)
male_records = work_df[work_df['Пол'] == 'м']
male_dict = male_records.groupby('Марка').apply(lambda x: list(zip(x['ФИО'], x['Год рождения'])), include_groups=False).to_dict()

# Фильтрация по возрасту (старше 40 лет)
old_records = work_df[work_df['Год рождения'] < 1983]
old_dict = old_records.groupby('Марка').apply(lambda x: list(zip(x['ФИО'], x['Год рождения'])), include_groups=False).to_dict()

# 2.4. Фильтрация по признакам темы
# Автомобилисты с высокой закредитованностью (>200000)
high_debt = work_df[work_df['Закредитованность'] > 200000]
high_debt_dict = high_debt.groupby('Категория').apply(lambda x: list(zip(x['ФИО'], x['Марка'], x['Закредитованность'])), include_groups=False).to_dict()

# Дополнительные фильтрации с сортировкой
# 1. Женщины с автомобилями марки Renault, сортировка по возрасту
filter1 = work_df[(work_df['Пол'] == 'ж') & (work_df['Марка'] == 'ВАЗ')].sort_values('Год рождения')
print("\nЖенщины с ВАЗ по возрасту:")
print(filter1[['ФИО', 'Год рождения']])

# 2. Водители с ростом выше 180 см, сортировка по весу
filter2 = work_df[work_df['Рост, см'] > 180].sort_values('Вес, кг')
print("\nВысокие водители по весу:")
print(filter2[['ФИО', 'Рост, см', 'Вес, кг']])

# 3. Водители с закредитованностью ниже среднего, сортировка по марке
avg_debt = work_df['Закредитованность'].mean()
filter3 = work_df[work_df['Закредитованность'] < avg_debt].sort_values('Марка')
print("\nВодители с закредитованностью ниже среднего:")
print(filter3[['ФИО', 'Марка', 'Закредитованность']])

# 4. Водители категории "Эконом" старше 40 лет, сортировка по году рождения
filter4 = work_df[(work_df['Категория'] == 'Эконом') & 
                 (work_df['Год рождения'] < 1983)].sort_values('Год рождения')
print("\nВодители эконом-класса старше 40 лет:")
print(filter4[['ФИО', 'Год рождения', 'Категория']])

# 5. Водители-мужчины, с высокой закредитованностью
filter5 = work_df[(work_df['Пол'] == 'м') & 
                 (work_df['Закредитованность'] > 200000)].sort_values('Закредитованность', ascending=False)
print("\nмужчины с высокой закредитованностью:")
print(filter5[['ФИО', 'Пол', 'Закредитованность']])

# 2.5. Сохранение результатов
with open('results.txt', 'w', encoding='utf-8') as f:
    f.write("=== Мужчины с автомобилями престижной категории ===\n")
    f.write(filtered[['ФИО', 'Марка', 'Категория']].to_string(index=False))
    f.write("\n\n===Женщины с Renault по возрасту===\n")
    f.write(filter1[['ФИО', 'Год рождения']].to_string(index=False))
    f.write("\n\n===Высокие водители по весу===\n")
    f.write(filter2[['ФИО', 'Рост, см', 'Вес, кг']].to_string(index=False))
    f.write("\n\n===Водители с закредитованностью ниже среднего===\n")
    f.write(filter3[['ФИО', 'Марка', 'Закредитованность']].to_string(index=False))
    f.write("\n\n===Водители эконом-класса старше 40 лет===\n")
    f.write(filter4[['ФИО', 'Год рождения', 'Категория']].to_string(index=False))
    f.write("\n\n=== Автомобилисты с высокой закредитованностью (>200000) ===\n")
    f.write(high_debt[['ФИО', 'Марка', 'Категория', 'Закредитованность']].to_string(index=False))
    f.write("\n\nПример словаря по маркам автомобилей:\n")
    for brand, values in list(dict_brand.items())[:2]:
        f.write(f"{brand}: {values[:2]}\n")

# Сохранение в Excel
with pd.ExcelWriter('results.xlsx') as writer:
    sorted_asc.to_excel(writer, sheet_name='Сортировка по возрастанию', index=False)
    filtered.to_excel(writer, sheet_name='Мужчины престиж', index=False)
    high_debt.to_excel(writer, sheet_name='Высокая закредитованность', index=False)



################################################################################################################


# Формирование множеств
brand_set = set(work_df['Марка'])
category_set = set(work_df['Категория'])
print("\nМножество марок автомобилей:", brand_set)

# Операции с множествами
popular_brands = {'ВАЗ', 'Hynday', 'Kia'}
print("Популярные марки в данных:", brand_set & popular_brands)