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

# Qpid C++ 1.39.0 Release Notes

Qpid C++ offers a connection-oriented messaging API supporting many
programming languages and a message broker written in C++ that stores,
routes, and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [QPID-7863](https://issues.apache.org/jira/browse/QPID-7863) - qpidd-1.36 init script fails with "source: not found" on ubuntu
 - [QPID-7926](https://issues.apache.org/jira/browse/QPID-7926) - [c++ broker] Windows build error "cannot convert from 'int' to 'qpid::sys::PODMutex"
 - [QPID-8155](https://issues.apache.org/jira/browse/QPID-8155) - Late changes to -Werror are broken in windows
 - [QPID-8169](https://issues.apache.org/jira/browse/QPID-8169) - Build fails on Windows due to faulty library link
 - [QPID-8186](https://issues.apache.org/jira/browse/QPID-8186) - Incorrect exception handling fails to build on GCC 8
 - [QPID-8187](https://issues.apache.org/jira/browse/QPID-8187) - Incompatible callback function pointer casts fail to build on GCC 8
 - [QPID-8188](https://issues.apache.org/jira/browse/QPID-8188) - Invalid type qualifiers causes build failure on GCC 8
 - [QPID-8221](https://issues.apache.org/jira/browse/QPID-8221) - [qpid-cpp] Client open connections to broker and waits forever
 - [QPID-8226](https://issues.apache.org/jira/browse/QPID-8226) - build up of 'unacknowledged' deliveries for browsing client
 - [QPID-8248](https://issues.apache.org/jira/browse/QPID-8248) - qpid-config lists deleted exchange