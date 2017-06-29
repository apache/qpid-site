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

# Qpid for Java 6.1.4 Release Notes

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7791](https://issues.apache.org/jira/browse/QPID-7791) - Recover metadata into direct memory
 - [QPID-7827](https://issues.apache.org/jira/browse/QPID-7827) - Recoverers allocate separate queue UUID for each recovered message instance

## Bugs fixed

 - [QPID-7811](https://issues.apache.org/jira/browse/QPID-7811) - [Java Broker] Asynchronous message store recoverer can delete message content for the message enqueued after broker startup