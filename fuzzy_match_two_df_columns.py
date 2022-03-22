from fuzzywuzzy import fuzz

#difference between two df columns 
def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

l1 = list(df['one_thing'].unique())
l2 = list(df_2['same_thing'].unique())

def Diff1(li1, li2): #in df but not df2
    li_dif = [i for i in li1 + li2 if i not in li1]
    return li_dif

def Diff2(li1, li2): #in df2 but not df
    li_dif = [i for i in li1 + li2 if i not in li2]
    return li_dif

diff1 = Diff1(l1, l2)
diff2 = Diff2(l1, l2)

tuples_list = [max([(fuzz.token_set_ratio(i,j),j) for j in diff2]) for i in diff1]

similarity_score, fuzzy_match = map(list,zip(*tuples_list))

pd.DataFrame({"list_A":diff1, "fuzzy match": fuzzy_match, "similarity score":similarity_score})
