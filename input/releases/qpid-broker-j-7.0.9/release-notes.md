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

# Qpid Broker-J 7.0.9 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8338](https://issues.apache.org/jira/browse/QPID-8338) - [Broker-J] [7.0.x] Prevent test failures due to slow initialisation of hostname resolution in HostnameAliasImpl
 - [QPID-8436](https://issues.apache.org/jira/browse/QPID-8436) - [Broker-J] [7.0.x] Improve performance of dequeuing old queue entries on triggering ring policy

## Bugs fixed

 - [QPID-8289](https://issues.apache.org/jira/browse/QPID-8289) - [Broker-J] Broker startup can fail due to ConcurrentModificationException
 - [QPID-8341](https://issues.apache.org/jira/browse/QPID-8341) - [Broker-J] Reject overflow policy can erroneously rejects messages when maximumQueueDepthBytes is specified
 - [QPID-8342](https://issues.apache.org/jira/browse/QPID-8342) - [Broker-J] Concurrent object creation with virtual host auto-creation policy can fail
 - [QPID-8343](https://issues.apache.org/jira/browse/QPID-8343) - [Broker-J][AMQP 1.0] Broker mistakenly creates durable dynamic destinations for lifetime policies "delete-on-close", "delete-on-no-links", "delete-on-no-messages" or "delete-on-no-links-or-messages"
 - [QPID-8345](https://issues.apache.org/jira/browse/QPID-8345) - [Broker-J][AMQP 1.0] Consumed messages are left in acquired state on a queue when receiver's desired snd-settle-mode is set to settled and transactions are not used for message receiving
 - [QPID-8356](https://issues.apache.org/jira/browse/QPID-8356) - [Broker-J] ACL rule properties 'from_network' and 'from_hostname' are lost on loading ACL from file in 'RuleBased' access control provider
 - [QPID-8366](https://issues.apache.org/jira/browse/QPID-8366) - [Broker-J] The loss of BDB HA majority on invocation of house keeping operations can crash the broker
 - [QPID-8432](https://issues.apache.org/jira/browse/QPID-8432) - [Broker-J][7.0.x] Message references can be leaked in some rare circumstances
 - [QPID-8433](https://issues.apache.org/jira/browse/QPID-8433) - [Broker-J][7.0.x] LastValueQueueList can leak deleted queue entries

## Tasks

 - [QPID-8434](https://issues.apache.org/jira/browse/QPID-8434) - [Broker-J][7.0.x] Upgrade jetty to version 9.4.26.v20200117
 - [QPID-8435](https://issues.apache.org/jira/browse/QPID-8435) - [Broker-J][7.0.x] Upgrade jackson dependency to version 2.10.3