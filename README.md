# Translator from Japanese to English

Especially for Japanese, we need pre-processing for the input.
We add pre-processing using MeCab.

Note: You can evaluate by Bleu using nlg-eval

## Run
1. Pre-process the input
`python3 prepare.py`

2. Learn the input
`python3 main.py`

3. Use [nlg-eval](https://github.com/Maluuba/nlg-eval) to evaluate


## Results

Bleu_1: 0.529807

Bleu_2: 0.371828

Bleu_3: 0.263771

Bleu_4: 0.196287


## Reference
- [Translator](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)
- [nlg-eval](https://github.com/Maluuba/nlg-eval)

