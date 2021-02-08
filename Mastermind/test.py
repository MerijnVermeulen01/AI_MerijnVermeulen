lst = [1, 3, 5, 6]
new_lst = [3, 1, 3, 2]
def feedbackTest(lst, new_lst):
    newLST = []
    count = 0
    lst.sort()
    new_lst.sort()
    print(lst)
    print(new_lst)
    for i in lst:
        if lst[count] == new_lst[count]:
            newLST.append(lst[count])
        count += 1

    print('Je hebt de ' + str(len(newLST)) + ' goed maar niet op de goede plek')


feedbackTest(lst, new_lst)