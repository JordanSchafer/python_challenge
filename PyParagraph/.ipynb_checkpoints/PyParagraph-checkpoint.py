#import dependencies
import os

letter_count=0
#give file path and file name either paragraph_1.txt or paragraph_2.txt
filepath=os.path.join("raw_data","paragraph_2.txt")

#open file
with open(filepath, "r") as txtfile:
    #read paragraph
    paragraph=txtfile.read()

#count spaces to estimate wordcount +1 to count last word    
word_count=paragraph.count(" ")+1

#use punctuation to estimate sentence count
sent_count=paragraph.count(".")+paragraph.count("?")+paragraph.count("!")

#count all the letters
for char in paragraph:
    if char.isalpha():
        letter_count+=1
#estimate avg letter count
avg_letter=letter_count/word_count

#estimate average sentence length
avg_sent=word_count/sent_count

# printing results to terminal
print("Paragraph Analysis")
print("----------------------------------")
print(f"Approximate Word Count:{ word_count}")
print(f"Approximate Sentence Count:{ sent_count}")
print(f"Average Letter Count:{avg_letter:.2f}")
print(f"Average Sentence Length:{avg_sent:.2f}" )