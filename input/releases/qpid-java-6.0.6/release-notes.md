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

# Qpid for Java 6.0.6 Release Notes

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [QPID-7470](https://issues.apache.org/jira/browse/QPID-7470) - [Java Broker] Address javax.xml.bind.DatatypeConverter shortcomings
 - [QPID-7508](https://issues.apache.org/jira/browse/QPID-7508) - Broker occasionally fails to report SUB-1003 in response to a consumer that has become suspended
 - [QPID-7560](https://issues.apache.org/jira/browse/QPID-7560) - AbstractVirtualHost defines two state transitions from ERROR to ACTIVE