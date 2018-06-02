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

# Qpid Broker-J 7.0.4 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8163](https://issues.apache.org/jira/browse/QPID-8163) - [Broker-J] [ACL] Owner ACL rules
 - [QPID-8181](https://issues.apache.org/jira/browse/QPID-8181) - [Broker-J] Add statistics for a total number of connections established on AMQP port

## Bugs fixed

 - [QPID-8160](https://issues.apache.org/jira/browse/QPID-8160) -  [Broker-J] [AMQP 1.0] AccessControlException when creating sending link reported as  amqp:internal-error rather than amqp:unauthorised-access
 - [QPID-8164](https://issues.apache.org/jira/browse/QPID-8164) - [Broker-J] [AMQP 1.0] [BINDMAP] Dynamic nodes created with the temporary-queue capability do not enforce connection exclusivity
 - [QPID-8165](https://issues.apache.org/jira/browse/QPID-8165) - [Broker-J][WMC] Validation of configured object names is too restrictive in Web Management Console
 - [QPID-8171](https://issues.apache.org/jira/browse/QPID-8171) - [Broker-J] Failed to start broker under Windows when QPID_JAVA_GC is set 
 - [QPID-8176](https://issues.apache.org/jira/browse/QPID-8176) - [Broker-J][WMC] Infinite loop in Web Management Console restart operation when OAuth2 authentication provider is configured on http port
 - [QPID-8182](https://issues.apache.org/jira/browse/QPID-8182) - [Broker-J] [Message Conversion] Message id fidelity lost when converting from AMQP 1.0 to 0-10 when message-id-string carries a ID: prefixed UUID
 - [QPID-8198](https://issues.apache.org/jira/browse/QPID-8198) - [Broker-J][Documentation] Account headers in formula for estimation of heap size