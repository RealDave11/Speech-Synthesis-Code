from Scrape import Scrape

s = Scrape()

scots_parl_links = ["https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=2686&i=12843&c=476704&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9429&i=84721&c=1697928&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=6756&i=61360&c=1270407&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=6756&i=61360&c=1270409&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9573&i=86855&c=1744951&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=8386&i=75918&c=1523104&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=6493&i=59067&c=1233721&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=7800&i=71125&c=1430786&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9485&i=85232&c=1708511&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=7653&i=69897&c=1407320&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=6091&i=54617&c=1173175&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=4016&i=25929&c=674213&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=2648&i=12632&c=469801&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=2765&i=13207&c=488557&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=4385&i=30893&c=778016&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=4577&i=34869&c=846288&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=4631&i=36268&c=864739&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=4360&i=30443&c=769190&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=6054&i=54310&c=1167861&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=4734&i=38697&c=898579&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=8386&i=75918&c=1523112&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=8386&i=75918&c=1522985&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9472&i=85131&c=1705698&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9416&i=84636&c=1696150&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9084&i=82045&c=1646618&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9130&i=82398&c=1655517&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9157&i=82611&c=1660399&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9367&i=84277&c=1690940&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9367&i=84277&c=1690940&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=9573&i=86855&c=1745014&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=10965&i=100250&c=2002539&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=2567&i=12280&c=453071&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=4626&i=36122&c=862893&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=622&i=2604&c=121907&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=3013&i=14622&c=532917&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=2768&i=13215&c=488931&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=2765&i=13207&c=488533&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=2765&i=13207&c=488546&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=2770&i=13224&c=489349&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=1312&i=5876&c=229830&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=2743&i=13131&c=485276&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=6508&i=59198&c=1235510&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=6668&i=60743&c=1258216&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=6668&i=60744&c=1258348&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=7178&i=65369&c=1335379&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=8793&i=79500&c=1596598&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=7990&i=72686&c=1459240&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=2642&i=12610&c=468174&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=4828&i=41026&c=929926&s=tax",
         "https://archive2021.parliament.scot/parliamentarybusiness/report.aspx?r=7990&i=72686&c=1459240&s=tax"
         ]


bad_words = ["Douglas Hamilton", "Kenway", "Orly", "Coffeys", "Harvie", "exgratia", "Aberfoyle", "Muscatelli", "Holyhead", "Stevenson", "Kerrs", "laissezfaire", "Imrie", "Purvis", "Heald", "Trossachs",
                   "Shelagh Rae", "Tait", "Springford", "Aberdeenshire", "Jeyes", "Mathers", "Sewel", "Springford", "passported", "ODonnel", "Ibrox", "Hampden", "Tavish", "Dilnot", "cliché", "Sawers", "Eadie",
                   "thatmembers", "McLetchie", "Eilidh", "throughcare", "routeMembers", "Diageo", "microeconometrics", "NHSScotland", "aquacultures", "Mundell", "na", "difficile", "Tha", "Coiuhallan",
                   "etc", "Bha", "LVTwould", "Doig", "ICAS", "chiad", "withThe", "NES", "Aceh", "NESEDP", "freagarrach", "adhbharan", "Chaidh", "hypothecation", "Thuirt", "feumaidh", "committeeMembers", "Rosyth",
                   "numbersshould", "Learningand", "Crawforth", "Barnettable", "toAgree", "SEPA", "CAMH", "Statoil", "Vaillancourt", "lymphoedema", "DOTAS", "basisMembers", "RAB", "Bernd", "Spahn", "comais",
                   "MUP", "Shelagh", "Togneri", "rubicon", "PUK", "soMembers", "SRIT", "gratia", "CIPFA", "Agus", "NESTRANS", "Monteiths", "weve", "Doha", "weremade", "Huhne", "Danson", "Brownlee", "NEBU",
                   "Mandelson", "contraindicative", "WIC", "Consignia", "SAMH", "agreedWe", "microeconometrics", "salaris", "thatMembers", "andTourism", "NESTRANS", "pre", "eil", "onthe", "Savoie", "Mundell",
                   "thecarrying", "macroalgae", "NFUS", "diugh", "reportMembers", "privateMembers", "dutiesMembers", "roghainn", "Amyas", "agreedMembers", "officialdoms", "ICAS", "beachd", "NFUS", "Feumaidh",
                   "MacB", "hypothecation", "Grahame", "millionfor", "wherebywealthier", "bhile", "asan", "SEPA", "Craigies", "bhios", "actionMembers", "Feumaidh", "Cha", "Shiona", "SEPA", "Lochheads", "PAYE",
                   "Arbuthnott", "STUC", "TIF", "Andrewss", "phraseas", "SportCommittee", "Crerar", "thatmilk", "Rannoch", "CAMHS", "NEBU", "bethe", "SAMH", "cuingealachadh", "FIFA", "SRIT", "FarquharEnvironment",
                   "payI", "GARL", "SAMH", "Renfrewshire", "uplan", "areunlikely", "proposalsMembers", "EU", "Sea"]

content_list = s.get_content_list(scots_parl_links)

sentence_list = s.get_sentence_list(content_list)

normalized_sentence_list = s.produce_normalized_sentence_list(sentence_list)

length_checked_sentence_list = s.sentence_length_checker(normalized_sentence_list)

print("length_checked_sentence_list =", length_checked_sentence_list)

sentence_list_no_numbers = s.remove_sentences_with_numbers(length_checked_sentence_list)

sentence_list_no_bad_words = s.remove_sentences_with_bad_words(sentence_list_no_numbers, bad_words)

unique_sentences =  s.unique_sentences_checker(sentence_list_no_bad_words)

s.produce_output_files(unique_sentences, "combined_code_spt_check")