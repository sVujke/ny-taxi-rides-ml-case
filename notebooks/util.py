from fbprophet import Prophet
from pandas.tseries.offsets import Week
import pandas as pd 
import numpy as np

import logging, sys
logging.disable(sys.maxsize)

def agg_to_weekly_forecast(forecast):
    forecast['ds_w'] = forecast['ds'].apply(lambda x: x if x.weekday() == 6 else x + Week(weekday=6))
    forecast_w = forecast.groupby('ds_w').agg(yhat=('yhat','sum'),
                                              yhat_lower=('yhat_lower', 'sum'),
                                              yhat_upper=('yhat_upper', 'sum')).reset_index()
    return forecast_w.rename(columns={'ds_w': 'ds'})

def agg_to_weekly_actuals(df_daily):
    df_daily['ds_w'] = df_daily['ds'].apply(lambda x: x if x.weekday() == 6 else x + Week(weekday=6)).copy()
    df_weekly = df_daily.groupby('ds_w').agg(y=('y','sum')).reset_index()
    return df_weekly.rename(columns={'ds_w': 'ds'})


def get_model_forecast(df_train, df_test, regressors, propeth_hparams={}):
    
    if bool(propeth_hparams):
        m = Prophet()
    else:
        m = Prophet(**propeth_hparams)
    
    for reg in regressors:
        m.add_regressor(reg)

    m.add_country_holidays(country_name='US')
    
    m.fit(df_train)  
    forecast = m.predict(df_test)
    
    return (m, forecast)