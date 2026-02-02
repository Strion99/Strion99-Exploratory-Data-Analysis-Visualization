# Strion99-Exploratory-Data-Analysis-Visualization
My first module focusing on the most critical step of any data project: Data Manipulation and Visualization. Using Python, Pandas, and Matplotlib, I built a workflow to process raw data and visualize the underlying distributions.

During the course we will be using Python 3. You are
required to install the following packages:
• Pandas
• Numpy
• Matplotlib

1.1 Data Manipulation and Operations using Pandas
The dataset you will be using for this assignment is the “heart.csv” file. It
contains 303 rows and 14 columns where each row represents a patient and each column
a quantity such as age, sex, cholesterol, etc. In machine learning, the columns are often
called features and the rows are called samples.

Perform the following operations using the Pandas library:

1. Read the dataset provided and run the functions head() and tail() to verify that
it was imported correctly.
2. Calculate and report the minimum value of the whole dataframe.
3. Calculate the mean of each feature and store this information in a dictionary
where the keys correspond to the feature names and the values to the mean of
each respective feature. Finally, report the feature name with the highest mean.
4. Calculate the standard deviation of each feature that has at least 10 unique values.
Sort the results in ascending order and store them in a variable with name
cont features std ascend.
5. Permute (shuffle) the dataframe and store the first 70% of the samples in a
dataframe and the remaining 30% in a different dataframe.
6. Save the new dataframes to disk but keep only the samples with the feature has
HeartDisease = 1. Include the two dataframes in your submission folder.

1.2 Visualizations using Matplotlib

Include each plot of this sub-task to your report!

1. Optional: Create a function my plot func(feature1, feature2, action) that takes
two features (feature1, feature2) and a plot type (action) as input. The role of this
function is, as its name implies, to plot data. The first argument feature1 will not
have a default value whereas feature2 will default to the value None. The third
argument action takes three possible string values, namely “scatter-plot”, “line”
or “histogram” and the default value is “scatter-plot”. When action = histogram
you can ignore the value of feature2.
2. Create a scatter plot with the feature age on the x-axis and the feature hasHeart
Disease on the y-axis. Both axes must be labelled.
3. Create a scatter plot of two new features: F1 = trestbps − chol on the x-axis and
F2 =agesex +1 on the y-axis. Both axes must be labelled.
4. Create a histogram of the feature with the highest mean, from the features that
you calculated in the previous task, using 10 bins. Both axes must be labelled.
5. Create a line plot using the cont features std ascend variable computed in Task
1.1.4. Show the feature names on the x-axis and the standard deviation that
corresponds to each feature on the y-axis
