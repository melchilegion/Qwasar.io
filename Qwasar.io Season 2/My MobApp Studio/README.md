# Welcome to My Mobapp Studio
***

## Task
 Google Play Store Data Analysis

This project involves analyzing the Google Play Store dataset to gain insights into mobile applications. The analysis includes summarizing the dataset, cleaning the data, visualizing distributions, and computing correlations among various features.

## Description
The dataset used for this analysis is `googleplaystore.csv`, which contains information about various apps available on the Google Play Store. The dataset includes the following columns:
- **App**: Name of the app
- **Category**: Category of the app
- **Rating**: User rating of the app
- **Reviews**: Number of user reviews
- **Size**: Size of the app
- **Installs**: Number of installations
- **Type**: Free or Paid
- **Price**: Price of the app
- **Content Rating**: Age group for which the app is suitable
- **Genres**: Genres associated with the app
- **Last Updated**: Date when the app was last updated
- **Current Ver**: Current version of the app
- **Android Ver**: Minimum Android version required

## Installation
How to install your project? npm install? make? make re?
all the Installation was used using pip install then (libraries)
- Python 3.x
- Pandas
- Matplotlib
- Seaborn

You can install the required packages using pip:
```bash
pip install pandas matplotlib
```
## Usage
 How does it work?
1. Clone this repository or download the notebook and dataset.
2. Ensure that the `googleplaystore.csv` file is in the same directory as the Jupyter notebook.
3. Open the Jupyter notebook.
4. Run the cells in order to perform the analysis.

## Functions
The notebook contains the following functions:
- `load_dataset()`: Loads the dataset from the CSV file.
- `print_summarize_dataset(dataset)`: Prints a summary of the dataset.
- `clean_dataset(dataset)`: Cleans the dataset by removing missing values and converting data types.
- `print_histograms(dataset)`: Plots histograms for the distribution of ratings and installations.
- `compute_correlations_matrix(dataset)`: Computes and prints the correlation matrix for numerical features.
- `print_scatter_matrix(dataset)`: Plots a scatter matrix to visualize relationships between features.

## Results
The analysis will provide insights into:
- Distribution of app ratings and installations.
- Correlation between different features.
- Visualizations to help understand the data better.


### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
