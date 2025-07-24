Data Preparation
- Download the file from the Internet
- Convert the parquet file to csv
- Check the total no of record present in the csv file
	?
- Check the total size of the CSV file in the hard disk
	?

--------------------------------------------------------------------------------------
Without Mapping
- Index the file using the logstash without mapping
	Note Down no of record present in the elasticsearch
	verify record count should match csv and the elasticsearch
-Capture the total time to index the data - watch the time in the logstash file

---------------------------------------------------------------------------------------

- Delete the previous created index(if the size is the constrains)

--------------------------------------------------------------------------------------
With Mapping
- Define the mapping in the elasticsearch
- Index the data into the elasticsearch
- Capture the total time to index the data - watch the time in the logstash file

------------------------------------------------------------------------------------------

Shards Size Performance Measurement
- set size to 2
- set size to 3
- Measure the index time for each of the configuration
