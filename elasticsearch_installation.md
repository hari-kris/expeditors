# Elasticsearch Installation and Startup Guide on Linux

This guide provides step-by-step instructions to download and start Elasticsearch on a Linux machine.

---

## 1. Prerequisites

- **Java**: Ensure Java is installed (Elasticsearch requires at least Java 11).  
  Check Java version:
  ```bash
  java -version
  ```
  If Java is not installed, install OpenJDK:
  ```bash
  sudo apt-get update
  sudo apt-get install openjdk-11-jdk
  ```

## 2. Download Elasticsearch
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-9.0.3-linux-x86_64.tar.gz
- Visit the [Elasticsearch downloads page](https://www.elastic.co/downloads/elasticsearch) or use `wget` to download:

  ```bash
  wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-9.0.3-linux-x86_64.tar.gz
  ```

  *(Replace `9.0.3` with the latest version if needed)*

## 3. Extract the Archive

```bash
tar -xzf elasticsearch-9.0.3-linux-x86_64.tar.gz
cd elasticsearch-9.0.3
```

## 4. Start Elasticsearch

- Start Elasticsearch as a background process:

  ```bash
  ./bin/elasticsearch -d
  ```

- Or start it in the foreground (shows logs):

  ```bash
  ./bin/elasticsearch
  ```

## 5. Verify Elasticsearch is Running

- Wait a few seconds, then check if it is running:

  ```bash
  curl http://localhost:9200/
  ```

  You should see a JSON response with cluster information.

---

## Notes

- **Default Port:** Elasticsearch runs on port `9200` by default.
- **Stopping Elasticsearch:** To stop the server, locate the process and kill it:
  ```bash
  pkill -f elasticsearch
  ```
- For production, consider installing Elasticsearch as a service and configuring security options.

---

**References**:  
- [Official Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
