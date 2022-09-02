soup = BeautifulSoup(driver.page_source, 'html.parser')

desC = []

download = soup.select("#dataTableResponsive > tbody > tr>td> table")#"#dataTableResponsive > tbody > tr > td:nth-child(5)")#"table tbody tr td.dtr-data")
# first10 = download[:10]
for description in download:
    print(description.text)
    desC.append(description.text) 