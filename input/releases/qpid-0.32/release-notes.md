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

# Qpid 0.32 Release Notes

Qpid is a cross-platform AMQP messaging system.  It provides message
brokers written in C++ and Java, and clients for C++, Java, Perl,
Python, Ruby, and .NET.  More about [Qpid]({{site_url}}/index.html).

The full list of changes in the Qpid 0.32 release incorporates
both the issues worked on during the 0.31 development
stream and any final touches made during the 0.32 release
process. A list of these JIRA issues can be found below.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-5538](https://issues.apache.org/jira/browse/QPID-5538) - [amqp1.0] Generate keep-alive frames for peers using idle timeout
 - [QPID-5650](https://issues.apache.org/jira/browse/QPID-5650) - [Java Broker] DurableConfigurationStoreUpgrader relies on the action of the AMQQueueFactory to reunite queue with its dead letter exchange
 - [QPID-5671](https://issues.apache.org/jira/browse/QPID-5671) - [linearstore] Add ability to use disk partitions and select per-queue EFPs
 - [QPID-5703](https://issues.apache.org/jira/browse/QPID-5703) - Don't log "Generated $file" during cmake configure
 - [QPID-5799](https://issues.apache.org/jira/browse/QPID-5799) - Allow qpid.messaging.endpoints.session to have all associated receivers mointored via epoll mechanism
 - [QPID-5968](https://issues.apache.org/jira/browse/QPID-5968) - Improve SSL hostname verification
 - [QPID-6020](https://issues.apache.org/jira/browse/QPID-6020) - HA logging improvements - log prefix with status and ID.
 - [QPID-6035](https://issues.apache.org/jira/browse/QPID-6035) - HA clearly distinguish qpid-ha commands intended for cluster manager.
 - [QPID-6040](https://issues.apache.org/jira/browse/QPID-6040) - [Java Broker] Add the ability to create a single consumer that consumes from multiple queues
 - [QPID-6046](https://issues.apache.org/jira/browse/QPID-6046) - [Java Broker] [AMQP 1.0] Treat request to receive from amq.fanout (or any fanout exchange) as a request to create a temp queue and bind it to that exchange with any binding key
 - [QPID-6047](https://issues.apache.org/jira/browse/QPID-6047) - [Java Broker] When converting an AMQP 1.0 message into an AMQP 0-10 message place the subject into the application property qpid.subject
 - [QPID-6063](https://issues.apache.org/jira/browse/QPID-6063) - HA Node role UNKNOWN means both not-reachable and awaiting election
 - [QPID-6074](https://issues.apache.org/jira/browse/QPID-6074) - BDB HA VHN to use context variables rather than system property to control timeouts etc
 - [QPID-6078](https://issues.apache.org/jira/browse/QPID-6078) - [JMS AMQP 1.0 Client] Allow Message and Delivery annotations to be read and modified through the JMS API
 - [QPID-6083](https://issues.apache.org/jira/browse/QPID-6083) - Utilise pathname2url when constructing spec file location on older python versions
 - [QPID-6084](https://issues.apache.org/jira/browse/QPID-6084) - Guard use of sys.argv when constructing connection properties
 - [QPID-6085](https://issues.apache.org/jira/browse/QPID-6085) - Support receiving additional messages property types sent by the Java client (08..091)
 - [QPID-6086](https://issues.apache.org/jira/browse/QPID-6086) - SSL support for the python client (08..091)
 - [QPID-6088](https://issues.apache.org/jira/browse/QPID-6088) - [Java Client] AMQP 0-8/8/9-1 prefetch should auto expand when receive is called in a situation where the prefetch buffer is full
 - [QPID-6093](https://issues.apache.org/jira/browse/QPID-6093) - UI to expose read/write operations for context name/value pairs
 - [QPID-6098](https://issues.apache.org/jira/browse/QPID-6098) - [JMS AMQP 1.0 Client] Messages with a data section body should use content-type to drive the message type creation
 - [QPID-6101](https://issues.apache.org/jira/browse/QPID-6101) - [Java Common] Add ability to append release version suffix whilst building qpid
 - [QPID-6108](https://issues.apache.org/jira/browse/QPID-6108) - Java Broker - Document changes made by 0.30
 - [QPID-6114](https://issues.apache.org/jira/browse/QPID-6114) - Migrate the State member variable to AbstractConfiguredObject class
 - [QPID-6116](https://issues.apache.org/jira/browse/QPID-6116) - [Python Client 08..091] Add ability to negotiate SASL mechanism and add support for SCRAM, CRAM, PLAIN mechanisms
 - [QPID-6118](https://issues.apache.org/jira/browse/QPID-6118) - Add qmf shutdown command to the broker 
 - [QPID-6125](https://issues.apache.org/jira/browse/QPID-6125) - [Java] Refactor AMQP 0-8/0-9/0-9-1 Support
 - [QPID-6126](https://issues.apache.org/jira/browse/QPID-6126) - [Java Broker] Improve CO validation on creation and transit CO into ERRORED state on exceptions whilst recovering
 - [QPID-6129](https://issues.apache.org/jira/browse/QPID-6129) - Consistently chain exceptions in Derby/JDBC store implementations
 - [QPID-6130](https://issues.apache.org/jira/browse/QPID-6130) - Introduce edit queue functionality to the web management dialog
 - [QPID-6133](https://issues.apache.org/jira/browse/QPID-6133) - Context variable defaults not visible from context panels within the UI
 - [QPID-6137](https://issues.apache.org/jira/browse/QPID-6137) - [Java Broker] Enhance JMXManagementPlugin implementation and add extra logging when InstanceAlreadyExistsException is thrown from JMX on creation of VH MBean
 - [QPID-6138](https://issues.apache.org/jira/browse/QPID-6138) - Update perf test profiles replacing persistent/auto-ack with persistent/transacted
 - [QPID-6140](https://issues.apache.org/jira/browse/QPID-6140) - [C++ Messaging] UI Gotchya in Hello World example
 - [QPID-6145](https://issues.apache.org/jira/browse/QPID-6145) - Write operational log messages when flow to disk activates/deactivates
 - [QPID-6154](https://issues.apache.org/jira/browse/QPID-6154) - Handle rollback of node when use of weak durability has allowed nodes to diverge
 - [QPID-6161](https://issues.apache.org/jira/browse/QPID-6161) - [Java Broker] Add support for virtual host aliasing
 - [QPID-6162](https://issues.apache.org/jira/browse/QPID-6162) - [Java Broker] Add Plain/MD5 hashed password authentication providers that do not need external user file
 - [QPID-6163](https://issues.apache.org/jira/browse/QPID-6163) - [Java Broker] Forcibly disconnect clients which ignore producer flow control requests
 - [QPID-6164](https://issues.apache.org/jira/browse/QPID-6164) - [Java Broker] Add support for 0-8/9/9-1 synchronous publish using AMQP extensions
 - [QPID-6165](https://issues.apache.org/jira/browse/QPID-6165) - [Java Broker] Allow the number of open connections to be limited on a per port basis
 - [QPID-6167](https://issues.apache.org/jira/browse/QPID-6167) - Allow protocol versions to be disabled
 - [QPID-6168](https://issues.apache.org/jira/browse/QPID-6168) - On create or change, validate an object's attributes against its valid values
 - [QPID-6174](https://issues.apache.org/jira/browse/QPID-6174) - [Java Broker] Expose mechanism for restricting the number of HTTP connections / queued requests
 - [QPID-6175](https://issues.apache.org/jira/browse/QPID-6175) - [Java Broker] Allow restricting maximum size of a message to be accepted by the broker
 - [QPID-6199](https://issues.apache.org/jira/browse/QPID-6199) - [Java Broker] Enhance BDBStoreUpgradeTestPreparer to create sorted queue, custom exchange and publish messages into priority queue
 - [QPID-6200](https://issues.apache.org/jira/browse/QPID-6200) - [Java Broker] Virtual host records in JSON configuration store from  earlier versions of the broker with model versions 1.x are not upgraded into virtual host node records
 - [QPID-6203](https://issues.apache.org/jira/browse/QPID-6203) - Prevent broker startup when invalid directory is passed --sasl-config
 - [QPID-6204](https://issues.apache.org/jira/browse/QPID-6204) - [Java Broker] Improve fairness of distribution in multi-queue consumers
 - [QPID-6221](https://issues.apache.org/jira/browse/QPID-6221) - [Java Broker] Allow for detection of low space on filesystems containing the store, and enforcing flow control
 - [QPID-6223](https://issues.apache.org/jira/browse/QPID-6223) - [Java Broker] Change the default number of housekeeping threads created to something sensible
 - [QPID-6227](https://issues.apache.org/jira/browse/QPID-6227) - Avoid hardcoding/manipulating help links in web management console
 - [QPID-6233](https://issues.apache.org/jira/browse/QPID-6233) - [Java Broker] Update operational logging appendix in Java Broker documentation
 - [QPID-6239](https://issues.apache.org/jira/browse/QPID-6239) - [Java Broker] Redirect embedded database logs into the standard broker log file
 - [QPID-6245](https://issues.apache.org/jira/browse/QPID-6245) - [Java Broker] Large messages can cause OOM exceptions in 0-9 path due to unnecessary retained references in the delivery path
 - [QPID-6246](https://issues.apache.org/jira/browse/QPID-6246) - Refactor authentication provider UIs to uses dedicated dialogues
 - [QPID-6250](https://issues.apache.org/jira/browse/QPID-6250) -  Remove the hard coded default username and password values defined in ConnectionSettings.java
 - [QPID-6253](https://issues.apache.org/jira/browse/QPID-6253) - Name the Qpid AMQP acceptor threads
 - [QPID-6255](https://issues.apache.org/jira/browse/QPID-6255) - [amqp1.0] Migrate to the new Proton event API
 - [QPID-6258](https://issues.apache.org/jira/browse/QPID-6258) - Simplify AbstractQueue by removing SubFlushRunner
 - [QPID-6263](https://issues.apache.org/jira/browse/QPID-6263) - [Java Broker] Move remaining ApplicationRegistry functionality into server.Broker class
 - [QPID-6276](https://issues.apache.org/jira/browse/QPID-6276) - Add UI for uploading/download virtual host configuration
 - [QPID-6289](https://issues.apache.org/jira/browse/QPID-6289) - Extend Java Broker model to capture permitted child types
 - [QPID-6290](https://issues.apache.org/jira/browse/QPID-6290) - Refactor the add VNH/VH feature to remove reliance on conditional logic in terms of VHN/VH type
 - [QPID-6291](https://issues.apache.org/jira/browse/QPID-6291) - Remove the now defunct 'supported' attributes
 - [QPID-6292](https://issues.apache.org/jira/browse/QPID-6292) - Refactor AbstractConfiguredObjects unit tests
 - [QPID-6293](https://issues.apache.org/jira/browse/QPID-6293) - Log Java Broker's pid on startup
 - [QPID-6294](https://issues.apache.org/jira/browse/QPID-6294) - [Java Client] Allow use of 0 prefetch in AMQP 0-8/9/9-1
 - [QPID-6295](https://issues.apache.org/jira/browse/QPID-6295) - [Java Broker] Allow ACL configuration file to be stored as a data:// URL inside the config
 - [QPID-6304](https://issues.apache.org/jira/browse/QPID-6304) - [Java Broker] Allow truststore and keystore (JKS) files to be stored as data:// URLs inside the config
 - [QPID-6306](https://issues.apache.org/jira/browse/QPID-6306) - [Java Broker] restrict the Broker to a single ACL provider at a time
 - [QPID-6312](https://issues.apache.org/jira/browse/QPID-6312) - Enable C++ components to build on IBM AIX with XL C++
 - [QPID-6316](https://issues.apache.org/jira/browse/QPID-6316) - Make UI support the upload of ACL files 
 - [QPID-6318](https://issues.apache.org/jira/browse/QPID-6318) - Make UI support the upload of JKS files 
 - [QPID-6333](https://issues.apache.org/jira/browse/QPID-6333) - [Java Broker] Upgrade Java Broker JE dependency to version 5.0.104
 - [QPID-6338](https://issues.apache.org/jira/browse/QPID-6338) - [Java AMQP 1.0 Client] [Java Broker] Validate message sections are in a valid order
 - [QPID-6339](https://issues.apache.org/jira/browse/QPID-6339) - [Java Broker] Use variable interpolation for help URL and initial config virtual host config
 - [QPID-6340](https://issues.apache.org/jira/browse/QPID-6340) - [Java] Allow defaults for system properties to be overridden from a properties file
 - [QPID-6341](https://issues.apache.org/jira/browse/QPID-6341) - [Java Broker] Enhancements to config object meta data model
 - [QPID-6342](https://issues.apache.org/jira/browse/QPID-6342) - [Java Broker] Fail fast if the client sends frames out of order
 - [QPID-6343](https://issues.apache.org/jira/browse/QPID-6343) - [Java Broker] Upgrade Apache Derby dependency to 10.11.1.1
 - [QPID-6345](https://issues.apache.org/jira/browse/QPID-6345) - [Java Broker] Allow enabled TLS Ciphers to be restricted through configuration
 - [QPID-6346](https://issues.apache.org/jira/browse/QPID-6346) - [Java Broker] Add UI for uploading of pem/der keys and certificates for non-java keystores/truststores into web management console
 - [QPID-6349](https://issues.apache.org/jira/browse/QPID-6349) - [JMS AMQP 1.0 Client] Add ability to change the SSL Protocol/Provider used to create the SSLContext
 - [QPID-6356](https://issues.apache.org/jira/browse/QPID-6356) - [Java Broker] Remove operational log "MNG-1006 : Using SSL Keystore : {0}"
 - [QPID-6360](https://issues.apache.org/jira/browse/QPID-6360) - [Java Broker] Extend the UI to support creation of alternate group providers and the new config based group provider plugin
 - [QPID-6361](https://issues.apache.org/jira/browse/QPID-6361) - [0-8..0-91] Active queue declare no longer to validate an existing queue's durability 
 - [QPID-6367](https://issues.apache.org/jira/browse/QPID-6367) - [Java Broker] Change broker model version to 3.0 due to backward incompatible model changes
 - [QPID-6390](https://issues.apache.org/jira/browse/QPID-6390) - [Java Broker] Move setting of initial properties from Main into Broker
 - [QPID-6395](https://issues.apache.org/jira/browse/QPID-6395) - [Java Broker] Add support for "default" filters on a queue, and for filters based soley on arrival time at the broker
 - [QPID-6396](https://issues.apache.org/jira/browse/QPID-6396) - [Java Broker] Allow queues to enforce all consumers to be non-destructive
 - [QPID-6401](https://issues.apache.org/jira/browse/QPID-6401) - [Java Broker] Add ability to validate connection attempts based on plugins
 - [QPID-6408](https://issues.apache.org/jira/browse/QPID-6408) - Expose the AMQP connection limits through the web management UI

## Bugs fixed

 - [QPID-3678](https://issues.apache.org/jira/browse/QPID-3678) - Can't set prefetch to 0 using capacity option in address
 - [QPID-4276](https://issues.apache.org/jira/browse/QPID-4276) - Java client - deadlock on concurrent close of consumer and connection
 - [QPID-4574](https://issues.apache.org/jira/browse/QPID-4574) - [JMS] Deadlock involving _failoverMutex and _messageDeliveryLock
 - [QPID-4575](https://issues.apache.org/jira/browse/QPID-4575) - Support Visual Studio 2012
 - [QPID-4710](https://issues.apache.org/jira/browse/QPID-4710) - [AMQP 1.0] Support for transactions
 - [QPID-4906](https://issues.apache.org/jira/browse/QPID-4906) - If Session close() or closed() method is invoked while inside onMessage(), they should be excuted after onMessage() has completed.
 - [QPID-5033](https://issues.apache.org/jira/browse/QPID-5033) - [Windows C++ client] An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full
 - [QPID-5099](https://issues.apache.org/jira/browse/QPID-5099) - [JMS 0-8...0-9-1]  Messages pre-aquired by the consumer are not released on MessageConsumer#close()
 - [QPID-5117](https://issues.apache.org/jira/browse/QPID-5117) - Java client deadlocks if connection is closed while onMessage() is creating a session
 - [QPID-5118](https://issues.apache.org/jira/browse/QPID-5118) - [JMS] Deadlock when closing a consumer and calling JMS operatons inside onMessage() on AMQP 0-8/0-9/0-9-1 connection
 - [QPID-5119](https://issues.apache.org/jira/browse/QPID-5119) - [JMS] 3-thread deadlock on pre-AMQP-0-10 connection involving messageDeliveryLock, failover mutex and sessionCreationLock
 - [QPID-5590](https://issues.apache.org/jira/browse/QPID-5590) - It is trivially easy to fatally crash qpidd using a dodgy exchange type in a TopicPolicy
 - [QPID-5842](https://issues.apache.org/jira/browse/QPID-5842) - Allow SSL hostname verification to be disabled on windows
 - [QPID-5855](https://issues.apache.org/jira/browse/QPID-5855) - JAVA Client Can not recieve message with qpid ha cluster "Session exception occured while trying to commit"
 - [QPID-5893](https://issues.apache.org/jira/browse/QPID-5893) - Perl unit tests fail to run
 - [QPID-5927](https://issues.apache.org/jira/browse/QPID-5927) - Broker does not support whitespace in passwords in SSL password file
 - [QPID-5950](https://issues.apache.org/jira/browse/QPID-5950) - C++ Broker Windows Timer launches two simultaneous QueueCleaner::purge instances (was: invalid heap)
 - [QPID-5966](https://issues.apache.org/jira/browse/QPID-5966) -  HA mixing tx enqueue and non-tx dequeue leaves extra messages on backup
 - [QPID-5973](https://issues.apache.org/jira/browse/QPID-5973) - HA cluster state may get stuck in recovering
 - [QPID-5974](https://issues.apache.org/jira/browse/QPID-5974) - HA qpid-txtest2 can bring down a cluster (JERR_MAP_LOCKED)
 - [QPID-5975](https://issues.apache.org/jira/browse/QPID-5975) - HA extra/missing messages when running qpid-txtest2 in a loop with failover. 
 - [QPID-5977](https://issues.apache.org/jira/browse/QPID-5977) - Ports created through the web management ui have no transports
 - [QPID-5995](https://issues.apache.org/jira/browse/QPID-5995) - C+ Messaging SenderContext uses uninitialized memory for delivery tags
 - [QPID-6007](https://issues.apache.org/jira/browse/QPID-6007) - qpid-route uses machine hostname if host not given
 - [QPID-6013](https://issues.apache.org/jira/browse/QPID-6013) - qpid-route shall warn that federation link hasn't been created
 - [QPID-6015](https://issues.apache.org/jira/browse/QPID-6015) - HA Python QMF console raises exception due to HA subscriptions.
 - [QPID-6021](https://issues.apache.org/jira/browse/QPID-6021) - [AMQP 1.0] Improve performance
 - [QPID-6025](https://issues.apache.org/jira/browse/QPID-6025) - Java port of QpidConfig give NPE when listing queue/exchanges
 - [QPID-6026](https://issues.apache.org/jira/browse/QPID-6026) - C++ Messaging WinSDK does not build all example code
 - [QPID-6032](https://issues.apache.org/jira/browse/QPID-6032) - Don't wait for reconnect to abort transaction due to transport failure
 - [QPID-6045](https://issues.apache.org/jira/browse/QPID-6045) - [AMQP 1.0] xml exchange reports support for amqp legacy topic filter
 - [QPID-6051](https://issues.apache.org/jira/browse/QPID-6051) - [Java Broker] When client socket is get closed after transaction commit but before sending TxCommitOk back, a message might be deleted from a store but left on queue causing later on unhandled "AMQStoreException: Metadata not found" and broker crash
 - [QPID-6055](https://issues.apache.org/jira/browse/QPID-6055) - [Java Broker] BDB Message Store can thow java.lang.IndexOutOfBoundsException on trying to retrieve the message content
 - [QPID-6057](https://issues.apache.org/jira/browse/QPID-6057) - Test MultiNodeTest.testClusterCannotStartWithIntruder fails sporadically
 - [QPID-6058](https://issues.apache.org/jira/browse/QPID-6058) - [Java Client] The client does not fail with a sensible error message if it tries to send a message header that is larger than the max frame size
 - [QPID-6061](https://issues.apache.org/jira/browse/QPID-6061) - [Java Broker] [AMQP 1.0] The Java Broker does not properly implement the legacy filters as it never routes on subject
 - [QPID-6067](https://issues.apache.org/jira/browse/QPID-6067) - [Java Broker] Test BDBHAVirtualHostNodeOperationalLoggingTest.testRemoteNodeDetached fails sporadically
 - [QPID-6071](https://issues.apache.org/jira/browse/QPID-6071) - Removing designated primary/electable group override from a node in a group without quorum should cause it to return to WAITING
 - [QPID-6072](https://issues.apache.org/jira/browse/QPID-6072) - [AMQP 1.0] tcp-nodelay not supported yet on 1.0 connections
 - [QPID-6073](https://issues.apache.org/jira/browse/QPID-6073) - Long field prompts can obscure field labels
 - [QPID-6075](https://issues.apache.org/jira/browse/QPID-6075) - Deleting VHN fails to delete underlying store files if VHN has not been started
 - [QPID-6081](https://issues.apache.org/jira/browse/QPID-6081) - Large (multi-frame body) messages fail to be received correctly (08..091)
 - [QPID-6082](https://issues.apache.org/jira/browse/QPID-6082) - Method body frames interleaving between message header/body frames can lead to unexpected behaviour (08..091)
 - [QPID-6087](https://issues.apache.org/jira/browse/QPID-6087) -  QMF Session name to contain user ID for AMQP 0-10
 - [QPID-6090](https://issues.apache.org/jira/browse/QPID-6090) - Disallow a removal of permitted node entry from BDB HA VHN attribute "permittedNodes", if that node is already a member of a group
 - [QPID-6092](https://issues.apache.org/jira/browse/QPID-6092) - Editing permitted node list to be allowed when VHN is master or in STOPPED/ERRORed state
 - [QPID-6095](https://issues.apache.org/jira/browse/QPID-6095) - Deletion of an ERRORED JSON VHN with an invalid store path causes an exception
 - [QPID-6099](https://issues.apache.org/jira/browse/QPID-6099) - Closing a 0-8..0-9-1 connection with an exception whose message exceeds 255 characters leads to unexpected Broker shutdown
 - [QPID-6100](https://issues.apache.org/jira/browse/QPID-6100) - NPE when the password is wrong
 - [QPID-6102](https://issues.apache.org/jira/browse/QPID-6102) - Client connection closure whilst HA transitioning state can lead to unexpected Broker shutdown
 - [QPID-6104](https://issues.apache.org/jira/browse/QPID-6104) - Test ReplicatedEnvironmentFacadeTest.testRemoveNodeFromGroup fails sporadically
 - [QPID-6105](https://issues.apache.org/jira/browse/QPID-6105) - Use of const keyword breaks compatibility with older IE browser
 - [QPID-6106](https://issues.apache.org/jira/browse/QPID-6106) - Replace empty fields with "unknown" in qpid-stat -c output 
 - [QPID-6107](https://issues.apache.org/jira/browse/QPID-6107) - Python Swig wrapped bindings consistently fail with spout and drain
 - [QPID-6109](https://issues.apache.org/jira/browse/QPID-6109) - qpid.messaaging builtin PLAIN auth does not agree on auth mechanism if password is None or ''
 - [QPID-6111](https://issues.apache.org/jira/browse/QPID-6111) - Ensure that ReplicatedEnvironmentFacade awaits sufficient time on shutdown for any in-progress restart to complete 
 - [QPID-6112](https://issues.apache.org/jira/browse/QPID-6112) - [C++ broker] Incoming QMF objects dont update "transfers" counter
 - [QPID-6119](https://issues.apache.org/jira/browse/QPID-6119) - [AMQP 1.0] - java.lang.NullPointerException on reconnect when link has been down between client and broker
 - [QPID-6123](https://issues.apache.org/jira/browse/QPID-6123) - [C++ Messaging] Build fail - proton no longer exports pn_transport_error()
 - [QPID-6127](https://issues.apache.org/jira/browse/QPID-6127) - nextReceiver() with IMMEDIATE duration doesn't throw TransportFailure
 - [QPID-6128](https://issues.apache.org/jira/browse/QPID-6128) - Error when casting from 'sockaddr*' to 'sockaddr_in*' on ARM platforms
 - [QPID-6131](https://issues.apache.org/jira/browse/QPID-6131) - Prevent messaging connection to virtualhost  that is in the process of being closed
 - [QPID-6132](https://issues.apache.org/jira/browse/QPID-6132) - SimpleLDAP produces NPE at authentication time if providerUrl is null.
 - [QPID-6134](https://issues.apache.org/jira/browse/QPID-6134) - Restarting a node that has detected an intruder should go back into the ERROR state not ACTIVE
 - [QPID-6135](https://issues.apache.org/jira/browse/QPID-6135) - build failure in qpid-cpp-0.30/src/tests/txshift.cpp
 - [QPID-6136](https://issues.apache.org/jira/browse/QPID-6136) - [Java Broker] On replica BDB HA Virtual host node permitted nodes are set every time when group monitoring thread is run even when they are not changed 
 - [QPID-6142](https://issues.apache.org/jira/browse/QPID-6142) - NPE on startup if key permissions are wrong
 - [QPID-6143](https://issues.apache.org/jira/browse/QPID-6143) - [Java Broker] Broker can crash on publishing/consuming messages during master transfer in BDB HA group 
 - [QPID-6144](https://issues.apache.org/jira/browse/QPID-6144) - [Java Broker] Environment invalid JE exception occured while transferring Master
 - [QPID-6148](https://issues.apache.org/jira/browse/QPID-6148) -  purging TTL expired messages via purge task should not increase acquires counters 
 - [QPID-6149](https://issues.apache.org/jira/browse/QPID-6149) - [Java Broker] Use better names for the domain of BDB HA node priority
 - [QPID-6151](https://issues.apache.org/jira/browse/QPID-6151) - Preference provider attributes missing from panel
 - [QPID-6152](https://issues.apache.org/jira/browse/QPID-6152) - Connection close timeout too short when connections have many sessions
 - [QPID-6156](https://issues.apache.org/jira/browse/QPID-6156) - [Java Broker] [Java Client] Disable SSLv3 support
 - [QPID-6157](https://issues.apache.org/jira/browse/QPID-6157) - linearstore: segfault when 2 journals request new journal file from empty EFP
 - [QPID-6159](https://issues.apache.org/jira/browse/QPID-6159) - [Java Broker] AbstractConfiguredObject.getContextKeys() should include values from the default context
 - [QPID-6160](https://issues.apache.org/jira/browse/QPID-6160) - CLONE - [CPP Broker] [CPP Client] Disable SSLv3 support
 - [QPID-6169](https://issues.apache.org/jira/browse/QPID-6169) - Prevent IllegalStateException possibility from remote state learner
 - [QPID-6171](https://issues.apache.org/jira/browse/QPID-6171) - [Java Common] Connection.getChannels() leaks a potentially thread-unsafe data structure
 - [QPID-6172](https://issues.apache.org/jira/browse/QPID-6172) - [Java Broker] Ensure the type attribute is always in the actual attributes of a configured object
 - [QPID-6173](https://issues.apache.org/jira/browse/QPID-6173) - Virtualhost corresponding to the replica should disallow attribute update
 - [QPID-6176](https://issues.apache.org/jira/browse/QPID-6176) - Re-instate the variables/values that are now missing from the Web UI Broker Attributes section
 - [QPID-6178](https://issues.apache.org/jira/browse/QPID-6178) - [C++ Broker] compiler error Visual Studio 2008 and Boost 1.55
 - [QPID-6181](https://issues.apache.org/jira/browse/QPID-6181) - JMX queue delete leaves queue in the store and leaks some memory
 - [QPID-6182](https://issues.apache.org/jira/browse/QPID-6182) - AMQP 1.0 consumer should be able to get messages from browse-only queue
 - [QPID-6184](https://issues.apache.org/jira/browse/QPID-6184) - [Java Broker] Java Broker leaks connections and sessions via SessionPrincipal and ConnectionPrincipal in Thread inherited access control context
 - [QPID-6185](https://issues.apache.org/jira/browse/QPID-6185) - Make the web management UI tables, tabs and panels more consistent in terms of style and STATE being displayed
 - [QPID-6186](https://issues.apache.org/jira/browse/QPID-6186) - Deleting a queue with bindings leaks the bindings
 - [QPID-6187](https://issues.apache.org/jira/browse/QPID-6187) - Disable SSL v3 for Windows SChannel
 - [QPID-6189](https://issues.apache.org/jira/browse/QPID-6189) - [Java Common] 0-8/9/9-1 parser can cause stack overflow if a frame is broken into many TCP reads/writes
 - [QPID-6190](https://issues.apache.org/jira/browse/QPID-6190) - [Java Broker] [AMQP 1.0] Transactionally sending to a queue (rather than an exchange) causes MessageDeletedException
 - [QPID-6192](https://issues.apache.org/jira/browse/QPID-6192) - Broker model closes exchanges/queues before connections
 - [QPID-6193](https://issues.apache.org/jira/browse/QPID-6193) - [AMQP 1.0 JMS Client] [Java broker] AMQP 1.0 Open frames with channel-max above the signed short range leads to failure
 - [QPID-6194](https://issues.apache.org/jira/browse/QPID-6194) - Allow Qpid broker to be configured to fail to start if it has a child object in ERRORED state
 - [QPID-6195](https://issues.apache.org/jira/browse/QPID-6195) - [Java Broker] On broker upgrade record updated in one upgrader and removed in another upgrader is recovered anyway (and fails)
 - [QPID-6196](https://issues.apache.org/jira/browse/QPID-6196) - Race condition makes it possible to create 2 queues with the same name on the same VirtualHost
 - [QPID-6197](https://issues.apache.org/jira/browse/QPID-6197) - qpid.messaging does not support unicode for username
 - [QPID-6198](https://issues.apache.org/jira/browse/QPID-6198) - [Java Broker] 0-10 session may unnecessarily retain reference to consumed queue entry leading to memory leak
 - [QPID-6201](https://issues.apache.org/jira/browse/QPID-6201) - BDB state change events must be delivered sequential to the virtualhostnode
 - [QPID-6202](https://issues.apache.org/jira/browse/QPID-6202) - Closing an AMQProtocolEngine can leave it in an inconsistent state if an AMQChannel fails to close
 - [QPID-6205](https://issues.apache.org/jira/browse/QPID-6205) - [0.8/0.9.x] JMS client leaks transport threads and sockets if connection cannot be established to the broker
 - [QPID-6206](https://issues.apache.org/jira/browse/QPID-6206) - [JMS 0-9 client] AMQDecoder uses buffered data from previous connection to decode broker frames
 - [QPID-6207](https://issues.apache.org/jira/browse/QPID-6207) - Broker retains hard references to persistent messages of uncommitted transactions
 - [QPID-6208](https://issues.apache.org/jira/browse/QPID-6208) - PermittedNodeList seen to disappear while performing certain HA operations
 - [QPID-6209](https://issues.apache.org/jira/browse/QPID-6209) - Ensure node discoverer returns a value for every node even if node is partitioned
 - [QPID-6210](https://issues.apache.org/jira/browse/QPID-6210) - VHMBean#createNewQueue throws QueueExistsException if the queue already exists
 - [QPID-6212](https://issues.apache.org/jira/browse/QPID-6212) - [WinSDK] build script does not provide hooks to include proton (AMQP 1.0)
 - [QPID-6213](https://issues.apache.org/jira/browse/QPID-6213) - qpidd misses heartbeats
 - [QPID-6214](https://issues.apache.org/jira/browse/QPID-6214) - Stopping a virtualhost that has in-flight asynchronous message store recovery can lead abnormal broker shutdown
 - [QPID-6216](https://issues.apache.org/jira/browse/QPID-6216) - Report to the BDB HA VirtualHostNode as early as possible that is's no longer the Master node
 - [QPID-6217](https://issues.apache.org/jira/browse/QPID-6217) - Java broker should not accept HTTP TRACE requests 
 - [QPID-6218](https://issues.apache.org/jira/browse/QPID-6218) - xml exchange can be induced to make http requests
 - [QPID-6219](https://issues.apache.org/jira/browse/QPID-6219) - Fix log4j warning logged on startup
 - [QPID-6220](https://issues.apache.org/jira/browse/QPID-6220) - Management UI displays misleading synchronisation attribute values when defaults are in force
 - [QPID-6222](https://issues.apache.org/jira/browse/QPID-6222) - [Java Broker] Replica can go into a loop if it runs out of disk space
 - [QPID-6224](https://issues.apache.org/jira/browse/QPID-6224) - Inappropriate use Environment.cleanLog in the BDB store leaves unnecessarily large transaction logs
 - [QPID-6225](https://issues.apache.org/jira/browse/QPID-6225) - Avoid repeated spamming of the logs when the group change listener times out trying to contact a remote node
 - [QPID-6226](https://issues.apache.org/jira/browse/QPID-6226) - Running client/server C++ client examples fail against the Java Broker with 'Cannot declare queue..'
 - [QPID-6230](https://issues.apache.org/jira/browse/QPID-6230) - [linearstore] qpid-qls-analyze fails when analyzing empty journal
 - [QPID-6231](https://issues.apache.org/jira/browse/QPID-6231) - [Perftests framework] Make performance framework fully JMS compatible
 - [QPID-6235](https://issues.apache.org/jira/browse/QPID-6235) - [Java Broker] backup-log4j.xml is not included into bdbstore jar
 - [QPID-6240](https://issues.apache.org/jira/browse/QPID-6240) - transactionally accepted messages stuck in acquired after abort
 - [QPID-6241](https://issues.apache.org/jira/browse/QPID-6241) - Windows build fails VS2010, x64
 - [QPID-6242](https://issues.apache.org/jira/browse/QPID-6242) - [Java Broker] AESKeyFileEncrypterFactory does not work on non-posix filesystems
 - [QPID-6243](https://issues.apache.org/jira/browse/QPID-6243) - [Java Broker] Updates to Json configuration stores cause a small memory leak
 - [QPID-6247](https://issues.apache.org/jira/browse/QPID-6247) - Updates to configuration files should maintain existing file permissions
 - [QPID-6248](https://issues.apache.org/jira/browse/QPID-6248) - [linearstore] Symlink creation fails if store dir path is not absolute
 - [QPID-6252](https://issues.apache.org/jira/browse/QPID-6252) - AMQP 1.0 browsing client generates large number of errors on broker.
 - [QPID-6257](https://issues.apache.org/jira/browse/QPID-6257) - [Java Broker] Excessive ERROR log entry is added into a Broker log file on unexpected socket close by the client
 - [QPID-6259](https://issues.apache.org/jira/browse/QPID-6259) - [Java Broker] On DatabaseException in BDB committer thread, stopping of Coalescing committer in the same committer thread hangs because it waits for committer thread to finish running
 - [QPID-6267](https://issues.apache.org/jira/browse/QPID-6267) - qpid.auto_delete_timeout of 0 on a topic is ignored
 - [QPID-6268](https://issues.apache.org/jira/browse/QPID-6268) - Broker statistic Queue#unacknowledgedMessages is maintained incorrectly when the client rolls-back a session with unacknowledged messages
 - [QPID-6269](https://issues.apache.org/jira/browse/QPID-6269) - timed autodelete doesn't work on recovered queues
 - [QPID-6271](https://issues.apache.org/jira/browse/QPID-6271) - [AMQP 1.0] receivers never removed from sessions list
 - [QPID-6272](https://issues.apache.org/jira/browse/QPID-6272) - Avoid leak potential for the 0-8..0-91 default queue
 - [QPID-6273](https://issues.apache.org/jira/browse/QPID-6273) - client/server example doesn't use content-object
 - [QPID-6274](https://issues.apache.org/jira/browse/QPID-6274) - [AMQP 1.0] subscriptions queues with timed autodelete should be deleted immediately when link is closed
 - [QPID-6275](https://issues.apache.org/jira/browse/QPID-6275) - reduce default timeout for durable subscription queues
 - [QPID-6278](https://issues.apache.org/jira/browse/QPID-6278) -  HA broker abort in TXN soak test
 - [QPID-6281](https://issues.apache.org/jira/browse/QPID-6281) - Child of type SessionAdapter already exists with name of 0
 - [QPID-6296](https://issues.apache.org/jira/browse/QPID-6296) - [linearstore] Restarting broker with empty journal created with qpid-config raises confusing warning
 - [QPID-6298](https://issues.apache.org/jira/browse/QPID-6298) - [C++Messaging] Server example never frees session senders
 - [QPID-6299](https://issues.apache.org/jira/browse/QPID-6299) - can't combine ring queue and lvq functionality
 - [QPID-6301](https://issues.apache.org/jira/browse/QPID-6301) - [C++Messaging] Client example never acknowledges responses
 - [QPID-6303](https://issues.apache.org/jira/browse/QPID-6303) - [linearstore] Roll back auto-upgrade of store directory structure
 - [QPID-6310](https://issues.apache.org/jira/browse/QPID-6310) - unexpected protocol sequences not properly checked
 - [QPID-6321](https://issues.apache.org/jira/browse/QPID-6321) - Can't build against latest 0.9
 - [QPID-6322](https://issues.apache.org/jira/browse/QPID-6322) - [AMQP 1.0] don't set qpid.auto_delete_timeout if the value is 0
 - [QPID-6323](https://issues.apache.org/jira/browse/QPID-6323) - [AMQP 1.0] don't set timeout by default for durable subscription if they are also flagged reliable
 - [QPID-6324](https://issues.apache.org/jira/browse/QPID-6324) - adjust when default timeout is applied
 - [QPID-6325](https://issues.apache.org/jira/browse/QPID-6325) - Improve 0-10 connection handling logic
 - [QPID-6329](https://issues.apache.org/jira/browse/QPID-6329) - TypeError on qpid.auto_delete_timeout assertion 
 - [QPID-6331](https://issues.apache.org/jira/browse/QPID-6331) - [Java Broker] Allow persistent AMQP 1.0 message content to be evicted from the heap
 - [QPID-6336](https://issues.apache.org/jira/browse/QPID-6336) - [0-8..0-91] State of connection can be corrupted by subsequent reconnection attempts
 - [QPID-6347](https://issues.apache.org/jira/browse/QPID-6347) - queue_event_generation option clean-up
 - [QPID-6350](https://issues.apache.org/jira/browse/QPID-6350) - [AMQP0-10] Original connection exception lost if Broker closes socket before client
 - [QPID-6351](https://issues.apache.org/jira/browse/QPID-6351) - [Java Broker] Remove provider name from edit UI, remove button "Add Preferences Provider" from Authentication provider tab and fix disabled  preferences provider fields in Add Authentication provider dialog
 - [QPID-6353](https://issues.apache.org/jira/browse/QPID-6353) - Java broker AMQP 1.0 impl doesn't seem to support "synchronous get" / respond to drain request
 - [QPID-6354](https://issues.apache.org/jira/browse/QPID-6354) - Non java keystore exceptions about incorrect format of private key or certificates are swallowed and ignored
 - [QPID-6358](https://issues.apache.org/jira/browse/QPID-6358) - session detach not detected by fetching receiver
 - [QPID-6362](https://issues.apache.org/jira/browse/QPID-6362) - Management mode generates null one-time-password (OTP)
 - [QPID-6363](https://issues.apache.org/jira/browse/QPID-6363) - Fail early if additional SASL providers cannot be registered with the Java Security API
 - [QPID-6364](https://issues.apache.org/jira/browse/QPID-6364) - [Java Broker] Keystore data url must be a secure attribute
 - [QPID-6365](https://issues.apache.org/jira/browse/QPID-6365) - [Java Broker] Secure management attributes need to be masked all the time
 - [QPID-6366](https://issues.apache.org/jira/browse/QPID-6366) - [Java Broker] Prevent data urls cluttering the UI and prevent potentially large data url consuming too much bandwidth during the regular REST poll
 - [QPID-6371](https://issues.apache.org/jira/browse/QPID-6371) - Prevent log4j warning during Broker startup
 - [QPID-6372](https://issues.apache.org/jira/browse/QPID-6372) - Prevent qpid-server.bat modifying the environment of its calling command shell
 - [QPID-6374](https://issues.apache.org/jira/browse/QPID-6374) - [Java Client] Eliminate deadlocks by acquiring locks in a consistent order
 - [QPID-6375](https://issues.apache.org/jira/browse/QPID-6375) - [Java Broker] [AMQP 1.0] ending a session with attached consumer link leads to NPE
 - [QPID-6378](https://issues.apache.org/jira/browse/QPID-6378) - Connection protocol name is wrong and decoding error on heartbeats
 - [QPID-6380](https://issues.apache.org/jira/browse/QPID-6380) - [AMQP 1.0 JMS Client ] detach with closed=true is issued when making durable subscriber inactive
 - [QPID-6381](https://issues.apache.org/jira/browse/QPID-6381) - [Java Broker] [AMQP 1.0] the 'closed' field is ignored when detaching
 - [QPID-6383](https://issues.apache.org/jira/browse/QPID-6383) - [Java Broker] [AMQP 1.0] durable subscription backing queue was not recovered after restart
 - [QPID-6384](https://issues.apache.org/jira/browse/QPID-6384) - [Java Broker] [AMQP 1.0] unable to recreate a durable subscription after calling unsubscribe
 - [QPID-6386](https://issues.apache.org/jira/browse/QPID-6386) - IoSender thread leak
 - [QPID-6387](https://issues.apache.org/jira/browse/QPID-6387) - ChannelToSessionMap/IdToConsumerMap array optimisation publishes in thread unsafe manner
 - [QPID-6388](https://issues.apache.org/jira/browse/QPID-6388) - [Java Broker] [AMQP 1.0] unable to resubscribe a durable subscription link when using 'configuration' terminus durability
 - [QPID-6389](https://issues.apache.org/jira/browse/QPID-6389) - [C++ Broker] [AMQP 1.0] consumer attach with a null source leads to unexpected response
 - [QPID-6393](https://issues.apache.org/jira/browse/QPID-6393) - Race condition in message delivery path may cause a queue browser's to be closed permaturely. 
 - [QPID-6398](https://issues.apache.org/jira/browse/QPID-6398) - [Java Broker] Update web management console UI to invoke dojo parser.parse as a promise due to changes in dojo 1.8 causing the parser to run in asynchronous fashion in some cases
 - [QPID-6400](https://issues.apache.org/jira/browse/QPID-6400) - Provide a mechanism to provide a KeyStore itself rather than a file system path to it
 - [QPID-6404](https://issues.apache.org/jira/browse/QPID-6404) - [AMQP 1.0 JMS Client ] Cannot send simple empty body JMS Message types
 - [QPID-6406](https://issues.apache.org/jira/browse/QPID-6406) - ACO generates attribute set events even if the attribute value is not changed
 - [QPID-6407](https://issues.apache.org/jira/browse/QPID-6407) - Edit dialogue for BDB HA does not faithfully populate attributes node priority or required number of nodes
 - [QPID-6410](https://issues.apache.org/jira/browse/QPID-6410) - [Java Broker] Disambiguate the connection adapter name by adding a connection ID to the name
 - [QPID-6411](https://issues.apache.org/jira/browse/QPID-6411) - [AMQP 1.0 JMS Client ] NPE during session#unsubscribe is link is refused but detach contains no error condition
 - [QPID-6413](https://issues.apache.org/jira/browse/QPID-6413) - Sporadic failure of HA tests causd by maxNegotiateTimeout
 - [QPID-6414](https://issues.apache.org/jira/browse/QPID-6414) - Skip HA tests if qpid-ha or qpid-config tools are not available.
 - [QPID-6415](https://issues.apache.org/jira/browse/QPID-6415) - Core dump in ha_tests and interlink_tests with proton 0.9
 - [QPID-6416](https://issues.apache.org/jira/browse/QPID-6416) - Mutex.h:116: void qpid::sys::Mutex::lock(): Assertion `0' failed. - during Messaging shutdown
 - [QPID-6418](https://issues.apache.org/jira/browse/QPID-6418) - [Java Broker] Use annotation to denote managed object which manage the storage of their childrens' data
 - [QPID-6419](https://issues.apache.org/jira/browse/QPID-6419) - [Java Broker] Queue counts can become corrupt in case of rapid acknowledgement
 - [QPID-6427](https://issues.apache.org/jira/browse/QPID-6427) - Problem building trunk qpid cpp on RHEL 5
 - [QPID-6432](https://issues.apache.org/jira/browse/QPID-6432) - [Java broker] [AMQP 1.0] add support for mapping JMSType header to message Subject
 - [QPID-6433](https://issues.apache.org/jira/browse/QPID-6433) - [Java broker] [AMQP 1.0] Deadlock if flow arrives as queue is sending message
 - [QPID-6437](https://issues.apache.org/jira/browse/QPID-6437) - [Java broker] [AMQP 1.0] deadlock if flow arrives as consumer is being notified queue is empty
 - [QPID-6439](https://issues.apache.org/jira/browse/QPID-6439) - Mandatory attribute storeUrl not supplied for instance of org.apache.qpid.server.security.FileKeyStoreImpl
 - [QPID-6444](https://issues.apache.org/jira/browse/QPID-6444) - Build fails due to unused function warning

## Tasks

 - [QPID-6337](https://issues.apache.org/jira/browse/QPID-6337) - [Java Broker] Upgrade Dojo version to 1.10.3