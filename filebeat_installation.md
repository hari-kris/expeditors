# Filebeat Installation & Setup Guide (Linux)

This document describes how to install and configure **Filebeat** on a Linux system and visualize **System ECS dashboards** in Kibana.

---

## 1. Prerequisites

- Linux server (Ubuntu / Debian / RHEL)
- Elasticsearch running and reachable
- Kibana running
- Root or sudo access

Verify Elasticsearch:
```bash
curl -k https://localhost:9200
2. Download Filebeat
bash
Copy code
cd /opt
wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-9.2.4-linux-x86_64.tar.gz
Extract the archive:

bash
Copy code
tar -xzf filebeat-9.2.4-linux-x86_64.tar.gz
cd filebeat-9.2.4-linux-x86_64
3. Set Permissions
bash
Copy code
sudo chown -R root:root /opt/filebeat-9.2.4-linux-x86_64
sudo chmod go-w /opt/filebeat-9.2.4-linux-x86_64
4. Configure Filebeat (filebeat.yml)
Minimal configuration for System ECS dashboards:

yaml
Copy code
filebeat.inputs: []

filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  enabled: true
  reload.enabled: false

output.elasticsearch:
  hosts: ["https://localhost:9200"]
  username: "elastic"
  password: "<ELASTIC_PASSWORD>"
  ssl.enabled: true
  ssl.verification_mode: none

setup.kibana:
  host: "localhost:5601"
Note: ssl.verification_mode: none is acceptable for development.
Use CA certificates for production.

5. Enable System Module
bash
Copy code
sudo ./filebeat modules enable system
Verify:

bash
Copy code
./filebeat modules list
Expected output:

text
Copy code
Enabled:
system
6. Configure System Filesets
Edit the System module configuration:

bash
Copy code
vi modules.d/system.yml
Paste the following exactly:

yaml
Copy code
- module: system

  syslog:
    enabled: true
    var.paths:
      - /var/log/syslog

  auth:
    enabled: true
    var.paths:
      - /var/log/auth.log
Filebeat must run as root to read auth.log.

7. Validate Configuration
bash
Copy code
./filebeat test config
./filebeat test output
Both commands must return OK.

8. Load Ingest Pipelines and Dashboards
bash
Copy code
sudo ./filebeat setup
This step:

Loads ingest pipelines

Creates index templates and ILM policies

Imports Kibana dashboards

9. Start Filebeat (Foreground Test)
bash
Copy code
sudo ./filebeat -e
Expected:

No fatal errors

No module system is configured but has no enabled filesets

Filebeat continues running

10. Verify Data in Kibana
Discover
Go to Kibana → Discover

Select data view: filebeat-*

Apply filter:

kql
Copy code
event.module : "system"
Dashboards
Open:

[Filebeat System] Syslog dashboard ECS

[Filebeat System] SSH login attempts ECS

[Filebeat System] Sudo commands ECS

Set time range to Last 15 minutes.

11. Run Filebeat as a Service (Optional)
Install as a system service:

bash
Copy code
sudo ./filebeat install
sudo systemctl enable filebeat
sudo systemctl start filebeat
Check status:

bash
Copy code
systemctl status filebeat
12. Common Troubleshooting
Error: module system is configured but has no enabled filesets
Ensure:

filebeat.inputs is empty or removed

system.yml exists

At least one fileset (syslog or auth) is enabled

Dashboards show no data
Confirm event.module : "system" returns documents

Ensure filebeat setup was executed

Check time range in Kibana

13. Summary Checklist
Step	Status
Filebeat installed	✅
System module enabled	✅
Filesets enabled	✅
Pipelines & dashboards loaded	✅
Data visible in Kibana	✅

End of document.
