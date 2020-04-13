# As you cycle through each line output the number of
# words and average word length

# wrtie on a file
with open("mydata.txt", mode="w", encoding="utf-8") as myfile:
    
    myfile.write("Hello World\nNeel Patel\nFresno, California\n")
 
# read individual lines from a file
with open("mydata.txt", encoding="utf-8") as myfile:
    
    line_num = 1
    
    # loop unitl line ends
    while True:
        
        # read each line 
        data = myfile.readline()
        
        sum_words = 0
        # split the string and save it in a new list
        word_list = data.split()
        lent_word = len(word_list)
        
        # count each character in the line
        for i in data:
            
            if i.isalpha():
                sum_words += 1

            
        # if line doesn't return data, breal the loop
        if not data:
            break
        
        print("Line Number ", line_num, ":", data, end="")
        print("No. of words: ", lent_word)
        print("Average Number of Words: {:.2f}".format(sum_words/lent_word))
        print("")
        
        line_num += 1
        
