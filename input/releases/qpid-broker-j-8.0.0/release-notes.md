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

# Qpid Broker-J 8.0.0 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8284](https://issues.apache.org/jira/browse/QPID-8284) - [Broker-J] Move remaining classes for AMQP protocols 0-8..0-91 from qpid-broker-core into plugin module qpid-broker-plugins-amqp-0-8-protocol
 - [QPID-8349](https://issues.apache.org/jira/browse/QPID-8349) - [Broker-J][AMQP 1.0][Tests] Improve protocol tests to be able to run the test suite against external broker
 - [QPID-8350](https://issues.apache.org/jira/browse/QPID-8350) - [Broker-J][AMQP 1.0][Tests] Fix protocol tests
 - [QPID-8367](https://issues.apache.org/jira/browse/QPID-8367) - [Broker-J] Trusted CA revocation list
 - [QPID-8369](https://issues.apache.org/jira/browse/QPID-8369) - [Broker-J] Limit number of connections per user
 - [QPID-8370](https://issues.apache.org/jira/browse/QPID-8370) - [Broker-J] Option to disable WebGUI
 - [QPID-8374](https://issues.apache.org/jira/browse/QPID-8374) - [Broker-J][ACL] Allow case insensitive mapping of group members to groups in existing GroupProvider
 - [QPID-8382](https://issues.apache.org/jira/browse/QPID-8382) - [Broker-J] Allow for attribute injectors to be type specific
 - [QPID-8389](https://issues.apache.org/jira/browse/QPID-8389) - [Broker-J] Support the ability to limit the number of active consumers
 - [QPID-8392](https://issues.apache.org/jira/browse/QPID-8392) - [Broker-J] Use context variable for configuring  queue default alternate binding  and remove references to x-qpid-dlq-enabled from docs
 - [QPID-8402](https://issues.apache.org/jira/browse/QPID-8402) - [Broker-J][Tests] Use Bouncy Castle API to generate certificate resources on the fly in unit and system tests
 - [QPID-8409](https://issues.apache.org/jira/browse/QPID-8409) - [Broker-J]Misleading Documentation of "Node Priority" for the initial configuration
 - [QPID-8415](https://issues.apache.org/jira/browse/QPID-8415) - [Broker-J] Change model version to 8.0

## Bugs fixed

 - [QPID-8105](https://issues.apache.org/jira/browse/QPID-8105) - [Broker-J] broker-core unit tests are failing because of wrong locale
 - [QPID-8414](https://issues.apache.org/jira/browse/QPID-8414) - [Broker-J][WMC] The checkboxes Need/Want SSL Client Certificate are always checked on create/edit port UI
 - [QPID-8423](https://issues.apache.org/jira/browse/QPID-8423) - [Broker-J] [Logback] The outcome of logging rule for the exact logger could be superseded by the rule for logger with a trailing wild card

## Tasks

 - [QPID-8331](https://issues.apache.org/jira/browse/QPID-8331) - [Broker-J] Upgrade derby dependency
 - [QPID-8335](https://issues.apache.org/jira/browse/QPID-8335) - [Broker-J] Upgrade bcel dependency to version 6.3.1
 - [QPID-8361](https://issues.apache.org/jira/browse/QPID-8361) - [Broker-J] Create a developer guide for Qpid Broker-J
 - [QPID-8417](https://issues.apache.org/jira/browse/QPID-8417) - [Broker-J] Update unit test dependencies to the latest vesrions
 - [QPID-8418](https://issues.apache.org/jira/browse/QPID-8418) - [Broker-J] Update jetty dependency to the latest version
 - [QPID-8419](https://issues.apache.org/jira/browse/QPID-8419) - [Broker-J] Update slf4j dependencies to the latest version
 - [QPID-8420](https://issues.apache.org/jira/browse/QPID-8420) - [Broker-J] Update guava dependency to the latest version
 - [QPID-8421](https://issues.apache.org/jira/browse/QPID-8421) - [Broker-J] Update dojo toolkit version
 - [QPID-8422](https://issues.apache.org/jira/browse/QPID-8422) - [Broker-J] Update integration test dependecies to the latest versions