from elasticsearch import Elasticsearch

# Connect to Elasticsearch (default: localhost:9200)
es = Elasticsearch("http://localhost:9200")

# Index name
index_name = "users"

# Replace with the actual ID returned when you indexed the document
document_id = "<PASTE_DOCUMENT_ID_HERE>"

# Retrieve the document by ID
response = es.get(index=index_name, id=document_id)

# Print the retrieved document
print("Document found:", response['_source'])
