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

# Qpid Broker-J 7.0.0 Release Notes

Qpid Broker-J 7.0 brings the following major changes:

- Improved AMQP 1.0 support
- Support for AMQP JMS Mapping Version 1.0 WD09
- Support for JMS 2.0 shared subscriptions
- Improved message conversion for applications using different AMQP protocols
- Improved direct memory management

For more information about this release, including download links and
documentation, see the [release overview](index.html).

## New features and improvements

 - [QPID-6028](https://issues.apache.org/jira/browse/QPID-6028) - [Java Broker] Configured model objects should have only one parent
 - [QPID-6779](https://issues.apache.org/jira/browse/QPID-6779) - [Java Broker] Refactor consumer closing functionality to make it consistent between different protocols
 - [QPID-7034](https://issues.apache.org/jira/browse/QPID-7034) - Inactive web management console session not automatically timed-out
 - [QPID-7184](https://issues.apache.org/jira/browse/QPID-7184) - Protocol layers should retain an association between a delivered message and the consumer to which it is delivered.
 - [QPID-7190](https://issues.apache.org/jira/browse/QPID-7190) - Enhance Java Broker documentation to include usage for AMQP 1.0
 - [QPID-7212](https://issues.apache.org/jira/browse/QPID-7212) - [Java Broker, WMC] Don't transmit inherited context variables by default
 - [QPID-7220](https://issues.apache.org/jira/browse/QPID-7220) - [Java Broker, WMC] REST requests for ConfiguredObjects should not return children by default
 - [QPID-7229](https://issues.apache.org/jira/browse/QPID-7229) - [Java Broker] Update Dojo to 1.12.2
 - [QPID-7283](https://issues.apache.org/jira/browse/QPID-7283) - [Java Broker] Simplify SASL authentication functionality across broker AMQP layers
 - [QPID-7310](https://issues.apache.org/jira/browse/QPID-7310) - [Java Broker] SiteSpecificTrustStore should use protocol default port when no port is specified
 - [QPID-7311](https://issues.apache.org/jira/browse/QPID-7311) - [Java Broker] SiteSpecificTrustStore does not provide helpful error messages when protocol is missing
 - [QPID-7316](https://issues.apache.org/jira/browse/QPID-7316) - WMC should permit the navigation from a consumer on a queue back to the connection 
 - [QPID-7345](https://issues.apache.org/jira/browse/QPID-7345) - [Java Broker] Remove support for ACL checking based on the "immediate" flag
 - [QPID-7371](https://issues.apache.org/jira/browse/QPID-7371) - Log failed login attempts
 - [QPID-7434](https://issues.apache.org/jira/browse/QPID-7434) - Mature the AMQP message conversion layer (headers and content)
 - [QPID-7468](https://issues.apache.org/jira/browse/QPID-7468) - [Java Broker] Upgrade logback to 1.1.11 and SLF4J to 1.7.24
 - [QPID-7471](https://issues.apache.org/jira/browse/QPID-7471) - [Java Broker] MessageConverter should respect mimeType
 - [QPID-7486](https://issues.apache.org/jira/browse/QPID-7486) - [Java Broker] Refactor broker startup code, remove BrokerOptions
 - [QPID-7496](https://issues.apache.org/jira/browse/QPID-7496) - [Java Broker] Reduce the implementation burden of creating non-standard virtual hosts
 - [QPID-7497](https://issues.apache.org/jira/browse/QPID-7497) - [Java Broker] Reduce size of anonymous state change listener classes by using abstract base class
 - [QPID-7506](https://issues.apache.org/jira/browse/QPID-7506) - [Java Broker] Move queue statistics accounting into a separate class
 - [QPID-7509](https://issues.apache.org/jira/browse/QPID-7509) - [Java Broker] Remove redundant RecordDeliveryMethod interface/implementations
 - [QPID-7514](https://issues.apache.org/jira/browse/QPID-7514) - [Java Broker] Do all message delivery processing on the IO threads and remove the QueueRunner
 - [QPID-7517](https://issues.apache.org/jira/browse/QPID-7517) - [Java Broker] Add a ManagedOperation to allow selected retrieval of statistics from an object
 - [QPID-7518](https://issues.apache.org/jira/browse/QPID-7518) - [Java Broker] Reduce cost of calculating size of buffered data in NonBlockingConnection
 - [QPID-7519](https://issues.apache.org/jira/browse/QPID-7519) - Remove unnecessary Jetty dependency (jetty-client) from Broker
 - [QPID-7520](https://issues.apache.org/jira/browse/QPID-7520) - [Java Broker] Fix "&amp;" vs "&amp;&amp;" typo in BooleanWriter from AMQP 1.0 codec 
 - [QPID-7521](https://issues.apache.org/jira/browse/QPID-7521) - [Java Broker] Close stream in SSLUtil#readPrivateKey
 - [QPID-7525](https://issues.apache.org/jira/browse/QPID-7525) - [Java Broker] Invoke attribute methods on initialisation of reporting in Broker
 - [QPID-7528](https://issues.apache.org/jira/browse/QPID-7528) - Add serializationVersionId to the classes implementing Serializable
 - [QPID-7529](https://issues.apache.org/jira/browse/QPID-7529) - [Java Broker] Implement producer flow control in AMQP 1.0
 - [QPID-7531](https://issues.apache.org/jira/browse/QPID-7531) - [Java Broker] Tidy up AMQP 1.0 implementation
 - [QPID-7532](https://issues.apache.org/jira/browse/QPID-7532) - [Java] Replace AMQConstant class with constant integer error codes
 - [QPID-7533](https://issues.apache.org/jira/browse/QPID-7533) - [Java Broker] Implement wd12 version of the AMQP Management working draft
 - [QPID-7539](https://issues.apache.org/jira/browse/QPID-7539) - [Java Broker] Support connection and user level logging
 - [QPID-7551](https://issues.apache.org/jira/browse/QPID-7551) - Expose Broker version as a Virtualhost derived attribute
 - [QPID-7552](https://issues.apache.org/jira/browse/QPID-7552) - Use management to retrieve the Broker's version number
 - [QPID-7555](https://issues.apache.org/jira/browse/QPID-7555) - Improve performance-test maven pom to allow the convenient running of performance tests from Maven
 - [QPID-7558](https://issues.apache.org/jira/browse/QPID-7558) - [Java Broker] Allow Multiple JDBC Virtual Hosts / Message Stores to share the same database
 - [QPID-7561](https://issues.apache.org/jira/browse/QPID-7561) - [Java Broker] Do not allow the creation of Derby Virtual Hosts if the Derby JDBC driver is not present
 - [QPID-7563](https://issues.apache.org/jira/browse/QPID-7563) - Implement Virtualhost centric REST interface
 - [QPID-7564](https://issues.apache.org/jira/browse/QPID-7564) - Add competing consumer test to the performance test suite
 - [QPID-7568](https://issues.apache.org/jira/browse/QPID-7568) - [Java Broker] [AMQP 1.0] support Delayed Delivery with the JMS 2.0 client
 - [QPID-7569](https://issues.apache.org/jira/browse/QPID-7569) - [Java Broker] [AMQP 1.0] support for shared subscriptions
 - [QPID-7570](https://issues.apache.org/jira/browse/QPID-7570) - [Java Broker] [AMQP 1.0] Add support for anonymous sending links
 - [QPID-7571](https://issues.apache.org/jira/browse/QPID-7571) - Allow model to designate operation parameters as not nullable
 - [QPID-7572](https://issues.apache.org/jira/browse/QPID-7572) - [Java Broker] Refactor Consumer related interfaces
 - [QPID-7575](https://issues.apache.org/jira/browse/QPID-7575) - [Java Broker] Improve AMQP 1.0 codec to retain encoded message data
 - [QPID-7578](https://issues.apache.org/jira/browse/QPID-7578) - [Java Broker] make AMQP 1.0 temporary queues globally addressable 
 - [QPID-7580](https://issues.apache.org/jira/browse/QPID-7580) - [Java Broker] Expose the type of message (AMQP 0-9-1/0-10/1-0/Non-AMQP) through REST/Management
 - [QPID-7586](https://issues.apache.org/jira/browse/QPID-7586) - [Java Broker] [AMQP 1.0] Simplify the AMQP codec so that it always assumes that the buffer it is writing into is large enough
 - [QPID-7597](https://issues.apache.org/jira/browse/QPID-7597) - Expose the bound (i.e. listening) port number on Port model object
 - [QPID-7601](https://issues.apache.org/jira/browse/QPID-7601) - [Java Broker] Allow annotations to define ManagedAttributeValueTypes as abstract, some methods as derived
 - [QPID-7602](https://issues.apache.org/jira/browse/QPID-7602) - Message reply-to conversion between protocols for point to point and publish subscribe messaging patterns
 - [QPID-7603](https://issues.apache.org/jira/browse/QPID-7603) - [AMQP 1.0] Maximum Delivery Count/Dead-lettering
 - [QPID-7605](https://issues.apache.org/jira/browse/QPID-7605) - [Java Broker] [AMQP1.0] Container id uniqueness
 - [QPID-7606](https://issues.apache.org/jira/browse/QPID-7606) - Generalise Queue|Exchange#alternateExchange as alternateBinding
 - [QPID-7607](https://issues.apache.org/jira/browse/QPID-7607) - AMQP 1.0 conversion layer to use 'Map' x-opt-jms-msg-type annotation when message is representable as a JMS Map Message and recipent known to be the Qpid JMS Client 
 - [QPID-7609](https://issues.apache.org/jira/browse/QPID-7609) - JMS 2.0 systests module
 - [QPID-7610](https://issues.apache.org/jira/browse/QPID-7610) - [Java Broker] MemorySystemConfig should override the default preferenceStoreAttributes
 - [QPID-7618](https://issues.apache.org/jira/browse/QPID-7618) - Ring policy type
 - [QPID-7621](https://issues.apache.org/jira/browse/QPID-7621) - Target Java 8+, i.e. drop support for Java 7
 - [QPID-7622](https://issues.apache.org/jira/browse/QPID-7622) - Separate Qpid Broker for Java and 0-x JMS Client in source tree
 - [QPID-7633](https://issues.apache.org/jira/browse/QPID-7633) - Remove SessionAdapter
 - [QPID-7639](https://issues.apache.org/jira/browse/QPID-7639) - Implement large transaction guard  restricting direct memory consumption by messages from uncommitted transactions on the connection
 - [QPID-7653](https://issues.apache.org/jira/browse/QPID-7653) - [Java Broker] Separate JDBC and Derby Plugins from Broker Core
 - [QPID-7664](https://issues.apache.org/jira/browse/QPID-7664) - [Java Broker] [AMQP1.0] Support defaultOutcome handling
 - [QPID-7665](https://issues.apache.org/jira/browse/QPID-7665) - Protocol system test suite for AMQP 1.0
 - [QPID-7667](https://issues.apache.org/jira/browse/QPID-7667) - [Java Broker] [AMQP1.0] Implement multi-ssns-per-txn for the transaction controller
 - [QPID-7668](https://issues.apache.org/jira/browse/QPID-7668) - [Java Broker] Add MySQL configuration to the set of known DBMS types in JDBCDetails
 - [QPID-7680](https://issues.apache.org/jira/browse/QPID-7680) - Isolate 0-10 Xid to the 0-10 protocol layer
 - [QPID-7683](https://issues.apache.org/jira/browse/QPID-7683) - Remove knowledge of 0-x encoders from the AMQP 1.0 protocol layers
 - [QPID-7689](https://issues.apache.org/jira/browse/QPID-7689) - [Java Broker] Consider message header size where appropriate
 - [QPID-7708](https://issues.apache.org/jira/browse/QPID-7708) - [Java Broker] [AMQP 1.0] Allow the incoming session credit window to be configured with a context value
 - [QPID-7722](https://issues.apache.org/jira/browse/QPID-7722) - [0-10] Avoid repetitious AccessController.doPrivileged calls if incoming buffer contains a sequence of frames for the same channel 
 - [QPID-7724](https://issues.apache.org/jira/browse/QPID-7724) - [Java Broker] update optional BDB store to use version 7.3.7 of BDB JE 
 - [QPID-7730](https://issues.apache.org/jira/browse/QPID-7730) - [Java Broker] Upgrade logback to latest version (1.2.2)
 - [QPID-7731](https://issues.apache.org/jira/browse/QPID-7731) - Upgrade to Jetty 9.4
 - [QPID-7736](https://issues.apache.org/jira/browse/QPID-7736) - [Java Broker] Upgrade SLF4j to 1.7.25
 - [QPID-7740](https://issues.apache.org/jira/browse/QPID-7740) - [BDB HA] Improve ReplicatedEnvironmentFacade API for updating priority, designated primary and electoral group override
 - [QPID-7745](https://issues.apache.org/jira/browse/QPID-7745) - [Java Broker] Bump dependency version of Apache Derby
 - [QPID-7760](https://issues.apache.org/jira/browse/QPID-7760) - Allow annotation processor ConfiguredObjectRegistrationGenerator to handle incremental compilation
 - [QPID-7762](https://issues.apache.org/jira/browse/QPID-7762) - Add ability to turn off flow to disk
 - [QPID-7769](https://issues.apache.org/jira/browse/QPID-7769) - [AMQP 0-8..0-91] Support decoding of type codes u (unsigned short) and B (unsigned byte) to maximise compatibility with other AMQP implementations
 - [QPID-7771](https://issues.apache.org/jira/browse/QPID-7771) - Allow exchange to exchange bindings to substitute the routing key
 - [QPID-7772](https://issues.apache.org/jira/browse/QPID-7772) - Add statistics panel to view tabs within the Web Management Console
 - [QPID-7773](https://issues.apache.org/jira/browse/QPID-7773) - REST API queries that identify a single object by its full path should return a object rather than a list.
 - [QPID-7775](https://issues.apache.org/jira/browse/QPID-7775) - Flow to disk should consider the size of the resident messages in memory.
 - [QPID-7776](https://issues.apache.org/jira/browse/QPID-7776) - Add flow to disk queue policy
 - [QPID-7787](https://issues.apache.org/jira/browse/QPID-7787) - [Java Broker] In AMQP 1.0 allow the SASL outcome to carry additional information
 - [QPID-7790](https://issues.apache.org/jira/browse/QPID-7790) - Include statistics in API docs
 - [QPID-7791](https://issues.apache.org/jira/browse/QPID-7791) - Recover metadata into direct memory
 - [QPID-7793](https://issues.apache.org/jira/browse/QPID-7793) - [1.0] Avoid repetitious AccessController.doPrivileged calls if incoming buffer contains a sequence of frames for the same channel 
 - [QPID-7799](https://issues.apache.org/jira/browse/QPID-7799) - Broker should be able to write a periodic dump of statistics
 - [QPID-7800](https://issues.apache.org/jira/browse/QPID-7800) - [Java Broker] Refactor Port classes to remove unnecessary intermediate classes/interfaces
 - [QPID-7804](https://issues.apache.org/jira/browse/QPID-7804) - Change default virtualhost store type from Derby to BDB JE
 - [QPID-7806](https://issues.apache.org/jira/browse/QPID-7806) - [Java Broker] [AMQP 1.0] Slow connection ticker should be running until OPEN performative is received or timeout expires
 - [QPID-7807](https://issues.apache.org/jira/browse/QPID-7807) - Add support temporary-topics (as per AMQP bindmap WD9)
 - [QPID-7812](https://issues.apache.org/jira/browse/QPID-7812) - [Java Broker] [AMQP1.0] Wire up unacknowledged message bytes/count statistics
 - [QPID-7815](https://issues.apache.org/jira/browse/QPID-7815) - Reject policy type
 - [QPID-7816](https://issues.apache.org/jira/browse/QPID-7816) - [Java Broker] [AMQP 1.0] Ensure that delivery tag is set on transfer
 - [QPID-7820](https://issues.apache.org/jira/browse/QPID-7820) - Extend AMQP 1.0 protocol tests to support web socket tests too
 - [QPID-7825](https://issues.apache.org/jira/browse/QPID-7825) - Improve queue accounting statistics
 - [QPID-7826](https://issues.apache.org/jira/browse/QPID-7826) - Refactor ACO#addChildAsync to remove most overrides
 - [QPID-7827](https://issues.apache.org/jira/browse/QPID-7827) - Recoverers allocate separate queue UUID for each recovered message instance
 - [QPID-7831](https://issues.apache.org/jira/browse/QPID-7831) - Refactor AbstractJDBCMessageStore to use try-with-resources 
 - [QPID-7832](https://issues.apache.org/jira/browse/QPID-7832) - Refactor store/protocol API using Collection&lt;QpidByteBuffers&gt;
 - [QPID-7838](https://issues.apache.org/jira/browse/QPID-7838) - Make AMQP Management Node respect secure attributes and secure operations
 - [QPID-7839](https://issues.apache.org/jira/browse/QPID-7839) - Tidy-up maven dependency management
 - [QPID-7842](https://issues.apache.org/jira/browse/QPID-7842) - [AMQP 1.0] Refactor link endpoint implementations
 - [QPID-7843](https://issues.apache.org/jira/browse/QPID-7843) - [Java Broker] Correct queue attribute minimumMessageTtl/maximumMessageTtl documentation
 - [QPID-7856](https://issues.apache.org/jira/browse/QPID-7856) - [Java Broker] Convert broker connection related attributes into context variables and expose them on amqp port as derived attributes
 - [QPID-7858](https://issues.apache.org/jira/browse/QPID-7858) - [Java Broker] Bump com.fasterxml.jackson dependency 2.5 =&gt; 2.8
 - [QPID-7864](https://issues.apache.org/jira/browse/QPID-7864) - [Java Broker] Update Google Guava dependency
 - [QPID-7865](https://issues.apache.org/jira/browse/QPID-7865) - [Java Broker] Tidy-up AMQP 1.0 'Destination' classes
 - [QPID-7867](https://issues.apache.org/jira/browse/QPID-7867) - Authentication using expired certificate
 - [QPID-7869](https://issues.apache.org/jira/browse/QPID-7869) - [Java Broker] Truststore improvements
 - [QPID-7870](https://issues.apache.org/jira/browse/QPID-7870) - [Java Broker] Remove support for the x-opt-jms-type message annotation
 - [QPID-7881](https://issues.apache.org/jira/browse/QPID-7881) - [Java Broker] [WMC] Expose broker restart operation through Management Console.
 - [QPID-7886](https://issues.apache.org/jira/browse/QPID-7886) - [Java Broker] [WMC] Expose ability to get a thread dump
 - [QPID-7887](https://issues.apache.org/jira/browse/QPID-7887) - [Java Broker] Message conversion error handling
 - [QPID-7896](https://issues.apache.org/jira/browse/QPID-7896) - Create system tests testing end-to-end message conversion
 - [QPID-7904](https://issues.apache.org/jira/browse/QPID-7904) - [Java Broker] ensure ACLs work with AMQP 1.0
 - [QPID-7907](https://issues.apache.org/jira/browse/QPID-7907) - [Documentation] Update the HA docs to advise users to set both the je and the qpid limit explicitly
 - [QPID-7910](https://issues.apache.org/jira/browse/QPID-7910) - [Java Broker] Improve qpid.stop script
 - [QPID-7914](https://issues.apache.org/jira/browse/QPID-7914) - [Java Broker] Queue Minimum/Maximum Message TTL default should be overridable by context variables
 - [QPID-7917](https://issues.apache.org/jira/browse/QPID-7917) - [Java Broker, WMC] Upgrade dgrid to version 1.2.1 and dstore to version 1.1.2
 - [QPID-7921](https://issues.apache.org/jira/browse/QPID-7921) - [Java Broker] [ACL] Tactical improvements to ACL to allow managed operation invocations to be controlled
 - [QPID-7923](https://issues.apache.org/jira/browse/QPID-7923) - [Java Broker] Allow attribute level ACL to be enforced on update
 - [QPID-7932](https://issues.apache.org/jira/browse/QPID-7932) - [Java Broker, AMQP 1.0] Improve Error handling when decoding
 - [QPID-7935](https://issues.apache.org/jira/browse/QPID-7935) - [Java Broker] [ACL] Allow legacy ACL rule set to specify a default result of defer
 - [QPID-7939](https://issues.apache.org/jira/browse/QPID-7939) - [Java Broker] update BDB JE dependency from 7.3.7 to 7.4.5
 - [QPID-7953](https://issues.apache.org/jira/browse/QPID-7953) - [Stress Test Tools] Simple changes to allow running against the qpid-jms-client
 - [QPID-7957](https://issues.apache.org/jira/browse/QPID-7957) - [Java Broker, AMQP 1.0] Add support for max-message-size on Attach
 - [QPID-7960](https://issues.apache.org/jira/browse/QPID-7960) - [Java Broker, AMQP 1.0] Add support for undeliverable-here on Modified outcome
 - [QPID-7974](https://issues.apache.org/jira/browse/QPID-7974) - JdbcUtils.TableExists is very slow on big databases such as Oracle
 - [QPID-7983](https://issues.apache.org/jira/browse/QPID-7983) - Bump the initial-config's model version from 6.1 to 7.0 
 - [QPID-7984](https://issues.apache.org/jira/browse/QPID-7984) - [Java Broker] [Tools] Remove unused tools
 - [QPID-7986](https://issues.apache.org/jira/browse/QPID-7986) - [Qpid Broker-J] [AMQP0-10] Remove redundant casts left by collapse of ServerConnection/SessionSession etc
 - [QPID-7990](https://issues.apache.org/jira/browse/QPID-7990) - [Qpid Broker-J] [AMQP0-8] Dead _model reference in AMQPChannel
 - [QPID-7992](https://issues.apache.org/jira/browse/QPID-7992) - [Broker-J] Add auxiliary operation to purge and dump links from link registry
 - [QPID-8000](https://issues.apache.org/jira/browse/QPID-8000) - [Broker-J] Improve buffer statistic names
 - [QPID-8001](https://issues.apache.org/jira/browse/QPID-8001) - [Broker-J] [Documentation] Updates to docbook documentation to reflect changes/new features in v7
 - [QPID-8002](https://issues.apache.org/jira/browse/QPID-8002) - [Broker-J][REST] Increase sasl exchange expiry interval
 - [QPID-8005](https://issues.apache.org/jira/browse/QPID-8005) - [Broker-J][WMC] Redirect requests for removed 'login.html' to 'index.html'
 - [QPID-8012](https://issues.apache.org/jira/browse/QPID-8012) - [Broker-J][WMC] Use ResourceWidget to configure path for access control provider of type AclFile 
 - [QPID-8020](https://issues.apache.org/jira/browse/QPID-8020) - [Broker-J] Rename binary and source distribution bundles for broker-j
 - [QPID-8023](https://issues.apache.org/jira/browse/QPID-8023) - [Broker-J] Remove com.google.code.findbugs:jsr305 dependency
 - [QPID-8024](https://issues.apache.org/jira/browse/QPID-8024) - [Broker-J] Reflect missing components and changes in copyright dates in the NOTICE file

## Bugs fixed

 - [QPID-3987](https://issues.apache.org/jira/browse/QPID-3987) - Tests broker_0_9.queue.QueueTests.test_unbind_fanout and broker_0_9.queue.QueueTests.test_unbind_headers fail with 404, 'No such binding'
 - [QPID-6653](https://issues.apache.org/jira/browse/QPID-6653) - Earlier Qpid Java client: receiver issue with multi-transfer pre-settled messages
 - [QPID-6738](https://issues.apache.org/jira/browse/QPID-6738) - Joram test TopicSessionTest#testDurableSubscriber hangs against Java Broker when invoked a second time (qpid-jms-client 0.5.0)
 - [QPID-7059](https://issues.apache.org/jira/browse/QPID-7059) - BDBHAVirtualHostNodeRestTest.testDeleteMasterNode failed sporadically on Apache CI
 - [QPID-7272](https://issues.apache.org/jira/browse/QPID-7272) - [Java Broker] Direct memory QpidByteBuffer created in message conversion modules should be disposed as soon as possible after becoming unused
 - [QPID-7399](https://issues.apache.org/jira/browse/QPID-7399) - [Java Broker] ClosedSelectorException during shutdown
 - [QPID-7425](https://issues.apache.org/jira/browse/QPID-7425) - Management delete of a message may refund credit too early
 - [QPID-7459](https://issues.apache.org/jira/browse/QPID-7459) - ProducerFlowControlTest#testSendTimeout test fails sprodically on 0-10 profiles
 - [QPID-7473](https://issues.apache.org/jira/browse/QPID-7473) - [Java Broker] Asynchronous message recoverer should always delete orphan messages from the store
 - [QPID-7480](https://issues.apache.org/jira/browse/QPID-7480) - Incorrect error message when editing "number of connection threads" of a virtual host
 - [QPID-7481](https://issues.apache.org/jira/browse/QPID-7481) - Statistics gathering screen label uses wrong unit
 - [QPID-7482](https://issues.apache.org/jira/browse/QPID-7482) - Heartbeat screen label uses wrong units
 - [QPID-7487](https://issues.apache.org/jira/browse/QPID-7487) - [Java Broker] The option to "overwrite configuration" on Main does nothing
 - [QPID-7488](https://issues.apache.org/jira/browse/QPID-7488) - [Java Broker, WMC] Clicking on any of dashboard widget titlebar icons  (collapse pane, edit, goto, or close) triggers widget dragging in IE
 - [QPID-7491](https://issues.apache.org/jira/browse/QPID-7491) - [Java Broker] Fix AbstractSystemMessageSource#pullMessage
 - [QPID-7508](https://issues.apache.org/jira/browse/QPID-7508) - Broker occasionally fails to report SUB-1003 in response to a consumer that has become suspended
 - [QPID-7511](https://issues.apache.org/jira/browse/QPID-7511) - [Java Broker] AmqpPort objects cannot be properly closed unless virtual hosts are closed 
 - [QPID-7513](https://issues.apache.org/jira/browse/QPID-7513) - [Java Broker] If no virtualHostNode is provided, a PatternMatchingAlias should return the default virtual host node
 - [QPID-7516](https://issues.apache.org/jira/browse/QPID-7516) - [Java Broker] The timeout when waiting for a response from a server-initiated close should be configurable
 - [QPID-7522](https://issues.apache.org/jira/browse/QPID-7522) - [Java Broker] Fix state check in  ReplicatedEnvironmentFacade#tryToRestartEnvironment
 - [QPID-7523](https://issues.apache.org/jira/browse/QPID-7523) - [Java Broker] UpgradeFrom7To8#getConfigVersion should guard against NPE in case cursor is null
 - [QPID-7527](https://issues.apache.org/jira/browse/QPID-7527) - [Java Broker] ProtocolOutputConverterImpl$CompositeAMQBodyBlock#getSize and ProtocolOutputConverterImpl$SmallCompositeAMQBodyBlock#getSize should cast operands to long to avoid truncation to int
 - [QPID-7534](https://issues.apache.org/jira/browse/QPID-7534) - EncodingUtils#readLongAsShortString does not guard against the string containing characters not in the range '0'-'9'
 - [QPID-7537](https://issues.apache.org/jira/browse/QPID-7537) - Improve implementations of equal methods in various classes to be able to account for sub-classes
 - [QPID-7540](https://issues.apache.org/jira/browse/QPID-7540) - [Java Broker] The broker cannot recover durable Consumers (AMQP 1.0) which leaves it in an ERRORed state
 - [QPID-7545](https://issues.apache.org/jira/browse/QPID-7545) - [Java Broker] Make 0-10 CreditManagers work with Python client
 - [QPID-7548](https://issues.apache.org/jira/browse/QPID-7548) - [Java Broker] Upgrade of configuration from model version 3 fails
 - [QPID-7549](https://issues.apache.org/jira/browse/QPID-7549) - [Java Broker] Authentication using SimpleLDAP authentication provider fails with NPE when caching of authentication results is enabled(by default)
 - [QPID-7550](https://issues.apache.org/jira/browse/QPID-7550) - Metadata service does not set cache control headers
 - [QPID-7560](https://issues.apache.org/jira/browse/QPID-7560) - AbstractVirtualHost defines two state transitions from ERROR to ACTIVE
 - [QPID-7562](https://issues.apache.org/jira/browse/QPID-7562) - Ensure that HTTP threads always carry a ManagementConnectionPrincipal
 - [QPID-7576](https://issues.apache.org/jira/browse/QPID-7576) - Metadata loaded twice for recovered message
 - [QPID-7577](https://issues.apache.org/jira/browse/QPID-7577) - [Java Broker] Generic JDBC configuration store mistakenly is put into OPEN state in init
 - [QPID-7579](https://issues.apache.org/jira/browse/QPID-7579) -  AMQP 1.0 - settled flag set incorrectly for transactional sessions in mode rcvSettleMode FIRST
 - [QPID-7582](https://issues.apache.org/jira/browse/QPID-7582) - Auto unboxing null from Discharge#getFail() cause NPEs
 - [QPID-7583](https://issues.apache.org/jira/browse/QPID-7583) - [Java Broker] On AMQP 1.0 ensure Flow is sent to client when producer flow control changes state
 - [QPID-7591](https://issues.apache.org/jira/browse/QPID-7591) - Broker may send a deleted message to a queue browser
 - [QPID-7592](https://issues.apache.org/jira/browse/QPID-7592) - [AMQP1.0] leak from Session_1_0#_outgoingUnsettled for long lived JMS auto-ack consuming session.
 - [QPID-7593](https://issues.apache.org/jira/browse/QPID-7593) - Ending an AMQP1.0 connection with consumer leaks the connection, session and objects related to the consumer
 - [QPID-7600](https://issues.apache.org/jira/browse/QPID-7600) - AMQChannel#receivedComplete is performed without the SessionPrincipal within the thread access controller context
 - [QPID-7608](https://issues.apache.org/jira/browse/QPID-7608) - [Java Broker, Documentation] Chapter "9.6. Flow to Disk" is inaccessible
 - [QPID-7616](https://issues.apache.org/jira/browse/QPID-7616) - VirtualHostNode name is not expanded before creating thread
 - [QPID-7623](https://issues.apache.org/jira/browse/QPID-7623) - "SEVERE: RuntimeException while executing runnable" reported by Guava to stderr if a state transition method throws exception
 - [QPID-7625](https://issues.apache.org/jira/browse/QPID-7625) - [AMQP 1.0] Enforce lifetime-policy DeleteOnClose 
 - [QPID-7627](https://issues.apache.org/jira/browse/QPID-7627) - [Java Broker] Ensure DoOnConfigThread annotation is processed across compilation units
 - [QPID-7631](https://issues.apache.org/jira/browse/QPID-7631) - [Java Broker, WMC] In BDBHA 2-node group you should be able to configure priority
 - [QPID-7634](https://issues.apache.org/jira/browse/QPID-7634) - [Java Broker,amqp 1.0] Broker does not respond to Flow command with drain=true if queue is empty and prefetch is 0
 - [QPID-7635](https://issues.apache.org/jira/browse/QPID-7635) - [Java Broker] If ANONYMOUS-RELAY finds the destination it should defer the delivery outcome to the destination
 - [QPID-7636](https://issues.apache.org/jira/browse/QPID-7636) - [AMQP 1.0] producer message flow does not restart after disk-space based flow control relinquished
 - [QPID-7637](https://issues.apache.org/jira/browse/QPID-7637) - [AMQP 1.0] existing block state not applied to newly created sessions
 - [QPID-7644](https://issues.apache.org/jira/browse/QPID-7644) - [Java Broker] [AMQP 1.0] Remove non-standard support for UTF-16 Strings from the AMQP type system
 - [QPID-7646](https://issues.apache.org/jira/browse/QPID-7646) - [Java Broker] fix AbstractAMQPSession#getLocalTransactionOpen to support values &gt; 1
 - [QPID-7647](https://issues.apache.org/jira/browse/QPID-7647) - [Java Broker] fix handling of broker type in configuration
 - [QPID-7648](https://issues.apache.org/jira/browse/QPID-7648) - [Java Broker] Reject AMQP 1.0 durable messages if no persistent store is configured
 - [QPID-7661](https://issues.apache.org/jira/browse/QPID-7661) - [Java Broker] Stop creating 'dead letter queue' for a durable subscription queue
 - [QPID-7670](https://issues.apache.org/jira/browse/QPID-7670) - [Java Broker] WebSocket transport does not respect AMQP idle timeout
 - [QPID-7675](https://issues.apache.org/jira/browse/QPID-7675) - [Java Broker] Runtime exception can be thrown by REST API on failure to create BDB HA Virtual Host Node
 - [QPID-7682](https://issues.apache.org/jira/browse/QPID-7682) - [Java Broker] CloudFoundry group provider plugin reports 404 errors from the service as 500 errors
 - [QPID-7684](https://issues.apache.org/jira/browse/QPID-7684) - [Java Broker, BDB] Close Cursor when LockConflictException is thrown
 - [QPID-7685](https://issues.apache.org/jira/browse/QPID-7685) - [Java Broker, BDB] AsyncRecovery and Queue#enqueue can contend for a BDB Lock potentially bringing down the broker
 - [QPID-7690](https://issues.apache.org/jira/browse/QPID-7690) - [Java Broker] Cannot create VirtualHostLogger with certain ACLs in place
 - [QPID-7695](https://issues.apache.org/jira/browse/QPID-7695) - [Java Broker, BDB HA] Indefinite hang when new node joins existing group but existing node is unresponsive
 - [QPID-7707](https://issues.apache.org/jira/browse/QPID-7707) - [Java Broker, WMC] If ACL reload operation fails due to  malformed ACL rules, etc, the error is not reported back to the user invoking the operation
 - [QPID-7719](https://issues.apache.org/jira/browse/QPID-7719) - [Java Broker] Set response code to 500 when unexpected error occurs during REST call 
 - [QPID-7723](https://issues.apache.org/jira/browse/QPID-7723) - [0-10] Re-encoding of the 0-10 message during computation of updateStatsOnEnqueue causes performance slow down
 - [QPID-7729](https://issues.apache.org/jira/browse/QPID-7729) - [Java Broker, WMC] Fix evaluation of context path in the Web Management Console
 - [QPID-7733](https://issues.apache.org/jira/browse/QPID-7733) - [Java Broker] Misplaced ch.qos.logback.classic.spi.Configurator services file prevents use of logback in the Broker without the Qpid logging-logback module
 - [QPID-7734](https://issues.apache.org/jira/browse/QPID-7734) - [Java Broker, WMC] Fix anonymous login to the WMC
 - [QPID-7735](https://issues.apache.org/jira/browse/QPID-7735) - [Java Broker] Allow multiple ports to be configured using dynamic port 0
 - [QPID-7739](https://issues.apache.org/jira/browse/QPID-7739) - [Java Broker] In AMQP 1.0 fix handling of channel Id &gt; 2^15
 - [QPID-7741](https://issues.apache.org/jira/browse/QPID-7741) - [Java Broker] In AMQP 1.0 gracefully handle non-compliant performatives
 - [QPID-7742](https://issues.apache.org/jira/browse/QPID-7742) - [Java Broker] [AMQP 1.0] Hostname should be taken from SNI or sasl-init if it is not present in open
 - [QPID-7743](https://issues.apache.org/jira/browse/QPID-7743) - [Java Broker] Propagate current IO thread when switching protocol engine to facilitate the correct processing of pipelined requests
 - [QPID-7744](https://issues.apache.org/jira/browse/QPID-7744) - [Java Broker] Fix NPE in AbstractVirtualHost$MessageHeaderImpl when there is no user principal
 - [QPID-7746](https://issues.apache.org/jira/browse/QPID-7746) - [Java Broker] Enforce AMQP 1.0 channel-max correctly
 - [QPID-7748](https://issues.apache.org/jira/browse/QPID-7748) - [Java Broker] In AMQP 1.0 ensure we send Flow echo in a timely fashion
 - [QPID-7749](https://issues.apache.org/jira/browse/QPID-7749) - [Java Broker] In AMQP 1.0 settle incoming messages when rcv-settle-mode is default
 - [QPID-7750](https://issues.apache.org/jira/browse/QPID-7750) - [Java Broker] NPE in AbstractQueue#getOldestMessageArrivalTime when Queue was not opened
 - [QPID-7751](https://issues.apache.org/jira/browse/QPID-7751) - [Java Broker] Login attempt using SimpleLDAP might result in 500
 - [QPID-7752](https://issues.apache.org/jira/browse/QPID-7752) - [AMQP 1.0] producer message flow control should not be applied to transaction coordinator links
 - [QPID-7753](https://issues.apache.org/jira/browse/QPID-7753) - Sparsely occupied message buffers may lead to java.lang.OutOfMemoryError: Direct buffer memory
 - [QPID-7763](https://issues.apache.org/jira/browse/QPID-7763) - [Java Broker] Flow to disk if allocated direct memory exceeds broker wide broker.flowToDiskThreshold
 - [QPID-7766](https://issues.apache.org/jira/browse/QPID-7766) - [Java Broker] [Derby Store] Unsigned byte type should be used when reading stored message metada type
 - [QPID-7777](https://issues.apache.org/jira/browse/QPID-7777) - [AMQP 1.0] NPE during consumer target delivery path 
 - [QPID-7781](https://issues.apache.org/jira/browse/QPID-7781) - [Java Broker] 500 error whilst deleting a virtualhost.
 - [QPID-7782](https://issues.apache.org/jira/browse/QPID-7782) - [Java Broker] [AMQP1.0] NPE on connection when no default virtualhost exists
 - [QPID-7783](https://issues.apache.org/jira/browse/QPID-7783) - [Java Broker] Closing a virtualhost does not dispose QBBs associated with messages on queues
 - [QPID-7784](https://issues.apache.org/jira/browse/QPID-7784) - [Java Broker] Closing a virtualhost does not dispose QBBs still associated with pooled IO threads
 - [QPID-7789](https://issues.apache.org/jira/browse/QPID-7789) - [Java Broker, WMC] The webclient sasl implementation should always answer a challenge by sending back a response.
 - [QPID-7796](https://issues.apache.org/jira/browse/QPID-7796) - [Java Broker] Guard against NPE in 0-10 when storing messages without header
 - [QPID-7798](https://issues.apache.org/jira/browse/QPID-7798) - [Java Broker] AMQP Management Operation throws NPE when it cannot find the target object
 - [QPID-7803](https://issues.apache.org/jira/browse/QPID-7803) - [Java Broker] Support the sending of an incomplete unsettled map
 - [QPID-7808](https://issues.apache.org/jira/browse/QPID-7808) - [Java Broker] [AMQP 0-10] Producer flow control overflow policy is not triggered on breaching the threshold due to missing Session principal
 - [QPID-7811](https://issues.apache.org/jira/browse/QPID-7811) - [Java Broker] Asynchronous message store recoverer can delete message content for the message enqueued after broker startup
 - [QPID-7817](https://issues.apache.org/jira/browse/QPID-7817) - [Java Broker] [WebSocket] Websocket implementation must not assume that web socket frame contains a whole AMQP frame
 - [QPID-7823](https://issues.apache.org/jira/browse/QPID-7823) - [Java Broker] [AMQP1.0] Contradicting message-formats on multi transfer deliveries should result in error
 - [QPID-7836](https://issues.apache.org/jira/browse/QPID-7836) - NPE logged at WARN during management view of messages whilst consumer active
 - [QPID-7837](https://issues.apache.org/jira/browse/QPID-7837) - Malformed annotated messages (message format 0) can lead to ClassCastException 
 - [QPID-7846](https://issues.apache.org/jira/browse/QPID-7846) - [Java Broker] [AMQP 1.0] Transaction Coordinator Links are accumulated in LinkRegistry
 - [QPID-7854](https://issues.apache.org/jira/browse/QPID-7854) - [Java Broker] Queue that has been used as a alternative binding cannot be removed
 - [QPID-7855](https://issues.apache.org/jira/browse/QPID-7855) - [Java Broker] [AMQP 1.0] expiryPolicy=SESSION_END seemingly not respected if connection closed abnormally
 - [QPID-7857](https://issues.apache.org/jira/browse/QPID-7857) - [Java Broker] Invalid routing key
 - [QPID-7866](https://issues.apache.org/jira/browse/QPID-7866) - [Java Broker] AMQP 1.0 publishing links do not register themselves with queues
 - [QPID-7872](https://issues.apache.org/jira/browse/QPID-7872) - [Java Broker] [AMQP 1.0] Message expiry should be driven from ttl header only
 - [QPID-7889](https://issues.apache.org/jira/browse/QPID-7889) - [Java Broker] [0-91] extension basic.nack does not release message for delivery elsewhere
 - [QPID-7913](https://issues.apache.org/jira/browse/QPID-7913) - [Java Broker] Improve message recovery logging
 - [QPID-7928](https://issues.apache.org/jira/browse/QPID-7928) - [Java Broker] [ACL] Authorisation decisions about the access control provider itself considers its own local rules rather than those of the wider system
 - [QPID-7933](https://issues.apache.org/jira/browse/QPID-7933) - [Java Broker] Changes made to existing durable children of virtualhost not recorded to the configuration store after a virtualhost restart
 - [QPID-7934](https://issues.apache.org/jira/browse/QPID-7934) - [Java Broker] [ACL] A recovered RuleBasedVirtualHostAccessControlProvider doesn't tell the virtualhost about updates to its rule-state
 - [QPID-7937](https://issues.apache.org/jira/browse/QPID-7937) - [Java Broker] [AMQP1.0] Message grouping feature does not utilise group-id from the message properties
 - [QPID-7940](https://issues.apache.org/jira/browse/QPID-7940) - [Java Broker] JSON context substitution does not work with nested variables
 - [QPID-7941](https://issues.apache.org/jira/browse/QPID-7941) - [Java Broker] DerbyUtils MEMORY_STORE_LOCATION is incorrect
 - [QPID-7944](https://issues.apache.org/jira/browse/QPID-7944) - [Java Broker] [AMQP1.0] Observing a message with a null object property cause 500 error to be sent to the browser
 - [QPID-7945](https://issues.apache.org/jira/browse/QPID-7945) - [Java Broker] SpawnedBrokerHolderTest fails on Windows
 - [QPID-7947](https://issues.apache.org/jira/browse/QPID-7947) - [Java Broker] [AMQP 1.0] Improve handling of empty and overlarge frames
 - [QPID-7950](https://issues.apache.org/jira/browse/QPID-7950) - [Java Broker, AMQP 1.0] Discharging transaction after consumer link detach does not apply the correct outcomes
 - [QPID-7955](https://issues.apache.org/jira/browse/QPID-7955) - Logback Stack overflow exception whilst reporting fatal BDB JE error
 - [QPID-7956](https://issues.apache.org/jira/browse/QPID-7956) - [Java Broker] Memory compactor threw NPE during Broker shutdown
 - [QPID-7958](https://issues.apache.org/jira/browse/QPID-7958) - [Java Broker] [AMQP0-10] References to messages sent by $virtualhostProperties node retained by store
 - [QPID-7962](https://issues.apache.org/jira/browse/QPID-7962) - [Java Broker][AMQP 1.0] In some circumstances Broker fails to send Flow back when Flow with drain flag set is received from client
 - [QPID-7963](https://issues.apache.org/jira/browse/QPID-7963) - [AMQP1.0] Sending a large message to a client uses excessive heap memory
 - [QPID-7967](https://issues.apache.org/jira/browse/QPID-7967) - [Java Broker] Internal Oracle TLS classes leaked per connection when connecting the Qpid JMS Client
 - [QPID-7968](https://issues.apache.org/jira/browse/QPID-7968) - [Java Broker] [AMQP 1.0] AccessControlException thrown on authorization of connection creation is caught in FrameHandler instead of AMQPConnection_1_0Impl
 - [QPID-7970](https://issues.apache.org/jira/browse/QPID-7970) - [Java Broker] [AMQP 1.0] Session leaks closed link endpoints
 - [QPID-7971](https://issues.apache.org/jira/browse/QPID-7971) - [Java Broker] [AMQP1.0] [AMQP0-9] Queue#ConsumerCountWithCredit statistic not decremented when consumer disconnects
 - [QPID-7973](https://issues.apache.org/jira/browse/QPID-7973) - Table Name Prefix is set to NULL if no prefix is provided instead of empty String
 - [QPID-7979](https://issues.apache.org/jira/browse/QPID-7979) - [Java Broker] [JDBCMessageStore] Some exception causes are hidden
 - [QPID-7980](https://issues.apache.org/jira/browse/QPID-7980) - [Java Broker] Queue delete (or routeToAlternate) leaves message instance records in the store
 - [QPID-7981](https://issues.apache.org/jira/browse/QPID-7981) - [Java Broker] [AMQP1.0] Handle erroneous null termini cases
 - [QPID-7982](https://issues.apache.org/jira/browse/QPID-7982) - [Java Broker] MariaDB backed JDBC virtualhost truncates message content at 64K leading to Broker abnormal shutdown
 - [QPID-7988](https://issues.apache.org/jira/browse/QPID-7988) - [Java Broker, AMQP 1.0] Receiving a Flow with an unknown handle MUST result in a session error
 - [QPID-7989](https://issues.apache.org/jira/browse/QPID-7989) - [Qpid Broker-J] [AMQP1.0] Session_1_0#unacknowledgedMessageCount not wired up
 - [QPID-7993](https://issues.apache.org/jira/browse/QPID-7993) - [Broker-J] Links for shared durable subscribers are accumulated in the link registry
 - [QPID-7994](https://issues.apache.org/jira/browse/QPID-7994) - [Broker-J] [JMS2.0 support] 'null source lookup' ends up in 'amqp:not-found' on attaching of unsubscribe links for global durable shared subscriptions
 - [QPID-7995](https://issues.apache.org/jira/browse/QPID-7995) - [Broker-J][WMC] VirtualHost queues/exchanges/loggers can be wrongly deleted from virtual host UI when "select all" checkbox is used to select all displayed rows and some of the rows are deselected afterwards
 - [QPID-8009](https://issues.apache.org/jira/browse/QPID-8009) - [Broker-J][WMC] New rows in message grid get selected after performing such operations like move messages and clear queue
 - [QPID-8010](https://issues.apache.org/jira/browse/QPID-8010) - [Broker-J][WMC] The row is selected on click or double-click for grids on virtual host tab
 - [QPID-8019](https://issues.apache.org/jira/browse/QPID-8019) - [Broker-J][WMC] Change link to broker documentation in web management console
 - [QPID-8028](https://issues.apache.org/jira/browse/QPID-8028) - [Broker-J][AMQP 0-8...0-9-1] Commit on nontransacted session causes broker to crash

## Tasks

 - [QPID-7444](https://issues.apache.org/jira/browse/QPID-7444) - [Java Broker] 500 http status code is returned on attempt to start SASL negotiation using SASL mechanism not supported by authentication provider 
 - [QPID-7502](https://issues.apache.org/jira/browse/QPID-7502) - [Java Broker] Add documentation for Query API
 - [QPID-7628](https://issues.apache.org/jira/browse/QPID-7628) - [java] update to current apache parent pom
 - [QPID-7638](https://issues.apache.org/jira/browse/QPID-7638) - Add ability to run JMS 2.0 TCK
 - [QPID-7640](https://issues.apache.org/jira/browse/QPID-7640) - [Java Broker] Migrate qpid-java svn to git 
 - [QPID-7656](https://issues.apache.org/jira/browse/QPID-7656) - [Java Broker] Clarify concerns of Link and LinkEndpoint in AMQP 1.0 plugin
 - [QPID-7658](https://issues.apache.org/jira/browse/QPID-7658) - [Java Broker] Improve LinkRegistry
 - [QPID-7659](https://issues.apache.org/jira/browse/QPID-7659) - [Java Broker, AMQP 1.0] Support Link stealing
 - [QPID-7660](https://issues.apache.org/jira/browse/QPID-7660) - [Java Broker] When recovering a AMQP 1.0 Link the Terminus should be recovered from the LinkRegistry
 - [QPID-7663](https://issues.apache.org/jira/browse/QPID-7663) - [Java Broker] Implement persistent storage of LinkRegistry
 - [QPID-7717](https://issues.apache.org/jira/browse/QPID-7717) - Remove tests and dependencies associated with the AMQP 0-10 JCA/RA components from Java Broker system test suite.
 - [QPID-7916](https://issues.apache.org/jira/browse/QPID-7916) - Rename qpid broker for java to qpid-broker-j in maven descriptions, documentations, website etc
 - [QPID-7985](https://issues.apache.org/jira/browse/QPID-7985) - [Qpid Broker-J] Update README.txt
 - [QPID-7998](https://issues.apache.org/jira/browse/QPID-7998) - [Broker-J] Allow global shared subscriptions but discard their links on detach
 - [QPID-8003](https://issues.apache.org/jira/browse/QPID-8003) - [Broker-J] Use log level 'info' to report conditions when no new rolled over log file is detected by the file logger
