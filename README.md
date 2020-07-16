# High School Graduation Rate
Linear and multiple regression models to predict graduation rate using many different independent variables

## Goal
Determine if there is a relationship between student attendance, regents scores, or teacher qualifications and graduation rates in NYC public high schools

## Exploratory Data Analysis
- R^2 and p-values for each individual regent compared to graduation rate
![alt text](https://github.com/gracejihaepark/hs_gradrate/blob/master/images/1%20individual%20regent%20compared%20to%20graduation%20rate.png?raw=true)

- R^2 and p-values for attendance and staff qualifications compared to graduation rate
![alt text](https://github.com/gracejihaepark/hs_gradrate/blob/master/images/2%20attendance%20and%20staff%20qualifications%20compared%20to%20graduation%20rate.png?raw=true)

- There is a clear linear relationship between regents results and graduation rate
  - Earth Science usually taken in 8th grade, and Algebra in 9th, which allows for early prediction of graduation rates
![alt text](https://github.com/gracejihaepark/hs_gradrate/blob/master/images/3%20linear%20relationship%20between%20regents%20results%20and%20graduation%20rate.png?raw=true)

## Model
- Ran a mutliple Regession for all regents for feature engineering to choose the regents subjects that most affected graduation rates
  - Alegbra, English, and US History and Government all had low p-values
  - Ran a multiple regression for these three regents, which resulted in all three regents having a p-value of less than .01
  - Checked normality and homoscedasticity
  ![alt text](https://github.com/gracejihaepark/hs_gradrate/blob/master/images/4%20normality%20and%20homoscedasticity%20for%20multiple%20regression%20for%20all%20regents.png?raw=true)

- Next, ran a multiple Regression for all independent variables, such as teacher qualifications, attendance, and the three regents from the first regression
  - Ran another multiple regression of variables with low p-values (percentage of teachers with no valid teaching certificate, attendance, US History and Government regents), which resulted in new p-values of under .01
  - Checked normality and homoscedasticity
  ![alt text](https://github.com/gracejihaepark/hs_gradrate/blob/master/images/5%20normality%20and%20homoscedasticity%20for%20multiple%20regression%20for%20all%20independent%20variables.png?raw=true)

## Conclusions
- Graduation rates can be predicted based on simple linear regression models for regent scores and attendance data
- US History and Government regents, attendance rates, and percentage of teachers with no valid teaching certificate gave us the best model

## Weaknesses and Future Work
- Lost thousands of data points after merging all the data due to the different ways that same schools were named in different data sets
- Would like to incorporate demographic data, English Language Learners (ELL) data, as well as special needs data to see if they have an effect as well
