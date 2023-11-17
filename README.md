# 28842025_churning_customers
## Project overview
This repository contains an implementation of a Multi-Layer Perceptron (MLP) model for predicting customer turnover using TensorFlow's Functional API. The model is intended to analyse customer data and forecast whether or not a customer is going to churn.
## link to the model: 
http://agent-connectapp.herokuapp.com/predictChurn/
##Video demonstrating model perfomance

## Dependencies
  -Python 3.x
  -TensorFlow 2.x
  -NumPy
  -Pandas
  -Seaborn 
  -Matplotlib (for visualization)
  -Scikit-learn (for evaluation metrics)
  # DATASET: 
  https://drive.google.com/file/d/1deqC-VzcKNvTIrGcXO3nGEfJ5_Gzyl0S/view?usp=sharing
  
  ## What does the model do
  using this model a user enters values for a customer profile and the model predicts whether the customer will churn or not
## TRAINING PROCESS
Cleaning Data and seleecting features that best relate to customer churn
Use Exploratory Data Analysis to find out which customer profiles relate to churning a lot.

Using the selected best features to define and train a Multi-Layer Perceptron model using the Functional API

Evaluate the model’s accuracy and calculate the AUC score

Create a platform to host the model either web-based or desktop application

Allow users to use the application to enter new data and your model should predict if the supplied data of a new customer can result in a churn or not giving the confidence factor of the model

