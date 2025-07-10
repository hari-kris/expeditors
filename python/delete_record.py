from elasticsearch import Elasticsearch

# Connect to Elasticsearch (default: localhost:9200)
es = Elasticsearch("http://localhost:9200")

# Index name
index_name = "users"

# Document ID to delete (replace with your actual document ID)
document_id = "<PASTE_DOCUMENT_ID_HERE>"

# Delete the document
response = es.delete(index=index_name, id=document_id)

print("Delete response:", response)
