cluster.name: gsc-em
node.name: gsc-em-2
network.host: 10.254.41.172

discovery.seed_hosts:
  - 10.254.41.251
  - 10.254.41.172
  - 10.254.41.239

cluster.initial_master_nodes:
  - gsc-em-1
  - gsc-em-2
  - gsc-em-3

node.roles: [ master, data, ingest ]
