# GeoData@SciLi API Tutorials and Examples

This repo includes several examples of fetching data via an API using Python 3 and the Requests module, illustrating bare-bones basic code for making requests and saving responses, as well as specific details for working with each of the API sources.

## Prerequisites

1. Install Python 3 (either directly from Python or via a package like Anaconda)

2. Install the Requests module (if it is not prepacked with your distribution)

3.  Register and get an API key from each source

4. Save the API key in a plain text file using the same filename used in the script, and store that file in the same folder as the script

## Concepts Demonstrated in All Examples

1. Setting variables

2. Formatting and creating a URL for making requests

3. Reading in an API key from a file

4. Making a request and saving it in a Python data structure

5. Saving the requested data in a CSV file using the built-in CSV module

## Examples with Additional Concepts

* avantage_api: Alpha Vantage API for retrieving intraday stock data by ticker symbol. Working with JSON data that's been converted into a dictionary format, date stamping the output file with the current date and time.

* census_api: US Census Bureau API for retrieving population data, in this case from the 2020 census, by specifying dataset and geography. This is the most basic example, includes working with psuedo-JSON data that can be read into a list format.

* census_api_loop: variation of the former, where the API call is made in a loop with a try / exception block to retrieve county-level data for a list of states.

* nyt_archives_api: New York Times Archive API, for searching all metadata in news articles published in a given year and month. Working with particularly complex JSON that's been converted to a dictionary format several levels deep, searching elements in these levels for particular terms, and using logic to keep records based on a match. The metadata includes article URLs, so a second step (not illustrated) could be scraping the text from these articles using the metadata.



## 
