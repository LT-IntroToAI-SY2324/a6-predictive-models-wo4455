# Project - Create your own predictive model

WILL OTWELL & LOUIS WOODLEY

Predictive models are used across industries to analyze and make predictions about data. From sports to beauty products to app usage, predictive models provide individuals and businesses with data to make informed decisions.

Throughout this module, you have learned how to program both supervised and unsupervised learning models. In this final project, you will create your own! Throughout this project, you will work through activities to complete the following steps:

1. Choose a dataset.
2. Determine which algorithm is the best fit. Based on the dataset you choose, you will need to figure out which algorithm to use. This will require you to get to know your data and your goals! Is there a linear correlation between variables? Are you looking for numerical value or a label/category? Do you know the labels or do you need the model to create them for you?
- Do some tests with matplotlib and visualize your data.  Does it provide a good correlation?  Why or why not?
3. Program your model. Once you have chosen your type of model, it’s time to create it! In this step, you will write a program that fits your chosen model to the data. Your program and output will be specific to the model you choose.  
4. Analyze and present your findings. An important part of creating predictive models is being able to communicate the results. In this final step of the project, you will present your findings using slides or an infographic. Your product should include the following components:
- Your reasoning for the algorithm you chose
Our model takes multiple variables into account when making a prediction. It analyzes the quality of a wine by looking at 10 variables such as density and pH value and returns a score between 1 and 10 for the quality of the wine. Since we needed to deal with multiple variables, we used the multivariable linear regression model.

- An explanation and analysis of the Our model lists the value for all of the variables along with the actual score and a predicted score it made based on the values of the variable.
output of your model: What results did your model produce? What do they mean?

- A prediction based on your model
For a wine with a Fixed Acidity between 8 to 8.5, a Citric Acid between 0.3 and 0.4, and an Alcohol level between 10.0 and 12.0, the quality score we predict based on our model’s output would be somewhere in between 6-7.

- A summary of the accuracy of your model
Our model is somewhat accurate. The predicted score is usually within 0.5 to 0.75 of the actual score.

- Real world implications
This program specifically could be used by wine connoisseurs to predict the score of a wine based on the various components within it. However, this type of linear regression model could be used for really any situation where multiple variables need to be analyzed.