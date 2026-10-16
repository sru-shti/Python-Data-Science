di={1:'Python',2:'Java',3:'C++'}

di.clear()
di2 = di.copy()
print(di.get(4))                                      # None
print(di.get(4 ,"keys not present"))                  # keys not present  
print(di.items())                                     # dict_items([(1, 'Python'), (2, 'Java'), (3, 'C++')])
print(di.keys())                                      # dict_keys([1, 2, 3])
di.pop(2)                                             # {1: 'Python', 3: 'C++'}

di.popitem()                                          # {1: 'Python', 2: 'Java'}

di.update({4: 'PHP',5:"Javascript"})                  # {1: 'Python', 2: 'Java', 3: 'C++', 4: 'PHP', 5: 'Javascript'}

print(di.values())                                    # dict_values(['Python', 'Java', 'C++'])