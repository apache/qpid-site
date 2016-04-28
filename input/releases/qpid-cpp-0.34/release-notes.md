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

# Qpid C++ 0.34 Release Notes

A connection-oriented messaging API that supports many languages and
platforms. A message-oriented middleware message broker written in C++
that stores, routes, and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-6492](https://issues.apache.org/jira/browse/QPID-6492) - When AMQP 1.0 link attach triggers an ACL error, the link should be refused
 - [QPID-6592](https://issues.apache.org/jira/browse/QPID-6592) - [amqp1.0] Add identifying information to the connection properties advertised to the client

## Bugs fixed

 - [QPID-6256](https://issues.apache.org/jira/browse/QPID-6256) - Improved control over AMQP versions tried
 - [QPID-6368](https://issues.apache.org/jira/browse/QPID-6368) - Coverity 1262251 - double free in ~PersistableQueue
 - [QPID-6392](https://issues.apache.org/jira/browse/QPID-6392) - [C++ Broker] [AMQP 1.0] the broker didnt respond to a link detach request
 - [QPID-6397](https://issues.apache.org/jira/browse/QPID-6397) - [C++ broker] segfault when processing QMF method during periodic processing
 - [QPID-6399](https://issues.apache.org/jira/browse/QPID-6399) - Windows run_test.ps1 script needs revamp to match run_test
 - [QPID-6409](https://issues.apache.org/jira/browse/QPID-6409) - Taking address of a 0-length vector throws exception
 - [QPID-6463](https://issues.apache.org/jira/browse/QPID-6463) - WinSDK script fails - Proton components have moved
 - [QPID-6470](https://issues.apache.org/jira/browse/QPID-6470) - FieldValue::getFloatingPointValue() converts endian each time it is called
 - [QPID-6484](https://issues.apache.org/jira/browse/QPID-6484) - AccessViolationException when creating queues
 - [QPID-6493](https://issues.apache.org/jira/browse/QPID-6493) - cmake install (TARGET ...) component syntax is incorrect in the src/CMakeLists.txt
 - [QPID-6511](https://issues.apache.org/jira/browse/QPID-6511) - [C++ Broker, clients] AMQP 0-10 windows clients can not connect to --no-auth broker
 - [QPID-6521](https://issues.apache.org/jira/browse/QPID-6521) - [AMQP 1.0] messages received pre-settled are never settled locally causing memory build up in client
 - [QPID-6524](https://issues.apache.org/jira/browse/QPID-6524) - [C++ broker]: Fix for QPID-5107 incomplete for queues
 - [QPID-6526](https://issues.apache.org/jira/browse/QPID-6526) - [AMQP 1.0]: race condition in creating senders/receivers
 - [QPID-6529](https://issues.apache.org/jira/browse/QPID-6529) - [C++ Client] Fails to compile with Proton 0.10
 - [QPID-6532](https://issues.apache.org/jira/browse/QPID-6532) - make sasl service name configurable
 - [QPID-6548](https://issues.apache.org/jira/browse/QPID-6548) - SYSV init scripts do not work properly wiht SSL-only broker.
 - [QPID-6549](https://issues.apache.org/jira/browse/QPID-6549) -  `service qpidd status` returns 1 - hidden error is "ConnectionError: connection-forced: Connection must be encrypted.(320)"
 - [QPID-6551](https://issues.apache.org/jira/browse/QPID-6551) - [C++ broker]: linearstore raising JERR_LFCR_SEQNUMNOTFOUND after sending many DTX transactions
 - [QPID-6559](https://issues.apache.org/jira/browse/QPID-6559) - NullSaslClient only support ANONYMOUS
 - [QPID-6563](https://issues.apache.org/jira/browse/QPID-6563) - [amqp1.0] broker does not clean up closed sessions or links
 - [QPID-6568](https://issues.apache.org/jira/browse/QPID-6568) - [amqp1.0] bump the minimum required proton version to 0.7
 - [QPID-6602](https://issues.apache.org/jira/browse/QPID-6602) - [AMQP 1.0] prefetch is not always accurate