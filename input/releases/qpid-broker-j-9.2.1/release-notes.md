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

# Qpid Broker-J 9.2.1 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8668](https://issues.apache.org/jira/browse/QPID-8668) - [Broker-J] Increase the model version to 9.1 in the docker image
 - [QPID-8669](https://issues.apache.org/jira/browse/QPID-8669) - [Broker-J] Dependency updates for version 9.2.1
 - [QPID-8680](https://issues.apache.org/jira/browse/QPID-8680) - [Broker-J] Broker should interpret the value of qpid.port.heartbeatDelay as half of the actual idle timeout
 - [QPID-8681](https://issues.apache.org/jira/browse/QPID-8681) - [Broker-J] Addressing lock contention in Sorted Queues under high load by optimizing property fetching

## Bugs fixed

 - [QPID-8439](https://issues.apache.org/jira/browse/QPID-8439) - [Broker-J] Stack overflow during logging
 - [QPID-8571](https://issues.apache.org/jira/browse/QPID-8571) - [Broker-J] Non-unique consumer tags created for AMPQ 0-9-1
 - [QPID-8674](https://issues.apache.org/jira/browse/QPID-8674) - [Broker-J] Jms Selector Parsing - multiple AND's
 - [QPID-8675](https://issues.apache.org/jira/browse/QPID-8675) - [Broker-J] XSS vulnerability in path
 - [QPID-8676](https://issues.apache.org/jira/browse/QPID-8676) - [Broker-J] NPE when detaching endpoint
 - [QPID-8677](https://issues.apache.org/jira/browse/QPID-8677) - [Broker-J] IllegalConfigurationException when deleting misconfigured port
 - [QPID-8678](https://issues.apache.org/jira/browse/QPID-8678) - [Broker-J] Broker REST API returns certificate details for truststores but not keystores
 - [QPID-8679](https://issues.apache.org/jira/browse/QPID-8679) - [Broker-J] Copy nested configuration files in work-init and work-override
 - [QPID-8683](https://issues.apache.org/jira/browse/QPID-8683) - [Broker-J] Broker GUI should reflect producer information
