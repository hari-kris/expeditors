https://www.elastic.co/downloads/past-releases/elasticsearch-8-13-4


adduser existinguser sudo



## Configuration Files:
The main configuration file, elasticsearch.yml, is located at /etc/elasticsearch/elasticsearch.yml. 
## Binary Files:
The Elasticsearch executable (elasticsearch) and plugin management script (elasticsearch-plugin) are typically found in /usr/share/elasticsearch/bin. 
Home Directory:
The Elasticsearch home directory, often referred to as $ES_HOME, is usually /usr/share/elasticsearch. 
## Environment Variables:
Environment variables, including those for heap size and file descriptors, are often sourced from /etc/sysconfig/elasticsearch. 
## Configuration Directory:
The location of the configuration directory can be changed by setting the ES_PATH_CONF environment variable. However, this variable is sourced from specific files depending on the distribution: /etc/default/elasticsearch for Debian and /etc/sysconfig/elasticsearch for RPM-based systems. 
