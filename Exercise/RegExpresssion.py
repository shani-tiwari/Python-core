# Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_sentence = sentence.replace("%", "").replace("$", "").replace("@", "").replace("&", "").replace("#", "").replace(";", "").replace("?", "")
print(clean_sentence)

# split the sentence into words
words = clean_sentence.split()
print(words)

# count the frequency of each word
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# get the three most frequent words
most_frequent_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]
print(most_frequent_words)
