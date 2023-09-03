dictionary = {
    "and": "va",
    "are": "hastand",
    "student": "danesh amooz",
    "at": "dar",
    "in": "dar",
    "school": "madrese",
}

input_sentence = input("Please enter a sentence in English:")
translated_words = [dictionary.get(word.lower(), word) for word in input_sentence.split()]
translated_sentence = ' '.join(translated_words)
print("translate:", translated_sentence)
