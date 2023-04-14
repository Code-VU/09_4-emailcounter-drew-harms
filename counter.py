def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
