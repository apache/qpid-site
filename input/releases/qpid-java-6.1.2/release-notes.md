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

# Qpid for Java 6.1.2 Release Notes

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7558](https://issues.apache.org/jira/browse/QPID-7558) - [Java Broker] Allow Multiple JDBC Virtual Hosts / Message Stores to share the same database
 - [QPID-7668](https://issues.apache.org/jira/browse/QPID-7668) - [Java Broker] Add MySQL configuration to the set of known DBMS types in JDBCDetails

## Bugs fixed

 - [QPID-7608](https://issues.apache.org/jira/browse/QPID-7608) - [Java Broker, Documentation] Chapter "9.6. Flow to Disk" is inaccessible
 - [QPID-7631](https://issues.apache.org/jira/browse/QPID-7631) - [Java Broker, WMC] In BDBHA 2-node group you should be able to configure priority
 - [QPID-7643](https://issues.apache.org/jira/browse/QPID-7643) - [Java Broker] Cannot login using SASL PLAIN against Base64MD5PasswordFilePrincipalDatabase
 - [QPID-7647](https://issues.apache.org/jira/browse/QPID-7647) - [Java Broker] fix handling of broker type in configuration
 - [QPID-7670](https://issues.apache.org/jira/browse/QPID-7670) - [Java Broker] WebSocket transport does not respect AMQP idle timeout
 - [QPID-7675](https://issues.apache.org/jira/browse/QPID-7675) - [Java Broker] Runtime exception can be thrown by REST API on failure to create BDB HA Virtual Host Node
 - [QPID-7682](https://issues.apache.org/jira/browse/QPID-7682) - [Java Broker] CloudFoundry group provider plugin reports 404 errors from the service as 500 errors
 - [QPID-7684](https://issues.apache.org/jira/browse/QPID-7684) - [Java Broker, BDB] Close Cursor when LockConflictException is thrown
 - [QPID-7685](https://issues.apache.org/jira/browse/QPID-7685) - [Java Broker, BDB] AsyncRecovery and Queue#enqueue can contend for a BDB Lock potentially bringing down the broker
 - [QPID-7690](https://issues.apache.org/jira/browse/QPID-7690) - [Java Broker] Cannot create VirtualHostLogger with certain ACLs in place
 - [QPID-7692](https://issues.apache.org/jira/browse/QPID-7692) - [Java Broker, 0-8..0-91]  Message sent to fanout exchange with no routing key is not delivered to application
 - [QPID-7695](https://issues.apache.org/jira/browse/QPID-7695) - [Java Broker, BDB HA] Indefinite hang when new node joins existing group but existing node is unresponsive
 - [QPID-7696](https://issues.apache.org/jira/browse/QPID-7696) - [Java Broker] Deletion of a temporary queue can crash the broker with certain ACLs
 - [QPID-7707](https://issues.apache.org/jira/browse/QPID-7707) - [Java Broker, WMC] If ACL reload operation fails due to  malformed ACL rules, etc, the error is not reported back to the user invoking the operation