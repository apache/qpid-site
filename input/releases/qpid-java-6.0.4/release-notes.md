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

# Qpid Java 6.0.4 Release Notes

Qpid Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

**Note**: This release addresses a security vulnerability in the JMS client,
CVE-2016-4974, see the [Security]({{site_url}}/security.html) pages for more details.

## New features and improvements

 - [QPID-7291](https://issues.apache.org/jira/browse/QPID-7291) - [Java Broker] [Documentation] Add documentation for ManagedCertificateStore and SiteSpecificTrustStore
 - [QPID-7305](https://issues.apache.org/jira/browse/QPID-7305) - [Java Broker] Queue operations copy/move/delete should take an optional JMS selector argument
 - [QPID-7323](https://issues.apache.org/jira/browse/QPID-7323) - [CVE-2016-4974] [Java Client] add whitelisting of trusted content for deserialization from ObjectMessage

## Bugs fixed

 - [QPID-7203](https://issues.apache.org/jira/browse/QPID-7203) - Model loses audit information 
 - [QPID-7282](https://issues.apache.org/jira/browse/QPID-7282) - Java Broker should always send server-final message (if required) to the client on succesful SASL negotiation
 - [QPID-7290](https://issues.apache.org/jira/browse/QPID-7290) - [Java Broker] [WMC] Incorrect title on 'Add TrustStore' dialog
 - [QPID-7298](https://issues.apache.org/jira/browse/QPID-7298) - [Java Broker] [0-8..0-91] Broker sends unsolicited ExchangeDeclareOk in response to declares of exchanges with reserved names 
 - [QPID-7301](https://issues.apache.org/jira/browse/QPID-7301) - [Java Client] [Java Broker] JMS Selector parsing will not fail if a valid selector is followed by invalid text
 - [QPID-7313](https://issues.apache.org/jira/browse/QPID-7313) - [Java Broker] Connection close REST request can hang when client application does not reply with ConnectionCloseOk to broker ConnectionClose command
