lixo = input();
entrada = [int(i) for i in input().split()];
#print(entrada);

#using recursive implementation of merge sort
def mergesort(left, right):
    result = [];
    count = 0;
    i= 0;
    j= 0;
    len_left = len(left);
    while i < len_left and j < len(right):
        # Have to change append for alocation, but no time
        if left[i] <= right[j]:
            result.append(left[i]);
            i += 1;
        else:
        # Have to change append for alocation, but no time
            result.append(right[j]);
            count += len_left - i;
            j += 1;
        #print(left, right)
    result += left[i:];
    result += right[j:];
    return result, count;

# First
def inversoes(array):
    if len(array) <= 1:
        return array, 0;
    #
    mid = int(len(array) / 2);
    temp1 = inversoes(array[:mid]);
    left = temp1[0];
    count1 = temp1[1];
    #
    temp2 = inversoes(array[mid:]);
    count2 = temp2[1];
    right = temp2[0];
    #
    #count1 = int(inversoes(array[:mid])[1]);
    temp3 = mergesort(left, right);
    result = temp3[0];
    count3 = temp3[1];
    return result, (count1 + count2 + count3);


print(inversoes(entrada)[1]);
'''
15
5 8 15 12 2 1 9 7 4 11 14 10 3 6 13
'''
