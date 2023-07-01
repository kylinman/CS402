import random

def gen_passage(ngram_dict, length=100):
    passage = []
    current_token = random.choice(sorted(ngram_dict.keys()))
    while len(passage) < passage_length:
        passage.extend(current_token.split())
        if current_token in ngram_dict:
            next_tuple = random.choice(ngram_dict[current_token])
            current_token = ' '.join(next_tuple)
        else:
            current_token = random.choice(sorted(ngram_dict.keys()))
# Truncate the passage to the specified length if necessary
passage = passage[:passage_length]
return ' '.join(passage)