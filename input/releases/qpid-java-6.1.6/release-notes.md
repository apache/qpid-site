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

# Qpid for Java 6.1.6 Release Notes

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8086](https://issues.apache.org/jira/browse/QPID-8086) - [Broker-J] Create tool to permit recovery from QPID-8066
 - [QPID-8136](https://issues.apache.org/jira/browse/QPID-8136) - [Broker-J] Upgrade Jackson dependencies

## Bugs fixed

 - [QPID-7892](https://issues.apache.org/jira/browse/QPID-7892) - [Java Broker] Qpid Logback plugin RollingPolicyDecorator tests fail since java.io.tmpdir pointed at directory containing parentheses 
 - [QPID-8049](https://issues.apache.org/jira/browse/QPID-8049) - Non-free ICC profiles
 - [QPID-8070](https://issues.apache.org/jira/browse/QPID-8070) - [Broker-J][JDBC Store] Instantiate asynchronous commits executor on open of JDBC message store
 - [QPID-8130](https://issues.apache.org/jira/browse/QPID-8130) - [Broker-J] IAE "Comparison method violates its general contract!" can be thrown whilst comparing log file details of file logger
 - [QPID-8144](https://issues.apache.org/jira/browse/QPID-8144) - [Broker-J] Memory compaction does not run when used direct memory exceeds 2GB