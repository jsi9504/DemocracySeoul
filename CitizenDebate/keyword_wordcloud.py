# -*- coding utf-8-*-
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import sys
import os

input_path= "data"
output_path="datalog"
image_path="wordcloud"
def get_tags(text, ntags=50):
    spliter = Okt()
    # konlpy의 Twitter객체
    nouns = spliter.nouns(text)
    # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns)
    # Counter객체를 생성하고 참조변수 nouns할당
    return_list = []  # 명사 빈도수 저장할 변수
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도수
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    # 명사와 사용된 갯수를 return_list에 저장합니다.
    return return_list


def main(iter_count):
    text_file_name = input_path + str(iter_count) + ".txt"
    # 분석할 파일
    noun_count = 50
    # 최대 많은 빈도수 부터 50개 명사 추출
    output_file_name = output_path + str(iter_count) + ".txt"
    # count.txt 에 저장
    open_text_file = open(text_file_name, 'r',encoding="utf-8")
    # 분석할 파일을 open
    text = open_text_file.read()  # 파일을 읽습니다.
    tags = get_tags(text, noun_count)  # get_tags 함수 실행
    open_text_file.close()  # 파일 close
    open_output_file = open(output_file_name, 'w')
    # 결과로 쓰일 count.txt 열기
    dict_for_cloud = {}
    tags.pop(0)
    for tag in tags:
        noun = tag['tag']
        count = tag['count']
        open_output_file.write('{} {}\n'.format(noun, count))
        dict_for_cloud[str(noun)] = float(count)

    # 결과 저장
    open_output_file.close()

    analyze_wordcloud(dict_for_cloud,image_path + str(iter_count) + ".jpeg")


def analyze_wordcloud(count_list,image_path):
    # 워드클라우드 생성
    font_path = 'c:\\windows\\fonts\\NanumGothic.ttf'
    wordcloud = WordCloud(
        font_path = font_path,
        width = 800,
        height = 800,
        background_color='white'
    )
    wordcloud = wordcloud.generate_from_frequencies(count_list)
    fig = plt.figure(figsize=(12,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    fig.savefig(image_path)


if __name__ == "__main__" :
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    main(sys.argv[1])

