import pytagcloud
import random
from konlpy.tag import Okt
from collections import Counter

file = open('frozen2.txt', 'r', encoding='utf-8')
reply_text = file.readlines()
file.close()

ok_twitter = Okt()
nouns = []
tags = []

for sentence in reply_text:  # 댓글에서 명사를 추출하고 nouns변수에 저장
    for noun in ok_twitter.nouns(sentence):
        if noun in ['함', '그', '이', '임', '도', '편', '점', '좀', '애', '영화', '것', '더', '상미', '볼', '보고', '저']:
            pass

        elif noun == '엘사':
            nouns.append('다민')

        else:
            nouns.append(noun)
count = Counter(nouns)  # 각 명사별로 빈도계산'''

for n, c in count.most_common(40):  # n : 명사, c : 빈도
    tags.append({'color': (random.randint(0, 255),
                           random.randint(0, 255),
                           random.randint(0, 255)),
                 'tag': n,
                 'size': 2 * c})
print(tags)
pytagcloud.create_tag_image(tags, '12345678.png', fontname='myfont', size=(1280, 720))

