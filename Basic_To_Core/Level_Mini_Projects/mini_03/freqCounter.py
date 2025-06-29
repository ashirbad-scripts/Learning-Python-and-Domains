from collections import Counter

def wordCounter(filename):
    try:
        with open(filename, "r") as f:
            text = f.read().lower()
            words = text.split()
            wordCount = Counter(words)

        print(f"Word frequency in {filename}")
        for eachWord, count in wordCount.items():
            print(f"{eachWord} - {count}")
    
    except FileNotFoundError as e:
        print("Error message", e)

wordCounter("Level_11 (Mini_Projects)/mini_03/demo.txt")