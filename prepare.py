# -*- coding: utf-8 -*-

import unicodedata
import re
import MeCab
import random

# Turn a Unicode string to plain ASCII.
def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

def normalizeString(s, lang):
    if lang == "jpn":
        tagger = MeCab.Tagger('-Owakati')
        s = tagger.parse(s).strip()
        return s

    s = unicodeToAscii(s.lower().strip())
    s = re.sub(r"([.!?])", r" \1", s)
    s = re.sub(r"[^a-zA-Z0-9.!?]+", r" ", s)
    return s

from lang_class import Lang 
addSentence = Lang.addSentence

def readLangs(lang1, lang2, reverse=False):
    print("Reading lines...")

    # Read the file and split into lines
    lines = open('data/%s-%s.txt' % (lang1, lang2), encoding='utf-8').\
        read().strip().split('\n')

    # Split every line into pairs and normalize
    pairs_sub = [[s for s in l.split('\t')] for l in lines]

    pairs = []
    i = 0
    for p in pairs_sub:
        a,b = p
        a = normalizeString(a, lang1)
        b = normalizeString(b, lang2)
        pairs.append([a,b])
        i+=1
        if i%1000==0:
            print(i,a,b)

    # Reverse pairs, make Lang instances
    if reverse:
        pairs = [list(reversed(p)) for p in pairs]
        input_lang = Lang(lang2)
        output_lang = Lang(lang1)
    else:
        input_lang = Lang(lang1)
        output_lang = Lang(lang2)

    return input_lang, output_lang, pairs

MAX_LENGTH = 10

eng_prefixes = (
    "i am ", "i m ",
    "he is", "he s ",
    "she is", "she s ",
    "you are", "you re ",
    "we are", "we re ",
    "they are", "they re "
)

def filterPair(p):
    return len(p[0].split(' ')) < MAX_LENGTH and \
        len(p[1].split(' ')) < MAX_LENGTH and \
        p[1].startswith(eng_prefixes)


def filterPairs(pairs):
    return [pair for pair in pairs if filterPair(pair)]


def prepareData(lang1, lang2, reverse=False):
    input_lang, output_lang, pairs = readLangs(lang1, lang2, reverse)
    print("Read %s sentence pairs" % len(pairs))

    pairs = filterPairs(pairs)
    print("Trimmed to %s sentence pairs" % len(pairs))
    print("Counting words...")

    # Make a dict
    for pair in pairs:
        input_lang.addSentence(pair[0])
        output_lang.addSentence(pair[1])
    print("Counted words:")
    print(input_lang.name, input_lang.n_words)
    print(output_lang.name, output_lang.n_words)
    return input_lang, output_lang, pairs

# Read eng-jpn.txt and prepare
# randomly 70% -> for_train.txt, 30% -> for_test.txt
def main():
    input_lang, output_lang, pairs = prepareData('eng', 'jpn', True)
    file1=0
    file2=0
    for pair in pairs:
        string = pair[0] + '\t' + pair[1] + '\n'
        if random.random() < 0.7:
            file1=open('data/for_train.txt', 'a')
            file1.write(string)
        else:
            file2=open('data/for_test.txt', 'a')
            file2.write(string)
    file1.close()
    file2.close()

if __name__=='__main__':
    main()