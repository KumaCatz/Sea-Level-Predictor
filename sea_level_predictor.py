import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df)

    # Create scatter plot
    plt.scatter(
        x=df['Year'],
        y=df['CSIRO Adjusted Sea Level']
        )

    # Create first line of best fit
    first_line = liregress(
        x=df
    )

    # Create second line of best fit
    second_line = liregress()

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()