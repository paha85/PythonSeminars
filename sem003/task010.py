# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ Ъ – 10 очков.

k = 'ноутбук'
one = list('AEIOULNSTRАВЕИНОРСТ')
two = list('DGДКЛМПУ')
three = list('BCMPБГЁЬЯ')
four = list('FHVWYЙЫ')
five = list('ЖЗХЦЧK')
eight = list('JXШЭЮ')
ten = list('QZФЩЪ')
word = list(k.upper())
count = 0

for i in word:
    if i in one:
        count+=1
    elif i in two:
        count+=2
    elif i in three:
        count+=3
    elif i in four:
        count+=4
    elif i in five:
        count+=5
    elif i in eight:
        count+=8
    elif i in ten:
        count+=10
# for i in word:
#     if i == 'A' or 'E' or 'I' or 'O' or 'U' or 'L' or 'N' or 'S'or 'T' or 'R':
#         count+=1
# print(count)
# for i in word:
#     if i == 'D' or 'G':
#         count+=2
print(count)

