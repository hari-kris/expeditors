from elasticsearch import Elasticsearch, helpers
import csv
import time

# Connect to Elasticsearch (default: localhost:9200)
es = Elasticsearch()

# Index name for this dataset
index = "titanic"
# Path to the CSV file to be indexed
filePath = "train.csv"

def read_csv(file_path):
    """
    Reads the CSV file and returns a list of dictionaries (one dict per row).
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)  # Read all rows into memory

def compose_documents(rows):
    """
    Generator that yields Elasticsearch actions for bulk indexing.
    Each dictionary in 'rows' is transformed into an action for the bulk API.
    """
    for row in rows:
        yield {
            "_index": index,
            "_source": {
                'Fare': row['Fare'],
                'Name': row['Name'],
                'Embarked': row['Embarked'],
                'Age': row['Age'],
                'Parch': row['Parch'],
                'Pclass': row['Pclass'],
                'Sex': row['Sex'],
                'Survived': row['Survived'],
                'SibSp': row['SibSp'],
                'PassengerId': row['PassengerId'],
                'Ticket': row['Ticket'],
            }
        }

if __name__ == "__main__":
    # Read all rows from CSV into a list of dictionaries
    rows = read_csv(filePath)

    # Prepare a generator of Elasticsearch bulk actions
    docs = compose_documents(rows)

    # Start the timer before bulk indexing
    start = time.time()
    # Bulk index all documents into Elasticsearch (no batching)
    helpers.bulk(es, docs)
    # End the timer after indexing
    end = time.time()

    # Print the total time taken for the bulk indexing process
    print(f"Time taken to bulk index: {end - start:.2f} seconds")
