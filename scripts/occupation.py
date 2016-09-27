import random
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")
def read_csv(filename):
    with open(filename, 'r') as f:
        pairs = f.readlines()
    pair_dict = {}
    for i in pairs:
        pair = i.strip()
        if i[0] == '"':
            comma_index = pair.find('"', 1) + 1
            key = pair[1:comma_index - 1]
        else:
            comma_index = pair.find(',')
            key = pair[:comma_index]
        val = pair[comma_index + 1:]
        if ((key != 'Job Class') & (val != 'Job Class')):
            pair_dict[key] = val
    return pair_dict


@app.route('/occupations')
def randomOccupation():
    occupations = read_csv("data/occupations.csv")
    #print (occupations)
    keys = occupations.keys()
    values = [occupations[i] for i in keys]
    randomInt = random.uniform(0.0,99.8)
    dictIterator = 0
    dictTotal = 0
    while (dictIterator < len(keys) - 1):
        if ((values[dictIterator] != '99.8') & (values[dictIterator] != 'Percentage') & (keys[dictIterator] != 'Job Class')):
            dictTotal += float(values[dictIterator])
            dictIterator += 1
            #print (dictTotal)
        else:
            dictIterator += 1
        if (randomInt < dictTotal):
            return {'occupation':keys[dictIterator - 1], 'table':zip(keys, values)}


if __name__ == '__main__':
    app.run()



















##def randomOccupation():
##    randomInt = random.uniform(0.0,99.8)
##    randomInt = 0.7
##    dictIterator = 0
##    dictTotal = 0
##    while (dictIterator < len(occupations) - 1):
##        if ((occupations.values() [dictIterator] != '99.8') & (occupations.values() [dictIterator] != 'Percentage')):
##            dictTotal += float( occupations.values() [dictIterator] [0: len(occupations.values() [dictIterator])])
##            dictIterator += 1
##            print (dictTotal)
##        else:
##            dictIterator += 1
##        if (randomInt < dictTotal):
##            print ("Your random occupation is: " + occupations.keys().index([occupations.values().index(occupations.values()[dictIterator - 1])]) + ".")
##            #return (occupations.keys()[occupations.values().index(occupations.values()[dictIterator])])
