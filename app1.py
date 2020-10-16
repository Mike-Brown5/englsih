import json
import difflib
# load the data from the json file
data = json.load(open("data.json"))


def define(word):
    # getting a close match to the input
    diff = difflib.get_close_matches(word,data.keys())

    #checking the input and defining the output
    if word in data:
        return data[word]
    elif len(diff) > 0:
        use = input(f"Did you mean {diff[0]}. Type (Y) for yes (N) no: ")
        if((use == "Y") | (use == "y")):
            return data[diff[0]]
        else:
            use = input(f"Did you mean {diff[1]}. Type (Y) for yes (N) no: ")
            if((use == "Y") | (use == "y")):
                return data[diff[1]]
            else:
                use = input(f"Did you mean {diff[2]}. Type (Y) for yes (N) no: ")
                if((use == "Y") | (use == "y")):
                    return data[diff[2]]
                else:
                    return "Sorry can't find your word. Please double check it."
    else:
        return "Sorry can't find your word. Please double check it."

while True:
    user = input("Enter a word ('\z' to end): ")
    out = define(user.lower())
    if( (user == "\z") | (user == "\Z")):
        break
    elif type(out) == list:
        # iterating over the output list and print its element
        for i in out:
            print("-",i)
    else:
        print("-",out)