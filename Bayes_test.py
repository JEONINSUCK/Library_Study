import math, sys
from konlpy.tag import Twitter

     class BayesianFilter:
         def __init__(self):
             self.words = set()  # 출현한 단어 기록
             # 카테고리마다의 출현 횟수 기록
             self.word_dict = {}
             self.category_dict = {}  # 카테고리 출현 횟수 기록
             print('생성자 호출됨')

         # (※1) 형태소 분석하기 : 형태소에 담아서 리스트에 담아 준다.
         def bayes_split(self, text):
             results = []
             twitter = Twitter()
             # 단어의 기본형 사용
             malist = twitter.pos(text, norm=True, stem=True)
             for word in malist:
                 # 조사, 어미, 구둣점은 제외하고 ...
                 if not word[1] in ["Josa", "Eomi", "Punctuation"]:
                     results.append(word[0])

             return results

         # (※3) : 텍스트 학습하기
         def fit(self, text, category):
             # word_list : 단어들을 저장하고 있는 리스트
             word_list = self.bayes_split(text)
             for word in word_list:
                 self.inc_word(word, category)

             self.inc_category(category)

             print('\nfit 함수 실행 결과')
             print('[category_dict 사전 내용]')
             print(self.category_dict)
             print('[word 집합 내용]')
             print(self.words)
             print('[word_dict 사전 values]')
             print(self.word_dict)

         # (※2) : 단어와 카테고리의 출현 횟수 세기
         def inc_word(self, word, category):  # 예시 : word('세일'), category('광고')

             # 단어를 카테고리에 추가하기
             if not category in self.word_dict:
                 self.word_dict[category] = {}
             if not word in self.word_dict[category]:
                 self.word_dict[category][word] = 0
             self.word_dict[category][word] += 1
             self.words.add(word)  # 단어들 모음집에 추가

         # 예측하기 --- (※5)
         def predict(self, text):
             best_category = None

             max_score = -sys.maxsize  # 시스템이 가질수 있는 가장 큰 정수(2**63-1)
             words = self.bayes_split(text)
             score_list = []
             # 사전에 들어 있는 카테고리 수만큼 반복 ....
             for category in self.category_dict.keys():
                 score = self.score(words, category)  # 이 단어들과 카테고리에 대하여...
             score_list.append((category, score))
             print('스코어')
             print(score)
             print(max_score)
             if score > max_score:  # 시스템이 가질 수 있는 최대 정수값
                 max_score = score
             best_category = category
             print('베스트 카테고리')
             print(best_category)
             return best_category, score_list

     def inc_category(self, category):
        # 카테고리 계산하기
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1

    # (※4) 단어 리스트에 점수 매기기
     def score(self, words, category):  # 예시 : words(['무료', '배송']), category('광고')
        score = math.log(self.category_prob(category))
        for word in words:
            score += math.log(self.word_prob(word, category))
        return score

        # 카테고리 내부의 단어 출현 횟수 구하기


     def get_word_count(self, word, category):
        if word in self.word_dict[category]:
            return self.word_dict[category][word]
        else:
            return 0

    # 카테고리 계산
     def category_prob(self, category):
        sum_categories = sum(self.category_dict.values())
        category_v = self.category_dict[category]
        print('모든 카테코리들의 빈도수 총합')
        print(sum_categories)
        print('해당 카테코리의 빈도 수')
        print(category_v)
        return category_v / sum_categories

    # 카테고리 내부의 단어 출현 비율 계산 --- (※6)
     def word_prob(self, word, category):

        # 없는 단어이면 n=0 인데 이렇게 되면 확률이 0 이 되므로 1 을 의도적으로 +1 시킨다.
        n = self.get_word_count(word, category) + 1  # ---(※6a)
        d = sum(self.word_dict[category].values()) + len(self.words)
        return n / d

#################################################################
bf = BayesianFilter()

# 텍스트 학습
bf.fit("세일 무료 배송 할인", "광고")
bf.fit("일정 확인", "중요")

bf.fit("백화점 세일", "광고")
bf.fit("파격 세일 할인", "광고")
bf.fit("프로젝트 진행 상황","중요")
bf.fit("쿠폰 선물 & 무료 배송", "광고")
bf.fit("봄과 함께 찾아온 따뜻한 신제품 소식", "광고")
bf.fit("인기 제품 기간 한정 세일", "광고")
bf.fit("계약 잘 부탁드립니다","중요")
bf.fit("회의 일정이 등록되었습니다.","중요")
bf.fit("오늘 일정이 없습니다.","중요")

# 메일 제목이 "무료 배송"이면 광고 메일인가, 중요 메일인가를 예측
pre, scorelist = bf.predict("무료 배송")
print("결과 =", pre)
print(scorelist)

pre, scorelist = bf.predict("일정 확인")
print("결과 =", pre)
print(scorelist)