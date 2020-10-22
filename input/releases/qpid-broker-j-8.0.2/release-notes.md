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

# Qpid Broker-J 8.0.2 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8471](https://issues.apache.org/jira/browse/QPID-8471) - [Broker-J] Enhance documentation by improving the end of line and other table structures
 - [QPID-8472](https://issues.apache.org/jira/browse/QPID-8472) - [Broker-J] Improve operational logging for queue operations copying, moving and deleting messages
 - [QPID-8473](https://issues.apache.org/jira/browse/QPID-8473) - [Broker-J] Add operational logs for publishing links added/removed on message destination
 - [QPID-8474](https://issues.apache.org/jira/browse/QPID-8474) - [Broker-J] Add statistics for messages/bytes received/sent into Session

## Bugs fixed

 - [QPID-8469](https://issues.apache.org/jira/browse/QPID-8469) - [Broker-J][Message Store] The message is already cleaned when the delete listener is called
 - [QPID-8470](https://issues.apache.org/jira/browse/QPID-8470) - [Broker-J] Deadlock  / latch timeout in BDB database
 - [QPID-8477](https://issues.apache.org/jira/browse/QPID-8477) - [Broker-J] Broker is not closing connections denied with ACL-1002 (this can lead to connection_limit being bypassed)
 - [QPID-8478](https://issues.apache.org/jira/browse/QPID-8478) - [Broker-J] NPE thrown for ACL rules like 'ALLOW ALL ALL' or 'DENY ALL ALL'