import sys
import pathlib
import pandas as pd
import shutil
from pandas.tseries.offsets import *
import datetime
import matplotlib.pyplot as plt
import time

sys.path.insert(0, '../src/FinToolsAP/')

import QueryWRDS
import FamaFrench

# set printing options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', shutil.get_terminal_size()[0])
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# directory for loacl wrds database 
LOCAL_WRDS_DB = pathlib.Path('/home/andrewperry/Documents/wrds_database/WRDS.db')

def main():
    FF = FamaFrench.FamaFrench('andrewperry', LOCAL_WRDS_DB)
    DB = QueryWRDS.QueryWRDS('andrewperry', LOCAL_WRDS_DB)
    start_date = datetime.date(1900, 6, 30)
    end_date = datetime.date(2100, 6, 30)
    # 6 BM/ME sorts
    s = time.time()
    ccm_df = DB.query_CCM(start_date, end_date)
    ccm_df = ccm_df[(ccm_df.years_in >= 2) & (ccm_df.ffbm > 0)]
    sortsBMME_df = FF.sort_portfolios(ccm_df, char_bkpts = {'me': [0.5], 'ffbm': [0.3, 0.7]}, sorting_funcs = {'me': FF.sort_50, 'ffbm': FF.sort_3070}, rebalance_freq = 'A')
    sortsBMME_df = sortsBMME_df.set_index('date').sort_index()
    print(time.time() - s)
    
    ff_BMME = pd.read_csv('test_data/FFSorts/Sorts6_ME_BM.CSV')
    ff_BMME.date = pd.to_datetime(ff_BMME.date, format = '%Y%m')
    ff_BMME.date += MonthEnd(0)
    ff_BMME = ff_BMME.set_index('date').sort_index()
    ff_BMME_nf = pd.read_csv('test_data/FFSorts/Sorts6_ME_BM_num_firms.CSV')
    ff_BMME_nf.date = pd.to_datetime(ff_BMME_nf.date, format = '%Y%m')
    ff_BMME_nf.date += MonthEnd(0)
    ff_BMME_nf = ff_BMME_nf.set_index('date').sort_index()
    ff_BMME = ff_BMME.loc[ff_BMME.index >= sortsBMME_df.index.min()]
    ff_BMME = ff_BMME.loc[ff_BMME.index <= sortsBMME_df.index.max()]
    ff_BMME_nf = ff_BMME_nf.loc[ff_BMME_nf.index >= sortsBMME_df.index.min()]
    ff_BMME_nf = ff_BMME_nf.loc[ff_BMME_nf.index <= sortsBMME_df.index.max()]
    print(sortsBMME_df.describe() * 100)
    print(ff_BMME.describe())

    corr_1 = ff_BMME['SMALL LoBM'].corr(sortsBMME_df.me1_ffbm1)
    corr_2 = ff_BMME['ME1 BM2'].corr(sortsBMME_df.me1_ffbm2)
    corr_3 = ff_BMME['SMALL HiBM'].corr(sortsBMME_df.me1_ffbm3)
    corr_4 = ff_BMME['BIG LoBM'].corr(sortsBMME_df.me2_ffbm1)
    corr_5 = ff_BMME['ME2 BM2'].corr(sortsBMME_df.me2_ffbm2)
    corr_6 = ff_BMME['BIG HiBM'].corr(sortsBMME_df.me2_ffbm3)

    fig, ax = plt.subplots(3, 2, figsize = (32, 18))
    fig.suptitle('6 BM/ME Sorts')
    ax[0, 0].plot(ff_BMME['SMALL LoBM'] / 100, label = 'ff')
    ax[0, 0].plot(sortsBMME_df.me1_ffbm1, label = 'mine')
    ax[0, 0].legend()
    ax[0, 0].set_title(f'Small Lo BM: Corr = {corr_1}')
    ax[0, 0].set_ylabel('Return')

    ax[1, 0].plot(ff_BMME['ME1 BM2'] / 100, label = 'ff')
    ax[1, 0].plot(sortsBMME_df.me1_ffbm2, label = 'mine')
    ax[1, 0].legend()
    ax[1, 0].set_title(f'Small Med BM: Corr = {corr_2}')
    ax[1, 0].set_ylabel('Return')

    ax[2, 0].plot(ff_BMME['SMALL HiBM'] / 100, label = 'ff')
    ax[2, 0].plot(sortsBMME_df.me1_ffbm3, label = 'mine')
    ax[2, 0].legend()
    ax[2, 0].set_title(f'Small Hi BM: Corr = {corr_3}')
    ax[2, 0].set_ylabel('Return')

    ax[0, 1].plot(ff_BMME['BIG LoBM'] / 100, label = 'ff')
    ax[0, 1].plot(sortsBMME_df.me2_ffbm1, label = 'mine')
    ax[0, 1].legend()
    ax[0, 1].set_title(f'BIG Lo BM: Corr = {corr_4}')
    ax[0, 1].set_ylabel('Return')

    ax[1, 1].plot(ff_BMME['ME2 BM2'] / 100, label = 'ff')
    ax[1, 1].plot(sortsBMME_df.me2_ffbm2, label = 'mine')
    ax[1, 1].legend()
    ax[1, 1].set_title(f'BIG Med BM: Corr = {corr_5}')
    ax[1, 1].set_ylabel('Return')
    ax[2, 1].plot(ff_BMME['BIG HiBM'] / 100, label = 'ff')
    ax[2, 1].plot(sortsBMME_df.me2_ffbm3, label = 'mine')
    ax[2, 1].legend()
    ax[2, 1].set_title(f'BIG Hi BM: Corr = {corr_6}')
    ax[2, 1].set_ylabel('Return')
    sortsBMME_df['roll_me1_ffbm1'] = sortsBMME_df.me1_ffbm1.rolling(window = 12, min_periods = 12).mean()
    sortsBMME_df['roll_me1_ffbm1_std'] = sortsBMME_df.me1_ffbm1.rolling(window = 12, min_periods = 12).std()
    sortsBMME_df['roll_me1_ffbm2'] = sortsBMME_df.me1_ffbm2.rolling(window = 12, min_periods = 12).mean()
    sortsBMME_df['roll_me1_ffbm2_std'] = sortsBMME_df.me1_ffbm2.rolling(window = 12, min_periods = 12).std()
    sortsBMME_df['roll_me1_ffbm3'] = sortsBMME_df.me1_ffbm3.rolling(window = 12, min_periods = 12).mean()
    sortsBMME_df['roll_me1_ffbm3_std'] = sortsBMME_df.me1_ffbm3.rolling(window = 12, min_periods = 12).std()
    sortsBMME_df['roll_me2_ffbm1'] = sortsBMME_df.me2_ffbm1.rolling(window = 12, min_periods = 12).mean()
    sortsBMME_df['roll_me2_ffbm1_std'] = sortsBMME_df.me2_ffbm1.rolling(window = 12, min_periods = 12).std()
    sortsBMME_df['roll_me2_ffbm2'] = sortsBMME_df.me2_ffbm2.rolling(window = 12, min_periods = 12).mean()
    sortsBMME_df['roll_me2_ffbm2_std'] = sortsBMME_df.me2_ffbm2.rolling(window = 12, min_periods = 12).std()
    sortsBMME_df['roll_me2_ffbm3'] = sortsBMME_df.me2_ffbm3.rolling(window = 12, min_periods = 12).mean()
    sortsBMME_df['roll_me2_ffbm3_std'] = sortsBMME_df.me2_ffbm3.rolling(window = 12, min_periods = 12).std()
    ff_BMME['roll_SMALL_LoBM'] = ff_BMME['SMALL LoBM'].rolling(window = 12, min_periods = 12).mean()
    ff_BMME['roll_SMALL_LoBM_std'] = ff_BMME['SMALL LoBM'].rolling(window = 12, min_periods = 12).std()
    ff_BMME['roll_ME1_BM2'] = ff_BMME['ME1 BM2'].rolling(window = 12, min_periods = 12).mean()
    ff_BMME['roll_ME1_BM2_std'] = ff_BMME['ME1 BM2'].rolling(window = 12, min_periods = 12).std()
    ff_BMME['roll_SMALL_HiBM'] = ff_BMME['SMALL HiBM'].rolling(window = 12, min_periods = 12).mean()
    ff_BMME['roll_SMALL_HiBM_std'] = ff_BMME['SMALL HiBM'].rolling(window = 12, min_periods = 12).std()
    ff_BMME['roll_BIG_LoBM'] = ff_BMME['BIG LoBM'].rolling(window = 12, min_periods = 12).mean()
    ff_BMME['roll_BIG_LoBM_std'] = ff_BMME['BIG LoBM'].rolling(window = 12, min_periods = 12).std()
    ff_BMME['roll_ME2_BM2'] = ff_BMME['ME2 BM2'].rolling(window = 12, min_periods = 12).mean()
    ff_BMME['roll_ME2_BM2_std'] = ff_BMME['ME2 BM2'].rolling(window = 12, min_periods = 12).std()
    ff_BMME['roll_BIG_HiBM'] = ff_BMME['BIG HiBM'].rolling(window = 12, min_periods = 12).mean()
    ff_BMME['roll_BIG_HiBM_std'] = ff_BMME['BIG HiBM'].rolling(window = 12, min_periods = 12).std()
    fig2, ax2 = plt.subplots(3, 2, figsize = (32, 18))
    fig2.suptitle('6 BM/ME Sorts 12 Month Rolling Average')
    ax2[0, 0].plot(ff_BMME['roll_SMALL_LoBM'] / 100, label = 'ff')
    ax2[0, 0].plot(sortsBMME_df.roll_me1_ffbm1, label = 'mine')
    ax2[0, 0].legend()
    ax2[0, 0].set_title(f'Small Lo BM: Corr = {corr_1}')
    ax2[0, 0].set_ylabel('Return')

    ax2[1, 0].plot(ff_BMME['roll_ME1_BM2'] / 100, label = 'ff')
    ax2[1, 0].plot(sortsBMME_df.roll_me1_ffbm2, label = 'mine')
    ax2[1, 0].legend()
    ax2[1, 0].set_title(f'Small Med BM: Corr = {corr_2}')
    ax2[1, 0].set_ylabel('Return')

    ax2[2, 0].plot(ff_BMME['roll_SMALL_HiBM'] / 100, label = 'ff')
    ax2[2, 0].plot(sortsBMME_df.roll_me1_ffbm3, label = 'mine')
    ax2[2, 0].legend()
    ax2[2, 0].set_title(f'Small Hi BM: Corr = {corr_3}')
    ax2[2, 0].set_ylabel('Return')

    ax2[0, 1].plot(ff_BMME['roll_BIG_LoBM'] / 100, label = 'ff')
    ax2[0, 1].plot(sortsBMME_df.roll_me2_ffbm1, label = 'mine')
    ax2[0, 1].legend()
    ax2[0, 1].set_title(f'BIG Lo BM: Corr = {corr_4}')
    ax2[0, 1].set_ylabel('Return')

    ax2[1, 1].plot(ff_BMME['roll_ME2_BM2'] / 100, label = 'ff')
    ax2[1, 1].plot(sortsBMME_df.roll_me2_ffbm2, label = 'mine')
    ax2[1, 1].legend()
    ax2[1, 1].set_title(f'BIG Med BM: Corr = {corr_5}')
    ax2[1, 1].set_ylabel('Return')
    ax2[2, 1].plot(ff_BMME['roll_BIG_HiBM'] / 100, label = 'ff')
    ax2[2, 1].plot(sortsBMME_df.roll_me2_ffbm3, label = 'mine')
    ax2[2, 1].legend()
    ax2[2, 1].set_title(f'BIG Hi BM: Corr = {corr_6}')
    ax2[2, 1].set_ylabel('Return')
    fig3, ax3 = plt.subplots(3, 2, figsize = (32, 18))
    fig3.suptitle('6 BM/ME Sorts 12 Month Rolling Standard Deviation')
    ax3[0, 0].plot(ff_BMME['roll_SMALL_LoBM_std'] / 100, label = 'ff')
    ax3[0, 0].plot(sortsBMME_df.roll_me1_ffbm1_std, label = 'mine')
    ax3[0, 0].legend()
    ax3[0, 0].set_title(f'Small Lo BM: Corr = {corr_1}')
    ax3[0, 0].set_ylabel('Return')
    ax3[1, 0].plot(ff_BMME['roll_ME1_BM2_std'] / 100, label = 'ff')
    ax3[1, 0].plot(sortsBMME_df.roll_me1_ffbm2_std, label = 'mine')
    ax3[1, 0].legend()
    ax3[1, 0].set_title(f'Small Med BM: Corr = {corr_2}')
    ax3[1, 0].set_ylabel('Return')
    ax3[2, 0].plot(ff_BMME['roll_SMALL_HiBM_std'] / 100, label = 'ff')
    ax3[2, 0].plot(sortsBMME_df.roll_me1_ffbm3_std, label = 'mine')
    ax3[2, 0].legend()
    ax3[2, 0].set_title(f'Small Hi BM: Corr = {corr_3}')
    ax3[2, 0].set_ylabel('Return')
    ax3[0, 1].plot(ff_BMME['roll_BIG_LoBM_std'] / 100, label = 'ff')
    ax3[0, 1].plot(sortsBMME_df.roll_me2_ffbm1_std, label = 'mine')
    ax3[0, 1].legend()
    ax3[0, 1].set_title(f'BIG Lo BM: Corr = {corr_4}')
    ax3[0, 1].set_ylabel('Return')
    ax3[1, 1].plot(ff_BMME['roll_ME2_BM2_std'] / 100, label = 'ff')
    ax3[1, 1].plot(sortsBMME_df.roll_me2_ffbm2_std, label = 'mine')
    ax3[1, 1].legend()
    ax3[1, 1].set_title(f'BIG Med BM: Corr = {corr_5}')
    ax3[1, 1].set_ylabel('Return')
    ax3[2, 1].plot(ff_BMME['roll_BIG_HiBM_std'] / 100, label = 'ff')
    ax3[2, 1].plot(sortsBMME_df.roll_me2_ffbm3_std, label = 'mine')
    ax3[2, 1].legend()
    ax3[2, 1].set_title(f'BIG Hi BM: Corr = {corr_6}')
    ax3[2, 1].set_ylabel('Return')
    # Number of firms
    fig4, ax = plt.subplots(3, 2, figsize = (32, 18))
    fig4.suptitle('6 BM/ME Sorts Number of Firms')
    ax[0, 0].plot(ff_BMME_nf['SMALL LoBM'], label = 'ff')
    ax[0, 0].plot(sortsBMME_df.me1_ffbm1_num_firms, label = 'mine')
    ax[0, 0].legend()
    ax[0, 0].set_title(f'Small Lo BM')
    ax[0, 0].set_ylabel('Number of Firms')

    ax[1, 0].plot(ff_BMME_nf['ME1 BM2'], label = 'ff')
    ax[1, 0].plot(sortsBMME_df.me1_ffbm2_num_firms, label = 'mine')
    ax[1, 0].legend()
    ax[1, 0].set_title(f'Small Med BM')
    ax[1, 0].set_ylabel('Number of Firms')

    ax[2, 0].plot(ff_BMME_nf['SMALL HiBM'], label = 'ff')
    ax[2, 0].plot(sortsBMME_df.me1_ffbm3_num_firms, label = 'mine')
    ax[2, 0].legend()
    ax[2, 0].set_title(f'Small Hi BM')
    ax[2, 0].set_ylabel('Number of Firms')

    ax[0, 1].plot(ff_BMME_nf['BIG LoBM'], label = 'ff')
    ax[0, 1].plot(sortsBMME_df.me2_ffbm1_num_firms, label = 'mine')
    ax[0, 1].legend()
    ax[0, 1].set_title(f'BIG Lo BM')
    ax[0, 1].set_ylabel('Number of Firms')

    ax[1, 1].plot(ff_BMME_nf['ME2 BM2'], label = 'ff')
    ax[1, 1].plot(sortsBMME_df.me2_ffbm2_num_firms, label = 'mine')
    ax[1, 1].legend()
    ax[1, 1].set_title(f'BIG Med BM')
    ax[1, 1].set_ylabel('Number of Firms')
    ax[2, 1].plot(ff_BMME_nf['BIG HiBM'], label = 'ff')
    ax[2, 1].plot(sortsBMME_df.me2_ffbm3_num_firms, label = 'mine')
    ax[2, 1].legend()
    ax[2, 1].set_title(f'BIG Hi BM')
    ax[2, 1].set_ylabel('Number of Firms')
    plt.show()

if __name__ == "__main__":
    main()