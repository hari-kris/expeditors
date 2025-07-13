# Generate TLS Certificates
./bin/elasticsearch-certutil ca --pem --out elastic-ca.zip --silent

./bin/elasticsearch-certutil cert --pem --in /data/elasticsearch-9.0.3-linux-x86_64/elasticsearch-9.0.3/instance.yml --out certs.zip --silent --self
-signed

./bin/elasticsearch-certutil cert --pem \
  --in instances.yml \
  --ca-cert elastic-ca/ca.crt \
  --ca-key elastic-ca/ca.key \
  --out certs.zip --silent
unzip certs.zip -d certs/


# Unzip and Distribute Certificates
unzip elastic-ca.zip -d elastic-ca
unzip certs.zip -d certs

