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

# Qpid JMS AMQP 0-x 6.3.0 Release Notes

Qpid JMS AMQP 0-x is JMS 1.1 compatible client which can speak AMQP 0-8,0-9,0-9-1 and 0-10.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPID-7292](https://issues.apache.org/jira/browse/QPID-7292) - Qpid clients should verify the server-final message when using SCRAM-* authentication
 - [QPID-7466](https://issues.apache.org/jira/browse/QPID-7466) - [Java Broker, Java Client for AMQP 0-8 to 0-10] Improve documentation for end-to-end encryption
 - [QPID-7476](https://issues.apache.org/jira/browse/QPID-7476) - [Java Client] Improve error message when timeout exception thrown in commit
 - [QPID-7524](https://issues.apache.org/jira/browse/QPID-7524) - [Java Client] New lines should be specified with '%n' in calls to String.format
 - [QPID-7530](https://issues.apache.org/jira/browse/QPID-7530) - [Java Client] AMQSession_0_8#isQueueExist contains dead code intending to send passive queue declaration when queue is bound to a default exchange and assert flag is set to true
 - [QPID-7532](https://issues.apache.org/jira/browse/QPID-7532) - [Java] Replace AMQConstant class with constant integer error codes
 - [QPID-7533](https://issues.apache.org/jira/browse/QPID-7533) - [Java Broker] Implement wd12 version of the AMQP Management working draft
 - [QPID-7538](https://issues.apache.org/jira/browse/QPID-7538) - [Java Client] Improve handling of hanshake status codes in SSLSender
 - [QPID-7622](https://issues.apache.org/jira/browse/QPID-7622) - Separate Qpid Broker for Java and 0-x JMS Client in source tree
 - [QPID-7718](https://issues.apache.org/jira/browse/QPID-7718) - Tidy up 0-x JMS Client source tree following separation from Broker.
 - [QPID-7725](https://issues.apache.org/jira/browse/QPID-7725) - Remove direct byte buffer implementation
 - [QPID-7726](https://issues.apache.org/jira/browse/QPID-7726) - Upgrade SLF4J to 1.7.25
 - [QPID-7737](https://issues.apache.org/jira/browse/QPID-7737) - [JMS AMQP 0-x Client] Upgrade SLF4j to 1.7.25
 - [QPID-7778](https://issues.apache.org/jira/browse/QPID-7778) - [Java Broker, Documentation] The Message encryption pages should mention that they require the Unlimited Strength JCE
 - [QPID-7779](https://issues.apache.org/jira/browse/QPID-7779) - [Qpid JMS Client 0-x] [0-8..0-91] sasl_mechs and other SASL connection options not supported
 - [QPID-8018](https://issues.apache.org/jira/browse/QPID-8018) - [Java Client, AMQP 0-x] Clarify error message when connection times out
 - [QPID-8034](https://issues.apache.org/jira/browse/QPID-8034) - [Qpid JMS AMQP 0-x] Update bundling to follow project conventions

## Bugs fixed

 - [QPID-7505](https://issues.apache.org/jira/browse/QPID-7505) - [JMS AMQP 0-x Client] [AMQP 0-10] Synchronous #receive(long) might return null even though there are messages on the queue and client has enough credit
 - [QPID-7507](https://issues.apache.org/jira/browse/QPID-7507) - AMQSession_0_10.isQueueExist() fails with NPE if SessionException does not have a cause
 - [QPID-7535](https://issues.apache.org/jira/browse/QPID-7535) - [Java Client] Strengthen notification between threads holding dispatcher lock
 - [QPID-7537](https://issues.apache.org/jira/browse/QPID-7537) - Improve implementations of equal methods in various classes to be able to account for sub-classes
 - [QPID-7544](https://issues.apache.org/jira/browse/QPID-7544) - [Java Client][AMQP 0-10] After resending a previously sent Message, the JMSMessageId is not updated
 - [QPID-7692](https://issues.apache.org/jira/browse/QPID-7692) - [Java Broker, 0-8..0-91]  Message sent to fanout exchange with no routing key is not delivered to application
 - [QPID-7774](https://issues.apache.org/jira/browse/QPID-7774) - [JMS Client 0-x] [0-8..0-91] MessageConsumer#receiveNoWait() always returns null after a successful failover
 - [QPID-7888](https://issues.apache.org/jira/browse/QPID-7888) - [Java Client] [Documentation] Correct typo in end to end encryption connection url examples
 - [QPID-7897](https://issues.apache.org/jira/browse/QPID-7897) - [Java 0-8...0-9-1 Client] Message#getJMSCorrelationIDAsBytes() erroneously first converts to string before retreiving bytes 
 - [QPID-7898](https://issues.apache.org/jira/browse/QPID-7898) - [Java 0-8...0-9-1 Client] Calling getJMSReplyTo on a received message can lead to NullPointerException
 - [QPID-7899](https://issues.apache.org/jira/browse/QPID-7899) - [Java 0-8...0-9-1 Client] Message#setJMSCorrelationIDAsBytes() erroneously converts the bytes to string
 - [QPID-7964](https://issues.apache.org/jira/browse/QPID-7964) - [Java Client, AMQP 0-x] SCRAM SASL implementation incorrectly encodes "=" and "," for passwords
 - [QPID-8033](https://issues.apache.org/jira/browse/QPID-8033) - [Qpid JMS AMQP 0-x] An establishment of connection times out if an exception is thrown from ConnectionStartMethoHandler due to unsupported sasl mechanisms

## Tasks

 - [QPID-7628](https://issues.apache.org/jira/browse/QPID-7628) - [java] update to current apache parent pom
 - [QPID-7716](https://issues.apache.org/jira/browse/QPID-7716) - Remove AMQP 0-10 based JCA/RA components from Qpid JMS 0-x Client
 - [QPID-7738](https://issues.apache.org/jira/browse/QPID-7738) - [Qpid JMS AMQP 0-x Client] Migrate qpid-java svn to git 
 - [QPID-7755](https://issues.apache.org/jira/browse/QPID-7755) - add release scripts for qpid-broker-j and qpid-jms-amqp-0-x