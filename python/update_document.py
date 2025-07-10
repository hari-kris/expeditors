from elasticsearch import Elasticsearch

# Connect to Elasticsearch (default: localhost:9200)
es = Elasticsearch("http://localhost:9200")

# Index name
index_name = "users"

# Document ID to update (replace with your actual document ID)
document_id = "<PASTE_DOCUMENT_ID_HERE>"

# Fields you want to update
updated_fields = {
    "age": 31,
    "email": "john.doe@newdomain.com"
}

# Update the document
response = es.update(
    index=index_name,
    id=document_id,
    doc={"doc": updated_fields}
)

print("Update response:", response)
