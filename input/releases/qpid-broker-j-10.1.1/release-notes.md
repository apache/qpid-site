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

# Qpid Broker-J 10.1.1 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

See also the [Broker-J security page]({{site_url}}/components/broker-j/security.html) for issues addressed in this release.

## Bugs fixed

 - [QPID-8672](https://issues.apache.org/jira/browse/QPID-8672) - [Broker-J] High CPU Usage because of unnecessary flushCreditState() calls for all consumers of session.
 - [QPID-8736](https://issues.apache.org/jira/browse/QPID-8736) - [Broker-J] NullPointerException: Cannot invoke "java.util.List.add(Object)" because "frames" is null
 - [QPID-8750](https://issues.apache.org/jira/browse/QPID-8750) - [Broker-J] AsyncAutoCommitTransaction can enqueue messages out of order when a queue's messageDurability forces storage of non-persistent messages
 - [QPID-8751](https://issues.apache.org/jira/browse/QPID-8751) - [Broker-J] AMQP 1.0 consumer is never resumed when the session incoming window is reopened by a flow naming another link
 - [QPID-8752](https://issues.apache.org/jira/browse/QPID-8752) - [Broker-J] Connection- and session-level Subject caching
 - [QPID-8757](https://issues.apache.org/jira/browse/QPID-8757) - [Broker-J] WebSocket idle checker queues unbounded tick jobs while a connection is writing, exhausting the broker heap
 - [QPID-8758](https://issues.apache.org/jira/browse/QPID-8758) - [Broker-J] Ensure AMQP-over-WebSocket connections terminate after an unanswered close
 - [QPID-8760](https://issues.apache.org/jira/browse/QPID-8760) - [Broker-J] ServletContextHandler.setHandler should not be called directly
 - [QPID-8761](https://issues.apache.org/jira/browse/QPID-8761) - [Broker-J] QueryEvaluationException: Objects of types 'null' and 'String' can not be compared
