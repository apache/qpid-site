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

# Qpid Broker-J 7.0.3 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7925](https://issues.apache.org/jira/browse/QPID-7925) - [Broker-J] [WMC] Add ability to maintain rule-based access control provider for virtualhost
 - [QPID-8136](https://issues.apache.org/jira/browse/QPID-8136) - [Broker-J] Upgrade Jackson dependencies
 - [QPID-8147](https://issues.apache.org/jira/browse/QPID-8147) - [Broker-J] Report first 8 received bytes as part of operational log message for unsupported protocol header

## Bugs fixed

 - [QPID-7948](https://issues.apache.org/jira/browse/QPID-7948) - [Broker-J] [AMQP0-9] [Publish Confirms] Client hangs if message sent to topic within no subscribers
 - [QPID-8016](https://issues.apache.org/jira/browse/QPID-8016) - [Broker-J] FileKeyStore alias does not select the correct certificate
 - [QPID-8113](https://issues.apache.org/jira/browse/QPID-8113) - [Broker-J] Incorrect symbolic descriptor used for (JMS) selector
 - [QPID-8115](https://issues.apache.org/jira/browse/QPID-8115) - [Broker-J] Incorrect symbolic descriptor used for no-local filter
 - [QPID-8121](https://issues.apache.org/jira/browse/QPID-8121) - [Broker-J] Virtualhost scoped statistics messages absent from virtualhost logs
 - [QPID-8124](https://issues.apache.org/jira/browse/QPID-8124) - [Broker-J][REST] Sucessfully authenticated user is reported as &lt;&lt;UNKNOWN&gt;&gt; in ACL operational logs when checking access to management
 - [QPID-8130](https://issues.apache.org/jira/browse/QPID-8130) - [Broker-J] IAE "Comparison method violates its general contract!" can be thrown whilst comparing log file details of file logger
 - [QPID-8137](https://issues.apache.org/jira/browse/QPID-8137) - [Broker-J] NPE is reported into broker logs on broker shutdown/restart when AMQP port is in ERRORED state due to port being bound by other process
 - [QPID-8144](https://issues.apache.org/jira/browse/QPID-8144) - [Broker-J] Memory compaction does not run when used direct memory exceeds 2GB