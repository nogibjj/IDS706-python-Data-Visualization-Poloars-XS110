from script import descript_stat
from script import plot_histogram
import polars as pl

WP_data = pl.read_csv('world_population.csv')



#country's population in 2022, growth rate and area.

data = WP_data[['2022 Population','Growth Rate','Area (km²)']]

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    descript_stat(data)
    plot_histogram(data)
