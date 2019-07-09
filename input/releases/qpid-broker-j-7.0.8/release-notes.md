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

# Qpid Broker-J 7.0.8 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8318](https://issues.apache.org/jira/browse/QPID-8318) - [Broker-J] [AMQP 0-8/9/9-1] Queue.Purge does not return deleted count

## Bugs fixed

 - [QPID-8316](https://issues.apache.org/jira/browse/QPID-8316) - [Broker-J][AMQP 0-8..0-91] The meta data of flowed to disk messages continue to occupy heap memory
 - [QPID-8322](https://issues.apache.org/jira/browse/QPID-8322) - [Broker-J] Error about negative credit used value is reported into broker logs
 - [QPID-8323](https://issues.apache.org/jira/browse/QPID-8323) - [Broker-J] NullPointerException when using temporary queues

## Tasks

 - [QPID-8315](https://issues.apache.org/jira/browse/QPID-8315) - update perftests visualisation csv dep to version available in maven central