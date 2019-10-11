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

# Qpid Broker-J 7.1.5 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8306](https://issues.apache.org/jira/browse/QPID-8306) - [Broker-J] Add ability to update TLS transport on AMQP port after changing keystore, trustores or other TLS related attributes
 - [QPID-8330](https://issues.apache.org/jira/browse/QPID-8330) - [Broker-J] Upgrade jetty dependencies to version 9.4.19.v20190610
 - [QPID-8332](https://issues.apache.org/jira/browse/QPID-8332) - [Broker-J] Upgrade slf4j dependency to version 1.7.26
 - [QPID-8333](https://issues.apache.org/jira/browse/QPID-8333) - [Broker-J] Upgrade logback dependencies to version 1.2.3
 - [QPID-8334](https://issues.apache.org/jira/browse/QPID-8334) - [Broker-J] Upgrade hamcrest dependency to version 2.1
 - [QPID-8339](https://issues.apache.org/jira/browse/QPID-8339) - [Broker-J] Upgrade junit dependency to version 4.12
 - [QPID-8340](https://issues.apache.org/jira/browse/QPID-8340) - [Broker-J] Upgrade mockito to version 2.28.2
 - [QPID-8348](https://issues.apache.org/jira/browse/QPID-8348) - [Broker-J] Add ability to reload keystore/truststore
 - [QPID-8353](https://issues.apache.org/jira/browse/QPID-8353) - [Broker-J][JMS AMQP 0-x] Add support for TLSv1.3
 - [QPID-8354](https://issues.apache.org/jira/browse/QPID-8354) - [Broker-J][JMS AMQP 0-x] Backlist TLSv1.1
 - [QPID-8363](https://issues.apache.org/jira/browse/QPID-8363) - [Broker-J] Add support for GSSAPI bind into SimpleLDAP authentication provider
 - [QPID-8364](https://issues.apache.org/jira/browse/QPID-8364) - [Broker-J] Add support for SPNEGO authentication into HTTP management
 - [QPID-8365](https://issues.apache.org/jira/browse/QPID-8365) - [Broker-J] Upgrade jackson dependencies to version 2.9.10

## Bugs fixed

 - [QPID-8126](https://issues.apache.org/jira/browse/QPID-8126) - [Broker-J][SimpleLDAP] NPE is reported into broker logs when search user is specified but search password is not set 
 - [QPID-8289](https://issues.apache.org/jira/browse/QPID-8289) - [Broker-J] Broker startup can fail due to ConcurrentModificationException
 - [QPID-8341](https://issues.apache.org/jira/browse/QPID-8341) - [Broker-J] Reject overflow policy can erroneously rejects messages when maximumQueueDepthBytes is specified
 - [QPID-8342](https://issues.apache.org/jira/browse/QPID-8342) - [Broker-J] Concurrent object creation with virtual host auto-creation policy can fail
 - [QPID-8343](https://issues.apache.org/jira/browse/QPID-8343) - [Broker-J][AMQP 1.0] Broker mistakenly creates durable dynamic destinations for lifetime policies "delete-on-close", "delete-on-no-links", "delete-on-no-messages" or "delete-on-no-links-or-messages"
 - [QPID-8344](https://issues.apache.org/jira/browse/QPID-8344) - [Broker-J] Generation of virtal host registry dump fails
 - [QPID-8345](https://issues.apache.org/jira/browse/QPID-8345) - [Broker-J][AMQP 1.0] Consumed messages are left in acquired state on a queue when receiver's desired snd-settle-mode is set to settled and transactions are not used for message receiving
 - [QPID-8355](https://issues.apache.org/jira/browse/QPID-8355) - [Broker-J] BrokerAttributeInjector can't load HotSpotDiagnosticMXBean on Eclipse J9
 - [QPID-8356](https://issues.apache.org/jira/browse/QPID-8356) - [Broker-J] ACL rule properties 'from_network' and 'from_hostname' are lost on loading ACL from file in 'RuleBased' access control provider
 - [QPID-8357](https://issues.apache.org/jira/browse/QPID-8357) - [Broker-J][AMQP 1.0] Broker-J does not set property 'open' performative property 'sole-connection-eforcement-policy' when 'close-existing' eforcement policy is requested
 - [QPID-8366](https://issues.apache.org/jira/browse/QPID-8366) - [Broker-J] The loss of BDB HA majority on invocation of house keeping operations can crash the broker
 - [QPID-8371](https://issues.apache.org/jira/browse/QPID-8371) - [Broker-J][WMC] The error messages are not communicated back to user of web management console on attempt to invoke operation without sufficient permissions