#-*- coding : utf-8-*-
# coding:unicode_escape
import jieba

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('cut.txt',encoding='UTF-8').readlines()]
    return stopwords

# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("continue")
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

# 给出文档路径
filename = "time4.csv"
outfilename = "time44.csv"
inputs = open(filename, 'r')
outputs = open(outfilename, 'w',encoding='UTF-8')

# 将输出结果写入ou.txt中
for line in inputs:
    line_seg = seg_depart(line)
    outputs.write(line_seg )
    print("yes")
outputs.close()
inputs.close()
print("mission completed")