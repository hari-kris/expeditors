cluster.name: em
node.name: em-1
network.host: 10.254.41.136

discovery.seed_hosts:
  - 10.254.41.136
  - 10.254.42.28
  - 10.254.42.135

cluster.initial_master_nodes:
  - em-1
  - em-2
  - em-3

node.roles: [ master, data, ingest ]
