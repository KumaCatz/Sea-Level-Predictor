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
    linear_regress = linregress(
        x=df['Year'],
        y=df['CSIRO Adjusted Sea Level']
    )
    predicted_years = list(range(2013, 2051))
    predicted_values = [linear_regress.slope * year + linear_regress.intercept for year in predicted_years]
    plt.plot(predicted_years, predicted_values, color='red', label='Predicted Line')

    # Create second line of best fit
    # second_line = liregress()

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()