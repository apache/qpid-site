;;
;; Licensed to the Apache Software Foundation (ASF) under one
;; or more contributor license agreements.  See the NOTICE file
;; distributed with this work for additional information
;; regarding copyright ownership.  The ASF licenses this file
;; to you under the Apache License, Version 2.0 (the
;; "License"); you may not use this file except in compliance
;; with the License.  You may obtain a copy of the License at
;; 
;;   http://www.apache.org/licenses/LICENSE-2.0
;; 
;; Unless required by applicable law or agreed to in writing,
;; software distributed under the License is distributed on an
;; "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
;; KIND, either express or implied.  See the License for the
;; specific language governing permissions and limitations
;; under the License.
;;

# Qpid Broker-J 8.0.1 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8451](https://issues.apache.org/jira/browse/QPID-8451) - [Broker-J][AMQP 1.0] Queues with enforced producer flow control should not allow to produce messages on sender links created on new connections
 - [QPID-8454](https://issues.apache.org/jira/browse/QPID-8454) - [Broker-J] Expose configured object statistics in prometheus format
 - [QPID-8455](https://issues.apache.org/jira/browse/QPID-8455) - [Broker-J]Use allow/deny list terminology for existing attributes and context variables

## Bugs fixed

 - [QPID-8448](https://issues.apache.org/jira/browse/QPID-8448) - [Broker-J] Http connection objects are leaked on HTTP port with a support for both TLS and TCP transports
 - [QPID-8449](https://issues.apache.org/jira/browse/QPID-8449) - [Broker-J][WMC] Query browser widget fails to load query data

## Tasks

 - [QPID-8464](https://issues.apache.org/jira/browse/QPID-8464) - [Broker-J] Upgrade jackson dependencies to latest versions
 - [QPID-8465](https://issues.apache.org/jira/browse/QPID-8465) - [Broker-J] Upgrade jetty dependencies
 - [QPID-8466](https://issues.apache.org/jira/browse/QPID-8466) - [Broker-J] Upgrade test dependencies to latest versions