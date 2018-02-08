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

# Qpid Broker-J 7.0.1 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8032](https://issues.apache.org/jira/browse/QPID-8032) - [Broker-J][AMQP1.0] AsyncAutoCommitTransaction optimisation
 - [QPID-8086](https://issues.apache.org/jira/browse/QPID-8086) - [Broker-J] Create tool to permit recovery from QPID-8066
 - [QPID-8090](https://issues.apache.org/jira/browse/QPID-8090) - [Broker-J] Allow to specify all possible BoneCP configuration settings via context

## Bugs fixed

 - [QPID-8017](https://issues.apache.org/jira/browse/QPID-8017) - [Broker-J] [BDB]  JE log events written at JUL level FINE and below not included in the log produced by a BrokerLogger
 - [QPID-8025](https://issues.apache.org/jira/browse/QPID-8025) - [Broker-J] Improve detach error message on unsubscribing from JMS shared subs
 - [QPID-8027](https://issues.apache.org/jira/browse/QPID-8027) - [Broker-J][AMQP 0-8..0-9-1] Receiving BasicAck with unknown tag crashes the broker
 - [QPID-8029](https://issues.apache.org/jira/browse/QPID-8029) - [Broker-J] [AMQP 0-8..0-91] tx.rollback on non-transacted channel should not rollback the channel 
 - [QPID-8030](https://issues.apache.org/jira/browse/QPID-8030) - [Broker-J] Message conversion from 0-8 to 1.0 should preserve binary correlationId
 - [QPID-8040](https://issues.apache.org/jira/browse/QPID-8040) - [Broker-J] Uncaught java.nio.channels.CancelledKeyException seen during Broker shutdown
 - [QPID-8042](https://issues.apache.org/jira/browse/QPID-8042) - [Broker-J][AMQP 1.0] Support for pipelined connection open containing SASL frames broken
 - [QPID-8046](https://issues.apache.org/jira/browse/QPID-8046) - [Broker-J] Allow SASL mechanisms PLAIN and XOAUTH2 to not require initial response
 - [QPID-8047](https://issues.apache.org/jira/browse/QPID-8047) - [Broker-J][AMQP 0-10] NPE on receiving session.detach for unknown session
 - [QPID-8049](https://issues.apache.org/jira/browse/QPID-8049) - Non-free ICC profiles
 - [QPID-8058](https://issues.apache.org/jira/browse/QPID-8058) - [Broker-J][AMQP 1.0] Broker does not respond to drain request from consumer of management temporary destination
 - [QPID-8060](https://issues.apache.org/jira/browse/QPID-8060) - [Broker-J] [AMQP 0-8..0-9-1] Declaring queue with an alternate binding that does not exist crashes the Broker
 - [QPID-8061](https://issues.apache.org/jira/browse/QPID-8061) - [Broker-J] [AMQP 0-8..0-9-1] Declaring exchange with not existing alternate binding crashes the Broker
 - [QPID-8062](https://issues.apache.org/jira/browse/QPID-8062) - [Broker-J][AMQP 1.0] Fix handling of routing errors when target destination cannot route received message
 - [QPID-8066](https://issues.apache.org/jira/browse/QPID-8066) - [Broker-J] Virtual host logger rules are left over in configuration store after deletion of virtual host logger on provided virtual host causing virtualhost restart failure
 - [QPID-8067](https://issues.apache.org/jira/browse/QPID-8067) - [Broker-J] Default queue filter for arrival time with non-zero replay period does not filter messages as documented
 - [QPID-8070](https://issues.apache.org/jira/browse/QPID-8070) - [Broker-J][JDBC Store] Instantiate asynchronous commits executor on open of JDBC message store
 - [QPID-8079](https://issues.apache.org/jira/browse/QPID-8079) - [Broker-J] If the future associated with an AsyncCommand completes abnormally, the associated action is not rolled-back
 - [QPID-8081](https://issues.apache.org/jira/browse/QPID-8081) - [Broker-J] FileLogger with "roll on restart" set to "true" does not roll log file on broker restart when "roll daily" is "true"
 - [QPID-8087](https://issues.apache.org/jira/browse/QPID-8087) - [Broker-J][BDB] [HA] Virtualhostnode fails to go into ERROR state following failure to recover
 - [QPID-8092](https://issues.apache.org/jira/browse/QPID-8092) - [Broker-J][Web Management Console] Fix label for max history of file loggers

## Tasks

 - [QPID-8094](https://issues.apache.org/jira/browse/QPID-8094) - [Broker-J] Release Qpid Broker-J 7.0.1