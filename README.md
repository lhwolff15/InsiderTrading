# Insider Trading
Looks up insider trading transactions in a date range

This program is designed to pull all the insider trading transactions within a specific date range from the Securities and Exchange Commission (SEC) website. Before running this code, you need to download the ticker_cik_edgar_cik.csv file that is included on the main page of this repository. This file contains all the tickers in the SEC EDGAR database along with their corresponding CIK number (how the SEC organizes their data for each company). Enter that file path into the pd.read_csv('') blank in Lines 10, 18, and 34. Lines 1-6 are the various imports needed to run this file. Lines 8-30 are additional functions I've created to ease the process. The first converts a symbol into a CIK number, the second function does the opposite of the first (CIK--->symbol), and the third function converts a url into a BeautifulSoup object. 

Lines 33-108 contain the main data-gathering function. Right now, the function is set to gather insider trading data for every publicly listed company. All you have to do is enter insider_trading() and the function will start to run. Currently, the runtime for gathering data for all public companies tends to be between 5 and 10 hours. Thankfully, you most likely wont need to run this function more than once or twice a quarter. The outputted data is in descending order of the buy-to-sell ratio. You can change this easily by setting ascending value in Line 106 to True instead of False.

In order to change the date range, simply change the "end" variable to another date in the format: 'YYYY-MM-DD'.
    
If you would like to save the data into an excel file, uncomment Line 106 and enter in your desired path to save the document. If you want to edit the function yourself to look up specific symbols, just delete Lines 34 and 35 and put "def insider_trading(symbols):" into Line 33. Then you can run the function with a specific set of symbols; Ex: insider_trading(['AAPL','TSLA']). Note that the symbols need to be in a list in order to run the function.


Any feedback would be greatly appreciated!

# Edit:
I wanted to include a link the page where the data is drawn from on the SEC site (the table on the bottom of the page). I just used Apple as an example.
https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK=0000320193
