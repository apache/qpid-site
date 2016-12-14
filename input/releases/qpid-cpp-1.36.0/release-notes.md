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

# Qpid C++ 1.36.0 Release Notes

Qpid C++ offers a connection-oriented messaging API supporting many
programming languages and a message broker written in C++ that stores,
routes, and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7430](https://issues.apache.org/jira/browse/QPID-7430) - Allow qpid::messaging addresses to be passed through to server
 - [QPID-7432](https://issues.apache.org/jira/browse/QPID-7432) - Make python management tools work over AMQP 1.0
 - [QPID-7439](https://issues.apache.org/jira/browse/QPID-7439) - Proton-based library for QMF management.

## Bugs fixed

 - [QPID-7406](https://issues.apache.org/jira/browse/QPID-7406) - release doesn't reset cursors for active consumers on LVQ
 - [QPID-7415](https://issues.apache.org/jira/browse/QPID-7415) - [AMQP 1.0]: reject, release &amp; modified ignored by qpid::messaging
 - [QPID-7494](https://issues.apache.org/jira/browse/QPID-7494) - Invocation of check_dependencies.py fails on CMake 2.8.11
 - [QPID-7500](https://issues.apache.org/jira/browse/QPID-7500) - [AMQP 1.0] session close is not synchronous
 - [QPID-7501](https://issues.apache.org/jira/browse/QPID-7501) - [AMQP 1.0] sessions and links should be freed under lock

## Tasks

 - [QPID-7581](https://issues.apache.org/jira/browse/QPID-7581) - update the 'tested proton version' check prior to release