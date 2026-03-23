print("\n 1. Повторения букв")

from collections import Counter

text = "Programming is fun!"
counter = Counter(text.lower())
print("Количество букв в тексте: ", dict(counter))



print("\n 2. Группировка студентов по классам")

from collections import defaultdict

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
grouped = defaultdict(list)

for clas, name in students:
   grouped[clas].append(name)
print("Студенты по классам: ", dict(grouped))



