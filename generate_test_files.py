import random
import string
from typing import Set

def generate_sorted_file(filename, num_lines, seed) -> None:
	random.seed(seed)  # Фиксируем seed для воспроизводимости
	words: Set[str] = set()

	while len(words) < num_lines:
		word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
		words.add(word)

	with open(filename, 'w', encoding='utf-8') as f:
		for word in sorted(words):  # Лексикографически сортируем перед записью
			f.write(word + '\n')

# Генерируем файлы
generate_sorted_file("input1.txt", 1_000_000, seed=42)
generate_sorted_file("input2.txt", 1_000_000, seed=43)

print("Файлы input1.txt и input2.txt созданы.")
