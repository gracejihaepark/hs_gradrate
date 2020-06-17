# High School Graduation Rate
Linear and multiple regression models to predict graduation rate using many different independent variables

## Goal
Determine if there is a relationship between student attendance, regents scores, or teacher qualifications and graduation rates in NYC public high schools

## Exploratory Data Analysis
- R^2 and p-values for each individual regent compared to graduation rate
![alt text](https://github.com/gracejihaepark/hs_gradrate/blob/master/readme%20images/Screen%20Shot%202020-06-15%20at%204.15.31%20PM.png?raw=true)

- R^2 and p-values for attendance and staff qualifications compared to graduation rate
![alt text](https://github.com/gracejihaepark/hs_gradrate/blob/master/readme%20images/Screen%20Shot%202020-06-15%20at%204.19.38%20PM.png?raw=true)

- There is a clear linear relationship between regents results and graduation rate
  - Earth Science usually taken in 8th grade, and Algebra in 9th, which allows for early prediction of graduation rates
![alt text](https://github.com/gracejihaepark/hs_gradrate/blob/master/readme%20images/Screen%20Shot%202020-06-15%20at%204.21.25%20PM.png?raw=true)

## Model
- Ran a mutliple Regession for all regents for feature engineering to choose the regents subjects that most affected graduation rates
  - Alegbra, English, and US History and Government all had low p-values
  - Ran a multiple regression for these three regents, which resulted in all three regents having a p-value of less than .01
  - Checked normality and homoscedasticity
  ![alt text](https://github.com/gracejihaepark/hs_gradrate/blob/master/readme%20images/Screen%20Shot%202020-06-17%20at%202.40.54%20AM.png?raw=true)

- Next, ran a multiple Regression for all independent variables, such as teacher qualifications, attendance, and the three regents from the first regression
  - Ran another multiple regression of variables with low p-values (percentage of teachers with no valid teaching certificate, attendance, US History and Government regents), which resulted in new p-values of under .01
  - Checked normality and homoscedasticity
  ![alt text](https://github.com/gracejihaepark/hs_gradrate/blob/master/readme%20images/Screen%Shot%202020-06-17%at%202.47.46%AM.png?raw=true)

## Conclusions
- Graduation rates can be predicted based on simple linear regression models for regent scores and attendance data
- US History and Government regents, attendance rates, and percentage of teachers with no valid teaching certificate gave us the best model

## Weaknesses and Future Work
- Lost thousands of data points after merging all the data due to the different ways that same schools were named in different data sets
- Would like to incorporate demographic data, English Language Learners (ELL) data, as well as special needs data to see if they have an effect as well
