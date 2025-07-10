# Logstash Installation and Startup Guide on Linux

This guide details the steps to download and start Logstash version 9.0.3 on a Linux machine.

---

## 1. Prerequisites

- **Java**: Logstash requires Java (OpenJDK 11 or later).
  - Check if Java is installed:
    ```bash
    java -version
    ```
  - If Java is not installed, install OpenJDK:
    ```bash
    sudo apt-get update
    sudo apt-get install openjdk-11-jdk
    ```

## 2. Download Logstash

- Go to the [Logstash downloads page](https://www.elastic.co/downloads/logstash) or use `wget` to download Logstash 9.0.3:
  ```bash
  wget https://artifacts.elastic.co/downloads/logstash/logstash-9.0.3-linux-x86_64.tar.gz
  ```

## 3. Extract the Archive

```bash
tar -xzf logstash-9.0.3-linux-x86_64.tar.gz
cd logstash-9.0.3
```

## 4. Start Logstash

- To quickly test Logstash, you can use the built-in `stdin` and `stdout` plugins:
  ```bash
  ./bin/logstash -e 'input { stdin { } } output { stdout { } }'
  ```
  - Type something and press Enter. Logstash will output an event.

- To start Logstash with a configuration file:
  ```bash
  ./bin/logstash -f path/to/your/logstash.conf
  ```

## 5. Verify Logstash is Running

- You should see logs in the terminal indicating Logstash has started.
- If using the sample command above, typing input should display JSON-formatted output.

---

## Notes

- **Stopping Logstash**: Press `Ctrl+C` in the terminal window to stop Logstash.
- For production use, create and use proper Logstash configuration files.
- Logstash default port for monitoring is `9600` (if enabled).

---

**References**:  
- [Official Logstash Documentation](https://www.elastic.co/guide/en/logstash/current/index.html)
