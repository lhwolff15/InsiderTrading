import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from IPython.display import clear_output
from tqdm import tqdm

#Looks up Edgar CIK Number
def symbol_to_cik(symbols):
    ticker_cik = pd.read_csv(r'Save and insert path to ticker_cik_edgar_cik.csv', delimiter=',')
    df = pd.DataFrame(ticker_cik)
    df.set_index('Ticker', inplace=True)
    new_symbols = [i.lower() for i in symbols]
    cik = [df.loc[i, 'CIK'] for i in new_symbols]
    return cik
#Looks up Symbol from CIK Number:
def cik_to_symbol(ciks):
    ticker_cik = pd.read_csv(r'Save and insert path to ticker_cik_edgar_cik.csv', delimiter=',')
    df = pd.DataFrame(ticker_cik)
    df.set_index('CIK', inplace=True)
    df = df[~df.index.duplicated(keep='first')]
    tickers = [df.loc[i, 'Ticker'] for i in ciks]
    new_tickers = [i.upper() for i in tickers]
    return new_tickers
#Turns URL into Soup object
def to_soup(url):
    url_response = requests.get(url)
    webpage = url_response.content
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup

#Pulls the Insider Trading Statistics
def insider_trading():
    ticker_csv = pd.read_csv(r'Save and insert path to ticker_cik_edgar_cik.csv', delimiter=',')
    symbols = [i.upper() for i in ticker_csv.Ticker]
    
    end = '2020-01-01'
    dfs = []
    with tqdm(total = len(symbols)) as pbar:
        for i in range(len(symbols)):
            try:
                lst = [symbols[i]]
                cik = symbol_to_cik(lst)
                page = 0
                beg_url = 'https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK='+str(cik[0])+'&type=&dateb=&owner=include&start='+str(page*80)
                urls = [beg_url]
                df_data = []
                for url in urls:
                    soup = to_soup(url)
                    transaction_report = soup.find('table', {'id':'transaction-report'})

                    t_chil = [i for i in transaction_report.children]
                    t_cont = [i for i in t_chil if i != '\n']

                    headers = [ i for i in t_cont[0].get_text().split('\n') if i != '']
                    data_rough = [i for lst in t_cont[1:] for i in lst.get_text().split('\n') if i != '' ]
                    data = [data_rough[i:i+12] for i in range(0,len(data_rough), 12)]
                    last_line = data[-1]
                    for i in data:
                        if (end > i[1]):
                            break
                        else:
                            if (i != last_line):
                                df_data.append(i)
                            else:
                                df_data.append(i)
                                page += 1
                                urls.append('https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK='+str(cik[0])+'&type=&dateb=&owner=include&start='+str(page*80))

                df = pd.DataFrame(df_data,columns = headers)                
                df['Purch'] = pd.to_numeric(df['Acquistion or Disposition'].apply(lambda x: 1 if x == 'A' else 0)
                               *df['Number of Securities Transacted'])
                df['Sale'] = pd.to_numeric(df['Acquistion or Disposition'].apply(lambda x: 1 if x == 'D' else 0)
                               *df['Number of Securities Transacted'])
                purch = df['Acquistion or Disposition'] == 'A'
                sale = df['Acquistion or Disposition'] == 'D'
                num_purch = len(df[purch])
                num_sale = len(df[sale])
                total_purch = int(df['Purch'].sum(skipna=True))
                total_sale = int(df['Sale'].sum(skipna=True))
                avg_purch = int(total_purch/num_purch)
                avg_sale = int(total_sale/num_sale)
                ratio = round(num_purch/num_sale, 2)
                new_df = pd.DataFrame({'Symbol': lst[0],
                                       'Purchases': num_purch,
                                       'Sales': num_sale,
                                       'Buy/Sell Ratio': ratio,
                                       'Total Bought': f'{total_purch:,}',
                                       'Total Sold': f'{total_sale:,}',
                                       'Avg Shares Bought': f'{avg_purch:,}',
                                       'Avg Shares Sold': f'{avg_sale:,}'},
                                        index = [0])

                new_df.set_index('Symbol', inplace=True)
                dfs.append(new_df)
                pbar.update(1)
            except:
                pbar.update(1)
                continue

    combo = pd.concat(dfs)    
    clear_output(wait=True)
    print('SCAN COMPLETE for period beginning: ' + end)
    combo = pd.concat(dfs)
    
    #combo.to_excel('Insert path where you want to save the .xlsx file', index = True)
    
    return combo.sort_values('Buy/Sell Ratio',ascending = False).head(100)
