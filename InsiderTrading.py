import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import DatabaseStocks as Ds
from datetime import date, timedelta
import yfinance as yf


def to_soup(url):
    url_response = requests.get(url)
    webpage = url_response.content
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup

how_many_days_in_the_past = 4

# Pulls the Insider Trading Statistics
def insider_trading():
    reader = csv.reader(open("ticker_and_edgar_cik.csv"), delimiter=',', quotechar='|')
    dictionary = {}
    for row in reader:
        if row[0] != "Ticker":
            dictionary[row[0].upper()] = row[1]

    print(dictionary)
    print(dictionary.keys())
    symbols = Ds.get_investing_lists()
    # symbols = dictionary.keys()

    start = str(date.today()-timedelta(how_many_days_in_the_past))
    end = str(date.today()+timedelta(30))
    dfs = []
    with tqdm(total=len(symbols)) as pbar:
        for stock in symbols:
            try:
                cik = dictionary[stock]
                page = 0
                beg_url = 'https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK=' + str(
                    cik) + '&type=&dateb=&owner=include&start=' + str(page * 80)
                urls = [beg_url]
                df_data = []

                soup = to_soup(beg_url)
                transaction_report = soup.find('table', {'id': 'transaction-report'})

                t_chil = [i for i in transaction_report.children]
                t_cont = [i for i in t_chil if i != '\n']

                headers = [i for i in t_cont[0].get_text().split('\n') if i != '']
                data_rough = [i for lst in t_cont[1:] for i in lst.get_text().split('\n') if i != '']
                data = [data_rough[i:i + 12] for i in range(0, len(data_rough), 12)]
                for i in data:
                    if end < i[1]:
                        continue
                    if start > i[1]:
                        break
                    else:
                        df_data.append(i)
                if len(df_data) != 0:
                    print(stock)
                    stock_data = yf.Ticker(stock)
                    price = float(stock_data.info["previousClose"])
                    df = pd.DataFrame(df_data, columns=headers)
                    df['Purch'] = pd.to_numeric(df['Acquistion or Disposition'].apply(lambda x: 1 if x == 'A' else 0)
                                                * df['Number of Securities Transacted'])
                    df['Sale'] = pd.to_numeric(df['Acquistion or Disposition'].apply(lambda x: 1 if x == 'D' else 0)
                                               * df['Number of Securities Transacted'])
                    purch = df['Acquistion or Disposition'] == 'A'
                    sale = df['Acquistion or Disposition'] == 'D'
                    num_purch = len(df[purch])
                    num_sale = len(df[sale])
                    total_purch = int(df['Purch'].sum(skipna=True))
                    total_sale = int(df['Sale'].sum(skipna=True))
                    total_value_purchased = int(total_purch * price)
                    total_value_sale = int(total_sale * price)
                    net_difference = int(pd.to_numeric(int(total_value_purchased - total_value_sale)))
                    if num_purch != 0:
                        avg_purch = int(total_purch / num_purch)
                    else:
                        avg_purch = 0
                    if num_sale !=0:
                        avg_sale = int(total_sale / num_sale)
                        ratio = round(num_purch / num_sale, 2)
                    else:
                        avg_sale = 0
                        ratio = 10000
                    if abs(net_difference) > 500000:
                        new_df = pd.DataFrame({'Symbol': stock,
                                               'Purchases': num_purch,
                                               'Sales': num_sale,
                                               'Buy/Sell Ratio': ratio,
                                               'Total Bought': f'{total_purch:,}',
                                               'Total Sold': f'{total_sale:,}',
                                               'Total Value Bought': f'{total_value_purchased:,}',
                                               'Total Value Sold': f'{total_value_sale:,}',
                                               'Net Diff': f'{net_difference:,}',
                                               'Avg Shares Bought': f'{avg_purch:,}',
                                               'Avg Shares Sold': f'{avg_sale:,}',
                                               'Link': "https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK=" +
                                                       str(cik)},
                                              index=[0])

                        new_df.set_index('Symbol', inplace=True)
                        dfs.append(new_df)
                pbar.update(1)
            except:
                print("upsy " + stock)
                pbar.update(1)
                continue
    print('SCAN COMPLETE for period beginning: ' + start)
    if len(dfs) > 1:
        combo = pd.concat(dfs)
    else:
        combo = dfs
    combo = combo.sort_values('Net Diff', ascending=False)
    combo.to_excel('results.xlsx', index=True)

    return combo
