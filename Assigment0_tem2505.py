import pandas as pd
import matplotlib.pyplot as plt
#open the file 
df = pd.read_csv('heart.csv')

#verify that the file imported corectly 
#print(df.head())
#print(df.tail())

#Calculate the minimum value
min_value = df.min()

#print(min_value)

#Calculate the mean of each feature
mean_values =df.mean(numeric_only=True)

#Store the mean values in a dictionary
mean_dict = mean_values.to_dict()

# Find the feature with the highest mean
max_feature = max(mean_dict, key=mean_dict.get)
max_value = mean_dict[max_feature]

#print("Mean values for each feature:", mean_dict)
#print(f"The feature with the highest mean is '{max_feature}' with a mean value of {max_value}.")

#select only the columns with numerical data types( in this case all collums have numerical data types)
numeric_features = df.select_dtypes(include='number')
#identify and store the columns with at lest 10 unique values
features_unique = [col for col in numeric_features.columns if df[col].nunique() >= 10]

std_values = numeric_features[features_unique].std()

cont_features_std_ascend = std_values.sort_values()

#print("Standard deviations of continuous features with at least 10 unique values (ascending order):")
#print(cont_features_std_ascend)

#Shuffle the dataframe
shuffled_df = df.sample(frac=1).reset_index(drop=True)

#Calculate the index for the 70% split
split_index = int(len(shuffled_df) * 0.7)

#Split the DataFrame 
df_70 = shuffled_df.iloc[:split_index]  # First 70% of the samples
df_30 = shuffled_df.iloc[split_index:]  # Remaining 30% of the samples

#Iinclude only samples where HeartDisease = 1
df_70_heart_disease = df_70[df_70['hasHeartDisease'] == 1]
df_30_heart_disease = df_30[df_30['hasHeartDisease'] == 1]

#Save the filtered DataFrames to CSV files
df_70_heart_disease.to_csv('70_percent_heart_disease.csv', index=False)
df_30_heart_disease.to_csv('30_percent_heart_disease.csv', index=False)

#print("CSV files created with only HeartDisease = 1 samples:")
#print("70_percent_heart_disease.csv' for the first 70% of the data")
#print("30_percent_heart_disease.csv' for the remaining 30% of the data")


def my_plot_func(feature1, feature2=None, action='scatter-plot'):
    #A function that creates a plot based on the action 
    x_label = feature1.name if hasattr(feature1, 'name') and feature1.name else 'Feature 1'
    y_label = feature2.name if feature2 is not None and hasattr(feature2, 'name') and feature2.name else 'Feature 2'
    if action == 'scatter-plot':
        if feature2 is not None:
            plt.figure(figsize=(8, 6))
            plt.scatter(feature1, feature2, alpha=0.7)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title('Scatter Plot of :' + feature1.name+ " and " + feature2.name)
            plt.grid(True)
            plt.show()
        else : 
            print("For a scater plot I need both fatures")
    elif action == 'line':
        if feature2 is not None:
            plt.figure(figsize=(8, 6))
            plt.plot(feature1, feature2, marker='o')
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title('Line Plot of '+ x_label+ " and " + y_label)
            plt.grid(True)
            plt.show()
        else:
            print("For a line plot I need both features")
    elif action == 'histogram':
        plt.figure(figsize=(8, 6))
        plt.hist(feature1, bins=20, alpha=0.7)
        plt.xlabel(x_label)
        plt.ylabel("None")
        plt.title('Histogram of :'+ feature1.name)
        plt.grid(True)
        plt.show()

    else:
        print("Please choose 'scatter-plot', 'line', or 'histogram'.")

#scatter plot with the feature age on the x-axis and the feature hasHeart
age = df['age']
has_heart_disease = df['hasHeartDisease']
#my_plot_func(age, has_heart_disease, action='scatter-plot')

#a scatter plot of two new features: F1 = trestbp −chol and F2 =agesex +1
F1= df['trestbps'] - df['chol']
F2=(df['age'] ** df['sex'])+ 1
F1.name='trestbps - chol'
F2.name='age^sex + 1'
#my_plot_func(F1, F2, action='scatter-plot')

#Calculate the mean of the unique features and find the highest of them then we create the histogram
mean_values = df[features_unique].mean()
mean_dict = mean_values.to_dict()
max_feature = max(mean_dict, key=mean_dict.get)
feature_data = df[max_feature]
#my_plot_func(feature_data, None, action='histogram')

#Create a line plot using the cont features std ascend variable
#my_plot_func(cont_features_std_ascend.index, cont_features_std_ascend.values, action='line')
