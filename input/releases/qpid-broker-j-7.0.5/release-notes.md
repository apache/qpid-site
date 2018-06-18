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

# Qpid Broker-J 7.0.5 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

**Note**: This release addresses security vulnerability CVE-2018-8030.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8204](https://issues.apache.org/jira/browse/QPID-8204) - [Broker-J] Add statistics to report the maximum size of incoming messages

## Bugs fixed

 - [QPID-8202](https://issues.apache.org/jira/browse/QPID-8202) - [Broker-J][AMQP 0-8...0-91] Large flowed to disk message can be re-loaded from store for every content chunk sent to the client
 - [QPID-8203](https://issues.apache.org/jira/browse/QPID-8203) - [Broker-J][AMQP 0-8...0-91] [CVE-2018-8030] Denial of Service Vulnerability when AMQP 0-8...0-91 messages exceed maximum size limit
 - [QPID-8207](https://issues.apache.org/jira/browse/QPID-8207) - [Broker-J] Flow to disk might not be triggered in some circumstances

## Tasks

 - [QPID-8205](https://issues.apache.org/jira/browse/QPID-8205) - [Broker-J] Release Qpid Broker-J 7.0.5
