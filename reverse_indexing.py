from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
    ]


def reverse_index(dataset):
    index_dictionary = {}
    x = dataset
    # for every part in the dataset x we should replace it with itself.lower() to lowercase it
    for i in range(len(x)):
        x[i] = x[i].lower()
    count = 0
    # split list into sentences (separate strings) and split into individual words
    for sentence in x:
        words = sentence.split(' ')
        # go through each word and ad it to the dictionary with the count as its value
        # (show in which sentence/string it is
        for word in words:
            # if the word already is in the dictionary the value should be [the prior value, new value]
            if word in index_dictionary.keys():
                index_dictionary[word] += [count]
            # otherwise just add it to the dictionary with the count as its value
            else:
                index_dictionary[word] = [count]
        count += 1

    # don't forget to return your resulting dictionary
    return index_dictionary

# You can see the output of your function here
print(reverse_index(dataset))
