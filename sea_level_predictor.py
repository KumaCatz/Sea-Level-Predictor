import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(
        x=df['Year'],
        y=df['CSIRO Adjusted Sea Level']
        )

    # Create first line of best fit
    first_regression = linregress(
        x=df['Year'],
        y=df['CSIRO Adjusted Sea Level']
    )
    predicted_years = list(range(df['Year'].iloc[0], 2051))
    predicted_values = [first_regression.slope * year + first_regression.intercept for year in predicted_years]
    plt.plot(predicted_years, predicted_values, color='blue', label='Predicted Line')

    # Create second line of best fit
    filter_by_year = df['Year'] >= 2000
    second_regression = linregress(
        x=df[filter_by_year]['Year'],
        y=df[filter_by_year]['CSIRO Adjusted Sea Level']
    )
    predicted_years = list(range(2000, 2051))
    predicted_values = [second_regression.slope * year + second_regression.intercept for year in predicted_years]
    plt.plot(predicted_years, predicted_values, color='red', label='Predicted Line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()