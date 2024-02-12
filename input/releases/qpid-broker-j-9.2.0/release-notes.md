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

# Qpid Broker-J 9.2.0 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8352](https://issues.apache.org/jira/browse/QPID-8352) - [Broker-J] Official Docker image for Broker-J
 - [QPID-8648](https://issues.apache.org/jira/browse/QPID-8648) - [Broker-J] Allow for max frame size >4096 before Open frame (SASL)
 - [QPID-8655](https://issues.apache.org/jira/browse/QPID-8655) - [Broker-J] Dependency updates for version 9.2.x
 - [QPID-8658](https://issues.apache.org/jira/browse/QPID-8658) - [Broker-J] Add Java 21 to the GitHub test matrix
 - [QPID-8661](https://issues.apache.org/jira/browse/QPID-8661) - [Broker-J] Apache Directory dependencies update
 - [QPID-8663](https://issues.apache.org/jira/browse/QPID-8663) - [Broker-J] Deprecate AESKeyFileEncrypter
 - [QPID-8666](https://issues.apache.org/jira/browse/QPID-8666) - [Broker-J] Broker plugin jdbc-provider-bone replacement
 - [QPID-8667](https://issues.apache.org/jira/browse/QPID-8667) - [Broker-J] Database connection with client certificate authentication exposes keystore / truststore passwords

## Bugs fixed

 - [QPID-8656](https://issues.apache.org/jira/browse/QPID-8656) - [Broker-J] Selector parsing logic error when combining NOT and LIKE
 - [QPID-8657](https://issues.apache.org/jira/browse/QPID-8657) - [Broker-J] ACL - Posting unknown attributes leaves broker in bad internal state
 - [QPID-8659](https://issues.apache.org/jira/browse/QPID-8659) - [Broker-J] Unit tests in QuerySettingsTest fail under some circumstances
 - [QPID-8660](https://issues.apache.org/jira/browse/QPID-8660) - [Broker-J] Logback logging disabled by inclusion of qpid-broker as a dependency
 - [QPID-8665](https://issues.apache.org/jira/browse/QPID-8665) - [Broker-J] Changing queue exclusive mode throws exception
