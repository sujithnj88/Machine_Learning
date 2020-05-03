import matplotlib.pyplot as plt

Rohit_T20 = {'Mat': 108, 'Inn': 100, 'NO': 14, 'Runs': 2773, 'HS': 118, 'Avg': 32.24, 'BF': 1998, 'SR': 138.79,
             '100_s': 4, '200_s': 0, '50_s': 21, '4_s': 245, '6_s': 127}
ABD_T20 = {'Mat': 78, 'Inn': 75, 'NO': 11, 'Runs': 1672, 'HS': 79, 'Avg': 26.12, 'BF': 1237, 'SR': 135.17,
           '100_s': 0, '200_s': 0, '50_s': 10, '4_s': 140, '6_s': 60}

T20_Rohit_Runs_per_Ball = Rohit_T20['Runs'] / Rohit_T20['BF']
T20_ABD_Runs_per_Ball = ABD_T20['Runs'] / ABD_T20['BF']

try:
    T20_Rohit_Cen_per_Match = Rohit_T20['Mat'] / Rohit_T20['100_s']
except:
    T20_ABD_Cen_per_Match = 0
try:
    T20_ABD_Cen_per_Match = ABD_T20['Mat'] / ABD_T20['100_s']
except:
    T20_ABD_Cen_per_Match = 0

try:
    T20_Rohit_Half_Cen_per_Match = Rohit_T20['Mat'] / Rohit_T20['50_s']
except:
    T20_Rohit_Half_Cen_per_Match = 0
try:
    T20_ABD_Half_Cen_per_Match = ABD_T20['Mat'] / ABD_T20['50_s']
except:
    T20_ABD_Half_Cen_per_Match = 0
print(T20_Rohit_Half_Cen_per_Match)
print(T20_ABD_Half_Cen_per_Match)

try:
    T20_Rohit_Double_Cen_per_Match = Rohit_T20['Mat'] / Rohit_T20['200_s']
except:
    T20_ABD_Double_Cen_per_Match = 0
try:
    T20_ABD_Double_Cen_per_Match = ABD_T20['Mat'] / ABD_T20['200_s']
    print(T20_ABD_Double_Cen_per_Match)
except:
    T20_ABD_Double_Cen_per_Match = 0

try:
    T20_Rohit_Fours_per_Match = Rohit_T20['Mat'] / Rohit_T20['4_s']
except:
    T20_Rohit_Fours_per_Match = 0
try:
    T20_ABD_Fours_per_Match = ABD_T20['Mat'] / ABD_T20['4_s']
except:
    T20_ABD_Fours_per_Match = 0

try:
    T20_Rohit_Six_per_Match = Rohit_T20['Mat'] / Rohit_T20['6_s']
except:
    print('Rohit    :   No Fours')
try:
    T20_ABD_Six_per_Match = ABD_T20['Mat'] / ABD_T20['6_s']
except:
    T20_ABD_Six_per_Match = 0

x = Rohit_T20.keys()
ax = plt.subplot(111)
w = 0.3
multipler = 0
for i in x:
    print(i,Rohit_T20[i])
    ax.bar(multipler*w, [Rohit_T20[i], ABD_T20[i]], width=w, color='b', align='center')
    multipler += 1
    ax.autoscale(tight=True)
plt.savefig('FIg_Test.png')