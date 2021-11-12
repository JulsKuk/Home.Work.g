m_text = 'один два один два три пять'

dict_t = {}
for w in m_text.split():
    if w in dict_t:
         dict_t[w] = dict_t[w] + 1
    else:
        dict_t [w] = 1
print(dict_t)


