import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from datetime import date, timedelta
import yfinance as yf


def to_soup(url):
    url_response = requests.get(url)
    webpage = url_response.content
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup

how_many_days_in_the_past = 7

# Pulls the Insider Trading Statistics
def insider_trading():
    reader = csv.reader(open("ticker_and_edgar_cik.csv"), delimiter=',', quotechar='|')
    dictionary = {}
    for row in reader:
        if row[0] != "Ticker":
            dictionary[row[0].upper()] = row[1]

    print(dictionary)
    print(dictionary.keys())
    symbols = dictionary.keys()

    start = str(date.today()-timedelta(how_many_days_in_the_past))
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
                for url in urls:
                    soup = to_soup(url)
                    transaction_report = soup.find('table', {'id': 'transaction-report'})

                    t_chil = [i for i in transaction_report.children]
                    t_cont = [i for i in t_chil if i != '\n']

                    headers = [i for i in t_cont[0].get_text().split('\n') if i != '']
                    data_rough = [i for lst in t_cont[1:] for i in lst.get_text().split('\n') if i != '']
                    data = [data_rough[i:i + 12] for i in range(0, len(data_rough), 12)]
                    last_line = data[-1]
                    for i in data:
                        if (start > i[1]):
                            break
                        else:
                            if (i != last_line):
                                df_data.append(i)
                            else:
                                df_data.append(i)
                                page += 1
                                urls.append('https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK=' + str(
                                    cik) + '&type=&dateb=&owner=include&start=' + str(page * 80))
                if len(df_data) != 0:
                    print(df_data)
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
                    total_value_purchased = total_purch * price
                    total_value_sale = total_sale * price
                    net_difference = total_value_purchased - total_value_sale
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
                                           'Avg Shares Sold': f'{avg_sale:,}'},
                                          index=[0])

                    new_df.set_index('Symbol', inplace=True)
                    dfs.append(new_df)
                pbar.update(1)
            except:
                pbar.update(1)
                continue
    print('SCAN COMPLETE for period beginning: ' + start)
    if len(dfs)>1:
        combo = pd.concat(dfs)
    else:
        combo = dfs
    combo.to_excel('results.xlsx', index=True)

    return combo.sort_values('Net Diff', ascending=False).head(30)
