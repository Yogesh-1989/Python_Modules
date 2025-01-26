#import matplotlib.pyplot as pyplot

import matplotlib
from matplotlib import pyplot

labels = ("python", "Java", "Go Lang", "C++", "Rust", "Javascript", "C")
sizes = [30,20,10,5,10,10,15]

pyplot.pie(sizes, labels=labels, autopct = '%1.f%%',
           counterclock=False, startangle=100)

pyplot.show()