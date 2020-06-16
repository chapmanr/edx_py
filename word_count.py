
from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt

stats = pd.DataFrame(columns=("language","author","title","length","unique"))



def count_words(text):
    text = text.lower()
    skips = [".",",","'",":",'"', ";"]
    for ch in skips:
        text = text.replace(ch,"")

    word_counts = Counter(text.split(" "))
    return word_counts


def count_words_slow(text):
    text = text.lower()
    skips = [".",",","'",":",'"', ";"]
    for ch in skips:
        text = text.replace(ch,"")
        
    word_counts = {}
    for word in text.split(" "):
        if(word in word_counts):
            word_counts[word] += 1
        else:
            word_counts[word]=1
    return word_counts

def read_book(title_path):
    """Read a book and return it as a string"""
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def word_stats(word_counts):
    """Return number of unique words and counts"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

#book_dir = ".Books"
def read_all_books(book_dir):
    title_num = 1
    for language in os.listdir(book_dir):
        for author in os.listdir(book_dir + "/" + language):
            for title in os.listdir(book_dir + "/" + language + "/" + author):
                inputfile = book_dir + "/" + language + "/" + author + "/" + title
                #print(inputfile)
                text = read_book(inputfile)
                (num_unique, counts) = word_stats(count_words(text))
                stats.loc[title_num] = language, author, title, sum(counts), num_unique
                title_num += 1


read_all_books("Books")
print(stats.head())
print(stats.tail())
#plt.plot(stats.length, stats.unique, "bo")
#plt.loglog(stats.length, stats.unique, "bo")

def plotall():
    plt.figure(figsize=(10,10))
    subset = stats[stats.language=="English"]
    plt.loglog(subset.length, subset.unique, "o", label="English", color = "crimson")

    subset = stats[stats.language=="German"]
    plt.loglog(subset.length, subset.unique, "o", label="German", color = "blue")

    subset = stats[stats.language=="French"]
    plt.loglog(subset.length, subset.unique, "o", label="French", color = "green")

    subset = stats[stats.language=="Portuguese"]
    plt.loglog(subset.length, subset.unique, "o", label="Portuguese", color = "yellow")
    plt.legend()
    plt.xlabel("Book Length")
    plt.ylabel("Number of unique words")
    plt.savefig("lang_plot.pdf")
    plt.show()


print(stats.length)

print(stats["length"])
#print(stats[,"length]")

#message = "This comprehension check is to check for comprehension."

#test_dict = count_words(message)
#print(len(test_dict))

#print(count_words(message) is count_words_slow(message))

#title_num = 1
#print(title_num =+ 1)
#print(title_num + 1)

