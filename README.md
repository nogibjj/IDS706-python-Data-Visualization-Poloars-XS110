
# World Population

## Data

The data is from kaggle [world population](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset). In this Dataset, we have Historical Population data for every Country/Territory in the world by different parameters like Area Size of the Country/Territory, Name of the Continent, Name of the Capital, Density, Population Growth Rate, Ranking based on Population, World Population Percentage, etc.

I downloaded `word_population.csv` from kaggle and uploaded it into this resporitory.

## Setup

I use week2 mini project as template and make the following modification: 

### 1. Update requirements.txt:
```
#script
polars
matplotlib==3.7.2
```
### 2. Read data

Instead of using pd.read_csv, I use `pl.read_csv` to read `world_population.csv`


### 3. Update script.py

I update the script.py using Polars for descriptive statistics to generate summary statistics (mean, median, standard deviation)

And I also create data visualization.

## Data Visualization

I analyse the 234 countries' population in 2022, growth rate and Area(km²).

### 1. Summary statistics using the describe method

![Alt text](/image/image1.png)

### 2. Mean, Median and Mode

![Alt text](/image/image2.png)

### 3. Variance and standard deviation

![Alt text](/image/image3.png)

### 4. histogram of 2022 population

![Alt text](/image/image4.png)

### 5. boxplot of 2022 population

![Alt text](/image/image5.png)