from flask import Flask, render_template, request

app = Flask(__name__)

# Method for KMP algorithm 
def KMP(pattern, string):
    ls = len(string)
    lp = len(pattern)
    table = prefix(pattern, lp)
    m = 0
    n = 0
    index = []

    while m != ls:
        if string[m] == pattern[n]:
            m = m+1;
            n = n+1;
        else:
            n = table[n-1]
        if n == lp:
            index.append(m-n)
            n = table[n-1]
        elif n == 0:
            m = m+1;
    return index

# Method for the prefix table that summarizes the indices of the pattern 
def prefix(pattern, lp):
    table = [0]*lp
    n = 0
    m = 1
    while (m != lp):
        if pattern[m] == pattern[n]:
            n = n+1;
            table[m] = n
            m = m+1
        elif n != 0:
            n = table[n-1]
        else:
            table[m]=0
            m = m+1
    return table   


@app.route("/",  methods=["GET", "POST"])
def home():
    
    if request.method == "POST":
        
        # Dictionary key that retrieves the pattern from the submit box
        pattern = request.form["pattern"]

        # Convert to uppercase the submitted pattern
        pattern = pattern.upper()

        # Open and convert the text into string sequence
        text_file = open("sequence.txt")
        string = text_file.read()
        text_file.close()

        selected_index = KMP(pattern, string)

        # Count the number of indices that are retrieved from KMP method
        count = 0
        for i in selected_index:
            count += 1
        
        return render_template("home.html", count = count)
        
    return render_template("home.html")


# Run the application on the local server
if __name__ == "__main__":
    app.run(host= "127.0.0.1", debug=True)
