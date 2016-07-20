infile = open('football.dat')
line_data_dic = {}
min_diff = 0
next(infile) #first row is the header, not contains data, jump it
for line in infile: # start to read row by row the footbal.dat file
    if line.rstrip():
        parts = line.split()
        if "--" in parts[0]: # if find - sign in file exit from loop
            break
        else:
            diffs = int(parts[6])-int(parts[8]) # start to calculate the results
            if min_diff < diffs: # check the result
                min_diff = diffs
                min_diff_line = str(parts[1])
line_data_dic[min_diff_line] = min_diff
for key in line_data_dic.keys(): #remove the brackets for print the result
    print ('Smallest difference at', (key),'team')
