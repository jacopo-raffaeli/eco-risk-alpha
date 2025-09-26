# eco-risk-alpha

## Project Overview

**Eco-Risk Alpha** is a data science project developed as part of a summer school on sustainable finance and economics. The project investigates the relationship between corporate ESG performance and credit risk, focusing on how ESG factors can influence credit spreads and counterparty risk in interest-rate swap portfolios.

The main objective is to explore whether "greener" companies benefit from lower credit spreads and reduced CVA (Credit Valuation Adjustment), potentially reflecting a measurable "green credit premium."  

---

## Repository Content

This repository contains all materials necessary to reproduce the project workflow, including:

- **Notebooks / Scripts**: Well-documented code for data exploration, model building, and CVA computation.
- **Data**: Small CSV datasets with corporate financial and ESG information, expected exposure profiles, and discount factors.
- **Models**: Saved machine learning models used for predicting CDS spreads and computing model-implied CVA.
- **Results**: Tables summarizing company-level CDS spreads, model predictions, CVA calculations, and derived green-premium measures.
- **Documentation**:  
  - Project report summarizing methodology, results, and insights.  
  - Slide deck highlighting key findings and takeaways.

---

## Key Tasks

The project workflow is structured around the following tasks:

1. **Data Exploration**  
   Visualize CDS spreads versus ESG scores, handle missing values and outliers, and perform basic data cleaning.  

2. **Baseline Modeling**  
   Establish simple linear models linking ESG scores and other factors to observed CDS spreads.  

3. **Feature Selection & Rationale**  
   Justify variable choices to isolate ESG effects on credit spreads.  

4. **CVA Computation**  
   Convert CDS spreads into default intensities and calculate unilateral CVA for benchmark exposures.  

5. **Machine Learning Modeling**  
   Train predictive models to estimate CDS spreads, evaluate performance with cross-validation, and compute model-implied CVA.  

6. **Insight Synthesis**  
   Compare actual versus model-implied CVA and derive the green-premium measure across the dataset.  


