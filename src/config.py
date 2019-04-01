#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

# REST fluentd logger
REST_TD_HOST = 'localhost'
REST_TD_PORT = 24224
REST_TD_LOG = 'lbtc_rest'
REST_LOG_FILE_LEVEL = logging.DEBUG

REST_BLOCK_STATUS_KYE_NODE_IP_TYPE = 'rest_block_status:node_ip_type'
REST_BLOCK_STATUS_KYE_DELEGATE_ADDRESS_TO_NAME = 'rest_block_status:delegate_address_to_name'

PARSE_BLOCK_STATUS_KYE_MYSQL_CURRENT_HEIGHT = 'parse_block_status:kye_mysql_current_height'
