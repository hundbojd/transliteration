d = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
}

with open('cyrillic.txt', 'rt', encoding='utf-8') as text, open('transliteration.txt', 'w') as trans:
    t = text.read()
    t2 = ''
    for i in t:
        if i.lower() in d:
            if i.isupper():
                t2 += d[i.lower()].title()
            else:
                t2 += d[i.lower()]
        else:
            t2 += i
    print(t2)
