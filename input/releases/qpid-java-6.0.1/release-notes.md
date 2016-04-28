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

# Qpid Java 6.0.1 Release Notes

Qpid Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-6932](https://issues.apache.org/jira/browse/QPID-6932) - Enhance model object to expose key JVM statistics such as heap memory, garbage collection
 - [QPID-6940](https://issues.apache.org/jira/browse/QPID-6940) - [Java Broker] [AMQP 1.0] The Delivery object does not need to retain a list of associated transfers
 - [QPID-6961](https://issues.apache.org/jira/browse/QPID-6961) - Use maven to generate Java Broker and (legacy) Java Client docbook
 - [QPID-6965](https://issues.apache.org/jira/browse/QPID-6965) - Make preemptive HTTP authentication pluggable
 - [QPID-6967](https://issues.apache.org/jira/browse/QPID-6967) - [Java Broker] Add SCRAM-SHA1/256 sasl support to authentication managers which store the password in cleartext
 - [QPID-6977](https://issues.apache.org/jira/browse/QPID-6977) - [Java Client] Partial port - Enable TLSv1.1 and v1.2 in client qpid-java-6.0.1
 - [QPID-6978](https://issues.apache.org/jira/browse/QPID-6978) - [Java Broker] Partial port - Port the ability to disable TLS Protocols qpid-java-6.0.1
 - [QPID-6993](https://issues.apache.org/jira/browse/QPID-6993) - [Java Broker] Improve security of SCRAM-* authentication managers by not storing the salted passwords
 - [QPID-7007](https://issues.apache.org/jira/browse/QPID-7007) - Add the ability to mutate JE configuration properties at runtime
 - [QPID-7009](https://issues.apache.org/jira/browse/QPID-7009) - BDD HA: DbPing call should have an independent timeout control
 - [QPID-7017](https://issues.apache.org/jira/browse/QPID-7017) - Include Queue UUID in QUE-1001/1002 operational log message
 - [QPID-7019](https://issues.apache.org/jira/browse/QPID-7019) - BDB JE turn on log file upgrade migration by default
 - [QPID-7027](https://issues.apache.org/jira/browse/QPID-7027) - [Java Broker] Make HTTP Management interactive login pluggable
 - [QPID-7028](https://issues.apache.org/jira/browse/QPID-7028) - [Java Broker] Add OAuth2 AuthenticationProvider
 - [QPID-7029](https://issues.apache.org/jira/browse/QPID-7029) - [Java Broker] Add OAuth2 PreemptiveAuthenticator
 - [QPID-7030](https://issues.apache.org/jira/browse/QPID-7030) - [Java Broker] Add OAuth2 HttpRequestInteractiveAuthenticator
 - [QPID-7031](https://issues.apache.org/jira/browse/QPID-7031) - [Java Broker] Add Pluggable OAuth2 AuthenticationProvider Backend for CloudFoundry
 - [QPID-7032](https://issues.apache.org/jira/browse/QPID-7032) - [Java Broker] Add information about the selected TLS protocol and cipher suite on Connection objects
 - [QPID-7035](https://issues.apache.org/jira/browse/QPID-7035) - [Java Broker] SCRAM implementation should make iteration count configurable
 - [QPID-7039](https://issues.apache.org/jira/browse/QPID-7039) - [Java Broker] Allow overriding of default initial configuration location via system property
 - [QPID-7045](https://issues.apache.org/jira/browse/QPID-7045) - [Java Broker] Add OAuth2 SASL mechanism
 - [QPID-7048](https://issues.apache.org/jira/browse/QPID-7048) - Log a warning if an AMQPPort does not have one or more virtual host aliases
 - [QPID-7049](https://issues.apache.org/jira/browse/QPID-7049) - [Java Broker] Provide a mechanism to inject attribute/statistic definitions into types at runtime
 - [QPID-7055](https://issues.apache.org/jira/browse/QPID-7055) - Improve GroupProvider API
 - [QPID-7056](https://issues.apache.org/jira/browse/QPID-7056) - [Java Broker/Client] Allow overriding of TLS cipher suites preferences
 - [QPID-7058](https://issues.apache.org/jira/browse/QPID-7058) - [Java Client] Log the current connection state when connection establishment times out
 - [QPID-7068](https://issues.apache.org/jira/browse/QPID-7068) - Drive AbstractConfiguredObject#validationChange from reflection rather than attribute metadata
 - [QPID-7069](https://issues.apache.org/jira/browse/QPID-7069) - [Java Broker] Add CloudFoundry specific GroupProvider
 - [QPID-7079](https://issues.apache.org/jira/browse/QPID-7079) - [Java Broker] Add connection state logging on idle timeout to 0-10 onnections

## Bugs fixed

 - [QPID-6817](https://issues.apache.org/jira/browse/QPID-6817) - [Java Broker] On abrupt connection close from client side when Broker is delivering messages to consumer the delivered messages might not be released as part of close in some unlucky circumstances
 - [QPID-6939](https://issues.apache.org/jira/browse/QPID-6939) - [Java Broker] [AMQP 1.0] Ensure all outstanding bytes get processed when received() is called on the connection
 - [QPID-6944](https://issues.apache.org/jira/browse/QPID-6944) - High CPU use sending message using SSL
 - [QPID-6950](https://issues.apache.org/jira/browse/QPID-6950) - [Java Broker] Starting embedded broker with http-management plugin using Broker#startup(BrokerOptions)  requires Thread.UncaughtExceptionHandler to be set
 - [QPID-6951](https://issues.apache.org/jira/browse/QPID-6951) - [Java Client] AMQSession.deregisterConsumer() leaks Memory
 - [QPID-6955](https://issues.apache.org/jira/browse/QPID-6955) - BufferOverflowException downloading message content
 - [QPID-6968](https://issues.apache.org/jira/browse/QPID-6968) - [Java Broker] Decoding of pipelined AMQP 0-9.x frames can fail when multiple frames are received as part of the same byte buffer
 - [QPID-6972](https://issues.apache.org/jira/browse/QPID-6972) - BDB HA: Node may remain detached from group following loss of quorum
 - [QPID-6975](https://issues.apache.org/jira/browse/QPID-6975) - NonBlockingConnectionTLSDelegate won't read to stream end if SSLEngine is closed
 - [QPID-6979](https://issues.apache.org/jira/browse/QPID-6979) - AttributeValueConverter's Certificate handling code assumes unix line endings
 - [QPID-6994](https://issues.apache.org/jira/browse/QPID-6994) - [Java Broker] AMQP connection close might fail to delete temporary queue after close of VirtualHost
 - [QPID-6996](https://issues.apache.org/jira/browse/QPID-6996) - Can't make a node master twice (during a single Broker lifetime)
 - [QPID-6997](https://issues.apache.org/jira/browse/QPID-6997) - [Java Broker, BDBStore] HA JE Transaction commit might end up in NullPointerException when commit is invoked when majority is lost
 - [QPID-6999](https://issues.apache.org/jira/browse/QPID-6999) - [Java Broker, BDBStore, HA] In replicated environment JE transactions aborted on committing can cause Broker shutdown
 - [QPID-7001](https://issues.apache.org/jira/browse/QPID-7001) - [Java Broker] NullPointerException can be thrown from Port IO Thread
 - [QPID-7002](https://issues.apache.org/jira/browse/QPID-7002) - [Java Broker] REST API throws NullPointerException when requesting all consumers
 - [QPID-7016](https://issues.apache.org/jira/browse/QPID-7016) - BDB JE cleaner can make no progress allowing for unbounded store growth
 - [QPID-7021](https://issues.apache.org/jira/browse/QPID-7021) - BDB hot backup (takeBackupNoLock) may fail with IOException
 - [QPID-7022](https://issues.apache.org/jira/browse/QPID-7022) - [Java Broker] Fix Web Management Console javascript issues
 - [QPID-7024](https://issues.apache.org/jira/browse/QPID-7024) - BDB HA - Group change thread-pool sized to availableProcessors +1
 - [QPID-7060](https://issues.apache.org/jira/browse/QPID-7060) - [Java Broker] [0-10] Connection close disassociates virtualhost before closing sessions and connection model object
 - [QPID-7061](https://issues.apache.org/jira/browse/QPID-7061) - [Java Broker] Web management console help URL is set to wrong location
 - [QPID-7065](https://issues.apache.org/jira/browse/QPID-7065) - [Java Broker] Wrong RegEx prohibits HA VHNs with dash ("-") in host address
 - [QPID-7067](https://issues.apache.org/jira/browse/QPID-7067) - Scram SHA upgrader loses the original password

## Tasks

 - [QPID-6925](https://issues.apache.org/jira/browse/QPID-6925) - [Java] Generate source bundle on releasing a new version of java components