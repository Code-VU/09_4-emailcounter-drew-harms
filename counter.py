def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    counts = dict()
    for line in handle:
        if line.startswith("From "):
           sender = send_line(line)

           counts[sender] = counts.get(sender, 0) + 1

    bigcount = None
    bigword = None
    for word,count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count

    print(bigword, bigcount)

def send_line(line: str) -> str:
    line = line.strip()
    line_list = line.split()
    sender = line_list[1]

    return sender





## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
