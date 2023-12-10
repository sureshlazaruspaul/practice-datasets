#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# read_data.R reads credit risk dataset.
# written by,
#  Suresh Paul, C.Phil, M.S., B.E.
#   Lecturer II, Balwin Wallace University
#   Founder & Sr. Data Scientist, Algorithm Basics LLC
# Copy of this code is available at,
#  https://raw.githubusercontent.com/sureshlazaruspaul/BUS662-practice-datasets/main/credit-risk/read_data.R
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# load packages ...

library("tidyverse")
library("data.table")
library("janitor")


gitpath <- "https://raw.githubusercontent.com/sureshlazaruspaul"

dirpath <- "/BUS662-practice-datasets/main/credit-risk/"


#------------------------------------------------------------------------------
# Documentation
#------------------------------------------------------------------------------
# loan_number: serial number for the loan
# person_age: age of the loan recipient
# person_income: income of the loan recipient
# person_home_ownership: home ownership status of the loan recipient (RENT, OWN, MORTGAGE, OTHER)
# person_emp_length: length of employment of the loan recipient
# loan_intent: purpose of the loan (PERSONAL, EDUCATION, MEDICAL, VENTURE, HOMEIMPROVEMENT, DEBTCONSOLIDATION)
# loan_grade: grade of loan (A, B, C, D, E, F, G)
# loan_amnt: loan amount
# loan_int_rate: effective loan interest rate
# loan_status: loan status (0 is active, 1 is default)
# cb_person_default_on_file: Historical default (Yes/No)
# cb_person_cred_hist_length: length of credit history
# loan_percent_income: loan as a % of income
#------------------------------------------------------------------------------

# create an empty dataframe
credit_risk = data.frame()



# read first csv file ...
credit_risk1 <- fread(paste0(gitpath, dirpath, "credit_risk1.csv")) # using data.table package

# use rbind() to append the imported data to the empty dataframe
credit_risk <- rbind(credit_risk, credit_risk1)



# read second csv file ...
credit_risk2 <- fread(paste0(gitpath, dirpath, "credit_risk2.csv")) # using data.table package

# use rbind() to append the imported data to the empty dataframe
credit_risk <- rbind(credit_risk, credit_risk2)



# read third csv file ...
credit_risk3 <- fread(paste0(gitpath, dirpath, "credit_risk3.csv")) # using data.table package

# use rbind() to append the imported data to the empty dataframe
credit_risk <- rbind(credit_risk, credit_risk3)



#list all objects in current R workspace
ls()

#remove credit_risk1 and credit_risk2
rm("credit_risk1", "credit_risk2", "credit_risk3")

