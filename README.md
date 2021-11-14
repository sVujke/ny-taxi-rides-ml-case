# FREE NOW ML Case Study

# EDA and Data Cleansing

# Problem #1

>By using 2020 March to August Yellow Cabs transactions try to forecast 2020
September daily and weekly transactions. While doing the forecasting try to
add Covid, Seasonality,and any other external variables to the equation.


The solution can be found in `notebooks/transaction_forecasting.ipynb`

# Problem #2
> Marketing is trying to identify pickup location ids to incentivise passengers in
order to increase the number of trips. By using 2020 March to August Yellow
Cabs transactions build a recommendation engine to help marketing identify
these potential location ids on a weekly basis? Also define why you think
these areas are potential areas to incentivise according to you?


The solution can be found in `notebooks/pu_location_recommender.ipynb`

# Problem #3
> We want to promote tipping to retain our driver base and increase the driver
engagement. Could you find the relation between [the trip duration, trips
distance, location id, vendor and passenger count] and tip amount, and make
suggestions on rolling out some experimentations?


The solution can be found in `notebooks/increase_tipping.ipynb`

# Helper notebook - EDA and Cleaning 

Some visualizations and data clensing can be found in the `notebooks/clean_trip_dataset.ipynb` .

# External Data 

The sources, transformations and exploration can be
found in `notebooks/external_data.ipynb`

# Dependencies

To make sure all the needed dependencies are installed run the following command:

 ```{r, engine='bash', count_lines}
conda env create -f environment.yml
 ```

 To add the environment as a kernel to your jupyter notebook run: 
  ```{r, engine='bash', count_lines}
python -m ipykernel install --user --name=free-now
 ```