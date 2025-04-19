import re
import matplotlib.pyplot as plt
from collections import Counter
import os
import sys

class DualOutput:
    """Класс для вывода одновременно в консоль и в файл"""
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, 'w', encoding='utf-8')
    
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    
    def flush(self):
        self.terminal.flush()
        self.log.flush()
    
    def close(self):
        self.log.close()

def read_text_file(filename, start_pos=None, end_pos=None):
    """Чтение текста из файла с возможностью указания диапазона позиций"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
            if start_pos is not None and end_pos is not None:
                if start_pos < 0 or end_pos > len(content) or start_pos > end_pos:
                    print("Ошибка: Некорректный диапазон позиций. Будет возвращен весь текст.")
                    return content
                return content[start_pos:end_pos]
            elif start_pos is not None:
                if start_pos < 0 or start_pos > len(content):
                    print("Ошибка: Некорректная начальная позиция. Будет возвращен весь текст.")
                    return content
                return content[start_pos:]
            else:
                return content
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

def process_text(text):
    """Статистическая обработка текста"""
    if not text:
        return None
    
    try:
        # Разделение на слова (учитываем апострофы и дефисы в словах)
        words = re.findall(r"\b[\w'-]+\b", text.lower())
        if not words:
            print("Ошибка: В тексте не найдено слов.")
            return None
        
        word_counts = Counter(words)
        
        # Статистика по длинам слов
        word_lengths = [len(word) for word in words]
        length_stats = Counter(word_lengths)
        
        # Разделение на предложения
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        # Количество слов в предложениях
        sentence_word_counts = []
        for sent in sentences:
            sent_words = re.findall(r"\b[\w'-]+\b", sent.lower())
            if sent_words:
                sentence_word_counts.append(len(sent_words))
        
        if not sentence_word_counts:
            print("Ошибка: Не удалось определить предложения.")
            return None
        
        return {
            'words': words,
            'word_counts': word_counts,
            'word_lengths': word_lengths,
            'length_stats': length_stats,
            'sentences': sentences,
            'sentence_word_counts': sentence_word_counts
        }
    except Exception as e:
        print(f"Ошибка при обработке текста: {e}")
        return None

def plot_stats(stats, sort_order='asc'):
    """Построение графиков статистики"""
    if not stats:
        print("Ошибка: Нет данных для построения графиков.")
        return
    
    try:
        length_stats = stats['length_stats']
        
        # Сортировка по возрастанию/убыванию
        if sort_order == 'asc':
            sorted_stats = sorted(length_stats.items())
        else:
            sorted_stats = sorted(length_stats.items(), reverse=True)
        
        lengths, counts = zip(*sorted_stats)
        
        # Гистограмма распределения длин слов
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.bar(lengths, counts)
        plt.xlabel('Длина слова (символов)')
        plt.ylabel('Частота')
        plt.title('Распределение длин слов')
        
        # График распределения длин слов
        plt.subplot(1, 2, 2)
        plt.plot(lengths, counts, 'ro-')
        plt.xlabel('Длина слова (символов)')
        plt.ylabel('Частота')
        plt.title('Зависимость частоты от длины слова')
        
        plt.tight_layout()
        plt.savefig('word_length_distribution.png')  # Сохраняем график в файл
        plt.show()
        
        # Гистограмма распределения количества слов в предложениях
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.hist(stats['sentence_word_counts'], bins=20)
        plt.xlabel('Количество слов в предложении')
        plt.ylabel('Частота')
        plt.title('Распределение слов в предложениях')
        
        plt.subplot(1, 2, 2)
        plt.boxplot(stats['sentence_word_counts'])
        plt.title('Boxplot длины предложений (в словах)')
        
        plt.tight_layout()
        plt.savefig('sentence_length_distribution.png')  # Сохраняем график в файл
        plt.show()
    except Exception as e:
        print(f"Ошибка при построении графиков: {e}")

def print_stats(stats):
    """Вывод статистики в консоль и файл"""
    if not stats:
        print("Ошибка: Нет данных для вывода статистики.")
        return
    
    try:
        print(f"\n{'='*50}")
        print(f"{'СТАТИСТИКА ТЕКСТА':^50}")
        print(f"{'='*50}\n")
        
        print(f"Общее количество слов: {len(stats['words'])}")
        print(f"Уникальных слов: {len(stats['word_counts'])}")
        print(f"Средняя длина слова: {sum(stats['word_lengths'])/len(stats['word_lengths']):.2f} символов")
        
        print("\nСтатистика длин слов:")
        for length, count in sorted(stats['length_stats'].items()):
            print(f"{length:>2} символов: {count:>4} слов")
        
        print(f"\nКоличество предложений: {len(stats['sentences'])}")
        print(f"Среднее количество слов в предложении: {sum(stats['sentence_word_counts'])/len(stats['sentence_word_counts']):.2f}")
        print(f"Максимальное количество слов в предложении: {max(stats['sentence_word_counts'])}")
        print(f"Минимальное количество слов в предложении: {min(stats['sentence_word_counts'])}")
        
        # Дополнительная статистика
        print("\n10 самых частых слов:")
        for word, count in stats['word_counts'].most_common(10):
            print(f"{word}: {count} раз")
        
        print("\n10 самых длинных слов:")
        unique_words = sorted(set(stats['words']), key=len, reverse=True)
        for word in unique_words[:10]:
            print(f"{word} ({len(word)} символов)")
    except Exception as e:
        print(f"Ошибка при выводе статистики: {e}")

def main():
    # Перенаправляем вывод в консоль и файл
    sys.stdout = DualOutput('output.txt')
    
    try:
        # Проверяем существование файла
        filename = "text1.txt"
        if not os.path.exists(filename):
            print(f"Файл '{filename}' не найден. Создайте текстовый файл с именем 'text.txt'")
            return
        
        # 1. Чтение файла
        print(f"\nЧтение файла '{filename}'...")
        full_text = read_text_file(filename)
        if not full_text:
            return
        
        # 2. Чтение фрагмента (пример)
        print("\nЧтение фрагмента текста (100-500 символов)...")
        fragment = read_text_file(filename, 100, 500)
        print(f"\nФрагмент текста (100-500 символов):\n{'='*50}")
        print(fragment)
        print(f"{'='*50}")
        
        # 3. Обработка текста
        print("\nОбработка текста...")
        stats = process_text(full_text)
        if not stats:
            return
        
        # 4. Вывод статистики
        print_stats(stats)
        
        # 5. Построение графиков
        print("\nПостроение графиков...")
        plot_stats(stats, sort_order='asc')  # по возрастанию
        plot_stats(stats, sort_order='desc') # по убыванию
        
        print("\nАнализ завершен. Результаты сохранены в:")
        print("- output.txt (текстовые результаты)")
        print("- word_length_distribution.png (график длин слов)")
        print("- sentence_length_distribution.png (график длин предложений)")
    finally:
        # Восстанавливаем стандартный вывод
        sys.stdout.close()
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()