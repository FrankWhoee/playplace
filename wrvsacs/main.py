import math
from sklearn import linear_model
import pyperclip
from bs4 import BeautifulSoup
import numpy

# read data.html and interpret it as html
with open("treeracks_data.html", "r") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")

# find all elements with the class trn-match-row in soup
# this is the class of the table rows that contain the data we want
rows = soup.find_all("div", class_="trn-match-row")

granularity = 30
MAX_ACS = 1000

hist = [[0, 0] for x in range(0, MAX_ACS // granularity + 1)]
games = []
for row in rows:
    acs = row.find_all("div", class_="trn-match-row__block min-w-16")[1].find_all("div", "trn-match-row__text-value")[
        0].text
    acs = int(acs)
    score = row.find_all("div", class_="vmr-score trn-match-row__block gap-1 items-center")[0].find_all("div",
                                                                                                        "trn-match-row__text-value flex flex-row gap-1 items-center")[
        0].text.split(":")
    time = row.find_all("div", class_="trn-match-row__text-label")[0].find_all("span")[0]["data-tooltip-description"]
    score = [int(x) for x in score]
    win = int(score[0]) > int(score[1])
    games.append((acs, win, time))
    acs = acs // granularity
    if win:
        hist[acs][0] += 1
    else:
        hist[acs][1] += 1
print(hist)
rangestring = ""
wrstring = ""

# print the histogram
for i in range(0, len(hist)):
    if hist[i][0] + hist[i][1] > 0:
        rangestring += f"{i*granularity}-{(i+1)*granularity}\n"

for i in range(0, len(hist)):
    if hist[i][0] + hist[i][1] > 0:
        # wrstring += f"{hist[i][0]/(hist[i][0]+hist[i][1])}\n"
        wrstring += f"{(hist[i][0]+hist[i][1])}\n"

# sort games by acs and split it into 10 equally sized groups and print out the winrate for each group
games.sort(key=lambda x: x[0])
print(len(games))
print(games)
data = []
for i in range(0, 10):
    start = math.floor(len(games) * i / 10)
    end = math.floor(len(games) * (i + 1) / 10)
    group = games[start:end]
    wins = 0
    for game in group:
        if game[1]:
            wins += 1
    data.append(((start + end) / 2, wins / len(group)))

# seperate data into x and y
x = numpy.array([d[0] for d in games]).reshape(-1, 1)
y = numpy.array([int(d[1]) for d in games])
# fit a logistic regression model to the data
model = linear_model.LogisticRegression()
model.fit(x, y)

#print model parameters
print(model.coef_)
print(model.intercept_)
print(numpy.exp(model.coef_))

# for g in games:
#     rangestring += f"{g[0]}\n"
#     wrstring += f"{model.predict([[g[0]]])}"

pyperclip.copy(rangestring)
input()
pyperclip.copy(wrstring)
