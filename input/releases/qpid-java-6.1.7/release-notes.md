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

# Qpid for Java 6.1.7 Release Notes

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [QPID-8202](https://issues.apache.org/jira/browse/QPID-8202) - [Broker-J][AMQP 0-8...0-91] Large flowed to disk message can be re-loaded from store for every content chunk sent to the client
 - [QPID-8207](https://issues.apache.org/jira/browse/QPID-8207) - [Broker-J] Flow to disk might not be triggered in some circumstances
 - [QPID-8219](https://issues.apache.org/jira/browse/QPID-8219) - [Broker-J] Authentication results are cached in SimpleLdap and OAUTH2 authentication providers per connection basis
 - [QPID-8229](https://issues.apache.org/jira/browse/QPID-8229) - [Broker-J][6.x] Queue bindings are not removed on queue deletion when BDB/DERBY/JDBC configuration stores are used
 - [QPID-8236](https://issues.apache.org/jira/browse/QPID-8236) - [Broker-J] Changing of group name, address or node name in BDB HA virtual host node should be disallowed