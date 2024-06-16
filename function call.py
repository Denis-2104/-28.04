def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if  root_word.lower() in  i.lower() or i. lower():
            same_words.append(i)
    return same_words
result2= single_root_words ('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result1= single_root_words ('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

print (result2)
print (result1)



       
 
