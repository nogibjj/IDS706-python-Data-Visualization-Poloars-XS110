import polars as pl
import matplotlib.pyplot as plt

def descript_stat(df):

    # Head 5 rows
    print("=== Dataset Overview ===")
    print(df.head())
    print("\n")

    # Summary statistics using the describe method
    summary_stats = df.describe()
    print("=== Descriptive Statistics Overview ===")
    print(summary_stats)
    print("\n")

    # Mean, Median and Mode
    print("=== Mean, Median and Mode Overview ===")
    mean = df.mean()
    median = df.median()
    print("Mean:\n", mean)
    print("Median:\n", median)
    print("\n")

    # Variance and standard deviation
    variance = df.var()
    std_deviation = df.std()
    print("=== Variance and standard deviation Overview ===")
    print("Variance:\n", variance)
    print("Standard Deviation:\n", std_deviation)




def plot_histogram(df):
    """
    Plot a histogram 

    """
    plt.hist(df[['2022 Population']], bins=20, color='blue', alpha=0.7)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of 2022 Population')
    plt.show()

WP_data = pl.read_csv('world_population.csv')



#country's population in 2022, growth rate and area.

data = WP_data[['2022 Population','Growth Rate','Area (km²)']]

if __name__ == "__main__":
    descript_stat(data)
    plot_histogram(data)