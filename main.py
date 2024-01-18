# Importing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Function to load data from a CSV file
def load_custom_data(file_path):
    """
    Loads data from a CSV file and returns a Pandas DataFrame.
    Args:
        file_path (str): The path of the CSV file to load.
    """
    df = pd.read_csv(file_path)
    return df

# Define a function to plot a line plot with multiple lines
def custom_line_chart(data, x_vals, y_vals_list, labels, chart_title, x_label, y_label):
    fig, ax = plt.subplots()

    # Plotting lines for each set of y-values
    for i, y_vals in enumerate(y_vals_list):
        ax.plot(data[x_vals], data[y_vals], label=labels[i])

    # Setting title and labels
    ax.set_title(chart_title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Setting legend
    ax.legend()

    # Saving the figure
    plt.savefig('custom_line_chart.png', dpi=300)

    # Displaying the plot
    plt.show()

# Define a function to plot a bar chart
def custom_bar_chart(data, x_vals, y_val, chart_title, x_label, y_label):
    fig, ax = plt.subplots()

    ax.bar(data[x_vals], data[y_val])

    # Setting title and labels
    ax.set_title(chart_title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Saving the figure
    plt.savefig('custom_bar_chart.png', dpi=300)

    # Displaying the plot
    plt.show()

# Define a function to plot a scatter plot
def custom_scatter_chart(data, x_vals, y_val, chart_title, x_label, y_label, marker_style, color_code):
    fig, ax = plt.subplots()

    ax.scatter(data[x_vals], data[y_val], marker=marker_style, color=color_code)

    # Setting title and labels
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(chart_title)

    # Saving the figure
    plt.savefig('custom_scatter_chart.png', dpi=300)

    # Displaying the plot
    plt.show()

# Loading custom data
crime_custom_data = load_custom_data("Custom_Crime_Data.csv")
os_custom_data = load_custom_data("custom_os_data_2023.csv")
income_custom_data = load_custom_data("custom_income_data.csv")

# Plotting a line chart with multiple lines
custom_line_chart(
    data=crime_custom_data,
    x_vals="Year",
    y_vals_list=["Violent","Property","Murder","Robbery","Burglary","Vehicle_Theft"],
    labels=["Violent","Property","Murder","Robbery","Burglary","Vehicle Theft"],
    chart_title="Total Crime over the Years",
    x_label="Year",
    y_label="Amount in Hundred Thousand",
)

# Plotting a bar chart
custom_bar_chart(
    data=os_custom_data,
    x_vals="Month",
    y_val="Windows",
    chart_title="Windows Market Share through 2023",
    x_label="Months of 2023",
    y_label="Percentage Market Share",
)

# Plotting a scatter chart
custom_scatter_chart(
    data=income_custom_data,
    x_vals='age',
    y_val='hours-per-week',
    chart_title='Hours worked by Age',
    x_label='Age',
    y_label='Hours per Week',
    marker_style='.',
    color_code='blue'
)


"""Summary

The three visualization methods used in this code are:

* Line plot: To show how multiple variables change over time.
* Bar plot: To compare the values of a variable across different categories.
* Pie chart: To show the distribution of a variable.

Data References

#Links 1- US_Crime_Rates_1960_2014 on #kaggle via @KaggleDatasets https://www.kaggle.com/datasets/mahmoudshogaa/us-crime-rates-1960-2014?utm_medium=social&utm_campaign=kaggle-dataset-share&utm_source=twitter 
#Links 2- American Citizens Annual Income on #kaggle via @KaggleDatasets https://www.kaggle.com/datasets/amirhosseinmirzaie/americancitizenincome?utm_medium=social&utm_campaign=kaggle-dataset-share&utm_source=twitter 
#Links 3- https://gs.statcounter.com/os-market-share#monthly-202301-202310 This work by Statcounter is licensed under a Creative Commons Attribution-Share Alike 3.0 Unported License 

"""
