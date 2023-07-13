def greedy_method(objs,weight,profit_list,total_weight):
    final_list=[]                                                        #This list will contain values from objs list
    extract=[profit_list[i]/weight[i]  for i in range (len(profit_list)) ] #using profit/weight formula
    weight_list=[]                                                         #weight of the selected element
    profit=0
    while total_weight!=0:
        highest=max(extract)
        index=extract.index(highest)
        weight_obj=weight[index]
        if(objs[index]  not in final_list):
            if(weight_obj<= total_weight):
                final_list.append(objs[index])
                total_weight -= weight_obj
                profit+=profit_list[index]*1
                weight_list.append(weight_obj)
                del extract[index],profit_list[index],weight[index],objs[index]
            elif (weight_obj> total_weight):
                weight_list.append(total_weight/weight_obj)
                final_list.append(objs[index])
                profit+=profit_list[index]*(total_weight*weight_obj)
                del extract[index],profit_list[index],weight[index],objs[index]
                break      
    return f"selected elements:{final_list} \n weight:{weight_list} \n profit: {profit}"
objs=[1,2,3,4,5,6,7]
profit_list=[10,5,15,7,6,18,3]
weight=[2,3,5,7,1,4,1]
total_weight=15
print(f"objects: {objs} \n profit:{profit_list} \n weight:{weight}")
print(greedy_method(objs,weight,profit_list,total_weight))