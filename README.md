# MAST30034 Project 1
- Name: Jenny Mai
- Student ID: 1538060

## Project Overview
This project focuses on analyzing the New York City Yellow Taxi data to generate insights and recommendations specifically for tourists. The analysis includes preprocessing, exploratory data analysis (EDA), and the application of machine learning models to predict taxi fares. The models used in this project include Linear Regression, Lasso Regression, Random Forest, and Gradient Boosted Trees.

## Research Goal
The primary goal of this project is to analyze taxi fare data and develop a model that can predict fare amounts accurately, with a specific focus on providing actionable insights for tourists visiting New York City.

## Timeline
6 months: November 2022 - April 2023

## Project Structure

- **notebooks/**
  - `processing_1.ipynb`: **Data Preprocessing and Standardization Pipeline**  
    This notebook handles the initial data preprocessing steps for taxi trip data, including schema standardization and merging multiple datasets into a consistent format for further analysis.
  
  - `processing_2.ipynb`: **Data Cleaning and Feature Engineering**  
    This notebook focuses on cleaning the data by handling missing values, removing outliers, and performing feature engineering to create new variables for analysis.
  
  - `processing_3.ipynb`: **Spatial Data Integration and Feature Engineering**  
    This notebook integrates geographic data with taxi trip data, identifies key zones like airports and tourist attractions, and creates features based on spatial information.
  
  - `processing_4.ipynb`: **Weather Data Integration and Duplicate Removal**  
    This notebook merges weather data with taxi trip data, cleans the combined dataset, and removes duplicates to ensure a clean and enriched dataset for analysis.
  
  - `eda_postcleaning.ipynb`: **Exploratory Data Analysis and Visualization**  
    This notebook performs exploratory data analysis (EDA) on the cleaned dataset, visualizing correlations, distributions, temporal patterns, and geospatial data to uncover key insights.
  
  - `transformation.ipynb`: **Log Transformation and Data Preparation**  
    This notebook applies log transformations to skewed features to normalize their distributions and prepares the data for modeling.
  
  - `linear_model.ipynb`: **Linear and Lasso Regression Model Development**  
    This notebook develops and evaluates Linear and Lasso regression models to predict taxi fares, with a focus on feature selection, residuals analysis, and model refinement.
  
  - `tree_model.ipynb`: **Random Forest and Gradient Boosting Model Development**  
    This notebook builds and evaluates Random Forest and Gradient Boosting models for taxi fare prediction, analyzing model performance, residuals, and feature importance.

- **plots/**
  - This directory contains all the plots generated during the EDA and modeling phases.

- **report/**
  - This directory contains the LaTeX files for the final report.

- **scripts/**
  - Contains any Python scripts used in the data preprocessing and analysis pipeline.

## Requirements
Ensure you have all necessary Python packages installed by using the `requirements.txt` file provided in the root directory.

## Running the Project

To replicate the analysis and run the models, please follow the steps below in the order specified:

1. **Data Preprocessing**:
   - Open and run the following notebooks sequentially:
     1. `processing_1.ipynb`
     2. `processing_2.ipynb`
     3. `processing_3.ipynb`
     4. `processing_4.ipynb`
   - These notebooks will handle all the necessary data preprocessing steps including cleaning, outlier removal, and feature engineering.

2. **Exploratory Data Analysis (EDA)**:
   - After preprocessing, proceed with the exploratory data analysis:
     - `eda_postcleaning.ipynb`
   - This notebook will help you understand the cleaned dataset through various visualizations.

3. **Data Transformation**:
   - Next, transform the data to prepare it for modeling:
     - `transformation.ipynb`
   - This includes scaling and applying transformations to ensure the data is suitable for the machine learning models.

4. **Modeling**:
   - Run the following notebooks to build and evaluate predictive models:
     - `linear_model.ipynb`: Implements Linear and Lasso Regression models.
     - `tree_model.ipynb`: Implements Random Forest and Gradient Boosted Trees models.