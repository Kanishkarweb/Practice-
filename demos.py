#add,update,remove,len ,pop,union,set,del,clear-->set
# st = {'item1', 'item2', 'item3', 'item4'}
# st.add('item7')
# st.update(['item5','item6','item7'])
# st.remove('item2')
# print(st.pop())
# # st.clear()
# # del st
# print(st)
# lst = ['item1', 'item2', 'item3', 'item4', 'item1']
# st = set(lst)
# print(st)
st1 = {'item1', 'item2', 'item3', 'item4',"item4"}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)
