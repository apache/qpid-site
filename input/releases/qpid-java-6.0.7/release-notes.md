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

# Qpid for Java 6.0.7 Release Notes

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7435](https://issues.apache.org/jira/browse/QPID-7435) - [Java Broker] Avoid BDB fetching dummy single byte database entries during message instance recovery
 - [QPID-7468](https://issues.apache.org/jira/browse/QPID-7468) - [Java Broker] Upgrade logback to 1.1.11 and SLF4J to 1.7.24
 - [QPID-7730](https://issues.apache.org/jira/browse/QPID-7730) - [Java Broker] Upgrade logback to latest version (1.2.2)
 - [QPID-7736](https://issues.apache.org/jira/browse/QPID-7736) - [Java Broker] Upgrade SLF4j to 1.7.25
 - [QPID-7737](https://issues.apache.org/jira/browse/QPID-7737) - [JMS AMQP 0-x Client] Upgrade SLF4j to 1.7.25
 - [QPID-7745](https://issues.apache.org/jira/browse/QPID-7745) - [Java Broker] Bump dependency version of Apache Derby

## Bugs fixed

 - [QPID-7408](https://issues.apache.org/jira/browse/QPID-7408) - [Java Broker] REST API streams compressed message content without a Content-Encoding header
 - [QPID-7505](https://issues.apache.org/jira/browse/QPID-7505) - [JMS AMQP 0-x Client] The subsequenct synchronous #recieve(long) might return null even when there are messages on the queue and client has enough credits
 - [QPID-7631](https://issues.apache.org/jira/browse/QPID-7631) - [Java Broker, WMC] In BDBHA 2-node group you should be able to configure priority
 - [QPID-7643](https://issues.apache.org/jira/browse/QPID-7643) - [Java Broker] Cannot login using SASL PLAIN against Base64MD5PasswordFilePrincipalDatabase
 - [QPID-7647](https://issues.apache.org/jira/browse/QPID-7647) - [Java Broker] fix handling of broker type in configuration
 - [QPID-7675](https://issues.apache.org/jira/browse/QPID-7675) - [Java Broker] Runtime exception can be thrown by REST API on failure to create BDB HA Virtual Host Node
 - [QPID-7684](https://issues.apache.org/jira/browse/QPID-7684) - [Java Broker, BDB] Close Cursor when LockConflictException is thrown
 - [QPID-7685](https://issues.apache.org/jira/browse/QPID-7685) - [Java Broker, BDB] AsyncRecovery and Queue#enqueue can contend for a BDB Lock potentially bringing down the broker
 - [QPID-7690](https://issues.apache.org/jira/browse/QPID-7690) - [Java Broker] Cannot create VirtualHostLogger with certain ACLs in place
 - [QPID-7695](https://issues.apache.org/jira/browse/QPID-7695) - [Java Broker, BDB HA] Indefinite hang when new node joins existing group but existing node is unresponsive
 - [QPID-7696](https://issues.apache.org/jira/browse/QPID-7696) - [Java Broker] Deletion of a temporary queue can crash the broker with certain ACLs
 - [QPID-7711](https://issues.apache.org/jira/browse/QPID-7711) - [Java Broker] Set correct Content-Encoding in REST response (6.0.x)
 - [QPID-7732](https://issues.apache.org/jira/browse/QPID-7732) - [Java Broker] Issues with using global address domains
 - [QPID-7743](https://issues.apache.org/jira/browse/QPID-7743) - [Java Broker] Propagate current IO thread when switching protocol engine
 - [QPID-7763](https://issues.apache.org/jira/browse/QPID-7763) - [Java Broker] Flow to disk if allocated direct memory exceeds broker wide broker.flowToDiskThreshold
 - [QPID-7783](https://issues.apache.org/jira/browse/QPID-7783) - [Java Broker] Closing a virtualhost does not dispose QBBs associated with messages on queues
 - [QPID-7784](https://issues.apache.org/jira/browse/QPID-7784) - [Java Broker] Closing a virtualhost does not dispose QBBs still associated with pooled IO threads
 - [QPID-7794](https://issues.apache.org/jira/browse/QPID-7794) - [Java Broker] Periodically report the number of bytes evacuated from memory by flow to disk (6.1/6.0)
 - [QPID-7795](https://issues.apache.org/jira/browse/QPID-7795) - [Java Broker] Ensure that a newly enqueued message that is flowed to disk does not immediately have meta-data reloaded (6.1/6.0)
 - [QPID-7796](https://issues.apache.org/jira/browse/QPID-7796) - [Java Broker] Guard against NPE in 0-10 when storing messages without header