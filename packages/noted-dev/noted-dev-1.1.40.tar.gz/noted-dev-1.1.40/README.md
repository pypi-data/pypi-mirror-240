# NOTED: a framework to optimise network traffic via the analysis of data from File Transfer Services

Copyright:
```
© Copyright 2022 CERN. This software is distributed under the terms of
the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
in the file "LICENCE.txt". In applying this licence, CERN does not waive
the privileges and immunities granted to it by virtue of its status as an
Intergovernmental Organization or submit itself to any jurisdiction.
```

PyPI Compilation steps:
```
# Steps to install NOTED by using a virtual environment
$ yum install python3-pip -y
$ yum install python3.8
$ pip3 install virtualenv 
$ python3.8 -m venv venv-noted
$ . venv-noted/bin/activate
(venv-noted) $ python3 -m pip install noted-dev
# Write your configuration file, there is one example in noted/config/
(venv-noted) $ nano noted/src/noted/config/config.yaml
# Run NOTED
# (venv-noted) $ noted noted/src/noted/config/config.yaml [--verbosity debug/info/warning]
```

Docker Compilation steps:
```
# Download noted docker container
$ docker pull noted-docker
# Run docker container and keep it running in the background
$ docker run --detach --entrypoint /sbin/init --network="host" --privileged --name noted_cern_kit_controller noted-docker
# Copy config file into the container
$ docker cp src/noted/config/config-example.yaml noted_cern_kit_controller:/app/noted/config
# Run commands in the container from outside
$ docker exec noted_cern_kit_controller noted -h
$ docker exec noted_cern_kit_controller /app/src/noted/scripts/setup.sh mail
$ docker exec noted_cern_kit_controller noted config/config-example.yaml &
# Stop noted
$ docker exec noted_cern_kit_controller pkill noted

# Optional: login into the container (NOTE: type "exit" to logout)
$ docker exec -it noted_cern_kit_controller /bin/bash
```

Program description:
```
noted -h
usage: noted [-h] [-v VERBOSITY] config_file

NOTED: a framework to optimise network traffic via the analysis of data from File Transfer Services.

positional arguments:
  config_file           the name of the configuration file [config-example.yaml]

optional arguments:
  -h, --help            show this help message and exit
  -v VERBOSITY, --verbosity VERBOSITY
                        defines the logging level [debug, info, warning]
```

Folder structure of NOTED:
1. In config folder is available one or more config.yaml where the user defines the parameters to monitor the links.
2. In logs folder:
    noted_email.txt: the last email notification that has been send to the responsible of the link to provide/cancel the dynamic circuit.
    transfer_broker.log: the log of NOTED [one log per execution].
    sense.log: the log of sense-o, it is generated when NOTED calls the sense-o API [one log per execution].
3. In query folder are available the queries to CERN Kibana [this folder is transparent to the user, don't use it].
4. In transfers folder:
    transfer_broker_all_transfers.txt: file with all the transfers in the link even if the source/destination dynamic circuits are down.
    transfer_broker_src_rcsite.txt: file with the transfers of {src -> dst}  when the source dynamic circuit is up, otherwise the transfers are not saved.
    transfer_broker_dst_rcsite.txt: file with the transfers of {dst -> src}  when the destination dynamic circuit is up, otherwise the transfers are not saved.
```
noted
├── config
│   └── config.yaml
├── logs
│   ├── noted_email.txt
│   └── sense.log
│   └── transfer_broker.log
├── query
│   ├── query_monit_prod_fts_raw_queue_dst_rcsite
│   └── query_monit_prod_fts_raw_queue_src_rcsite
├── sense-o
│   │   ├── sense-cancel.sh
│   │   └── sense-provision.sh
└── transfers
    ├── transfer_broker_all_transfers.txt
    ├── transfer_broker_dst_rcsite.txt
    └── transfer_broker_src_rcsite.txt
```

Structure of NOTED repository:
```
.
├── README.md
└── noted_transfer_broker
    ├── COPYRIGHT.txt
    ├── LICENCE.txt
    ├── Makefile
    ├── MANIFEST.in
    ├── README.md
    ├── setup.cfg
    ├── setup.py
    └── src
        ├── noted
            ├── __init__.py
            ├── main.py
            ├── config
            │   └── config-example.yaml
            ├── documentation
            │   ├── noted_main_function_documentation.pdf
            │   ├── noted_transfer_broker_class_documentation.pdf
            │   ├── reduced_noted_main_function_documentation.pdf
            │   └── reduced_noted_transfer_broker_class_documentation.pdf
            ├── html
            │   ├── TransferBroker.html
            │   └── main.html
            ├── logs
            │   ├── noted_email.txt
            │   ├── sense.log
            │   ├── transfer_broker.log
            ├── modules
            │   ├── __init__.py
            │   ├── plot_transfers.py
            │   └── transferbroker.py
            ├── params
            │   └── params.ini
            ├── query
            │   ├── query_monit_prod_fts_raw_queue_dst_rcsite
            │   └── query_monit_prod_fts_raw_queue_src_rcsite
            ├── scripts
            │   └── setup.sh
            ├── sense-o
            │   ├── sense-cancel.sh
            │   └── sense-provision.sh
            └── transfers
                ├── transfer_broker_all_transfers.txt
                ├── transfer_broker_dst_rcsite.txt
                └── transfer_broker_src_rcsite.txt
```
