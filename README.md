# Final Project - Bank Marketing Campaign

This final project is the means of my first journey to enter the Data Science Discipline while also as an application for the knowledge from the course I have been attended to in the past 5 months.

### Abstact

It is a dataset that describing Portugal bank marketing campaigns results.
Conducted campaigns were based mostly on direct phone calls, offering bank client to place a term deposit.
If after all marking afforts client had agreed to place deposit - target variable marked 'yes', otherwise 'no'

Sourse of the data
https://archive.ics.uci.edu/ml/datasets/bank+marketing

### Problem analysis

The management of a bank in Portugal received reports that a marketing campaign by telemarketers was ineffective and yielded unsatisfactory results. The steps taken by the bank are to analyze the data marketing campaign and create predictive models with the goal of making telemarketers more effective and increasing the results of the campaign. The things that will be analyzed are as follows:

1. What does the report tell the management?
2. What are the demographic factors that influence the client's decision?
3. What are the internal factors of the bank that influence client decisions?
4. What are the external factors of the bank that influence client decisions?
5. Are there any ideal conditions for someone to place their money in a time deposit?

### Conclusion:

If the bank wants to increase its effectiveness and results. The bank can do the things below,

The conditions are divided into 3:

**1. Client Profile**

- Elderly & Early Working Age is the age group with the largest percentage. Banks can increase the number of clients by calling that age group
- Students & retired make up the largest percentage of jobs. The bank can increase the number of clients by calling that group
- Single clients have the largest percentage. The bank can increase the number of clients by calling that group
- Banks can call a lot more to clients based on higher education
- If banks want to be more effective, They can choose customers who have housing loan and don't have a personal loan (although the difference is not too significant)

**2. Internal Bank**

- For the next campaign, the bank can increase the number of customers contacted in March, April, September, October, and December because the percentage in these months is quite high
- Companies can provide training for telemarketers, so that campaign results can be improved (more successful)
- Maybe telemarketers can make conversations more interesting because the duration really determines the client's decision.

**3. External Bank**

Client decision is influenced heavily by external factors. However, the banks cannot choose to do the things they wanted to do, even though, business-wise it would be the best opportunity for the bank to issue a marketing campaign. Sadly enough, The bank is regulated by the central bank and the government that makes them cannot seize the opportunity.

e.g. when there are conditions such as deflation or market pessimism, people tend to invest their money. However, the government will issue monetary policies such as the central bank asking all banks to lower bank interest rates, etc. to discourage people to spend their money instead of leaving it in the bank

### Modelling:

![image](https://user-images.githubusercontent.com/75253940/114907911-c467c880-9e45-11eb-8e29-6beb11518fb5.png)

Because the score is still very low and the data is imbalanced, we'll continue to resample using the **Random Under Sampler, Random Over Sampler, Near Miss, and SMOTE methods.**

![image](https://user-images.githubusercontent.com/75253940/114907968-d2b5e480-9e45-11eb-830c-0e721ee01413.png)

![image](https://user-images.githubusercontent.com/75253940/114908007-de091000-9e45-11eb-9174-44a8ba9888cd.png)

The best model and method is **Logistic Regression with Random Under Sampler** with a score of **70,776**

### Hyperparameter Tuning:

![image](https://user-images.githubusercontent.com/75253940/114908112-fa0cb180-9e45-11eb-9e2f-e8960570516e.png)

![image](https://user-images.githubusercontent.com/75253940/114908158-042eb000-9e46-11eb-9e5e-3586711f0304.png)

There is an increase in the score after tuning **70.776 -> 70.862 (+0.086)**

### Feature Selection:

![image](https://user-images.githubusercontent.com/75253940/114908398-42c46a80-9e46-11eb-9870-e5857d3f1e85.png)

drop *'age','education','marital','default','housing','day_of_week','month','job','loan','contact','poutcome'* (all category feature + age)

![image](https://user-images.githubusercontent.com/75253940/114908584-6f788200-9e46-11eb-9305-e9a84a61c125.png)

After feature selection, the running time is decrease from **0.717s -> 0.416s (-0.301s)**


### Saving Model:

![image](https://user-images.githubusercontent.com/75253940/114908691-87500600-9e46-11eb-9632-bbeb92013bc3.png)

### Model Deployment:

![image](https://user-images.githubusercontent.com/75253940/114912612-68537300-9e4a-11eb-960e-6ef2b39ee4b9.png)

![image](https://user-images.githubusercontent.com/75253940/114912575-5bcf1a80-9e4a-11eb-8d3a-c4f4f6b4849a.png)

### Dashboard:

**Home**
![image](https://user-images.githubusercontent.com/75253940/114912867-b6687680-9e4a-11eb-8732-c6f82a15e227.png)

**Dataset**
![image](https://user-images.githubusercontent.com/75253940/114912994-dac45300-9e4a-11eb-9911-81c77311eb6a.png)

**Data Visualization**
![image](https://user-images.githubusercontent.com/75253940/114913093-fd566c00-9e4a-11eb-8035-1509d104a1e9.png)

**About**
![image](https://user-images.githubusercontent.com/75253940/114913161-12cb9600-9e4b-11eb-98c8-0a54e4a59aa9.png)

