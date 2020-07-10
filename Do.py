
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:27:26 2018

@author: nocool
"""

import time
import pandas as pd

# 获取当天的时间:
time = time.strftime("%F")
time = time.replace("-", "")
#time = int(time) - 3


def get_data():
    """"获取当日股票数据"""
    with open("Datas/data.txt", "w") as out_file:
        # 获取对应的文件名称并打开
        file_name = "沪深Ａ股" + str(time) + ".txt"
        with open(file_name, "r") as file:
            datas = file.readlines()
            for i in datas[1:-1]:
                # 字段分割:
                str1 = i.split("	")[0:-1]
                stat_date = str(time)
                stock_id = str1[0].strip()
                stock_name = str1[1].strip()
                chg = str1[2].strip()
                new_trade = str1[3].strip()
                change = str1[4].strip()
                vol = str1[5].strip()
                exchange = str1[6].strip()
                open_day = str1[7].strip()
                high = str1[8].strip()
                low = str1[9].strip()
                last_close = str1[10].strip()
                amount = str1[11].strip()
                industry = str1[12].strip()
                num_stock_lt = str1[13].strip()
                mv_stock_lt = str1[14].strip()
                mv_stock = str1[15].strip()
                Ipo_Date = str1[16].strip()
                str_point = str1[17].strip()
                vit = str1[18].strip()
                Rise_Cnt = str1[19].strip()
                Num_Stock = str1[20].strip()
                Amplitude = str1[21].strip()
                Area = str1[22].strip()
                Beta = str1[23].strip()
                data_str = stat_date + ',' + stock_id + ',' + stock_name + ','\
                    + chg + ',' + new_trade + ',' + change + ',' + vol + ',' +\
                    exchange + ',' + open_day + ',' + high + ',' + low + ',' +\
                    last_close + ',' + amount + ',' + \
                    industry + ',' + num_stock_lt + ',' + mv_stock_lt + ',' +\
                    mv_stock + ',' + Ipo_Date + ',' + \
                    str_point + ',' + vit + ',' + Rise_Cnt + ',' + Num_Stock +\
                    ',' + Amplitude + ',' + Area + ',' + Beta
                out_file.write(data_str + '\n')


def get_brunt_data():
    """获取当日主力数据"""
    
    # 主力买入
    df = pd.read_csv('1.xls',sep = '	',
                     names = ['buy_time','stock_name','price','4'],encoding='GBK')
    df['stat_date'] = time
    df['type']= 'BUY'
    buy_df = df['price'].str.split('/',expand=True)
    buy_df = pd.concat([df[['stat_date','type','buy_time','stock_name']],buy_df],axis=1)
    buy_df.rename(columns={0:'price',1:'vol'},inplace='True')
    
    # 主力卖出
    df = pd.read_csv('2.xls',sep = '	',
                     names = ['buy_time','stock_name','price','4'],encoding='GBK')
    df['stat_date'] = time
    df['type']= 'SELL'
    sell_df = df['price'].str.split('/',expand=True)
    sell_df = pd.concat([df[['stat_date','type','buy_time','stock_name']],sell_df],axis=1)
    sell_df.rename(columns={0:'price',1:'vol'},inplace='True')
    
    # 合并、导出数据
    result = pd.concat([buy_df,sell_df],axis=0)
    result.to_csv('Datas/zl_data.csv',sep = ',',header=0,index=0,encoding='GBK')


if __name__ == '__main__':
    get_data()
    get_brunt_data()
