# Kibana Installation and Startup Guide on Linux

This guide provides step-by-step instructions to download and start Kibana version 9.0.3 on a Linux machine.

---

## 1. Prerequisites

- **Elasticsearch:** Kibana requires a running Elasticsearch instance (ideally of the same version).
- **Java:** Java is NOT required for Kibana itself, but is needed for Elasticsearch.

## 2. Download Kibana

- Go to the [Kibana downloads page](https://www.elastic.co/downloads/kibana) or use `wget` to download Kibana 9.0.3:
  ```bash
  wget https://artifacts.elastic.co/downloads/kibana/kibana-9.0.3-linux-x86_64.tar.gz
  ```

## 3. Extract the Archive

```bash
tar -xzf kibana-9.0.3-linux-x86_64.tar.gz
cd kibana-9.0.3
```

## 4. Configure Kibana (Optional)

- Edit the configuration file if you need to point Kibana to a remote Elasticsearch server or change the port:
  ```bash
  vi config/kibana.yml
  ```
  - Set the `elasticsearch.hosts` field if needed (default: `http://localhost:9200`).

## 5. Start Kibana

- Run Kibana in the foreground:
  ```bash
  ./bin/kibana
  ```

- Or run it in the background:
  ```bash
  nohup ./bin/kibana &
  ```

## 6. Access Kibana

- Open a browser and go to:
  ```
  http://localhost:5601
  ```
  (Default Kibana port is 5601)

## 7. Stopping Kibana

- If running in the foreground, press `Ctrl+C`.
- If running in the background, find the process and kill it:
  ```bash
  pkill -f kibana
  ```

---

**References**:  
- [Official Kibana Documentation](https://www.elastic.co/guide/en/kibana/current/index.html)
