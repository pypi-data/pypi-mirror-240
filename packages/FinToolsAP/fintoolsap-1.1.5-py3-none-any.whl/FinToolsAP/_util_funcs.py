from __future__ import annotations

import pandas as pd
import numpy as np
import datetime
import dateutil

def rhasattr(obj, attr):
    try: 
        left, right = attr.split('.', 1)
    except: 
        return(hasattr(obj, attr))
    return(rhasattr(getattr(obj, left), right))

def rgetattr(obj, attr, default = None):
    try: 
        left, right = attr.split('.', 1)
    except: 
        return(getattr(obj, attr, default))
    return(rgetattr(getattr(obj, left), right, default))

def rsetattr(obj, attr, val):
    try: 
        left, right = attr.split('.', 1)
    except: 
        return(setattr(obj, attr, val))
    return(rsetattr(getattr(obj, left), right, val))

def percentile_rank(df: pd.DataFrame, var: str) -> pd.DataFrame:
    ptiles = list(df[var].quantile(q = list(np.arange(start = 0, step = 0.01, stop = 1))))
    df[f'{var}_pr'] = 100
    for i in range(99, 0, -1):
        mask = df[var] < ptiles[i]
        df.loc[mask, f'{var}_pr'] = i
    return(df)

def prior_returns(df: pd.DataFrame, 
                  id_type: str, 
                  return_types: list[str], 
                  return_intervals: list[tuple[int, int]]
                  ) -> pd.DataFrame:
    """ Calculates the cummulative return between two backward looking time
    intervals
    """
    for ret_typ in return_types:
        for typ in return_intervals:
            name = f'pr{typ[0]}_{typ[1]}' if(ret_typ == 'adjret') else f'prx{typ[0]}_{typ[1]}'
            df[name] = 1
            dic = {}
            for i in range(typ[0], typ[1] + 1):
                dic[f'{ret_typ}_L{i}'] = 1 + df.groupby(by = [id_type])[ret_typ].shift(i)
                df[name] *= dic[f'{ret_typ}_L{i}']
            df = df.drop(df.filter(regex = '_L').columns, axis = 1)
            df[name] -= 1
    return(df)

def gorup_avg(df: pd.DataFrame, gr: list, vr: str, wt: str = None, name: str = None):
    name = vr if(name is None) else name
    if(wt is None):
        res = df.groupby(by = gr).mean(numeric_only = True)[vr]
    else:
        res = df.groupby(by = gr).apply(wavg, vr, wt)
    res = res.to_frame().reset_index()
    if(0 in list(res.columns)):
        res = res.rename(columns = {0: name})
    else:
        res = res.rename(columns = {vr: name})
    return(res)

def time_intervals(min_date: datetime.datetime, 
                   max_date: datetime.datetime, 
                   year_delta: int, 
                   overlap: bool = False
                   ) -> list[tuple[datetime.datetime, datetime.datetime]]:

    blocks = []
    start_date = min_date
    while(True):
        end_date = start_date + dateutil.relativedelta.relativedelta(years = year_delta)
        if(end_date >= max_date):
            end_date = max_date
            blocks.append((start_date, end_date))
            break

        if(not overlap):
            end_date_adj = end_date - dateutil.relativedelta.relativedelta(days = 1)
        blocks.append((start_date, end_date_adj))
        start_date = end_date

    return(blocks)

def time_intervals_monthly(min_date: datetime.datetime, 
                           max_date: datetime.datetime, 
                           month_delta: int, 
                           overlap: bool = False
                        ) -> list[tuple[datetime.datetime, datetime.datetime]]:

    blocks = []
    start_date = min_date
    while(True):
        end_date = start_date + dateutil.relativedelta.relativedelta(months = month_delta)
        if(end_date >= max_date):
            end_date = max_date
            blocks.append((start_date, end_date))
            break

        if(not overlap):
            end_date_adj = end_date - dateutil.relativedelta.relativedelta(days = 1)
        blocks.append((start_date, end_date_adj))
        start_date = end_date

    return(blocks)

def convert_to_list(val: list|str|float|int):
    if(isinstance(val, list)):
        return(val)
    else:
        return([val])

def list_diff(list1: list, list2: list) -> list:
    res = [e for e in list1 if e not in list2]
    return(res)

def list_inter(list1: list, list2: list) -> list:
    res = [e for e in list1 if e in list2]
    return(res)

def msci_quality(Z: float) -> float:
    if(Z >= 0):
        return(1 + Z)
    else:
        return(1 / (1 - Z))
        

# Weighted average
# can be used with groupby:  df.groupby('col1').apply(wavg, 'avg_name', 'weight_name')
# ML: corrected by ML to allow for missing values
def wavg(group, avg_name, weight_name=None):
    if weight_name==None:
        return group[avg_name].mean()
    else:
        x = group[[avg_name,weight_name]].dropna()
        try:
            return (x[avg_name] * x[weight_name]).sum() / x[weight_name].sum()
        except ZeroDivisionError:
            return group[avg_name].mean()
        