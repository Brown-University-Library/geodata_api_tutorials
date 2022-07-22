# GeoData@SciLi API Tutorials and Examples

This repo includes several examples of fetching data via an API using Python 3 and the Requests module, illustrating bare-bones basic code for making requests and saving responses, as well as specific details for working with each of the API sources. Each folder contains an annotated Python script and sample output.

## Prerequisites

1. Install Python 3 (either directly from [python.org](https://www.python.org/) or via a distribution like [Anaconda](https://www.anaconda.com/products/distribution))

2. Install the [Requests](https://requests.readthedocs.io/en/latest/) module (if it is not prepacked with your distribution)

3. Register and get an API key from each source, and note particular restrictions on number and volume of requests

4. Save the API key in a plain text file using the filename used in the script, and store that file in the same folder as the script

## Concepts Demonstrated in All Examples

1. Setting variables

2. Formatting and creating a URL for making requests

3. Reading in an API key from a file

4. Making a request and saving it in a Python [data structure](https://docs.python.org/3/tutorial/datastructures.html) like a list or dictionary

5. Saving the requested data in a CSV file using the built-in [CSV](https://docs.python.org/3/library/csv.html) module

## Example Scripts

Click on the folders at the top of this page to view the scripts and sample output. Click the green Code button and choose Download ZIP to download all the examples.

* **avantage_api**: [Alpha Vantage API](https://www.alphavantage.co/documentation/#intraday) for retrieving intraday stock data by ticker symbol. Working with JSON data and converting it to a dictionary format, counting returned records, date stamping the output file with the current date and time.

* **census_api**: [US Census Bureau API](https://www.census.gov/data/developers/data-sets.html) for retrieving population data, in this case from the 2020 census, by specifying dataset and geography. This is the most basic example, includes working with psuedo-JSON data and reading it into a list format.

* **census_api_loop**: variation of the former, where the API call is made in a loop with a try / exception block to retrieve county-level data for a list of states.

* **nyt_archives_api**: [New York Times Archive API](https://developer.nytimes.com/docs/archive-product/1/overview), for retrieving metadata for news articles published in a given year and month. Working with particularly complex JSON that's several levels deep, converting it to a dictionary format, searching elements in these levels for particular terms, and using logic to keep records based on a match. The metadata includes article URLs, so a second step (not illustrated) could be scraping the text from these articles using the URLs in the metadata.

## 
