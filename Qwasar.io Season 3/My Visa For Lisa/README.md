# Welcome to Visa For Lisa
***

## Task
- What is the problem? And where is the challenge?
This project for Galaxy Bank involves several key steps to build a predictive model for loan acceptance among deposit customers. Here's a structured approach to tackle the project:

### Project Outline

1. Data Collection and Cleaning
   - Obtain the loan dataset, which may include customer demographics, account details, previous loan history, etc.
   - Clean the data by handling missing values, removing duplicates, and ensuring data types are appropriate.

2. Data Exploration
   - Perform exploratory data analysis (EDA) to understand the dataset better.
   - Analyze the distribution of key variables, correlations, and any patterns that may exist.

3. Data Visualization
   - Create visualizations to represent the findings from the EDA.
   - Use plots like histograms, box plots, scatter plots, and correlation matrices to illustrate relationships and distributions.

4. Machine Learning
   - Implement a multi-variable linear regression model to predict loan acceptance.
   - Split the data into training and testing sets to evaluate the model's performance.
   - Assess the model using metrics such as R-squared, Mean Absolute Error (MAE), and Mean Squared Error (MSE).

5. Communication
   - Prepare a presentation summarizing the findings, model performance, and recommendations for the marketing team.
   - Include visualizations and key insights that can help in decision-making.

### Success Criteria
- Demonstrate a clear understanding of the data and the model.
- Show how the model can help improve conversion rates.
- Provide actionable insights for the marketing team.

### Expected Outcomes
- A well-documented codebase that the DevOps team can deploy.
- A presentation that effectively communicates the findings and recommendations to stakeholders, including the CEO.

### Next Steps
1. Upload the Dataset: If you have the loan dataset, please upload it so we can begin the data cleaning and exploration process.
2. Prepare the Code: I can help you write the code for data analysis, visualization, and model building.
3. Create Visualizations: We can generate plots to visualize the data and model results.


## Description
- How have you solved the problem?
### Summary Statistics
- Total Records: 5000
- Age: Mean = 45.34, Min = 23, Max = 67
- Experience: Mean = 20.10, Min = -3, Max = 43
- Income: Mean = 73.77, Min = 8, Max = 224
- Family Size: Mean = 2.40, Min = 1, Max = 4
- CCAvg (Credit Card Average Spending): Mean = 1.94, Min = 0, Max = 10
- Mortgage: Mean = 56.50, Min = 0, Max = 635
- Personal Loan Acceptance: Mean = 0.096 (approximately 9.6% acceptance rate)

### Next Steps
1. Data Cleaning: Check for missing values and outliers.
2. Data Exploration: Analyze relationships between features and the target variable (Personal Loan).
3. Data Visualization: Create visualizations to illustrate key insights.
4. Machine Learning: Build a multi-variable linear regression model.
### Data Cleaning Results

1. Missing Values: There are no missing values in the dataset for any of the features.
2. Duplicates: There are no duplicate records in the dataset.

### Outlier Analysis
The boxplots for the numerical features have been generated to visualize potential outliers. Here are the boxplots for the following features:

- Age
- Experience
- Income
- Family
- CCAvg (Credit Card Average Spending)
- Mortgage

![Boxplots of Numerical Features](attachment://boxplots.png)

### Next Steps
1. Outlier Treatment: If any outliers are identified, we can decide whether to remove or cap them.
2. Data Exploration: Analyze the relationships between features and the target variable (Personal Loan).
3. Data Visualization: Create additional visualizations to illustrate key insights.

## Installation
- How to install your project? npm install? make? make re?
You need to pip install sklearn, seaborn and numpy in order to show the images

## Usage
- How does it work?
The way it works is either by using Jupyter notebook to run each cell in this visa for lisa or you just run in the terminal ipython visa_for_lisa.ipynb Please note that you will not see images when you use the last option.


### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
