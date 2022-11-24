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

# Qpid Broker-J 9.0.0 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8368](https://issues.apache.org/jira/browse/QPID-8368) - [Broker-J] Graylog support
 - [QPID-8456](https://issues.apache.org/jira/browse/QPID-8456) - [Broker-J] Configurable shutdown timeout
 - [QPID-8484](https://issues.apache.org/jira/browse/QPID-8484) - [Broker-J] Reimplementation of the limit number of connections per user
 - [QPID-8487](https://issues.apache.org/jira/browse/QPID-8487) - [Broker-J] Enhance ACL rule evaluation
 - [QPID-8488](https://issues.apache.org/jira/browse/QPID-8488) - [Broker-J] Enhance ACL rule with multi-value properties
 - [QPID-8545](https://issues.apache.org/jira/browse/QPID-8545) - [Broker-J] SSL Engine looping circuit breaker
 - [QPID-8547](https://issues.apache.org/jira/browse/QPID-8547) - [Broker-J] Configurable parameters for CoalescingCommiter
 - [QPID-8548](https://issues.apache.org/jira/browse/QPID-8548) - [Broker-J] Enhance ACL file loading and parsing
 - [QPID-8558](https://issues.apache.org/jira/browse/QPID-8558) - [Broker-J] Enhancement of sole connection enforcement policy evaluation
 - [QPID-8563](https://issues.apache.org/jira/browse/QPID-8563) - [Broker-J] Purge all queues
 - [QPID-8565](https://issues.apache.org/jira/browse/QPID-8565) - [Broker-J] Enhancement of ACL rule predicates evaluation
 - [QPID-8566](https://issues.apache.org/jira/browse/QPID-8566) - [Broker-J] Implement composite authentication provider
 - [QPID-8573](https://issues.apache.org/jira/browse/QPID-8573) - [Broker-J] Logging enhancement of Sole Connection Enforcement Policy events
 - [QPID-8578](https://issues.apache.org/jira/browse/QPID-8578) - [Broker-J] ACL firewall predicates should be applied to HTTP(S) connections
 - [QPID-8581](https://issues.apache.org/jira/browse/QPID-8581) - [Broker-J] Query REST API improvements
 - [QPID-8590](https://issues.apache.org/jira/browse/QPID-8590) - [Broker-J] Purge on flow to disk queue
 - [QPID-8591](https://issues.apache.org/jira/browse/QPID-8591) - [Broker-J] Missing message id for add/update/delete user
 - [QPID-8592](https://issues.apache.org/jira/browse/QPID-8592) - [Broker-J] Pass context value from parent query into the subquery
 - [QPID-8596](https://issues.apache.org/jira/browse/QPID-8596) - [Broker-J] Migrate build process to JDK 11/17
 - [QPID-8601](https://issues.apache.org/jira/browse/QPID-8601) - [Broker-J] Instrumentation agent
 - [QPID-8602](https://issues.apache.org/jira/browse/QPID-8602) - [Broker-J] Show producer details in REST API
 - [QPID-8603](https://issues.apache.org/jira/browse/QPID-8603) - [Broker-J] Reset statistics
 - [QPID-8612](https://issues.apache.org/jira/browse/QPID-8612) - [Broker-J] Change default GC from CMS to G1

## Bugs fixed

 - [QPID-8452](https://issues.apache.org/jira/browse/QPID-8452) - [Broker-J] Message larger than 2GB
 - [QPID-8536](https://issues.apache.org/jira/browse/QPID-8536) - [Broker-J] Incorrect check of maximum open connections
 - [QPID-8568](https://issues.apache.org/jira/browse/QPID-8568) - [Broker-J] Context variables disappear from All list in GUI context editor
 - [QPID-8572](https://issues.apache.org/jira/browse/QPID-8572) - [Broker-J] The binding is broken when queue and exchange have the same name
 - [QPID-8588](https://issues.apache.org/jira/browse/QPID-8588) - [Broker-J] NullPointerException in AbstractVirtualHost.autoCreateNode
