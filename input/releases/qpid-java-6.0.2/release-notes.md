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

# Qpid Java 6.0.2 Release Notes

Qpid Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7159](https://issues.apache.org/jira/browse/QPID-7159) - [Java Client] Disabling user ids in AMQP messages

## Bugs fixed

 - [QPID-7023](https://issues.apache.org/jira/browse/QPID-7023) - BDB HA: JE Cleaner warnings written to qpid log during apparently normal operation 
 - [QPID-7033](https://issues.apache.org/jira/browse/QPID-7033) - [Java Broker] Busy IO thread pools may cause client connections to be unfairly closed
 - [QPID-7097](https://issues.apache.org/jira/browse/QPID-7097) - [Java Broker, HA] Broker configuration thread is used to perform notifications about removal of BDB HA VirtualHost when VH is closed in response to environment state transition events
 - [QPID-7114](https://issues.apache.org/jira/browse/QPID-7114) - [Java Broker] ConnectionBuilder should set protocol and cipher suites on all code paths
 - [QPID-7136](https://issues.apache.org/jira/browse/QPID-7136) - [Java Broker] [BDB HA] [AMQP 1.0] Connection to a replica throws an uncaught exception which closes the broker
 - [QPID-7154](https://issues.apache.org/jira/browse/QPID-7154) - Dead lettering of a message may timeout at store level, causing unexpected Broker shutdown
 - [QPID-7155](https://issues.apache.org/jira/browse/QPID-7155) - [Java Broker] Idle timeout ticker times out connection before heartbeating is negotiated
 - [QPID-7156](https://issues.apache.org/jira/browse/QPID-7156) - Possible Java Broker crash if connection is formed whilst virtualhost is stopping
 - [QPID-7181](https://issues.apache.org/jira/browse/QPID-7181) - [AMQP 1.0] Selector parsing error causes Java Broker to shutdown
 - [QPID-7186](https://issues.apache.org/jira/browse/QPID-7186) - CancelledKeyException from the accepting thread during Broker shutdown
 - [QPID-7189](https://issues.apache.org/jira/browse/QPID-7189) - [Java Client 0-8..0-10] Client fails to create delegate for AMQP 0.9.1 in response to broker supported protocol received during protocol negotiation