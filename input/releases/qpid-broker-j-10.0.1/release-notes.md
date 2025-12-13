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

# Qpid Broker-J 10.0.1 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8726](https://issues.apache.org/jira/browse/QPID-8726) - [Broker-J] Provide out-of-box uncaught exception handlers for the Main class
 - [QPID-8728](https://issues.apache.org/jira/browse/QPID-8728) - [Broker-J] Add useLegacyUriCompliance to HTTP Management Plugin UI configuration

## Bugs fixed

 - [QPID-8717](https://issues.apache.org/jira/browse/QPID-8717) - [Broker-J] Broker query engine may produce ClassCastException when using AVG function
 - [QPID-8718](https://issues.apache.org/jira/browse/QPID-8718) - [Broker-J] Broker query engine should support newline characters
 - [QPID-8727](https://issues.apache.org/jira/browse/QPID-8727) - [Broker-J] Jetty IllegalStateException leads to broker shutdown

## Dependency updates

 - [QPID-8716](https://issues.apache.org/jira/browse/QPID-8716) - [Broker-J] Maven plugins and test dependencies updates for version 10.0.1
 - [QPID-8719](https://issues.apache.org/jira/browse/QPID-8719) - [Broker-J] Bump fasterxml jackson dependencies to the version 3.0.3
 - [QPID-8720](https://issues.apache.org/jira/browse/QPID-8720) - [Broker-J] Bump logback dependencies to the version 1.5.21
 - [QPID-8721](https://issues.apache.org/jira/browse/QPID-8721) - [Broker-J] Bump jetty dependencies to the version 12.1.5
 - [QPID-8722](https://issues.apache.org/jira/browse/QPID-8722) - [Broker-J] Bump commons-cli dependency to the version 1.11.0
 - [QPID-8723](https://issues.apache.org/jira/browse/QPID-8723) - [Broker-J] Bump caffeine dependency to the version 3.2.3
 - [QPID-8724](https://issues.apache.org/jira/browse/QPID-8724) - [Broker-J] Bump bouncycastle dependencies to the version 1.8
 - [QPID-8725](https://issues.apache.org/jira/browse/QPID-8725) - [Broker-J] Bump asm dependencies to the version 9.9
