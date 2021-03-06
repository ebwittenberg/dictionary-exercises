# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.

user_sentence = input('Please enter your sentence here: ')
user_words = user_sentence.split(' ')

def word_tally(sentence):

    word_dict = {}

    #for each word in the array of user's words
    for word in sentence:
        # if that word key already exists in the dictionary
        if word in word_dict:
            # increase its value by one
            word_dict[word] += 1
        # otherwise if word key doesn't already exist
        else:
            word_dict[word] = 1

    # create array with values of word_dict
    word_totals = []
    # save top three values in a new array
    top_three_values = []

    for word in word_dict:
        word_totals.append(word_dict[word])
    # print(word_totals)

    # Append max value of word_totals values to top_three_totals, and remove that max from word totals array
    while len(top_three_values) < 3:
        top_three_values.append(max(word_totals))
        word_totals.remove(max(word_totals))
        print(top_three_values)

    # Top three values now has stored the top three values from the word dictionary


    # for each word in the word dictionary
    top_three_words = {}
    for word in word_dict:
        if len(top_three_words) < 3:
        # for each value in the already created top three values
            for value in top_three_values:
                # if the value of particular word key is a value in top three values
                if word_dict[word] == value:
                # create that key value pair in top_three_words dictionary
                    top_three_words[word] = value
                    print(len(top_three_words))

    print(top_three_words)
    



word_tally(user_words)
    