✅ Elasticsearch security features have been automatically configured!
✅ Authentication is enabled and cluster connections are encrypted.

ℹ️  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  Myqrjz9DuEWSicr+DeKQ

ℹ️  HTTP CA certificate SHA-256 fingerprint:
  49efa5b29b93590880a8b9ced656f679446baee0958b7c2b3b0fb671fd34bdcc

ℹ️  Configure Kibana to use this cluster:
• Run Kibana and click the configuration link in the terminal when Kibana starts.
• Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjE0LjAiLCJhZHIiOlsiMTcyLjIwLjcuODY6OTIwMCJdLCJmZ3IiOiI0OWVmYTViMjliOTM1OTA4ODBhOGI5Y2VkNjU2ZjY3OTQ0NmJhZWUwOTU4YjdjMmIzYjBmYjY3MWZkMzRiZGNjIiwia2V5IjoiNmJ3Tl9wY0JVbEVndUpZd3JwVUY6ZHFKeHhZR09IaG5uUHI2OFlEa3B6QSJ9

ℹ️  Configure other nodes to join this cluster:
• On this node:
  ⁃ Create an enrollment token with `bin/elasticsearch-create-enrollment-token -s node`.
  ⁃ Uncomment the transport.host setting at the end of config/elasticsearch.yml.
  ⁃ Restart Elasticsearch.
• On other nodes:
  ⁃ Start Elasticsearch with `bin/elasticsearch --enrollment-token <token>`, using the enrollment token that you generated.
