import random


list_of_technology = ["AAPL", "ACIW", "ACN", "ADBE", "ADI", "ADP", "ADSK", "AKAM", "AMD", "AMAT",
                      "ANET", "ANSS", "ARW", "ATVI", "AVGO", "AVT", "AZPN", "BA", "BB", "BLL",
                      "BLKB", "BR", "CDK", "CDNS", "CERN", "CHKP", "CIEN", "COMM", "COUP",
                      "CREE", "CRM", "CRUS", "CRWD", "CSCO", "CVLT",
                      "CY", "CYBR", "DBX", "DDD", "DDOG", "DLB", "DOCU", "DOX", "DXC", "EA", "EFX", "EQT",
                      "FCEL", "FDS", "FEYE", "FIT", "FTNT", "FVRR", "G", "GE", "GLW", "GPRO",
                      "GRMN", "GRPN", "HIMX", "HPE", "HPQ", "IAC", "IBM",
                      "INFO", "INTC", "IPGP", "IT", "JBL", "JCOM", "KEX", "LOGI",
                      "MCHP", "MSFT", "MCO", "MDB", "MDRX", "MOMO", "MSCI", "MSI", "MU", "NCR",
                      "NLOK", "NLSN", "NOW", "NUAN",
                      "NVDA", "NTAP", "NTGR",  "NXPI", "OKTA", "ON", "PANW", "PAYX", "PBI",
                      "PCG", "PFPT", "PING", "PTC", "PINS", "QCOM", "ORCL", "QRVO", "OTEX", "SABR",
                      "SHOP", "SNAP", "SPCE", "SPGI", "SPLK", "SQ", "SSNC",
                      "STM", "STX", "SYY", "SWKS", "TEAM", "TER", "TEVA", "TLND",
                      "TSM", "TTWO", "TWLO", "VEEV", "VLO", "VMW", "VRSK", "VSAT",
                      "WDC", "WIX", "WORK", "ZM", "XRX", "ZBRA", "ZEN", "ZNGA", "ZS"]

list_of_materials = ["AA", "ATI", "BLL", "CCJ", "CENX", "CCK", "UFS", "EXP", "EGO", "FCX", "GPK",
                     "IP", "KGC", "LPX", "MLM", "NEM", "NUE", "OC", "OI", "PKG", "PAAS", "RS", "RGLD", "SON", "SCCO",
                     "TRQ", "X", "VALE", "VMC", "WPM", "AUY", "MMM", "AIV", "ALB", "APD", "ASH", "AVY", "CE", "CX",
                     "CF", "CTVA", "DOW", "DD", "EXP", "EMN", "ECL", "IFF", "FMC", "HUN", "ICL", "LYB", "MEOH", "MOS",
                     "NEU", "POL", "PPG", "RPM", "SHW", "SLGN", "SQM", "GRA", "WLK"]

list_of_communication_services = ["ACIA", "GOOG", "AMCX", "T", "BIDU", "CTL", "CHTR", "CHL", "CHU", "CHT",
                                  "CMCSA", "DISCA", "DISH", "DIS", "EXPE", "FFIV", "FB", "FOXA", "FTR", "GDDY",
                                  "GRUB", "IPG", "LBTYA", "LN", "LYFT", "MTCH", "NFLX", "OMC",
                                  "PINS", "RCI", "ROKU", "SBAC", "SNAP", "SPOT", "S", "TMUS", "TU", "TTD", "TRIP",
                                  "TWTR", "UBER", "VEON", "VZ", "VIAC", "WB", "YNDX", "Z"]

list_of_utilities_and_real_estate = ["AES", "AEE", "AEP", "AWK", "WTR", "ATO", "CMS", "ED", "DUK", "EIX", "EVRG",
                                     "EXC", "FE", "MDU", "NFG", "NEE", "NI", "NRG", "OGE", "PPL", "PEG", "SRE", "SO",
                                     "UGI", "XEL", "AGNC", "ARE", "AMH", "AVB", "BXP", "CPT", "CBL", "CBRE", "CB",
                                     "CLNY", "CXP", "ESS", "FRT", "GLPI", "JLL", "PB", "SVC", "SITC"]

list_of_energy = ["LNT", "AR", "APA", "BKR", "COG", "CNP", "CHK", "CVX", "SNP", "CNX", "CXO", "COP",
                  "CLB", "DCP", "DVN", "DO", "D", "DRQ", "DTE", "ENS", "EPD", "EOG", "EQT", "XOM", "FSLR", "GPOR",
                  "HAL", "HP", "HES", "HFC", "KMI", "LPI", "MMP", "MRO", "MPC", "MUR", "NBR", "NOV", "NBL",
                  "NS", "OAS", "OXY", "OII", "OKE", "PBR", "PSX", "PXD", "QEP", "RRC", "RES", "SSL", "SLB", "SM",
                  "SWN", "SPWR", "TRGP", "FTI", "VAL", "VLO", "VSLR", "WLL", "WMB", "WEC", "INT"]

list_of_industrials = ["AOS", "AYI", "AEIS", "ACM", "AER", "AGCO", "ALLE", "ALSN", "AME", "APH", "AXE", "BA", "CAT",
                       "CLH", "CGNX", "CFX", "CR", "CSX", "CMI", "DE", "DCI", "DOV", "ETN", "EMR", "FAST", "FDX",
                       "FLEX", "FLS", "FLR", "GD", "GE", "GWR", "GLNG", "GGG", "HXL", "HON", "HII", "IEX", "ITW",
                       "IR", "ITRI", "JEC", "JCI", "KSU", "KBR", "KMT", "KEYS", "KEX", "KNX", "LII", "LECO", "LFUS",
                       "LMT", "MIC", "MIDD", "MSM", "NDSN", "NOC", "NSC", "ODFL", "PH", "PNR", "PWR", "RTN", "RBC",
                       "RSG", "ROK", "ROP", "R", "SPR", "SPXC", "TDY", "TEX", "TXT", "TTC", "TDG", "TRMB", "TRN", "UAL",
                       "URI", "UTX", "UNP", "UPS", "VMI", "WAB", "WM", "WCC", "XPO", "XYL"]

list_of_consumer_discretionary = ["ANF", "ADNT", "ALK", "BABA", "AMZN", "AAL", "AEO", "APTV", "ASNA", "AN", "AZO",
                                  "CAR",
                                  "BBBY", "BBY", "BJ", "BLMN", "BWA", "BV", "EAT", "BC", "BURL", "CAL", "GOOS", "CPRI",
                                  "KMX", "CRI", "CVNA", "CHWY", "CMG", "CHRW", "CNK", "CTAS", "COLM", "CPA", "CPRT",
                                  "DHI", "DAN", "DLPN", "DAL", "DKS", "DDS", "DOL", "DNKN", "EBAY", "ELF", "ETSY",
                                  "RACE", "FCAU", "FL", "F", "FBHS", "FOSL", "GME", "GPS", "GTX", "GPC", "GIL", "GM",
                                  "GNC", "GT", "HRB", "HBI", "HOG", "HAS", "HD", "H", "IGT", "IRBT", "ITT",
                                  "JPC", "SJM", "JD", "JBLU", "JMIA", "KAR", "KSS", "KTB", "LB", "LVS", "LEA", "LEG",
                                  "LEN", "LEVI", "LYV", "LKQ", "LOW", "LULU", "M", "MANU", "MAN", "MAR", "MAS", "MAT",
                                  "MCD", "MLCO", "MELI", "MGM", "MHK", "NWL", "NKE", "NIO", "JWN", "NVEE", "OSK",
                                  "PTON", "PDD", "PII", "POOL", "PHM", "PVH", "RL", "RVLV", "RHI", "RCL", "SBH",
                                  "SGMS", "SMG", "SEE", "SIX", "SNA", "LUV", "SAVE", "SWK", "SBUX", "TPR",
                                  "TEN", "TSLA", "MSG", "REAL", "TJX", "THO", "TIF", "TOL", "TSCO", "TUP",
                                  "ULTA", "UAA",
                                  "URBN", "VFC", "VC", "W", "WEN", "WHR", "WSM", "WW", "WYND", "WYNN"]

list_of_consumer_staples = ["MO", "ADM", "BYND", "BRFS", "BG", "CPB", "CHD", "CLX", "KO", "CL", "CAG", "STZ", "COTY",
                            "DG", "ENR", "EL", "FLO", "GIS", "HLF", "HLT", "HRL", "INGR", "K", "KDP", "KMB", "KHC",
                            "KR", "MKC", "TAP", "MDLZ", "PEP", "PM", "RAD", "SPB", "SFM", "SYY", "TGT",
                            "HAIN", "TSN", "UNFI", "VFF", "WBA", "WMT", "YUM"]

list_of_healthcare = ["ABT", "ABBV", "ACAD", "ALC", "ALXN", "ALGN", "ALKS", "AGN", "ALNY", "ABC", "AMGN", "ANTM",
                      "ARNA", "AVTR", "BHC", "BAX", "BDX", "BIO", "BIIB", "BMRN", "BSX", "BMY", "BKD", "BRKR", "CARA",
                      "CAH", "CNC", "CI", "COO", "CRBP", "CRSP", "CVS", "DHR", "DVA", "EW", "LLY", "EHC", "ENDP",
                      "EXAS", "GILD", "GWPH", "HCA", "HUM", "IDXX", "ILMN", "INCY", "INVA", "ISRG", "NVTA", "IQV",
                      "JAZZ", "JNJ", "LH", "LVGO", "MCK", "MD", "MDT", "MRK", "MTD", "MYL", "NGM", "OPK", "PKI",
                      "PFE", "QGEN", "REGN", "SGEN", "SYK", "TDOC", "TFX", "THC", "TEVA", "TMO", "TLRY", "UNH",
                      "UHS", "VAR", "VRTX", "WAT", "ZBH", "ZTS"]

list_of_financials = ["AFC", "AIG", "ACC", "AXP", "AMT", "AMP", "NLY", "AON", "ACGL", "ARCC", "AJG", "AIZ", "AGO",
                      "AXS", "BAC", "BK", "BKU", "BLK", "BOKF", "BRO", "COF", "CBOE", "CBRE", "SCHW",
                      "CIM", "CINF", "CIT", "C", "CME", "CNO", "CMA", "CBSH", "CXW", "BAP", "CCI", "CWK", "DLR", "DFS",
                      "DEI", "DRE", "ETFC", "EWBC", "EQIX", "EQR", "RE", "EXR", "FII", "FIS", "FNF", "FITB", "FHN",
                      "FRC", "BEN", "CFR", "GNW", "GPN", "GS", "HBAN", "PEAK", "HIG", "HST", "HHC", "IEP", "ICE",
                      "IBN", "IVZ", "IRM", "ITUB", "JKHY", "JHG", "JEF", "JPM", "KEY", "KRC", "KIM", "KKR", "LAZ",
                      "LM", "LC", "TREE", "LNC", "L", "LPLA", "MTB", "MKL", "MMC", "MA", "MET", "MTG", "MS", "NDAQ",
                      "NTRS", "NYCB", "ORI", "PYPL", "PBCT", "PNC", "BPOP", "PFG", "PSEC", "PRU", "RDN", "RJF",
                      "RLGY", "REG", "RF", "RGA", "RNR", "SEIC", "SBNY", "SLM", "SQ", "STT", "SF", "STI", "SIVB",
                      "SNV", "TROW", "AMTD", "ALL", "BX", "PGR", "TD", "TRV", "TFC", "TWO", "USB", "UBS",
                      "UMPQ", "UNM", "V", "WRB", "WBS", "WFC", "WELL", "WU", "WEX", "WLTW", "WETF", "ZION"]


european_stocks = ["ADS.DE", "ALO.PA", "BAYN.DE", "BMW.DE", "IFX.DE", "LHA.DE", "MAERSK-B.CO", "NOVO-B.CO",
                   "NZYM-B.CO", "SU.PA", "VWS.CO"]


def get_lists():
    print(len(list_of_industrials + list_of_technology + list_of_communication_services + list_of_energy +
              list_of_utilities_and_real_estate + list_of_materials + list_of_consumer_discretionary +
              list_of_consumer_staples + list_of_healthcare + list_of_financials))
    list_CFD = list_of_industrials + list_of_technology + list_of_communication_services + list_of_energy + \
        list_of_utilities_and_real_estate + list_of_materials + list_of_consumer_discretionary + \
        list_of_consumer_staples + list_of_healthcare + list_of_financials
    random.shuffle(list_CFD)
    return list_CFD


# investing side of Trading212

investing_list_of_energy = ["ADES", "AES", "ARPL", "AMRC", "AMSC", "APA", "ARCH", "AROC", "BKR", "BLDP", "BSM", "BCEI",
                            "COG", "CRC", "CPE", "CNQ", "CSIQ", "CQP", "CVX", "XEC", "CMS", "CRK", "CXO", "COP", "CEIX",
                            "CLR", "CZZ", "CVI", "DCP", "DVN", "DO", "FANG", "DRQ", "DTE", "ENB", "ET", "ENLC", "ENPH",
                            "ETR", "EPD", "EVA", "EOG", "EQT", "EQNR", "ES", "EXC", "EXTN",
                            "XOM", "FSLR", "FCEL", "GEOS", "HAL", "HP", "HES", "HEP", "JKS", "KMI", "KOS", "MMP", "MRO",
                            "MPC", "MPLX", "MUR",
                            "MUSA", "NC", "NOV", "NGS", "NEE", "NBL", "DNOW", "OMP", "OXY", "OKE", "PBF", "BTU", "PBA",
                            "PBR", "PSX", "PSXP", "PXD", "PAA", "PLUG", "RRC",
                            "SLB", "SHLX", "SEDG", "SO", "SWN", "SPI", "SPWR", "RUN", "TRGP", "TRNX", "TRP", "FTI",
                            "TOT", "RIG", "VAL", "VLO", "VET", "VNOM", "VSLR", "VOC", "WES", "WMB", "WPX"]

investing_list_of_materials = ["MMM", "ASIX", "AEM", "AIV", "ADP", "ALB", "AA", "AMCR", "AU", "AVY", "BCPC", "BLL",
                               "GOLD", "BBL", "BHP", "BCC", "BREE.L", "CCJ", "CSL", "CRS", "CE", "CF", "CLF", "CDXS",
                               "BVN", "DOW", "DRD",
                               "DD", "EMN", "ESI", "UUUU", "EQX", "AG", "FMC", "FNV", "FCX", "GCP", "ICL", "IP", "IFF",
                               "LIN", "LAC", "LTHM", "LYB", "MLM", "MATW", "MDU", "NEM", "NXE", "NTIC", "NUE", "NTR",
                               "OI", "PAAS", "PPG", "RIO", "RGLD", "SAND", "SSL", "SCHN", "SEE", "SHW", "SBSW", "SMTS",
                               "SCOO", "STLD", "MOS", "TREX", "URG", "UEC", "VVV", "VRS", "VMC", "WRK", "WPM", "AUY"]

investing_list_of_industrials = ["AOS", "AIR", "ATU", "ADSW", "AEIS", "ACM", "AVAV", "ALG", "ALRM", "ALK", "ALGT",
                                 "ALLE", "AMOT", "AME", "APH", "AGX", "ATRO", "AAXN", "BMI", "BDC", "BHE", "BEST",
                                 "BLNK", "BE", "BA", "BGG", "CHRW", "WHD", "CAI", "CAMT", "CNI", "CARR", "CAT", "CFX",
                                 "CTG", "CPA", "CVA", "CYRX", "CSX", "CMI", "CW", "CYBE", "DE",
                                 "DAL", "DOV", "DYNT", "ETN", "ESLT", "EME", "EMR", "WATT", "ERII", "AQUA", "EXPD",
                                 "EXPO", "FAST", "FDX", "FLS", "FLR", "FORR", "FTV", "FRG", "FELE", "FTDR", "GLOG",
                                 "GLOP", "GD", "GE", "GFL", "EAF", "GHM", "HEES", "HDS", "HCCI",
                                 "HON", "HWM", "HUBB", "ICHR", "ITW", "IR", "IVAC", "ITRI", "JBHT", "J", "JBLU", "JBT",
                                 "JCI", "KAI", "KSU", "KEYS",
                                 "KE", "LHX", "LSTR", "LTM", "LECO", "LFUS", "LMT", "MAGS", "MNTX", "MRCY", "MIDD",
                                 "MTSC", "NSSC", "NATI", "LASR", "NAT", "NSC", "NOC", "NOVT", "ODFL", "OSIS", "OTIS",
                                 "PCAR", "PH", "PNR", "POWL", "PWR", "RBC", "RSG", "RGP",
                                 "RXN", "ROK", "ROP", "R", "SAIA", "SHIP", "SITE", "SNA", "LUV", "SAVE", "SPXC", "FLOW",
                                 "SXI", "SRCL", "TEL", "TNC", "TTEK", "TXT", "GBX", "HCKT", "SHYF", "TKR", "TOPS",
                                 "BLD", "TRNS", "TDG", "TRMB", "TWIN", "UNP", "UPS", "URI", "VSEC", "GWW", "WCN", "WM",
                                 "WTS", "WLDN", "WWD", "WKHS", "WRTC", "XYL", "ZTO"]

investing_list_of_consumer_discretionary = ["FLWS", "TWOU", "AAN", "ANF", "ACTG", "ACCO", "AEY", "ADNT", "ATGE", "AAP",
                                            "BABA", "AMZN", "AMC", "AAL", "APEI", "AMWD", "CRMT", "APTV", "ARC", "FUV",
                                            "ARCO", "ASGN", "AN",
                                            "AZO", "CAR", "AZEK", "BBSI", "BECN", "BBBY", "BBY", "BGSF", "BGFV", "BJRI",
                                            "BLMN", "APRN", "BOOT", "BWA",
                                            "BYD", "BRC", "BV", "BC", "BKE", "BLDR", "BURL", "CZR", "CAL", "CWH",
                                            "GOOS", "CPRI", "KMX", "CCL",
                                            "CVNA", "CSPR", "CATO", "FUN", "CHWY", "CMG", "CHH", "CHUY", "CNK", "CTAS",
                                            "CPRT", "CTVA", "CRVL", "CROX", "DHI", "DRI",  "PLAY", "TACO",
                                            "DENN", "DKS", "DPZ", "DKNG", "EBAY", "ECL", "LOCO", "EEX", "ETSY",
                                            "FTCH", "RACE", "FCAU", "FCFS", "FVRR", "FL", "F", "FRSX", "FOR", "FOSL",
                                            "FOXF", "FRPT", "FNKO",
                                            "GME", "GPS", "GTX", "GM", "GNTX", "GPC", "GDEN", "GT", "GHG", "GFF",
                                            "GRWG", "GES", "HRB", "HBI", "HOG", "HAS",
                                            "HSII", "MLHR", "HIBB", "HLT", "HMSY", "HD", "HUD", "NSP", "TILE", "IRBT",
                                            "JD", "JMIA", "KELYA", "KEQU", "KFRC", "KBAL", "KSS", "KTB",
                                            "KFY", "KRUS", "LB", "LAKE", "LAUR", "LEG", "LEN", "LEVI", "LQDT", "LAD",
                                            "LYV", "LOW", "LULU", "M", "MANU",
                                            "MAN", "HZO", "MAR", "MAS", "MAT", "MCD", "MELI", "MTH", "METX", "MGM",
                                            "MOGU", "MCRI", "MNRO", "NRC", "EDU", "NWL", "NKE",
                                            "NIO", "JWN", "NCLH", "ORLY", "OSW", "OSTK", "PTON", "PENN", "PETQ", "PETS",
                                            "PDD", "PLNT", "PLYA", "PII", "RL", "PHM", "NEW", "PVH", "QRTEA", "RDIB",
                                            "RCII", "QSR", "RVLV", "RHI", "ROST", "RCL", "RUHN", "RUTH", "SBH", "SGMS",
                                            "SEAS", "SHAK", "SCVL", "SSTI", "SIG", "SIX", "SKY",
                                            "SKYW", "SNBR", "SLM", "SPWH", "SSI", "SWK", "SBUX", "SHOO", "SFIX", "STRA",
                                            "TAL", "TPR", "TH", "TMHC", "TSLA", "TXRH", "CAKE", "PLCE", "MIK", "REAL",
                                            "WEN", "THO",
                                            "TIF", "TJX", "TOL", "TM", "TSCO", "TNET", "TBI", "ULTA", "UAA", "UNF",
                                            "UAL", "URBN", "VFC", "MTN", "VVI", "VIPS", "SPCE", "VSTO", "VRM", "WTRH",
                                            "WSG", "W", "WSTG", "WHR", "WING", "WINA", "WW", "WYND", "WYNN", "XSPA",
                                            "YUMC", "YUM", "YJ", "ZUMZ"]

investing_list_of_consumer_staples = ["MO", "BUD", "ADM", "BGS", "BYND", "BIG", "BJ", "BTI", "BF-A", "BG", "CALM",
                                      "CVGW", "CPB", "CELH", "CHD", "CLX", "KO", "CCEP", "CL", "CAG",
                                      "STZ", "COST", "COTY", "CRON", "DAR", "DEO", "DG", "DLTR", "ELF", "EL", "GIS",
                                      "GO", "HELE", "HLF",
                                      "HRL", "IMKTA", "IPAR", "SJM", "K", "KDP", "KMB", "KHC", "KR", "MKC", "MGPI",
                                      "TAP", "MDLZ", "MNST", "FIZZ", "OLLI", "PEP", "PAHC",
                                      "PM", "PPG", "PG", "RAD", "SAFM", "SPTN", "SYY", "TGT", "SAM", "CHEF", "HSY",
                                      "TSN", "UN", "UVV", "VFF", "WBA", "WMT", "WMK"]

investing_list_of_healthcare = ["TXG", "ABT", "ABBV", "ABMD", "ACIU", "ACHC", "ACAD", "AXDX", "XLRN", "ACOR", "AHCO",
                                "ADPT", "ADUS", "ADVM", "AERI", "AGEN", "AGRX", "A", "AGIO", "AIMT", "AKCA", "AKBA",
                                "AKRO", "AKUS", "ALBO",
                                "ALC", "ALEC", "ALXN", "ALGN", "ALKS", "ALLK", "AHPI", "ALLO", "ALNY", "AMRN", "AMED",
                                "AMS", "ABC", "AMGN", "FOLD", "AMN", "AMRX", "AMPH", "ANAB", "ANGO", "ANIP", "ANIK",
                                "ANPC", "ATRS", "ANTM", "APLS", "APHA", "AMEH", "APLT", "APRE", "APTO", "ARCT", "ARQT",
                                "ARDX",
                                "ARNA", "ARWR", "ARVN", "ASDN", "ASMB", "AZN", "ATRA", "ATNX", "ATHX", "BCEL", "ATRC",
                                "ATRI", "ACB", "AVDL", "AVNS", "AVTR", "AVGR", "AVRO", "AXNX", "AXGT", "AXSM",
                                "BXRX", "BHC", "BAX", "BEAM", "BDX", "BGNE", "BLCM", "BYSI", "TECH", "BASI", "BIOC",
                                "BCRX", "BDSI", "BIIB", "BLFS", "BMRN", "PHGE", "BNTX", "BSTC", "BEAT", "BTAI",
                                "BLUE", "BPMC", "BSX", "BBIO", "BMY", "BRKR", "BNR", "CABA", "CTST", "CGC", "CARA",
                                "CRDF", "CAH", "CSII", "CDNA", "CSTL", "CPRX", "CNC", "CNTG", "CERS", "GIB", "CCXI",
                                "CBPO", "CPHI", "CI", "CLIN.L", "CLVS", "CODX", "COCP", "CHRS", "COLL", "CGEN", "CNST",
                                "CRBP", "CORT", "CRTX", "CVET", "CRNX", "CRSP",
                                "CCRN", "CUE", "CUTR", "CVS", "CBAY", "CYTK", "CTMX", "DHR", "DVA", "DCPH", "DNLI",
                                "XRAY", "DMTK", "DXCM", "DRNA", "DFFN", "DVAX", "EGRX", "EDIT", "EW", "LLY", "ENTA",
                                "ENDP", "EPZM", "ESPR", "ESTA", "EXAS", "EXEL", "FATE", "FGEN", "FMTX",
                                "FREQ", "FUSN", "GTHX", "GBIO", "GNPX", "GERN", "GILD", "GSK", "GBT", "GOSS", "GH",
                                "GHSI", "GWPH", "HALO", "HBIO", "HCA", "HQY", "HTBX", "HSIC", "HEPA", "HRTX", "HSKA",
                                "HEXO", "HOLX", "FIXX", "HZNP", "HUM", "IMAB", "IBIO", "ICLR", "ICUI", "IDXX", "IGMS",
                                "ILMN", "IMGN", "IMMU", "IMRN", "NARI", "INCY", "IFRX", "INMD", "INVA", "INGN", "INO",
                                "INSM", "PODD", "NTEC", "LOGM", "NTLA", "ICPT", "ISRG", "NVTA", "IONS", "IOVA", "IQV",
                                "IRTC", "IRWD", "JAZZ", "JNJ", "KALA", "KRTX", "KPTI", "KNSA", "KTOV", "KOD", "KRYS",
                                "KURA", "LH", "LTRN", "LNTH", "LMAT", "LHCG", "LGND", "LIVN", "LVGO", "LMNX", "MGNX",
                                "MDGL", "MGLN", "MNK", "MNKD", "MASI",
                                "MCK", "MEDP", "MDT", "MEIP", "MGTX", "MRK", "VIVO", "MMSI", "MRSN", "MRUS", "MTP",
                                "MRTX", "MIRM", "MRNA", "MTEM", "MNTA", "MORF", "MYL", "MYOK", "MYGN", "NSTG", "NH",
                                "NK", "NTRA", "NTUS", "NKTR", "NEOG", "NEO", "NBIX", "NXTC", "NGM", "NVS", "NVAX",
                                "NVO", "NVCR", "NUVA", "OCGN", "ODT", "OMER", "OTRK", "OPK", "OPCH", "OGEN", "OSUR",
                                "ORTX", "OGI", "OFIX", "KIDS", "OYST", "PACB", "PCRX", "PRTK", "PASG", "PDCO",  "PAVM",
                                "PDLI", "PKI", "PRGO", "PFE", "PHAT", "PLRX", "PYPD", "PPD", "PRAH", "PGEN", "PRPO",
                                "DTIL", "PINC", "PRVL", "PRNB", "PROG", "PGNY", "PRTA", "PRVB", "PTCT", "PULM", "PLSE",
                                "PBYI", "QLGN", "QTRX", "DGX", "QDEL", "QTNT", "RDUS", "RDNT", "RAPT", "RETA", "RDHL",
                                "REGN", "RGNX", "RLMD", "RPTX", "RGEN", "REPL", "KRMD", "RTRX", "RVNC", "RVMD", "RYTM",
                                "RCKT", "RMTI", "RPRX", "RUBY", "SAGE", "SNY", "SRPT", "SRRK", "SGEN", "SNCA", "SWAV",
                                "SIBN", "SIGA", "SILK", "SINT", "SDC", "SOLY", "SRNE", "SWTX", "STAA", "STOK", "SYK",
                                "SNSS", "SUPN", "SGRY", "SRDX", "SNDX", "SYNH", "SNV", "SYRS", "TCMD", "TNDM", "TARO",
                                "TDOC", "TFX", "THC", "TEVA", "TGTX", "COO", "ENSG", "PRSC", "TXMD", "TBPH", "TMO",
                                "TLRY", "TMDI", "TTNP", "TVTY", "TBIO", "TMDX",
                                "TCDA", "TRIL", "TRIB", "GTS", "TPTX", "TWST", "RARE", "QURE", "UNH", "UTHR", "UHS",
                                "URGN", "VNDA", "VREX", "VAR", "VXRT", "VBIV", "VCYT", "VRTX", "VIE", "VMD", "VKTX",
                                "VIR", "VYGR", "WAT", "WST", "WMGI", "XBIT", "XNCR", "XENE", "YMAB", "ZLAB", "ZNTL",
                                "ZBH", "ZIOP", "ZTS", "ZGNX", "ZYXI"]

investing_list_of_financials = ["SRCE", "QFIN", "JFU", "AER", "AMG", "AFL", "AGMH", "AGNC", "AIG", "AL", "ALEX", "ADS",
                                "AB", "ALL", "ALLY", "AMBC", "AXP", "AMP", "ABCB", "AMSF", "NLY",
                                "AON", "ARI", "APO", "ACGL", "ARCC", "ARES", "AROW", "AJG", "APAM", "ASB", "AC", "AIZ",
                                "AGO", "AUB", "AXS", "BANF", "BSMX", "BAC", "BOH", "BMO", "BK", "BNS", "OZK", "BKU",
                                "BANR", "BBDC", "BCBP", "BRK-B",
                                "BLK", "BCOR", "BOKF", "BDGE", "BHF", "BRLIU", "BYFC", "BAM", "BPYU", "BRO", "CADE",
                                "CM", "COF", "CPTA", "CFFN", "CATM", "CATY", "CBTX", "SCHW", "CIM", "CB", "CCXX",
                                "CINF", "C", "CHCO", "CME", "CCH", "COLB", "CMA", "CBU",
                                "CODI", "COWN", "BAP", "CACC", "CRT", "CVBF", "DLR", "DFS", "DX", "ETFC", "EGBN",
                                "EHTH", "EFC", "ECPG", "ESGR", "EPR", "ERIE", "ESNT", "EVR", "FANH", "FIS", "FITB",
                                "BUSE", "FCNCA", "FFIN", "FHB", "FHN",
                                "FISV", "FLT", "FEAC", "WPF", "FMCI", "BEN", "FRHC", "FSK", "FULT", "FUSE", "FUTU",
                                "GATX", "GFN", "GNW", "GBCI", "GOOD", "GAIN", "GPN", "GL", "GS", "GSHD", "AJX", "GSKY",
                                "GDYN", "HLNE", "HASI", "HIG", "HDB", "HTLF", "HOPE", "HRZN", "HLI", "HSBC", "HBAN",
                                "IBKR", "ICE", "IVZ", "IVR", "ISBC", "ITUB",
                                "JKHY", "JRVR", "JHG", "JEF", "JFIN", "JPM", "KMPR", "KW", "KCAC", "KEY", "KNSL", "KKR",
                                "LADR", "LKFN", "LCA", "LAZ", "LGC", "LM", "TREE", "LX", "LNC", "L", "MTB", "MAIN",
                                "MFC", "MKL", "MMC",
                                "MA", "MCY", "MET", "MFA", "MC", "MGI", "MS", "COOP", "NDAQ", "NAVI", "NNI", "NRZ",
                                "NYMT", "NREF", "NKLA", "NMIH", "NTRS", "NWBI", "OCFC", "ONB", "ORI", "OXLC", "PPBI",
                                "PACW", "PLMR", "PKBK", "PAYC", "PYPL", "PAYS", "PBCT", "PNFP", "PNC",
                                "BPOP", "PFC", "PRA", "PGR", "PSEC", "PRU", "QIWI", "QD", "RDN", "RWT", "RF", "RNST",
                                "RPAY", "RY", "SAFT", "SASR", "SLCT", "SIGI", "SLQT", "FOUR", "SUNS", "SBSI", "SPAQ",
                                "SQ", "STWD", "STFC", "STT", "SCM", "STNE", "SLF", "SIVB", "SYF", "TROW",
                                "AMTD", "TCBI", "TFSL", "BX", "THG", "TRV", "TPRE", "TSBK", "TD", "SHLL", "TOWN.L",
                                "TSC",
                                "TFC", "TRUP", "TWO", "USB", "UMBF", "UMPQ", "UBSI", "UIHC", "UVE", "UNM", "VLY", "VEL",
                                "VCTR", "VBFC", "VIRT", "V", "WAFD", "WSBF", "WSBC", "WFC", "WAL", "WNEB", "WU", "WHG",
                                "WLTW", "WTFC", "XP", "ZION"]

investing_list_of_technology = ["ONEM", "DDD", "ATEN", "ACN", "ACIW", "ATVI", "ADBE", "ADTN", "AMD", "AGYS", "API",
                                "AIRG", "AKAM", "KERN", "AKTS", "MDRX", "AOSL", "AYX",
                                "AMBA", "AMSWA", "AMKR", "ASYS", "ADI", "PLAN", "ANSS", "ATEX", "APPF", "APPN", "AAPL",
                                "APDN", "AMAT", "AAOI", "ANET", "ARLO", "ASML",
                                "AZPN", "ASUR", "TEAM", "ATOM", "AUDC", "AEYE", "ADSK", "ADP", "AVNW", "AVID", "AVT",
                                "AWRE", "ACLS", "AXTI", "BAND", "BZUN",
                                "BNFT", "BILI", "BILL", "BLKB", "BB", "BL", "BAH", "BRQS", "EPAY", "BOX", "BCOV",
                                "AVGO", "BRKS", "CCMP", "CACI", "CDNS",
                                "CAMP", "CASA", "CDW", "CRNT", "CRNC", "CERN", "CEVA", "CHNG", "ECOM", "CHKP", "IMOS",
                                "CRUS", "CSCO", "CTXS", "CLFD", "CLDR", "NET", "CTSH",
                                "COHR", "COMM", "CPSI", "CNDT", "CLGX", "CSOD", "GLW", "CSGP", "COUP", "CREE", "CRWD",
                                "CSGS",
                                "CTS", "CUB", "CYBR", "DJCO", "DAKT", "DDOG", "DELL", "DSGX", "DGII", "DMRC", "APPS",
                                "DIOD", "DOCU", "DOMO", "DOYU", "DBX", "DSPG", "DXC", "EBON", "EBIX", "EGAN", "ESTC",
                                "EA",
                                "EMKR", "EMIS.L", "DAVA", "EIGI", "ENV", "EPAM", "PLUS", "EFX", "ERIC", "EVBG", "MRAM",
                                "EVH",  "EXTR", "FFIV", "FDS", "FICO",
                                "FSLY", "FEYE", "FIT", "FIVN", "FLEX", "FLIR", "FORM", "FTNT", "FEIM", "GRMN", "IT",
                                "GNUS", "GILT", "GSB", "GLOB",
                                "GLUU", "GPRO", "GRVY", "GSIT", "GSX", "GTYH", "GWRE", "HLIT", "HPE", "HPQ", "HIMX",
                                "HUBS", "HUYA", "IBM", "IDEA.L", "IDEX", "INVE", "IDOX.L", "INFO", "IIVI", "IMMR",
                                "INFN",
                                "INOV", "IPHI", "INPX", "INSG", "NSIT", "INSE", "INTC", "IDCC", "INTU", "IPGP", "IQE.L",
                                "JCOM", "JBL", "JNPR", "KLAC",
                                "KOPN", "KLIC", "LRCX", "LTRX", "LSCC", "LDOS", "LLNW", "LPSN", "RAMP", "LIZI", "LOGI",
                                "LOGM", "LITE", "LUNA", "MTSI", "MGIC", "MANH", "MANT", "MKTX",
                                "MRVL", "MTLS", "MAXR", "MXIM", "MXL", "MCHP", "MU", "MSFT", "MSTR", "MIME", "MITK",
                                "MIXT", "MOBL",
                                "MODN", "MDB", "MPWR", "MCO", "MSI", "NPTN", "NTAP", "NTES", "NTGR", "NTCT",
                                "NEWR", "EGOV", "NICE", "NLSN", "NOK", "NLOK", "NVMI", "NUAN", "NTNX", "NVEC", "NVDA",
                                "NXPI", "OKTA", "OMCL",
                                "ON", "OCFT", "OSPN", "ORCL", "PD", "PANW", "PCYG", "PKE", "PAYX", "PCTY", "PCTI",
                                "PDFS", "PEGA", "PRFT", "PERI", "PFSW",
                                "PLAB", "PING", "PBI", "PXLW", "PLXS", "POWI", "PRGS", "PFPT", "PRO", "PTC", "QADA",
                                "QADB", "QRVO", "QCOM", "QLYS", "QMCO", "QTT", "RDCM", "RMBS", "RPD", "RTX", "RNWK",
                                "RP", "RDVT", "RESN", "RBBN", "RMNI", "RNG", "RIOT", "RST", "SBGI",
                                "SABR", "CRM", "SANM", "SAP", "SPNS", "SCSC", "SDGR", "SCPL", "SE", "SEAC", "STX",
                                "SCWX", "SMTC", "NOW", "SREV", "SWIR", "SILC", "SLAB", "SIMO", "SLP", "SITM", "SWKS",
                                "WORK", "SGH", "SMAR", "SMSI", "SMTX", "SONO", "SNE", "SPLK", "SPOT", "SPT", "SPSC",
                                "SSNC", "SRT", "SSYS",
                                "SMCI", "SVMK", "SYKE", "SYNC", "SYNA", "SNCR", "SNX", "SNPS", "TRHC", "TSM", "TTWO",
                                "TLND", "TM17.L", "TENB", "TDC",
                                "TER", "TXN", "TSEM", "TRU", "TTEC", "TTMI", "TWLO", "TYL", "UI", "UCTT", "UIS",
                                "UMC", "OLED", "UPLD", "UTSI",
                                "VRNS", "VECO", "VEEV", "VRNT", "VRSK", "VERI", "VSAT", "VIAV", "VICR", "VRTU", "VISL",
                                "VMW", "VCRA", "VOXX", "VUZI", "WAND.L", "WDC", "WIT", "WNS",
                                "WDAY", "WK", "XRX", "XLNX", "XPER", "XNET", "YEXT", "ZBRA", "ZEN", "ZUO", "ZNGA", "ZS"]

investing_list_of_communication_services = ["VNET", "EGHT", "ACIA", "ALLT", "GOOGL", "GOOG", "ANGI", "T", "ATNI",
                                            "ATHM", "BIDU", "BCE", "WIFI", "BKNG", "BOMN", "CABO", "CDLX", "CARG",
                                            "LUMN",
                                            "CHTR", "CHL", "CHU", "CHT", "CIDM", "CCOI", "CMCSA", "CVLT", "CMTL",
                                            "CNSL", "CRTO", "DADA", "DESP", "DISCA", "DISCK", "DISH", "SSP", "SATS",
                                            "EB",
                                            "EXPE", "FB", "FOXA", "FTR", "GCI", "GDDY", "GOGO", "GRPN", "GRUB", "HSTM",
                                            "IHRT", "IAC", "INAP", "IPG", "IQ",
                                            "IRDM", "KVHI", "LBRDA", "LBTYA", "LILA", "LTRPA", "LGF-B", "LORL",
                                            "LYFT", "MMYT", "MCHX", "MTCH", "MDP", "MOMO", "NCMI", "NFLX", "NWS", "OMC",
                                            "OPRA", "PTNR", "PT", "PINS", "QNST", "QRTEA", "MARK", "RCI", "ROKU", "SJR",
                                            "SHOP", "SSTK", "SINA", "SBGI", "SIRI", "SKM", "SNAP", "SOGO", "SOHU",
                                            "STMP", "TMUS", "TTGT", "TGNA", "TEF", "TU", "TME", "TTD",
                                            "TZOO", "TPCO", "TCOM", "TRIP", "TRVG", "TRUE", "TCX", "TWTR", "UBER",
                                            "UCL", "USM", "UONE", "UXIN", "VEON", "VRSN", "VZ", "VIAC",
                                            "VOD", "VG", "DIS", "WMG", "WB", "WIX", "WWE", "YNDX", "Z", "ZIXI", "ZM"]


investing_list_of_utilities_and_real_estate = ["AQN", "ALE", "LNT", "AEE", "AEP", "AWR", "AWK", "ATO", "AGR", "AVA",
                                               "AZRE", "BKH", "BIP", "BEP", "CIG", "CNP", "EBR", "ED", "CWCO", "D",
                                               "DUK", "EIX", "ENIA", "ENIC", "EVRG", "FE", "FTS", "GWRS", "HNP", "ITCI",
                                               "KEP", "MGEE", "NEP", "NI", "NRG", "OGS", "ORA", "PCG", "PNW", "POR",
                                               "PPL", "PEG", "RGCO", "SRE", "SWX", "SR", "SPH", "UGI", "UTL", "VST",
                                               "WEC", "XEL", "ADC", "ALEX", "ALX", "ARE", "ACC", "AFIN", "AMT", "COLD",
                                               "AHT", "AVB", "BXP", "BRX",
                                               "BPY", "CTRE", "CBL", "CBRE", "CDR", "CLDT", "CIO", "CLNY", "CXW", "COR",
                                               "CUZ", "CRESY", "CCI", "CUBE", "CONE", "DLR", "DEI", "DEA", "EGP",
                                               "ESRT", "EQIX", "ELS", "EQR", "ESS", "EXPI", "EXR", "FPI-PB",
                                               "FRT", "FPH", "FCPT", "GOOD", "LAND", "GNL", "HASI", "HTA", "PEAK", "HT",
                                               "HST", "HPP", "IIPR", "INVH", "IRM", "MAYS", "KIM", "LMRK", "LTC", "MAC",
                                               "CLI", "MGRC", "MPW", "MAA", "MNR", "NNN", "NMRK", "OHI", "PK", "DOC",
                                               "PLYM", "APTS", "PLD", "PSB", "PSA", "RYN", "O", "RVI", "REXR", "RLJ",
                                               "RMR", "SBRA", "SAFE", "BFS",
                                               "SBAC", "SPG", "SLG", "SRC", "STAG", "STOR", "SUI", "SHO", "SKT", "TRNO",
                                               "GEO", "UMH", "VTR", "VER", "VICI", "VNO", "WPC",
                                               "WELL", "WY", "WSR"]


def get_investing_lists():
    investment_list = investing_list_of_industrials + investing_list_of_technology + \
                      investing_list_of_communication_services + investing_list_of_energy + \
                      investing_list_of_utilities_and_real_estate + investing_list_of_materials + \
                      investing_list_of_consumer_discretionary + investing_list_of_consumer_staples + \
                      investing_list_of_healthcare + investing_list_of_financials

    random.shuffle(investment_list)
    print(len(investment_list))
    return investment_list

# print(get_investing_lists())
