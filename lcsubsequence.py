 
def lcs(X , Y):

    m = len(X)
    n = len(Y)

    string = ""

    L = [[None]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
                string = string + X[i-1]
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    # return L[m][n]
    return string

X = raw_input("Enter the 1st string: ")
Y = raw_input("Enter the 2nd string: ")

print "\nLength of Longest Common Subsequence:", len(lcs(X, Y))
print "Longest Common Subsequence: ", lcs(X, Y)