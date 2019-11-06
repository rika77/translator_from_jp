# -*- coding: utf-8 -*-

from main import evaluate

lines = open('data/for_train.txt', encoding='utf-8').read().strip().split('\n')
pairs = [[s for s in l.split('\t')] for l in lines]

file = open('data/ref.txt', 'w')

i = 0
print("begin")
for pair in pairs:
	i+=1
	# write into ref.txt
	string = pair[1] + '\n'
	file.write(string)
	if i%100==0:
		print("nyanko", pair)
file.close()
print("end")


i=0
file = open('data/hyp.txt', 'w')
for pair in pairs:
	i+=1
	output_words, attentions = evaluate(encoder1, attn_decoder1, pair[0].strip())
	output_sentence = ' '.join(output_words)
	output_sentence += '\n'
	file.write(output_sentence)
	if i%100==0:
		print(pair)
file.close()