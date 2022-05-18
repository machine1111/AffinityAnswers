import re

def prof_check():
    for sentence in sentences:
        print(sentence)
        # Removing all punchuation from sentence
        sentence = re.sub(r'[^\w\s]','',sentence)
        if len(sentence) > 0:
            sentence = sentence.split(' ')
            count = 0
            # Comparing each word of the sentence to set of words provided
            if any(prof.lower() == word.lower() for word in sentence for prof in profane_words):
                count += 1

            profanity = round(count/len(sentence) * 100, 2)
            print(f'Profanity : {profanity}%')


if __name__ == '__main__':
    try:
        with open('test_tweets.txt', 'r') as f:
            text = f.read()
        sentences = text.split('\n')
    finally:
        f.close()

    profane_words = ['bad','worse','worst','fat','ugly','stupid']

    prof_check()
