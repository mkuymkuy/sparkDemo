def splitCols(saleRow):
    '''this function will split a string with '. Some columns are quoted with
    "". So we need to handle it'''
    saleRow = saleRow.split(',')
    result = []
    flag = True # if flag is false, the current i is within a pair of "
    for i in range(len(saleRow)):
        if flag:
            result.append(saleRow[i])
            if '"' in saleRow[i]:
                flag = False
        else:
            result[-1] = result[-1] + saleRow[i]
            if '"' in saleRow[i]:
                flag = True
    return result
