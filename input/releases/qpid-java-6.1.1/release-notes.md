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

# Qpid for Java 6.1.1 Release Notes

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7519](https://issues.apache.org/jira/browse/QPID-7519) - Remove unnecessary Jetty dependency (jetty-client) from Broker
 - [QPID-7561](https://issues.apache.org/jira/browse/QPID-7561) - [Java Broker] Do not allow the creation of Derby Virtual Hosts if the Derby JDBC driver is not present

## Bugs fixed

 - [QPID-7491](https://issues.apache.org/jira/browse/QPID-7491) - [Java Broker] Fix AbstractSystemMessageSource#pullMessage
 - [QPID-7508](https://issues.apache.org/jira/browse/QPID-7508) - Broker occasionally fails to report SUB-1003 in response to a consumer that has become suspended
 - [QPID-7513](https://issues.apache.org/jira/browse/QPID-7513) - [Java Broker] If no virtualHostNode is provided, a PatternMatchingAlias should return the default virtual host node
 - [QPID-7515](https://issues.apache.org/jira/browse/QPID-7515) - [Java Broker] VirtualHost#publishMessage throws NPE if request body is empty
 - [QPID-7535](https://issues.apache.org/jira/browse/QPID-7535) - [Java Client] Strengthen notification between threads holding dispatcher lock
 - [QPID-7548](https://issues.apache.org/jira/browse/QPID-7548) - [Java Broker] Upgrade of configuration from model version 3 fails
 - [QPID-7549](https://issues.apache.org/jira/browse/QPID-7549) - [Java Broker] Authentication using SimpleLDAP authentication provider fails with NPE when caching of authentication results is enabled(by default)
 - [QPID-7560](https://issues.apache.org/jira/browse/QPID-7560) - AbstractVirtualHost defines two state transitions from ERROR to ACTIVE
 - [QPID-7577](https://issues.apache.org/jira/browse/QPID-7577) - [Java Broker] Generic JDBC configuration store mistakenly is put into OPEN state in init