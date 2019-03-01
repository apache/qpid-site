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

# Qpid Broker-J 7.0.7 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8224](https://issues.apache.org/jira/browse/QPID-8224) - [Broker-J][WMC] Add UI to configure exchange unroutable message behaviour for AMQP 1.0
 - [QPID-8232](https://issues.apache.org/jira/browse/QPID-8232) - [Broker-J] Disabling logging using  log level OFF is not respected by the logging framework
 - [QPID-8238](https://issues.apache.org/jira/browse/QPID-8238) - [Broker-J] Improve performance of asynchronous publishing of transient messages into topic exchange having queues bound using non-overlapping selectors 
 - [QPID-8243](https://issues.apache.org/jira/browse/QPID-8243) - [Broker-J] Optimize logback turbo filter implemented to provide a workaround for Logback1027
 - [QPID-8244](https://issues.apache.org/jira/browse/QPID-8244) - [Broker-J] Optimize fanout exchange routing functionality
 - [QPID-8256](https://issues.apache.org/jira/browse/QPID-8256) - [Broker-J] Update Guava to version 27.0
 - [QPID-8260](https://issues.apache.org/jira/browse/QPID-8260) - [Broker-J] Add support for provided preferences store into Derby and JDBC system configs
 - [QPID-8264](https://issues.apache.org/jira/browse/QPID-8264) - [Broker-J] ClassCastException are thrown on creation and update of VirtualHostUserOrConnectionLogInclusionRule
 - [QPID-8279](https://issues.apache.org/jira/browse/QPID-8279) - [Broker-J] Upgrade Jackson dependencies

## Bugs fixed

 - [QPID-8201](https://issues.apache.org/jira/browse/QPID-8201) - [Broker-J] [AMQP1.0] Queue backing temporary subscription deleted twice during link close
 - [QPID-8216](https://issues.apache.org/jira/browse/QPID-8216) - [Broker-J] Operational log message CHN-1011 about moving message to dead letter queue is not reported
 - [QPID-8219](https://issues.apache.org/jira/browse/QPID-8219) - [Broker-J] Authentication results are cached in SimpleLdap and OAUTH2 authentication providers per connection basis
 - [QPID-8223](https://issues.apache.org/jira/browse/QPID-8223) - [Broker-J] [AMQP 1.0] Broker can stop delivering messages when sending link delivery-count value exceeds Integer.MAX_VALUE, wraps around and turns negative
 - [QPID-8225](https://issues.apache.org/jira/browse/QPID-8225) - [Broker-J][AMQP 0-10] stops delivering queue/consumer messages after 4 GB data transfer
 - [QPID-8231](https://issues.apache.org/jira/browse/QPID-8231) - [Broker-J] [AMQP 0-8...0-9-1] Broker crashes on delivery of messages from queue having attribute 'messageGroupKeyOverride' set to an empty string
 - [QPID-8233](https://issues.apache.org/jira/browse/QPID-8233) - [Broker-J][AMQP 1.0] Failure on connecting to a virtual host which is not yet active should use connection-forced error
 - [QPID-8236](https://issues.apache.org/jira/browse/QPID-8236) - [Broker-J] [BDB HA] Changing of group name, address or node name in BDB HA virtual host node should be disallowed 
 - [QPID-8254](https://issues.apache.org/jira/browse/QPID-8254) - [Broker-J] Illegal ascii characters are used in keystore passwords