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

# Qpid Broker-J 9.1.0 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8613](https://issues.apache.org/jira/browse/QPID-8613) - [Broker-J] Update slf4j / logback dependencies
 - [QPID-8614](https://issues.apache.org/jira/browse/QPID-8614) - [Broker-J] Deprecated reflection methods
 - [QPID-8615](https://issues.apache.org/jira/browse/QPID-8615) - [Broker-J] JUnit 5 migration
 - [QPID-8616](https://issues.apache.org/jira/browse/QPID-8616) - [Broker-J] Privacy Violation: Heap Inspection in ManagedUser
 - [QPID-8617](https://issues.apache.org/jira/browse/QPID-8617) - [Broker-J] Jetty server dependencies update
 - [QPID-8618](https://issues.apache.org/jira/browse/QPID-8618) - [Broker-J] ACL check on link stealing
 - [QPID-8620](https://issues.apache.org/jira/browse/QPID-8620) - [Broker-J] HTTP management plugin can reveal system data or debug information
 - [QPID-8621](https://issues.apache.org/jira/browse/QPID-8621) - [Broker-J] Add operation "resetStatistics" to Producer
 - [QPID-8625](https://issues.apache.org/jira/browse/QPID-8625) - [Broker-J] ACL rules require full DN when using LDAP authentication
 - [QPID-8626](https://issues.apache.org/jira/browse/QPID-8626) - [Broker-J] Dependency updates
 - [QPID-8644](https://issues.apache.org/jira/browse/QPID-8644) - [Broker-J] JUnit 5 tests refactoring for broker-plugins/access-control
 - [QPID-8645](https://issues.apache.org/jira/browse/QPID-8645) - [Broker-J] JUnit 5 tests refactoring for broker-plugins/amqp-0-8-protocol
 - [QPID-8646](https://issues.apache.org/jira/browse/QPID-8646) - [Broker-J] JUnit 5 tests refactoring for broker-plugins/amqp-0-10-protocol
 - [QPID-8647](https://issues.apache.org/jira/browse/QPID-8647) - [Broker-J] JUnit 5 tests refactoring for broker-plugins/amqp-1-0-protocol
 - [QPID-8649](https://issues.apache.org/jira/browse/QPID-8649) - [Broker-J] JUnit 5 tests refactoring for amqp-1-0-bdb-store and amqp-1-0-jdbc-store
 - [QPID-8650](https://issues.apache.org/jira/browse/QPID-8650) - [Broker-J] JUnit 5 tests refactoring for broker-plugins/qpid-broker-plugins-amqp-msg-conv-0-8-to-0-10
 - [QPID-8651](https://issues.apache.org/jira/browse/QPID-8651) - [Broker-J] JUnit 5 tests refactoring for broker-plugins/qpid-broker-plugins-amqp-msg-conv-0-8-to-1-0
 - [QPID-8652](https://issues.apache.org/jira/browse/QPID-8652) - [Broker-J] JUnit 5 tests refactoring for broker-plugins/qpid-broker-plugins-amqp-msg-conv-0-10-to-1-0
 - [QPID-8653](https://issues.apache.org/jira/browse/QPID-8653) - [Broker-J] Code cleanup: collection type arguments, collection factory methods, lambdas
 - [QPID-8654](https://issues.apache.org/jira/browse/QPID-8654) - [Broker-J] Delayed delivery producers data not displayed correctly in REST API

## Bugs fixed

 - [QPID-8622](https://issues.apache.org/jira/browse/QPID-8622) - [Broker-J] Documentation about BDB licensing
 - [QPID-8623](https://issues.apache.org/jira/browse/QPID-8623) - [Broker-J] AESKeyFile encryption breaks SimpleLDAPAuthenticationManager user search
 - [QPID-8624](https://issues.apache.org/jira/browse/QPID-8624) - [Broker-J] Unable to auto generate self signed certificate on Java17
 - [QPID-8640](https://issues.apache.org/jira/browse/QPID-8640) - [Broker-J] Remove producer on link destruction
