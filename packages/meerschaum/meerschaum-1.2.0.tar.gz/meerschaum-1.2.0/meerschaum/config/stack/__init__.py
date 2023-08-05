#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Docker Compose stack configuration goes here
"""

from __future__ import annotations
from meerschaum.utils.typing import Optional, List, Any, SuccessTuple, Dict

import os
import json
from meerschaum.config._paths import (
    GRAFANA_DATASOURCE_PATH,
    GRAFANA_DASHBOARD_PATH,
    ROOT_DIR_PATH,
)
from meerschaum.config._paths import STACK_COMPOSE_FILENAME, STACK_ENV_FILENAME
from meerschaum.config._paths import CONFIG_DIR_PATH, STACK_ENV_PATH, STACK_COMPOSE_PATH
from meerschaum.config._paths import GRAFANA_DATASOURCE_PATH, GRAFANA_DASHBOARD_PATH

db_port = "MRSM{meerschaum:connectors:sql:main:port}"
db_user = "MRSM{meerschaum:connectors:sql:main:username}"
db_pass = "MRSM{meerschaum:connectors:sql:main:password}"
db_base = "MRSM{meerschaum:connectors:sql:main:database}"

### default localhost, db for docker network
db_hostname = "db"
db_host = 'MRSM{stack:' + str(STACK_COMPOSE_FILENAME) + ':services:db:hostname}'
api_port = "MRSM{meerschaum:connectors:api:main:port}"
api_host = "meerschaum_api"

env_dict = {
    'COMPOSE_PROJECT_NAME' : 'meerschaum_stack',
    'TIMESCALEDB_VERSION' : 'latest-pg14-oss',
    'POSTGRES_USER' : f'{db_user}',
    'POSTGRES_PASSWORD' : f'{db_pass}',
    'POSTGRES_DB' : f'{db_base}',
    'MEERSCHAUM_API_HOSTNAME' : f'{api_host}',
    'ALLOW_IP_RANGE' : '0.0.0.0/0',
    'MEERSCHAUM_API_CONFIG_RESOURCES' : '/meerschaum',
}
### apply patch to host config to change hostname to the Docker service name
env_dict['MEERSCHAUM_API_CONFIG'] = json.dumps(
    {
        'meerschaum' : 'MRSM{!meerschaum}',
        'system' : 'MRSM{!system}',
    },
    separators = (',', ':'),
).replace(
    '"MRSM{!system}"', 'MRSM{!system}'
).replace(
    '"MRSM{!meerschaum}"', 'MRSM{!meerschaum}',
)

env_dict['MEERSCHAUM_API_PATCH'] = json.dumps(
    {
        'meerschaum' : {
            'connectors' : {
                'sql' : {
                    'main' : {
                        'host' : db_host,
                    },
                },
            },
        },
    }
)

compose_header = """
##############################################################
#                                                            #
#                   DO NOT EDIT THIS FILE!                   #
#                                                            #
#          Any changes you make will be overwritten.         #
#                                                            #
# Instead, you can change this file's configuration with     #
# `edit config stack` under the docker-compose.yaml section. #
#                                                            #
##############################################################
"""

volumes = {
    'api_root' : '/meerschaum',
    'meerschaum_db_data' : '/var/lib/postgresql/data',
    'grafana_storage' : '/var/lib/grafana',
}
networks = {
    'frontend' : None,
    'backend' : None,
}

default_docker_compose_config = {
    'version' : '3.2',
    'services': {
        'db' : {
            'environment' : [
                'TIMESCALEDB_TELEMETRY=off',
                'POSTGRES_USER=' + env_dict['POSTGRES_USER'],
                'POSTGRES_DB=' + env_dict['POSTGRES_DB'],
                'POSTGRES_PASSWORD=' + env_dict['POSTGRES_PASSWORD'],
                'ALLOW_IP_RANGE=' + env_dict['ALLOW_IP_RANGE'],
            ],
            'command': 'postgres -c max_connections=1000 -c shared_buffers=1024MB',
            'restart' : 'always',
            'image' : 'timescale/timescaledb:' + env_dict['TIMESCALEDB_VERSION'],
            'ports' : [
                f'{db_port}:{db_port}',
            ],
            'hostname' : f'{db_hostname}',
            'volumes' : [
                'meerschaum_db_data' + ':' + volumes['meerschaum_db_data'],
            ],
            'shm_size': '1024m',
            'networks' : [
                'backend',
            ],
        },
        'api' : {
            'image' : 'bmeares/meerschaum:api',
            'ports' : [f'{api_port}:{api_port}'],
            'hostname' : f'{api_host}',
            'networks' : [
                'frontend',
                'backend',
            ],
            'command' : 'start api --production',
            'environment' : [
                "MRSM_CONFIG='" + env_dict['MEERSCHAUM_API_CONFIG'] + "'",
                "MRSM_PATCH='" + env_dict['MEERSCHAUM_API_PATCH'] + "'",
            ],
            'restart' : 'always',
            'depends_on' : [
                'db',
            ],
            'volumes' : [
                'api_root:' + volumes['api_root'],
            ],
        },
        'grafana' : {
            'image' : 'grafana/grafana:latest',
            'ports' : [
                '3000:3000',
            ],
            'networks' : [
                'frontend',
                'backend',
            ],
            'restart' : 'always',
            'depends_on' : [
                'db',
            ],
            'volumes' : [
                'grafana_storage' + ':' + volumes['grafana_storage'],
                ### NOTE: Mount with the 'z' option for SELinux.
                f'{GRAFANA_DATASOURCE_PATH.parent}:/etc/grafana/provisioning/datasources:z,ro',
                f'{GRAFANA_DASHBOARD_PATH.parent}:/etc/grafana/provisioning/dashboards:z,ro',
            ],
            'environment' : [
                'GF_SECURITY_ALLOW_EMBEDDING=true',
                'GF_ANALYTICS_REPORTING_ENABLED=false',
                'GF_AUTH_ANONYMOUS_ENABLED=true',
                'GF_AUTH_ANONYMOUS_ORGANIZATION=public',
            ],
        },
    },
}
default_docker_compose_config['networks'] = networks
default_docker_compose_config['volumes'] = {}
for key in volumes:
    default_docker_compose_config['volumes'][key] = None

default_stack_config = {}
### compose project name (prepends to all services)
default_stack_config['project_name'] = 'mrsm'
compose_filename = os.path.split(STACK_COMPOSE_PATH)[1]
default_stack_config[compose_filename] = default_docker_compose_config
from meerschaum.config.stack.grafana import default_grafana_config
default_stack_config['grafana'] = default_grafana_config
default_stack_config['filetype'] = 'yaml'

### check if configs are in sync

def _sync_stack_files():
    from meerschaum.config._sync import sync_yaml_configs
    sync_yaml_configs(
        CONFIG_DIR_PATH / 'stack.yaml',
        ['stack', STACK_COMPOSE_FILENAME],
        STACK_COMPOSE_PATH,
        substitute = True,
    )
    sync_yaml_configs(
        CONFIG_DIR_PATH / 'stack.yaml',
        ['stack', 'grafana', 'datasource'],
        GRAFANA_DATASOURCE_PATH,
        substitute = True,
    )
    sync_yaml_configs(
        CONFIG_DIR_PATH / 'stack.yaml',
        ['stack', 'grafana', 'dashboard'],
        GRAFANA_DASHBOARD_PATH,
        substitute = True,
    )

NECESSARY_FILES = [STACK_COMPOSE_PATH, GRAFANA_DATASOURCE_PATH, GRAFANA_DASHBOARD_PATH]
def get_necessary_files():
    from meerschaum.config import get_config
    return {
        STACK_COMPOSE_PATH : (
            get_config('stack', STACK_COMPOSE_FILENAME, substitute=True), compose_header
        ),
        GRAFANA_DATASOURCE_PATH : get_config('stack', 'grafana', 'datasource', substitute=True),
        GRAFANA_DASHBOARD_PATH : get_config('stack', 'grafana', 'dashboard', substitute=True),
    }


def write_stack(
        debug: bool = False 
    ):
    """Write Docker Compose configuration files."""
    from meerschaum.config._edit import general_write_yaml_config
    from meerschaum.config._sync import sync_files
    general_write_yaml_config(get_necessary_files(), debug=debug)
    return sync_files(['stack'])
   
def edit_stack(
        action : Optional[List[str]] = None,
        debug : bool = False,
        **kw
    ):
    """Open docker-compose.yaml or .env for editing

    Parameters
    ----------
    action : Optional[List[str]] :
         (Default value = None)
    debug : bool :
         (Default value = False)
    **kw :
        

    Returns
    -------

    """
    from meerschaum.config._edit import general_edit_config
    if action is None:
        action = []
    files = {
        'compose' : STACK_COMPOSE_PATH,
        'docker-compose' : STACK_COMPOSE_PATH,
        'docker-compose.yaml' : STACK_COMPOSE_PATH,
    }
    return general_edit_config(action=action, files=files, default='compose', debug=debug)

