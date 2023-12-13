# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
The model was less accurate than before, becuase when the data is scaled it is better fitted for the model and without it, can mess things up. 

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
The model was ~0.8 with the scaler, which is accurate enough becuase it is relatively close to 1. 

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model did well, getting the majority correct. This led to a noticeable trend, I did not see any pattern to the incorrect inputs. 

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
According to the model, she would not buy an SUV. 

