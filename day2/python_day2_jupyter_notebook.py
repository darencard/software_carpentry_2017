
# coding: utf-8

# In[4]:

# create a new function to calculate fahrenheit by celsius
def celsius_fahrenheit():
    # F = (C * 9/5) + 32
    fahrenheit = (22 * (9 / 5)) + 32
    print(fahrenheit)
    return fahrenheit


# In[6]:

# call our new function
celsius_fahrenheit()


# In[7]:

# create a more flexible function that takes an argument of celsius
def celsius_fahrenheit(C):
    # F = (C * 9/5) + 32
    fahrenheit = (C * (9 / 5)) + 32
    return fahrenheit


# In[8]:

# we get an error when no argument is specified
celsius_fahrenheit()


# In[9]:

# We can translate the boiling point in celsius to fahrenheit
celsius_fahrenheit(100)


# In[12]:

# explicitely pass to argument
celsius_fahrenheit(C=100)


# In[17]:

# make a function that converts fahrenheit to celsius
# C = (F - 32) x (5 / 9)
# allow user to specify input fahrenheit
# define a default
def fahrenheit_celsius(F = 10):
    # C = (F - 32) x (5 / 9)
    celsius = (F - 32) * (5 / 9)
    return celsius


# In[18]:

# run function with default of F=10
fahrenheit_celsius()


# In[19]:

# run function but set a new option of F=35
fahr = fahrenheit_celsius(F = 35)


# In[20]:

fahr


# In[21]:

# import pandas
import pandas as pd


# In[22]:

# import data
dem_health_data = pd.read_csv("Dem_Health_Full.txt",
                             sep="\t")


# In[24]:

# top of dataframe
dem_health_data.head(20)


# In[25]:

# let's create a function that returns a dataframe of only urban counties
# urban being defined as county with population density greater than 1000
def get_urban(df):
    urban = df.loc[df['Population_Density'] >= 1000, 
                   :]
    return urban


# In[26]:

# run command and store to variable
urban_counties = get_urban(dem_health_data)


# In[28]:

# look at results
urban_counties.head()


# In[29]:

# create a more flexible function that allows user to set a threshold
def get_urban(df, threshold):
    urban = df.loc[df['Population_Density'] >= threshold, 
                   :]
    return urban


# In[30]:

# run function with an 'urban threshold' of 500
urban_counties = get_urban(dem_health_data, 500)


# In[31]:

# look at results
urban_counties.head()


# In[32]:

# finally, print a function that returns both urban and rural counties
# based on a user-defined threshold
# these two dataframes are returned in a single list
def split_county_by_pop(df, threshold):
    urban = df.loc[df['Population_Density'] >= threshold, 
                   :]
    rural = df.loc[df['Population_Density'] < threshold, 
                   :]
    return [urban, rural]


# In[33]:

# run the command
urban_rural_counties = split_county_by_pop(dem_health_data, 500)


# In[51]:

# we get an error because a list doesn't have a 'head' like a dataframe does
urban_rural_counties.head()


# In[53]:

# we need to excise the dataframe from the list to look at its head
# let's extract first dataframe (urban counties)
# notice that first element is 0, as Python is 0-based/0-indexed
urban_rural_counties[0].head()


# In[42]:

# calculate the minimum of a given dataframe
urban_rural_counties[1].min()


# In[57]:

# look at shape of dataframe (rows, columns)
urban_rural_counties[0].shape


# In[58]:

################################################################
################### Python Visualization #######################
################################################################


# In[59]:

# Pygal return SVG images we need to import SVG to display them
from IPython.display import SVG


# In[60]:

# importing pandas
import pandas as pd
# importing pygal
import pygal


# In[97]:

# I'm reading data into a variable called 'dem_health_data'
dem_health_data = pd.read_csv('Dem_Health_Full.txt', sep='\t')


# In[62]:

# look at the top of the dataframe
dem_health_data.head()


# In[63]:

# get help on a given Python object
# remember, Python is 'object oriented' and works on data types known as objects
help(dem_health_data)


# In[64]:

# can also look at what commands are available for an object
dir(dem_health_data)


# In[65]:

# subset data to pull out specific column
dem_health_data['State']


# In[66]:

# if we want more than one column, can't specify like this
dem_health_data['State', 'Poverty']


# In[67]:

# instead we need to give them as a list
dem_health_data[['State', 'Poverty']]


# In[68]:

# use 'loc' to excise certain columns/rows
# index (like x-/y- coordinates) are within []
# format [row, column]
# here we extract all columns (:) of the first row (0)
dem_health_data.loc[0, :]


# In[69]:

# or we can exract certain columns by providing them as a list as 2nd element
dem_health_data.loc[0, ['Population_Density','Poverty']]


# In[70]:

# or we can use 'iloc' to use index numbers instead of names
# first value is inclusive and 2nd value is exclusive
# columns 2-4 of row 1
dem_health_data.iloc[0, 2:4]


# In[78]:

# let's extract all rows from AL and TX
# '|' means 'or'
# each test must be in ()
dem_health_data[(dem_health_data['State']=='AL') | (dem_health_data['State']=='TX')]


# In[87]:

# cleaning the data by removing missing/bad values
# there is an undefined infant mortality in the following county
dem_health_data.iloc[3126]
# now we can replace it with 0, doing it in place
dem_health_data.fillna(0, inplace=True)
# check result
dem_health_data.iloc[3126]


# In[88]:

# or save it to new variable and don't replace 'in place'
dem_health_data_fix = dem_health_data.fillna(0)
# and check
dem_health_data_fix.iloc[3126]


# In[89]:

# cleaning suicide rate values (e.g., -1111.1)
# notice weird value in the 6th row
dem_health_data.head(6)


# In[100]:

# replace -1111.1 with 0
dem_health_data['Suicide'].replace(-1111.1, 0, inplace=True)
# check the result and see difference
dem_health_data.head(6)


# In[101]:

# or you can always write it to a new column in your dataframe called 'Suicide_fix'
# save a dummy dataset to test on
dem_health_data_fix = dem_health_data
# do the replacement
dem_health_data_fix['Suicide_fix'] = dem_health_data['Suicide'].replace(-1111.1, 0)
# check result, and notice new, fixed column
dem_health_data_fix.head(6)


# In[104]:

# lets review data structure
# tuples are surrounded by ()
a_tuple = (1, 2)
# lists are surrounded by []
a_list = [1, 2]
# can also nest tuple inside list
nested_list = [(1, 2), (3, 4)]


# In[106]:

# let's create our first plot
# correlate population density and poverty rate in the state of Alabama
# first need to subset our dataset and get the data we want
data_for_al = dem_health_data.loc[dem_health_data['State'] == 'AL',                                  ['Population_Density', 'Poverty']]


# In[110]:

# in order to plot with pygal, we need to supply our data point as a tuple
# for example, (x-coord, y-coord)
# if we have multiple data points, we have to supply them as a list
# we can use a fancy for loop in python to do this automatically
lst = [tuple(x) for x in data_for_al.values]
# look at first 10 values
lst[1:10]


# In[113]:

# or to translate this to a more conventional for loop command
# the version above is what we commonly refer to as 'pythonic' and most languages handle for loops as follows
list = []
for value in data_for_al.values:
    list.append(tuple(value))
list[1:10]


# In[115]:

# create our scatter plot
# initiatlize a pygal scatter plot object
scatter_plot = pygal.XY(stroke=False)
# add data points to the plot by passing the list of tuples we created
# and defining that as the legend element 'AL' for Alabama
scatter_plot.add('AL', lst)
# then, in order to render the SVG so we can see it, we do
SVG(scatter_plot.render())


# In[116]:

# let's add a plot to the title (note new line)
scatter_plot = pygal.XY(stroke=False)
scatter_plot.title = 'Population Density vs. Poverty Correlation'
scatter_plot.add('AL', lst)
SVG(scatter_plot.render())


# In[117]:

# and some x and y axis labels
scatter_plot = pygal.XY(stroke=False,                         x_title='Population Density',                         y_title='Poverty Rate')
scatter_plot.title = 'Population Density vs. Poverty Correlation'
scatter_plot.add('AL', lst)
SVG(scatter_plot.render())


# In[118]:

# Challenge:
# Parse population and poverty data for any state and put it into a nested list of tuples
# for Texas
data_for_tx = dem_health_data.loc[dem_health_data['State'] == 'TX',                                   ['Population_Density','Poverty']]
data_for_tx.head()


# In[119]:

# create the list of tuples for plotting
lst2 = [tuple(x) for x in data_for_tx.values]


# In[120]:

# Let us create a TX plot, like that above
scatter_plot = pygal.XY(stroke=False, x_title='Population Density', y_title='Poverty')
scatter_plot.title = 'Population Density vs Poverty Corelation'
scatter_plot.add('TX', lst2)
SVG(scatter_plot.render())


# In[121]:

# we can also add two sets of data from different states to same plot
scatter_plot = pygal.XY(stroke=False, x_title='Population Density', y_title='Poverty')
scatter_plot.title = 'Population Density vs Poverty Corelation'
scatter_plot.add('AL', lst)
scatter_plot.add('TX', lst2)
SVG(scatter_plot.render())


# In[122]:

# to change axes labels, we must understand for loops
# here is an example
for i in range(0, 6):
    print(i)


# In[123]:

# or you can specify a 3rd argument to range that steps by 2
for i in range(0, 10, 2):
    print(i)


# In[125]:

# let's use this principle to supply a tuple of x-axis labels to our scatter plot object
scatter_plot = pygal.XY(stroke=False, x_title='Population Density', y_title='Poverty', min_scale=10)
scatter_plot.title = 'Population Density vs Poverty Corelation'
# creates labels from 0 to 3000, by 100s
scatter_plot.x_labels = (i for i in range (0, 3000, 100))
scatter_plot.add('AL', lst)
scatter_plot.add('TX', lst2)
SVG(scatter_plot.render())


# In[126]:

# they are a bit smooshed, so we can modify the number of labels by varying the step
scatter_plot = pygal.XY(stroke=False, x_title='Population Density', y_title='Poverty', min_scale=10)
scatter_plot.title = 'Population Density vs Poverty Corelation'
# creates labels from 0 to 3000, by *200s*
scatter_plot.x_labels = (i for i in range (0, 3000, 200))
scatter_plot.add('AL', lst)
scatter_plot.add('TX', lst2)
SVG(scatter_plot.render())


# In[127]:

# or we can constrain our plot so it only looks at a certain range of values
# note xrange option on 1st line where a tuple of the endpoints was specified
scatter_plot = pygal.XY(stroke=False, x_title='Population Density',                         y_title='Poverty', min_scale=10, xrange=(0,200))
scatter_plot.title = 'Population Density vs Poverty Corelation'
scatter_plot.add('AL', lst)
scatter_plot.add('TX', lst2)
SVG(scatter_plot.render())


# In[128]:

# we can also adjust the size of the points
scatter_plot = pygal.XY(stroke=False, x_title='Population Density',                         y_title='Poverty', min_scale=10, dots_size=2)
scatter_plot.title = 'Population Density vs Poverty Corelation'
scatter_plot.x_labels = (i for i in range (0, 3000, 200))
scatter_plot.add('AL', lst)
scatter_plot.add('TX', lst2)
SVG(scatter_plot.render())


# In[131]:

# you can also use themes that people have created
from pygal.style import NeonStyle
scatter_plot = pygal.XY(stroke=False, x_title='Population Density',                         y_title='Poverty', xrange=(0,100), dots_size=2,                         style=NeonStyle, fill=True)
scatter_plot.title = 'Population Density vs Poverty Corelation'
scatter_plot.add('AL', lst)
scatter_plot.add('TX', lst2)
SVG(scatter_plot.render())


# In[138]:

# let's work with another type of plot, bar plots
# however, we need average values for each state in this context
# here is how we can get the average of poverty for Alabama
al = dem_health_data.loc[dem_health_data['State'] == 'AL', ['Poverty']]
poverty_mean_al = al['Poverty'].mean()
poverty_mean_al


# In[170]:

# let's generalize this and make it into a function so we can calculate 
# the mean of a column for any state
def mean_of_column(state_name, column_name):
    state_df = dem_health_data.loc[dem_health_data['State'] == state_name,                                    [column_name]]
    return state_df[column_name].mean()
# usage example: mean_of_column('TX', 'Poverty')


# In[171]:

# now we can test this
mean_of_column('TX', 'Poverty')


# In[174]:

# now we can use this function in the context of our new plot
# this plot makes vertical bars
bar_chart = pygal.Bar()
bar_chart.title = 'Mean of Poverty per State'
# this for loop calculates the mean poverty in each state and adds
# it to the plot
for state in dem_health_data['State'].unique():
    bar_chart.add(state, mean_of_column(state, 'Poverty'))
SVG(bar_chart.render())


# In[188]:

# make it a horizontal bar plot instead
line_chart = pygal.HorizontalBar()
for state in dem_health_data['State'].unique():
    line_chart.add(state,mean_of_column(state,'Poverty'))
SVG(line_chart.render())


# In[189]:

# but that legend sucks; let's move it to the bottom so everything is displayed
line_chart = pygal.HorizontalBar(legend_box_size=10,                                  legend_at_bottom=True,                                  legend_at_bottom_columns=11)
for state in dem_health_data['State'].unique():
    line_chart.add(state,mean_of_column(state,'Poverty'))
SVG(line_chart.render())


# In[ ]:



