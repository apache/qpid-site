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

# Qpid Broker-J 10.1.0 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

## New features and improvements

 - [QPID-8013](https://issues.apache.org/jira/browse/QPID-8013) - [Broker-J] Reduce footprint of AMQP 1.0 protocol objects
 - [QPID-8706](https://issues.apache.org/jira/browse/QPID-8706) - [Broker-J] Move AMQP-1.0 symbols declarations to a utility class
 - [QPID-8731](https://issues.apache.org/jira/browse/QPID-8731) - [Broker-J] Security Manager removal
 - [QPID-8738](https://issues.apache.org/jira/browse/QPID-8738) - [Broker-J] JUnit 6 migration - TlsResource should support parameter injection
 - [QPID-8740](https://issues.apache.org/jira/browse/QPID-8740) - [Broker-J] JUnit 6 migration - QpidUnitTestExtension should be stateless
 - [QPID-8743](https://issues.apache.org/jira/browse/QPID-8743) - [Broker-J] Add operation to close idle connections
 - [QPID-8744](https://issues.apache.org/jira/browse/QPID-8744) - [Broker-J] Jackson ObjectMapper instances shouldn't be created on each method call

## Bugs fixed

 - [QPID-8748](https://issues.apache.org/jira/browse/QPID-8748) - [Broker-J] NPE when sorting results in broker query engine
 - [QPID-8749](https://issues.apache.org/jira/browse/QPID-8749) - [Broker-J] AMQP connections may not close while processing pending writes

## Dependency updates

 - [QPID-8729](https://issues.apache.org/jira/browse/QPID-8729) - [Broker-J] Maven plugins and test dependencies updates for version 10.1.0
 - [QPID-8730](https://issues.apache.org/jira/browse/QPID-8730) - [Broker-J] Bump logback/slf4j dependencies to the version 1.6.0/2.0.18
 - [QPID-8733](https://issues.apache.org/jira/browse/QPID-8733) - [Broker-J] Bump fasterxml jackson dependencies to the version 3.2.1
 - [QPID-8734](https://issues.apache.org/jira/browse/QPID-8734) - [Broker-J] Bump asm dependencies to the version 9.10.1
 - [QPID-8737](https://issues.apache.org/jira/browse/QPID-8737) - [Broker-J] Bump jetty dependencies to the version 12.1.11
 - [QPID-8741](https://issues.apache.org/jira/browse/QPID-8741) - [Broker-J] Bump logback-db dependency to the version 1.5.32
 - [QPID-8742](https://issues.apache.org/jira/browse/QPID-8742) - [Broker-J] Bump bouncycastle dependencies to the version 1.84
 - [QPID-8745](https://issues.apache.org/jira/browse/QPID-8745) - [Broker-J] Bump caffeine dependency to the version 3.2.4
 - [QPID-8746](https://issues.apache.org/jira/browse/QPID-8746) - [Broker-J] Bump hikaricp dependency to the version 7.1.0
 - [QPID-8747](https://issues.apache.org/jira/browse/QPID-8747) - [Broker-J] Bump logback-gelf dependency to the version 6.1.2


