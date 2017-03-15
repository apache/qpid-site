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

# Qpid JMS 0.20.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-207](https://issues.apache.org/jira/browse/QPIDJMS-207) - Implement the JMS 2.0 API
 - [QPIDJMS-215](https://issues.apache.org/jira/browse/QPIDJMS-215) - Eliminate the need to copy messages on MessageProducer send
 - [QPIDJMS-216](https://issues.apache.org/jira/browse/QPIDJMS-216) - Don't encode a Header for Messages that don't require one
 - [QPIDJMS-217](https://issues.apache.org/jira/browse/QPIDJMS-217) - Remove unecessary copy of the body if an inbound BytesMessage
 - [QPIDJMS-219](https://issues.apache.org/jira/browse/QPIDJMS-219) - allow MessageListeners to be used when prefetch is configured to 0 
 - [QPIDJMS-229](https://issues.apache.org/jira/browse/QPIDJMS-229) - allow supplying an SslContext instead of the configuration used to create one
 - [QPIDJMS-232](https://issues.apache.org/jira/browse/QPIDJMS-232) - Perform Authentication when the remote connection is established instead of waiting until Connection is used
 - [QPIDJMS-235](https://issues.apache.org/jira/browse/QPIDJMS-235) - add option to complete AMQP Open without waiting for a ClientID to [not] be set
 - [QPIDJMS-238](https://issues.apache.org/jira/browse/QPIDJMS-238) - update to proton-j 0.16.0
 - [QPIDJMS-240](https://issues.apache.org/jira/browse/QPIDJMS-240) - Add configuration option to determine if the Connection maintains a non-daemon thread
 - [QPIDJMS-250](https://issues.apache.org/jira/browse/QPIDJMS-250) - Handle invalid URI on ConnectionFactory create in a consistent manner
 - [QPIDJMS-253](https://issues.apache.org/jira/browse/QPIDJMS-253) - have transport config defaults pick up changes to the SSL system properties

## Bugs fixed

 - [QPIDJMS-208](https://issues.apache.org/jira/browse/QPIDJMS-208) - Can't set custom deserialization policy on ConnectionFactory
 - [QPIDJMS-209](https://issues.apache.org/jira/browse/QPIDJMS-209) - Failover Transport can hold completion of operations that it doesn't need to when the connection fails
 - [QPIDJMS-218](https://issues.apache.org/jira/browse/QPIDJMS-218) - ConcurrentModificationException during remote closure of session with multiple producers or consumers
 - [QPIDJMS-221](https://issues.apache.org/jira/browse/QPIDJMS-221) - Blocked receive calls are not unblocked on session / consumer close when awaiting a drain response
 - [QPIDJMS-222](https://issues.apache.org/jira/browse/QPIDJMS-222) - Footer value not included in Message Copy.
 - [QPIDJMS-223](https://issues.apache.org/jira/browse/QPIDJMS-223) - Redirect Exception creation return wrong exception in some cases
 - [QPIDJMS-224](https://issues.apache.org/jira/browse/QPIDJMS-224) - QueueSender calls incorrect superclass send method
 - [QPIDJMS-226](https://issues.apache.org/jira/browse/QPIDJMS-226) - Failover recovery can hang when Temporary Destination is being recreated.
 - [QPIDJMS-227](https://issues.apache.org/jira/browse/QPIDJMS-227) - NullPointerException on closing anonymous producer
 - [QPIDJMS-228](https://issues.apache.org/jira/browse/QPIDJMS-228) - Connection close can use wrong timeout value and stall
 - [QPIDJMS-234](https://issues.apache.org/jira/browse/QPIDJMS-234) - set supported source outcomes on Coordinator links
 - [QPIDJMS-236](https://issues.apache.org/jira/browse/QPIDJMS-236) - include all supported outcomes on producer link source
 - [QPIDJMS-237](https://issues.apache.org/jira/browse/QPIDJMS-237) - Connection doesn't always shutdown its internal threads on connection loss
 - [QPIDJMS-242](https://issues.apache.org/jira/browse/QPIDJMS-242) - Creation of consumer, producer or session hangs when connection is in a process of re-establishing by failover
 - [QPIDJMS-243](https://issues.apache.org/jira/browse/QPIDJMS-243) - NPE is reported when failover tries to connect to stopped/not available broker
 - [QPIDJMS-245](https://issues.apache.org/jira/browse/QPIDJMS-245) - Factory connection string in JNDI properties file will be decoded twice resulting to unexpected value
 - [QPIDJMS-249](https://issues.apache.org/jira/browse/QPIDJMS-249) - Don't close consumer when a drain request times out if the consumer is in a Transaction
 - [QPIDJMS-251](https://issues.apache.org/jira/browse/QPIDJMS-251) - Thread unsafe use of MessageListener and state variable in JmsMessageConsumer
 - [QPIDJMS-254](https://issues.apache.org/jira/browse/QPIDJMS-254) - trust store config password default taken from incorrect system property

## Tasks

 - [QPIDJMS-225](https://issues.apache.org/jira/browse/QPIDJMS-225) - Add additional testing for not yet covered code paths and use cases
 - [QPIDJMS-233](https://issues.apache.org/jira/browse/QPIDJMS-233) - Update test dependency to ActiveMQ 5.14.2 
 - [QPIDJMS-246](https://issues.apache.org/jira/browse/QPIDJMS-246) - Update to latest Netty 4.1.6 release and fix usages deprecated netty methods
 - [QPIDJMS-247](https://issues.apache.org/jira/browse/QPIDJMS-247) - Update slf4j to 1.7.22 
 - [QPIDJMS-248](https://issues.apache.org/jira/browse/QPIDJMS-248) - Target Java 8+, i.e. drop support for Java 7
 - [QPIDJMS-252](https://issues.apache.org/jira/browse/QPIDJMS-252) - update to current apache parent pom
