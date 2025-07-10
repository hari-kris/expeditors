from elasticsearch import Elasticsearch

# Connect to Elasticsearch (default: localhost:9200)
es = Elasticsearch("http://localhost:9200")

# Index name
index_name = "users"

# Search for all documents in the index
response = es.search(index=index_name, query={"match_all": {}}, size=10000)  # Adjust size as needed

# Print all documents
for hit in response['hits']['hits']:
    print(hit['_source'])
