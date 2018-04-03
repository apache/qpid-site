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

# Qpid C++ 1.38.0 Release Notes

Qpid C++ offers a connection-oriented messaging API supporting many
programming languages and a message broker written in C++ that stores,
routes, and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7089](https://issues.apache.org/jira/browse/QPID-7089) - Documentation should point to PPA for Debian/Ubuntu
 - [QPID-7499](https://issues.apache.org/jira/browse/QPID-7499) - Define test script dependencies in CMake so make test picks up changes
 - [QPID-7630](https://issues.apache.org/jira/browse/QPID-7630) - Add a CMake switch to allow -Werror to be switched off
 - [QPID-7999](https://issues.apache.org/jira/browse/QPID-7999) - Relocate distro-specific etc files
 - [QPID-8073](https://issues.apache.org/jira/browse/QPID-8073) - Various documentation fixes

## Bugs fixed

 - [QPID-7051](https://issues.apache.org/jira/browse/QPID-7051) - Crash after reconnect with transactional session (with patch)
 - [QPID-7054](https://issues.apache.org/jira/browse/QPID-7054) - Crash when closing a sender after the connection has been closed (with patch).
 - [QPID-7821](https://issues.apache.org/jira/browse/QPID-7821) - Missing man pages
 - [QPID-8075](https://issues.apache.org/jira/browse/QPID-8075) - BrokerAgent not working for me
 - [QPID-8118](https://issues.apache.org/jira/browse/QPID-8118) - qpidd crashes at startup in certain conditions
 - [QPID-8131](https://issues.apache.org/jira/browse/QPID-8131) - [cpp] Fix some problems with the legacystore tests

## Tasks

 - [QPID-8072](https://issues.apache.org/jira/browse/QPID-8072) - Remove the obsolete Ruby management API
 - [QPID-8128](https://issues.apache.org/jira/browse/QPID-8128) - [cpp] Link to libqpid-proton-core, not libqpid-proton
 - [QPID-8129](https://issues.apache.org/jira/browse/QPID-8129) - Remove the obsolete Python management API