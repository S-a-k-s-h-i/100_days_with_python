def Result_List(original_l,remove_e):
    for i in remove_e:
       if i in original_l:
          original_l.remove(i)
    print("New_List = ",original_l)

original_list=[int(x) for x in input().split()]
remove_elements=[int(x) for x in input('Remove: ').split()]
Result_List(original_list,remove_elements)