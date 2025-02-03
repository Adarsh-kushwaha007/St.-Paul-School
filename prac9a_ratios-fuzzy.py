from fuzzywuzzy import fuzz
from fuzzywuzzy import process

s1="I love fuzzysforfuzzys"
s2="I am loving fuzzysforfuzzys"
print("FuzzyWuzzy Ratio:",fuzz.ratio(s1,s2))
print("FuzzyWuzzyPartial Ratio:",fuzz.partial_ratio(s1,s2))
print("FuzzyWuzzyTokenSort Ratio:",fuzz.token_sort_ratio(s1,s2))
print("FuzzyWuzzyTokenSet Ratio:",fuzz.token_set_ratio(s1,s2))
print ("FuzzyWuzzyWRatio: ", fuzz.WRatio(s1, s2),'\n\n')

#for process library
query="fuzzy for fuzzys"
choices=['fuzzy for fuzzy','fuzzy fuzzy','g.for fuzzys']
print("List of ratios:")
print(process.extract(query,choices),'\n')
print("Best among the above list:",process.extractOne(query,choices))
