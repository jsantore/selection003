us_recession_start_years=[1920, 1923, 1926, 1929, 1937,
1945, 1949,1953, 1958, 1960, 1969, 1973, 1980, 1981,
1990, 2001, 2008, 2020]
total_election_years = 0
for recession_year in us_recession_start_years:
     if recession_year % 4 == 0:
         total_election_years = total_election_years +1
         print(f"election and recession in {recession_year}")
print(f"There were {total_election_years} that both started recessions and were election years")
