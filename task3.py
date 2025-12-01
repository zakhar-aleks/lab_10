import matplotlib.pyplot as plt

vowels = ["a", "e", "i", "o", "u"]
vowel_counts = {v: 0 for v in vowels} 
filename = "text.txt"

try:
    with open(filename, "r", encoding='utf-8') as f:
        text = f.read().lower() 

        for letter in text:
            if letter in vowel_counts:
                vowel_counts[letter] += 1

    names = list(vowel_counts.keys())
    values = list(vowel_counts.values())

    plt.figure(figsize=(8, 6)) 
    plt.bar(names, values, color='skyblue', edgecolor='black')

    plt.title("Частота появи голосних літер у тексті")
    plt.xlabel("Голосні літери")
    plt.ylabel("Кількість")
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.savefig("vowels_histogram.png") 
    print("Гістограму успішно збережено у файл 'vowels_histogram.png'")
    
    plt.show() 

except FileNotFoundError:
    print(f"Помилка: Файл '{filename}' не знайдено. Будь ласка, створіть файл з текстом.")