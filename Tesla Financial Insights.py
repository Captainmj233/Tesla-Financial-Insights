html_data = requests.get(url).text


# Parse the html data using `beautiful_soup`.
soup = BeautifulSoup(data, 'html5lib')


# Using `BeautifulSoup` or the `read_html` function extract the table with `Tesla Revenue` and stored it into a dataframe named `tesla_revenue`. 
# Locate the table containing Tesla Revenue data
table = soup.find_all('tbody')[1]

dates = []
revenues = []

# Loop through each row in the table
for row in table.find_all("tr"):
    cols = row.find_all("td")
    
    if len(cols) >= 2:
        date = cols[0].text
        revenue = cols[1].text
        
        # Append the data to the respective lists
        dates.append(date)
        revenues.append(revenue)

# Create a DataFrame from the collected data
tesla_revenue = pd.DataFrame({'Date': dates, 'Revenue': revenues})

# Print the first few rows of the DataFrame
print(tesla_revenue.head())                         


# Execute the following line to remove the comma and dollar sign from the `Revenue` column. 
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")


# Execute the following lines to remove an null or empty strings in the Revenue column.
tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# Display the last 5 row of the `tesla_revenue` dataframe using the `tail` function.
tesla_revenue.tail()


# Used the `make_graph` function to graph the Tesla Stock Data,  Note the graph will only show data upto June 2021.

make_graph(tesla_data, tesla_revenue, 'Tesla')

