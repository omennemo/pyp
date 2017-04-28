# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 23:33:32 2017
@filename: 05A-MatPlotLib
@author: cyruslentin
"""

# Anatomy Of A Plot
# The Figure is the overall window or page that everything is drawn on. It’s 
# the top-level component of all the ones that you will consider in the 
# following points. You can create multiple independent Figures. 
# A Figure can have several other things in it, such as a suptitle, which is 
# a centered title to the figure. You’ll also find that you can add a legend 
# and color bar to your Figure.
# Axes - most plotting ocurs on an Axes. The axes is the area on which the 
# data is plotted and that can have ticks, labels, etc. associated with it. 
# This explains why Figures can contain multiple Axes.
# Each Plot has an x-axis and a y-axis, which contain ticks, which have major 
# and minor ticklines and ticklabels. There’s also the axis labels, title, and 
# legend to consider when you want to customize your axes, but also taking into 
# account the axis scales and gridlines might come in handy.
# Spines are lines that connect the axis tick marks and that designate the 
# boundaries of the data area. In other words, they are the simple black 
# square that you get to see when you don’t plot any data at all but when you 
# have initialized the Axes.

# matplotlib
# gallery: http://matplotlib.org/index.html

# import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# prepare the data
x = np.linspace(0, 10, 100)
# plot the data
plt.plot(x, x, label='linear')
# add a legend
plt.legend()
# show the plot
plt.show()


# simple plot
# In this section, we want to draw the cosine and sine functions on the same 
# plot. Starting from the default settings, we'll enrich the figure step by 
# step to make it nicer.
# First step is to get the data for the sine and cosine functions:
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
# prepare data
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C = np.cos(X)
S = np.sin(X)
# prepare plot
plt.plot(X,C)
plt.plot(X,S)
# show plot
plt.show()

# now backto basics
# line chart
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
# prepare plot
plt.plot([1,2,3],[4,5,1])
# show plot
plt.show()

# more of basics
# line chart
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
# prepare data
x = [5,8,10]
y = [12,16,6]
# prepare plot
plt.plot(x,y)
# annotations
plt.title('Graph Title')
plt.xlabel('X axis')
plt.ylabel('Y axis')
# show plot
plt.show()

# style
# line chart
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style  as style
# use style
style.use('ggplot')
# prepare data
x1 = [5,8,10]
y1 = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
# prepare plot
plt.plot(x1,y1,linewidth=5)
plt.plot(x2,y2,linewidth=5)
# annotations
plt.title('Graph Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# show plot
plt.show()

# grid
# line chart
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style  as style
# use style
style.use('ggplot')
# prepare data
x1 = [5,8,10]
y1 = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
# prepare plot
plt.plot(x1,y1,'g', label='line one', linewidth=1, marker = 'D', fillstyle = "left", ls = ':')
plt.plot(x2,y2,'c', label='line two', linewidth=1, marker = 'D', fillstyle = "right", ls = '--')
# annotations
plt.title('Graph Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# show plot
plt.legend()
plt.grid(True,color='k')
plt.show()

# barchart
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style  as style
# use style
style.use('ggplot')
# prepare data
x1 = [5,8,10]
y1 = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
# prepare plot
#plt.bar(x1,y1)
#plt.bar(x2,y2)
#plt.bar(x1,y1,align='center')
#plt.bar(x2,y2,align='center')
plt.bar(x1,y1,align='center',color='b')
plt.bar(x2,y2,align='center',color='b')
#plt.plot(x1,y1)
#plt.plot(x2,y2)
# annotations
plt.title('Graph Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# show plot
plt.show()

# scatter
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style  as style
# use style
style.use('ggplot')
# prepare data
x1 = [5,8,10]
y1 = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
# prepare plot
plt.scatter(x1,y1, label='Group 1')
plt.scatter(x2,y2, label='Group 2')
#plt.scatter(x1,y1,color='b')
#plt.scatter(x2,y2,color='b')
# annotations
plt.title('Graph Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
# show plot
plt.show()

# histogram
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style  as style
# use style
style.use('ggplot')
# prepare data
ages = [22,55,62,15,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
# prepare plot
#plt.hist(ages, bins, histtype='bar', rwidth=1)
#plt.hist(ages, bins, histtype='step', rwidth=1)
plt.hist(ages, bins, histtype='stepfilled', rwidth=1)
# annotations
plt.title('Graph Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.show()

# barchart with string in x-axis
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style  as style
# use style
style.use('ggplot')
# prepare data
x1 = ['00', '01', '02', '03', '04', '05', '11', '12', '13', '14', '15']
y1 = [173, 135, 141, 148, 140, 149, 152, 178, 135, 96]
# prepare plot
plt.bar(range(len(y1)), y1)
plt.xticks(range(len(x1)), x1)
# annotations
plt.title('Graph Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# show plot
plt.show()

# barchart with date in x-axis
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style  as style
import datetime
x1 = [datetime.datetime(2017, 1, 1),
    datetime.datetime(2017, 1, 2),
    datetime.datetime(2017, 1, 3)]
#x1 = [datetime.datetime(2017, 1, 1),
#    datetime.datetime(2017, 2, 1),
#    datetime.datetime(2017, 3, 1)]
y1 = [4, 9, 2]
# prepare plot
plt.bar(x1, y1)
# annotations
plt.title('Graph Title')
plt.xlabel('X axis')
# show plot
plt.show()

# line chart with string in x-axis
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style  as style
# use style
style.use('ggplot')
# prepare data
x1 = ['00', '01', '02', '03', '04', '05', '11', '12', '13', '14', '15']
y1 = [173, 135, 141, 148, 140, 149, 152, 178, 135, 96]
# prepare plot
plt.plot(range(len(y1)), y1)
plt.xticks(range(len(y1)), x1)
# annotations
plt.title('Graph Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# show plot
plt.show()

# line chart with date in x-axis
# import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style  as style
import datetime
# use style
style.use('ggplot')
# prepare data
x1 = [datetime.datetime(2017, 1, 1),
    datetime.datetime(2017, 1, 2),
    datetime.datetime(2017, 1, 3)]
#x1 = [datetime.datetime(2017, 1, 1),
#    datetime.datetime(2017, 2, 1),
#    datetime.datetime(2017, 3, 1)]
y1 = [4, 9, 2]
# prepare plot
plt.plot(x1, y1)
# annotations
plt.title('Graph Title')
plt.xlabel('X axis')
# show plot
plt.show()


# scatter plot using dataframe
# import 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# use style
style.use('ggplot')
# prepare data
# create dataframe
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])
print(df)
# prepare plot
plt.scatter(df.preTestScore, df.postTestScore)
plt.scatter(df.female, df.preTestScore)
# annotation
plt.title('Graph Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# show plot
plt.show()

# line plot using dataframe
# import 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# use style
style.use('ggplot')
# create dataframe
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])
print(df)
# prepare plot
plt.plot(df.preTestScore, df.postTestScore)
# annotation
plt.title('Graph Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# show plot
plt.show()

# bar plot using dataframe
# import 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# use style
style.use('ggplot')
# create dataframe
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])
print(df)
# prepare plot
plt.bar(df.index, df.age)
plt.xticks(df.index, df.first_name)
# annotation
plt.title('Graph Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# show plot
plt.show()

# group bar plot using dataframe
# plot the individual bars & add annotations
# import 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# use style
style.use('ggplot')
# create data frame
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'pre_score': [4, 24, 31, 2, 3],
        'mid_score': [25, 94, 57, 62, 70],
        'post_score': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'pre_score', 'mid_score', 'post_score'])
print(df)
# setting the positions and width for the bars
pos = list(range(len(df['pre_score'])))
width = 0.25
# create a bar with pre_score data, in position pos,
plt.bar(pos,
        #using df['pre_score'] data,
        df['pre_score'],
        # of width
        width,
        # with alpha 0.5
        #alpha=0.5,
        # with color
        color='r',
        # with label the first value in first_name
        label=df['first_name'][0])
# create a bar with mid_score data, in position pos + width,
plt.bar([p + width for p in pos],
        #using df['mid_score'] data,
        df['mid_score'],
        # of width
        width,
        # with alpha 0.5
        #alpha=0.5,
        # with color
        color='g',
        # with label the second value in first_name
        label=df['first_name'][1])
# create a bar with post_score data, in position pos + width * 2
plt.bar([p + width*2 for p in pos],
        #using df['post_score'] data,
        df['post_score'],
        # of width
        width,
        # with alpha 0.5
        #alpha=0.5,
        # with color
        color='b',
        # with label the third value in first_name
        label=df['first_name'][2])
# annotation
plt.title('Test Subject Scores')
plt.ylabel('Scores')
plt.xlabel('Subjects')
# set label for x ticks
plt.xticks(df.index, df.first_name)
# set the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*5)
plt.ylim([0, max(df['pre_score'] + df['mid_score'] + df['post_score'])] )
# adding the legend and showing the plot
plt.legend(['Pre Score', 'Mid Score', 'Post Score'], loc='upper right')
# show grid
plt.grid()
# show plot
plt.show()

