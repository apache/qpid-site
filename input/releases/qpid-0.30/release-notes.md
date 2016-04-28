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

# Qpid 0.30 Release Notes

Qpid is a cross-platform AMQP messaging system.  It provides message
brokers written in C++ and Java, and clients for C++, Java, Perl,
Python, Ruby, and .NET.  More about [Qpid]({{site_url}}/index.html).

The full list of changes in the Qpid 0.30 release incorporates
both the issues worked on during the 0.29 development
stream and any final touches made during the 0.30 release
process. A list of these JIRA issues can be found below.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-2305](https://issues.apache.org/jira/browse/QPID-2305) - Remote IP authentication
 - [QPID-3389](https://issues.apache.org/jira/browse/QPID-3389) - Provide more descriptive error text when sasl config. file is malformed
 - [QPID-3978](https://issues.apache.org/jira/browse/QPID-3978) - Broker should remove messages with expired TTL even if they are prefetched by the client
 - [QPID-4123](https://issues.apache.org/jira/browse/QPID-4123) - C++ Broker Acl creates too many run-time rules
 - [QPID-4254](https://issues.apache.org/jira/browse/QPID-4254) -  Java Broker - make Group Database closeable
 - [QPID-4304](https://issues.apache.org/jira/browse/QPID-4304) - [Java Broker] Add queue property to distinguish between persistent queue definition and persistent message storage
 - [QPID-4874](https://issues.apache.org/jira/browse/QPID-4874) - Alternate exchange unable to set from REST
 - [QPID-4947](https://issues.apache.org/jira/browse/QPID-4947) - C++ Broker could use ACL to restrict hosts from which a user may connect
 - [QPID-5409](https://issues.apache.org/jira/browse/QPID-5409) - [Java Broker] Add support for multi-node HA cluster into BDB JE HA message store
 - [QPID-5489](https://issues.apache.org/jira/browse/QPID-5489) - C++ Uuid code needs cleaning up
 - [QPID-5554](https://issues.apache.org/jira/browse/QPID-5554) - [Java Broker Documentation]  Add docbook for environment variables, system properties and logging
 - [QPID-5624](https://issues.apache.org/jira/browse/QPID-5624) - [Java Broker] Remove virtual host configuration xml
 - [QPID-5634](https://issues.apache.org/jira/browse/QPID-5634) - [Java Broker] Allow ACL rules to express virtual host predicates / remove support for AccessPlugins at vhost level
 - [QPID-5639](https://issues.apache.org/jira/browse/QPID-5639) - [Java Broker] Add SCRAM-SHA-1 Sasl support
 - [QPID-5653](https://issues.apache.org/jira/browse/QPID-5653) - [Java Broker] Make message and configuration store stateless
 - [QPID-5665](https://issues.apache.org/jira/browse/QPID-5665) - [Java Broker] VirtualHost implementations should directly implement the model interface
 - [QPID-5683](https://issues.apache.org/jira/browse/QPID-5683) - 1.0 protocol logging is much less complete than 0-10 logging
 - [QPID-5685](https://issues.apache.org/jira/browse/QPID-5685) - Store config version as an attribute of virtualhost within configuration store
 - [QPID-5702](https://issues.apache.org/jira/browse/QPID-5702) - upgrade JUnit version from 3.8.1 to 4.11
 - [QPID-5743](https://issues.apache.org/jira/browse/QPID-5743) - Explain how to use pkg-config to locate proton.
 - [QPID-5744](https://issues.apache.org/jira/browse/QPID-5744) - [Java Broker] Change REST API to adopt URI scheme including major version
 - [QPID-5745](https://issues.apache.org/jira/browse/QPID-5745) - [Java Broker] Close the socket if authentication fails and a client does not send back command "connection.close-ok" as response to a broker "connection.close" during pre-defined period
 - [QPID-5748](https://issues.apache.org/jira/browse/QPID-5748) - [C++ broker] Make Queue::purgeExpired more efficient by calling AbsTime::now() just once
 - [QPID-5752](https://issues.apache.org/jira/browse/QPID-5752) - Maven POM files should have special characters escaped or removed
 - [QPID-5768](https://issues.apache.org/jira/browse/QPID-5768) - Add bind before search capability to SimpleLDAP authentication provider
 - [QPID-5779](https://issues.apache.org/jira/browse/QPID-5779) - JMX plugin's server sockets should set the SO_REUSEADDR socket option
 - [QPID-5800](https://issues.apache.org/jira/browse/QPID-5800) - Refactoring: Introduce MessageStoreProvider interface to improve message/configuration store implementations
 - [QPID-5801](https://issues.apache.org/jira/browse/QPID-5801) - BDB store: remove facade initialisation tasks
 - [QPID-5802](https://issues.apache.org/jira/browse/QPID-5802) - Introduce hierarchy of virtual host types
 - [QPID-5803](https://issues.apache.org/jira/browse/QPID-5803) - Add ability for the virtualhostnode to create a virtualhost using a blueprint supplied by context variable
 - [QPID-5806](https://issues.apache.org/jira/browse/QPID-5806) - It would be useful to allow formally illegal characters into selector identifiers
 - [QPID-5807](https://issues.apache.org/jira/browse/QPID-5807) - Rework the qpid options code so that Boost::program_options is entirely contained in qpidcommon library
 - [QPID-5817](https://issues.apache.org/jira/browse/QPID-5817) - [C++ broker] Improve ACL authorisation of QMF methods and queries
 - [QPID-5836](https://issues.apache.org/jira/browse/QPID-5836) - [Python client] Report error when encountering unrecognized connection option
 - [QPID-5867](https://issues.apache.org/jira/browse/QPID-5867) - [Java Broker] Add functionality to prevent unintended HA node creation and mechanisms to react on intruder HA nodes
 - [QPID-5873](https://issues.apache.org/jira/browse/QPID-5873) - Allow ACL rules to be applied to VirtualHostNode objects
 - [QPID-5878](https://issues.apache.org/jira/browse/QPID-5878) - [Java Broker] Add SCRAM-SHA-256 SASL support
 - [QPID-5879](https://issues.apache.org/jira/browse/QPID-5879) - [Java Broker] Json Configuration Store should take deep copy of ConfiguredObjectRecords
 - [QPID-5891](https://issues.apache.org/jira/browse/QPID-5891) - Add BDB HA operational logging
 - [QPID-5911](https://issues.apache.org/jira/browse/QPID-5911) - Increase default maximum heap size from 1g to 2g
 - [QPID-5930](https://issues.apache.org/jira/browse/QPID-5930) - [Java Broker] Reduce Memory footprint of persistent messages
 - [QPID-5934](https://issues.apache.org/jira/browse/QPID-5934) - [Java Broker] Allow TTL to be overridden on a per-Queue basis
 - [QPID-5935](https://issues.apache.org/jira/browse/QPID-5935) - Web Management UI style refactor to remove html inline styles and standardise via css
 - [QPID-5937](https://issues.apache.org/jira/browse/QPID-5937) - [Java Broker] Add parameters to REST servlet to allow return of actual vs. effective attribute values
 - [QPID-5944](https://issues.apache.org/jira/browse/QPID-5944) - Expose queue clear management operation to the REST API and Web Management Console
 - [QPID-5945](https://issues.apache.org/jira/browse/QPID-5945) - qpid-config to pass integer arguments whenever possible
 - [QPID-5956](https://issues.apache.org/jira/browse/QPID-5956) - [Java Broker] Management UI should allow for ports to be specified as using both TCP and SSL
 - [QPID-5957](https://issues.apache.org/jira/browse/QPID-5957) - Session model object to expose transaction start and update information
 - [QPID-5958](https://issues.apache.org/jira/browse/QPID-5958) - Wire up the Connection#remoteProcessPid attribute to the client's pid obtained during 0-8..0-10 connection negotiation
 - [QPID-5960](https://issues.apache.org/jira/browse/QPID-5960) - ssl_verify_hostname should default to true rather than false
 - [QPID-5962](https://issues.apache.org/jira/browse/QPID-5962) - Prevent two or more BDB virtual host or virtual hosts nodes sharing the same JE environment path
 - [QPID-5965](https://issues.apache.org/jira/browse/QPID-5965) - [Java Broker] Store transient messages to disk (and remove from memory) when in low memory conditions
 - [QPID-5969](https://issues.apache.org/jira/browse/QPID-5969) - [Java Common] Add support of AMQP 0-9-1 field-array type
 - [QPID-5970](https://issues.apache.org/jira/browse/QPID-5970) - [Java Broker] Expose "age of oldest message on queue" to management apis
 - [QPID-5971](https://issues.apache.org/jira/browse/QPID-5971) - [Java Broker] enable long running transaction warnings by default
 - [QPID-5972](https://issues.apache.org/jira/browse/QPID-5972) - Web UI to edit actual attribute values rather than effective values
 - [QPID-5981](https://issues.apache.org/jira/browse/QPID-5981) - [Java Broker] Add ability to set binding arguments in web management console
 - [QPID-5988](https://issues.apache.org/jira/browse/QPID-5988) - Default VHN/VH store paths to path location based on QPID_WORK
 - [QPID-5992](https://issues.apache.org/jira/browse/QPID-5992) - [Java Broker] Allow HTTP management responses to be compressed
 - [QPID-5993](https://issues.apache.org/jira/browse/QPID-5993) - [Java] Address issues identified by Findbugs
 - [QPID-5999](https://issues.apache.org/jira/browse/QPID-5999) - Make the documented selector syntax consistent with the implemented syntax
 - [QPID-6000](https://issues.apache.org/jira/browse/QPID-6000) - [Java Broker] Add ability to automatically compress/decompress message bodies to clients
 - [QPID-6006](https://issues.apache.org/jira/browse/QPID-6006) - UI to expose attribute defaults during create and edit workflows
 - [QPID-6009](https://issues.apache.org/jira/browse/QPID-6009) - [Java Broker] Add meta data to managed attributes to provide information where valid values are restricted
 - [QPID-6010](https://issues.apache.org/jira/browse/QPID-6010) - [Java Tests] Use context value defaulting for setting the protocols in use, rather than a system property 
 - [QPID-6014](https://issues.apache.org/jira/browse/QPID-6014) - [Java] Declare variables as ConcurrentMap not ConcurrentHashMap to avoid issues afetr compiling on Java 8
 - [QPID-6016](https://issues.apache.org/jira/browse/QPID-6016) - Improve Web Management Console error handling
 - [QPID-6017](https://issues.apache.org/jira/browse/QPID-6017) - [Java Broker] Provide a mechanism by which "secure" attributes in the configuration can be encrypted
 - [QPID-6022](https://issues.apache.org/jira/browse/QPID-6022) - [Java] Address more issues brought to light by Findbugs / PMD / etc.
 - [QPID-6027](https://issues.apache.org/jira/browse/QPID-6027) - [Java Broker] Establish a consistent stable order for configured object attributes with Json extracts and stores
 - [QPID-6029](https://issues.apache.org/jira/browse/QPID-6029) - [Java Broker] Allow ConfiguredObjectRecordConverter to resolve Json where the secondary parent is identified by name
 - [QPID-6030](https://issues.apache.org/jira/browse/QPID-6030) - [Java Tests] The mock virtualhost creation in the BrokerTestHelper has not been updated for VirtualHostNodes
 - [QPID-6034](https://issues.apache.org/jira/browse/QPID-6034) - Refactor Port UI to use metadata service rather than hard-coding a list of protocols/transports etc
 - [QPID-6036](https://issues.apache.org/jira/browse/QPID-6036) - [Java Broker] Allow extract of vhost configuration from one broker to another, or the use of virtualhost templates (incl. queues, exchanges and bindings)
 - [QPID-6037](https://issues.apache.org/jira/browse/QPID-6037) - [Java Client] Add basic support for ADDR addresses to the AMQP 0-8/9/9-1 client
 - [QPID-6044](https://issues.apache.org/jira/browse/QPID-6044) - [Java Broker] AMQP 1.0 open containing a hostname that resolves to the machine should resolve to the default vhost if it does not resolve directly

## Bugs fixed

 - [QPID-2969](https://issues.apache.org/jira/browse/QPID-2969) - AMQConnectionFactory is not Serializable
 - [QPID-3650](https://issues.apache.org/jira/browse/QPID-3650) - cast-align errors while building for various architectures
 - [QPID-4299](https://issues.apache.org/jira/browse/QPID-4299) - [Java Broker Web Console] The 2 virtual host aliases with the same names are displayed for virtual host when both http and https are enabled
 - [QPID-4307](https://issues.apache.org/jira/browse/QPID-4307) - [Java Broker] prevent moving/copying messages back onto queues they already exist on
 - [QPID-4429](https://issues.apache.org/jira/browse/QPID-4429) - Java Broker allows frame-size to be negotiated to zero then later fails during message delivery with obscure IllegalArgumentException
 - [QPID-4520](https://issues.apache.org/jira/browse/QPID-4520) - The deletion of autodelete queue requires ACL rights for deleting the queue
 - [QPID-5234](https://issues.apache.org/jira/browse/QPID-5234) -  [Java Broker] HAClusterManagementTest. testRestartNodeWithNewPortNumberWithoutFirstCallingUpdateAddressThrowsAnException seen to fail against IBM JDK
 - [QPID-5400](https://issues.apache.org/jira/browse/QPID-5400) - Deadlock when using amqp-1-0 client to connect to amqp-0-9-1 broker
 - [QPID-5426](https://issues.apache.org/jira/browse/QPID-5426) - PropertiesFileInitialContextFactory only working with properties file on absolute path
 - [QPID-5543](https://issues.apache.org/jira/browse/QPID-5543) - BDBHAMessageStoreManagerMBean is not unregistered when the corresponding virtual host is deleted
 - [QPID-5560](https://issues.apache.org/jira/browse/QPID-5560) - HA tests do not use AMQP 1.0
 - [QPID-5609](https://issues.apache.org/jira/browse/QPID-5609) - QPID fails to compile in C++11 with Boost 1.54 
 - [QPID-5635](https://issues.apache.org/jira/browse/QPID-5635) - [Java Broker] Virtualhost host attribute "minConnectionsPerPartition" for BoneCP connection tool is incorrectly set into array value on creation with Web Management console
 - [QPID-5637](https://issues.apache.org/jira/browse/QPID-5637) - Python client does not reset the Selector singleton when the process id changes.
 - [QPID-5643](https://issues.apache.org/jira/browse/QPID-5643) - "qpid-route route map" does not pass credentials to other brokers in the "route map"
 - [QPID-5647](https://issues.apache.org/jira/browse/QPID-5647) - [Java Broker]  Spurious DLQ is created when DLQ are enabled at Broker (or Virtualhost) level
 - [QPID-5651](https://issues.apache.org/jira/browse/QPID-5651) - [C++ broker] segfault in qpid::linearstore::journal::jdir::clear_dir when declaring durable queue
 - [QPID-5667](https://issues.apache.org/jira/browse/QPID-5667) - C++ broker: QMF subscribe events are not raised with AMQP 1.0
 - [QPID-5684](https://issues.apache.org/jira/browse/QPID-5684) - 1.0 detach on error doesn't specify closed=True
 - [QPID-5687](https://issues.apache.org/jira/browse/QPID-5687) - [Java Broker] The broker will not startup without a config store as the packaged initial config store is incorrect
 - [QPID-5705](https://issues.apache.org/jira/browse/QPID-5705) - [AMQP 1.0] wrong error message when domain already exists
 - [QPID-5706](https://issues.apache.org/jira/browse/QPID-5706) - [AMQP 1.0] can't easily correlate broker initiated inks with their domain
 - [QPID-5707](https://issues.apache.org/jira/browse/QPID-5707) - '#' implies create for queue, but not topic/exchange
 - [QPID-5708](https://issues.apache.org/jira/browse/QPID-5708) - Don't set address 'type' when both exchange and routing key are empty
 - [QPID-5711](https://issues.apache.org/jira/browse/QPID-5711) - HA cannot promote primary if SASL security is enabled.
 - [QPID-5718](https://issues.apache.org/jira/browse/QPID-5718) - Dead code in the HA codebase
 - [QPID-5719](https://issues.apache.org/jira/browse/QPID-5719) - HA becomes unresponsive once any of the brokers are SIGSTOPed
 - [QPID-5720](https://issues.apache.org/jira/browse/QPID-5720) - HA exception raised by the store for durable transactions
 - [QPID-5722](https://issues.apache.org/jira/browse/QPID-5722) - Client connection read can hang forever since socket timeout is 0 
 - [QPID-5725](https://issues.apache.org/jira/browse/QPID-5725) - Message::getProperty() can return result for a property name which is a prefix of the actual name
 - [QPID-5729](https://issues.apache.org/jira/browse/QPID-5729) - [AMQP 1.0] concurrent triggering of auto-created topic causes exception
 - [QPID-5735](https://issues.apache.org/jira/browse/QPID-5735) - The Selector property amqp.redelivered is not computed correctly
 - [QPID-5736](https://issues.apache.org/jira/browse/QPID-5736) - [AMQP 1.0] synchronous send not unblocked by settled message
 - [QPID-5737](https://issues.apache.org/jira/browse/QPID-5737) - [AMQP 1.0] client can hang if session window is moved after last message is sent
 - [QPID-5747](https://issues.apache.org/jira/browse/QPID-5747) -  Federated link ends up in Connecting state forever after connecting to shutting down broker
 - [QPID-5751](https://issues.apache.org/jira/browse/QPID-5751) - File qpid/cpp/RELEASE_NOTES is out of date
 - [QPID-5758](https://issues.apache.org/jira/browse/QPID-5758) - purging expired messages holds up other timer events
 - [QPID-5760](https://issues.apache.org/jira/browse/QPID-5760) - BDBHAVirtualHostNodeRestTest test should call waitForAttributeChange to avoid potential test failure race condition
 - [QPID-5761](https://issues.apache.org/jira/browse/QPID-5761) - Fix BDBHAVirtualHostNodeRestTest test failure caused by premature call to virtual host rest service before opening of virtual host
 - [QPID-5762](https://issues.apache.org/jira/browse/QPID-5762) - Broker won't start from default broker artefact unless JE is added to ./lib
 - [QPID-5765](https://issues.apache.org/jira/browse/QPID-5765) - rerouting messages to non-local filtered queue crashes broker
 - [QPID-5766](https://issues.apache.org/jira/browse/QPID-5766) - Intitialisation of StatisticsCounter objects can lead to NPE when looking to observe their objects via Management API
 - [QPID-5767](https://issues.apache.org/jira/browse/QPID-5767) - [C++ broker][linearstore] broker segfaults when recovering journal file with damaged header
 - [QPID-5771](https://issues.apache.org/jira/browse/QPID-5771) - [Java broker] severed 1.0 connections can prevent clean shutdown
 - [QPID-5773](https://issues.apache.org/jira/browse/QPID-5773) - Qpid Protocol Negotiation Sometime Fails with Python Qpid with SSL
 - [QPID-5776](https://issues.apache.org/jira/browse/QPID-5776) - Unhandled Exception java.lang.IllegalArgumentException causes broker to exit
 - [QPID-5781](https://issues.apache.org/jira/browse/QPID-5781) - [Java broker] exceptions while closing entries in the ConnectionRegistry can prevent clean shutdown
 - [QPID-5782](https://issues.apache.org/jira/browse/QPID-5782) - VirtualHostHouseKeeper tries to check queues that are not yet open leading to NPE in logs
 - [QPID-5783](https://issues.apache.org/jira/browse/QPID-5783) - unnecessary copying of date for message on many queues
 - [QPID-5784](https://issues.apache.org/jira/browse/QPID-5784) - BDB store's CoalescingCommiter can NPE on Broker shutdown
 - [QPID-5785](https://issues.apache.org/jira/browse/QPID-5785) - QueueBindTest.testQueueCanBeReboundOnTopicExchange shows NPE in logs when trying to unbind exchange
 - [QPID-5787](https://issues.apache.org/jira/browse/QPID-5787) - Management can observe a child object before its constructor has completed
 - [QPID-5788](https://issues.apache.org/jira/browse/QPID-5788) - Delay initialization of NSS library until the creation of first SSL connection.
 - [QPID-5791](https://issues.apache.org/jira/browse/QPID-5791) - JsonStore implementation does not synchronise update allowing for race with create/delete
 - [QPID-5792](https://issues.apache.org/jira/browse/QPID-5792) - [AMQP 1.0 JMS Client] Decoding destinations with no attributes can lead to NullPointerException
 - [QPID-5794](https://issues.apache.org/jira/browse/QPID-5794) - example clients (spout.rb, map_sender.rb) are reporting errors
 - [QPID-5795](https://issues.apache.org/jira/browse/QPID-5795) - Closing a connection leaks a ConnectionAdapter object
 - [QPID-5796](https://issues.apache.org/jira/browse/QPID-5796) - ConnectionRegistry may suffer an ArrayIndexOutOfBounds if closed at the same moment as a messaging connection is closed
 - [QPID-5797](https://issues.apache.org/jira/browse/QPID-5797) - [qpid-tools]: inability to call some QMF methods (queueMoveMessages / setLogLevel or so)
 - [QPID-5798](https://issues.apache.org/jira/browse/QPID-5798) - Intermittent failure of FailoverBehaviourTest due to race condition with test
 - [QPID-5804](https://issues.apache.org/jira/browse/QPID-5804) - Selectoy parser incorrectly parses unary '+' operator
 - [QPID-5805](https://issues.apache.org/jira/browse/QPID-5805) - Selector parser shouldn't allow either % or _ character as an ESCAPE character in a LIKE comparison
 - [QPID-5808](https://issues.apache.org/jira/browse/QPID-5808) - Python framer can discard inbound data under some circumstances.
 - [QPID-5814](https://issues.apache.org/jira/browse/QPID-5814) - default to utf9 for strings in Variant::parse()
 - [QPID-5819](https://issues.apache.org/jira/browse/QPID-5819) - Starting a Broker with a virtualhostnode in stopped state causes exception
 - [QPID-5823](https://issues.apache.org/jira/browse/QPID-5823) - Python client should create a node with name starting '#'
 - [QPID-5825](https://issues.apache.org/jira/browse/QPID-5825) - Java broker tries to downgrade to the wrong amqp protocol version
 - [QPID-5828](https://issues.apache.org/jira/browse/QPID-5828) - qpid::Messaging API Sender/Receiver assorted bugs
 - [QPID-5829](https://issues.apache.org/jira/browse/QPID-5829) - Swigged bindings code does not link on windows
 - [QPID-5830](https://issues.apache.org/jira/browse/QPID-5830) - [Python client] Unable to create bindings on already existing broker objects using addressing
 - [QPID-5831](https://issues.apache.org/jira/browse/QPID-5831) - Unexpected internal exception when closing JE Replicated environment
 - [QPID-5835](https://issues.apache.org/jira/browse/QPID-5835) - [C++ broker] Broker recovery forgets auto-delete flag on queues and exchanges
 - [QPID-5839](https://issues.apache.org/jira/browse/QPID-5839) - [C++ broker] Broker does not set lifetime-policy in AMQP1.0 attach performative
 - [QPID-5840](https://issues.apache.org/jira/browse/QPID-5840) - .NET Binding example.server confuses argument indexing
 - [QPID-5841](https://issues.apache.org/jira/browse/QPID-5841) - Allow SSL hostname verification to be disabled
 - [QPID-5845](https://issues.apache.org/jira/browse/QPID-5845) - [AMQP 1.0] auto delete delay specified in pollicy is overridden by link, even when not explicit
 - [QPID-5846](https://issues.apache.org/jira/browse/QPID-5846) - [Java Broker] NPE on BDB HA virtual host recovery from the configuration store
 - [QPID-5848](https://issues.apache.org/jira/browse/QPID-5848) - Update doxygen for connection options
 - [QPID-5849](https://issues.apache.org/jira/browse/QPID-5849) - mechanism not set when auth=no
 - [QPID-5852](https://issues.apache.org/jira/browse/QPID-5852) - [Python client]  connection.opened() returns True after unsuccessful connection 
 - [QPID-5853](https://issues.apache.org/jira/browse/QPID-5853) - [Java Broker] System tests starting spawn broker(s) fail when the project location has spaces
 - [QPID-5857](https://issues.apache.org/jira/browse/QPID-5857) - [Java Broker] Test ConsumerLoggingTest.testSubscriptionCreateQueue sporadically fails
 - [QPID-5858](https://issues.apache.org/jira/browse/QPID-5858) - Session::checkError() throws exceptions of wrong type
 - [QPID-5859](https://issues.apache.org/jira/browse/QPID-5859) - Qpidd only listens to protocols that are already up when it starts
 - [QPID-5860](https://issues.apache.org/jira/browse/QPID-5860) - Sender lock held when invoking on Session
 - [QPID-5865](https://issues.apache.org/jira/browse/QPID-5865) - The client and broker heartbeat code can get confused when the system time changes
 - [QPID-5869](https://issues.apache.org/jira/browse/QPID-5869) - Specifying an invalid ACL file will cause a core dumps when management is disabled
 - [QPID-5874](https://issues.apache.org/jira/browse/QPID-5874) - C++ broker has odd treatment of empty and whitespace only selectors
 - [QPID-5875](https://issues.apache.org/jira/browse/QPID-5875) - [Java Tests] Test VirtualHostRestTest testPutCreateVirtualHostUsingProfileNodeType is failing because ProvidedStore virtual host cannot be used with JSON VHN
 - [QPID-5877](https://issues.apache.org/jira/browse/QPID-5877) - Potential for rejected messages to be resent out of order
 - [QPID-5882](https://issues.apache.org/jira/browse/QPID-5882) - [AMQP 1.0] Authentication failures not handled correctly
 - [QPID-5883](https://issues.apache.org/jira/browse/QPID-5883) - Error message for certain authentication failures is not clear
 - [QPID-5884](https://issues.apache.org/jira/browse/QPID-5884) - NullPointerException when using Base64MD5 file for AMQP 1.0 authentication
 - [QPID-5885](https://issues.apache.org/jira/browse/QPID-5885) - Virtualhostnode to replace real virtualhost with replica virtualhost in the event that the BDB HA goes into detached state
 - [QPID-5886](https://issues.apache.org/jira/browse/QPID-5886) - C++  Broker OutgoingMessage change exposes Completion handle export issue on Windows
 - [QPID-5887](https://issues.apache.org/jira/browse/QPID-5887) - transaction should always be aborted on failover
 - [QPID-5888](https://issues.apache.org/jira/browse/QPID-5888) - transaction should always be aborted on failover
 - [QPID-5890](https://issues.apache.org/jira/browse/QPID-5890) - C++ Broker AclModule.h compiles static code dozens of times
 - [QPID-5892](https://issues.apache.org/jira/browse/QPID-5892) - SSL Sender may spuriously timeout if SSL negotiation fails
 - [QPID-5898](https://issues.apache.org/jira/browse/QPID-5898) - C++ Broker AclHost test fails on systems with no IPv6
 - [QPID-5902](https://issues.apache.org/jira/browse/QPID-5902) - C++ Broker Acl changes break RHEL5 builds
 - [QPID-5903](https://issues.apache.org/jira/browse/QPID-5903) - [Java Broker] Provide mechanism to include strings with backslashes in interpolated json
 - [QPID-5908](https://issues.apache.org/jira/browse/QPID-5908) - [AMQP 1.0] annotations clobber application properties
 - [QPID-5909](https://issues.apache.org/jira/browse/QPID-5909) - [Java Broker] Activation of  BDB HA virtual host fails when changing node role from Master to Replica and back to Master because message store durability is already set
 - [QPID-5910](https://issues.apache.org/jira/browse/QPID-5910) - Throughput regression relative to 0.14
 - [QPID-5912](https://issues.apache.org/jira/browse/QPID-5912) - "Unable to find message with id" exception will result if message is delivered straight through and transport exception occurs during send to consumer
 - [QPID-5915](https://issues.apache.org/jira/browse/QPID-5915) - Stopping virtualhost does not close existing messaging connection
 - [QPID-5917](https://issues.apache.org/jira/browse/QPID-5917) - Scram auth provider - deleting a user from the management ui deletes the auth provider itself
 - [QPID-5918](https://issues.apache.org/jira/browse/QPID-5918) - Prevent file system paths with mixed file separator conventions when running on Windows
 - [QPID-5921](https://issues.apache.org/jira/browse/QPID-5921) - Queue not created if exchange of the same name exists
 - [QPID-5923](https://issues.apache.org/jira/browse/QPID-5923) - delete policy ignores node type
 - [QPID-5926](https://issues.apache.org/jira/browse/QPID-5926) - On restarting a non-HA virtualhost no queues or exchanges are available
 - [QPID-5931](https://issues.apache.org/jira/browse/QPID-5931) - [Java client]  JMSException instead of InvalidDestinationException raised when sending to temporary destination after session closure
 - [QPID-5936](https://issues.apache.org/jira/browse/QPID-5936) - Tests from suite VirtualHostMessageStoreTest are failing on json test profiles when BDB VH is used
 - [QPID-5942](https://issues.apache.org/jira/browse/QPID-5942) - qpid HA cluster may end-up in joining state after HA primary is killed
 - [QPID-5943](https://issues.apache.org/jira/browse/QPID-5943) - [Java Broker] Test BDBHAVirtualHostNodeOperationalLoggingTest.testSetPriority fails sporadically
 - [QPID-5953](https://issues.apache.org/jira/browse/QPID-5953) - Web UI: queue, exchange and connection tables have stopped refreshing automatically
 - [QPID-5954](https://issues.apache.org/jira/browse/QPID-5954) - [Java Broker] UnsupportedOperationException is thrown from GenericJDBCConfigurationStore and GenericJDBCConfigurationStore on trying to evaluate settings for Bone Connection Pool provider
 - [QPID-5959](https://issues.apache.org/jira/browse/QPID-5959) - [AMQP 1.0] can't read content encoding on received message
 - [QPID-5963](https://issues.apache.org/jira/browse/QPID-5963) - Decoding error on outgoing connection over SSL
 - [QPID-5964](https://issues.apache.org/jira/browse/QPID-5964) - C++ Messaging .NET Binding does not do SetContentObject for list or map
 - [QPID-5967](https://issues.apache.org/jira/browse/QPID-5967) - Intruder node detection must be mandatory and should validate all necessary arguments
 - [QPID-5976](https://issues.apache.org/jira/browse/QPID-5976) - File Keystores or truststores created with the incorrect path/password cannot be deleted
 - [QPID-5977](https://issues.apache.org/jira/browse/QPID-5977) - Ports created through the web management ui have no transports
 - [QPID-5978](https://issues.apache.org/jira/browse/QPID-5978) - [Java Client] Failure to negotiate SSL in AMQP 0-8/9/9-1 (e.g. because of an invalid certificate) causes a 30s delay before failure
 - [QPID-5979](https://issues.apache.org/jira/browse/QPID-5979) - Derby/JDBC logs unnecessary 'message not found' at WARN on rollback.
 - [QPID-5980](https://issues.apache.org/jira/browse/QPID-5980) - fix up Javadoc to resolve errors during use of the apache-release profile on Java8
 - [QPID-5982](https://issues.apache.org/jira/browse/QPID-5982) - Stopped node viewed remotely reports stale replication transaction id
 - [QPID-5983](https://issues.apache.org/jira/browse/QPID-5983) - Virtualhostnode displays misleading role whilst in STOPPED state
 - [QPID-5984](https://issues.apache.org/jira/browse/QPID-5984) - Queue tab improvements
 - [QPID-5985](https://issues.apache.org/jira/browse/QPID-5985) - nextReceiver() with IMMEDIATE duration always returns null
 - [QPID-5986](https://issues.apache.org/jira/browse/QPID-5986) - Second column atrributes on virtual host, virtual host node and queue tabs not aligned correctly in IE
 - [QPID-5987](https://issues.apache.org/jira/browse/QPID-5987) - [Java Broker] Make VHN/VH grid consistent with other grids on broker tab in web management console
 - [QPID-5989](https://issues.apache.org/jira/browse/QPID-5989) - Maven build generates duplicate system test class files
 - [QPID-5994](https://issues.apache.org/jira/browse/QPID-5994) - [Java Broker]Test BDBHAVirtualHostNodeOperationalLoggingTest.testRemoteNodeReAttached fails sporadically
 - [QPID-5996](https://issues.apache.org/jira/browse/QPID-5996) - [Java Build] Test coverage reports are not currently working
 - [QPID-5998](https://issues.apache.org/jira/browse/QPID-5998) - [Java Broker] HA operational logging messages should be consistent in use of tense and terse phrasing
 - [QPID-6001](https://issues.apache.org/jira/browse/QPID-6001) - Prevent NPE when publishing using ADDR destination to Broker using AMQP 0-9-1 or lower 
 - [QPID-6002](https://issues.apache.org/jira/browse/QPID-6002) - Server crash with Rabbit MQ C# client
 - [QPID-6003](https://issues.apache.org/jira/browse/QPID-6003) - [Java Broker] Message conversion from 1.0 to 0-10 does not convert AMQP 1.0 types in maps
 - [QPID-6004](https://issues.apache.org/jira/browse/QPID-6004) - [Java AMQP 1.0 JMS Client] Provider better description when attempting to receive from non existant queue
 - [QPID-6005](https://issues.apache.org/jira/browse/QPID-6005) - [Java Broker] Restoring durable AMQP 1.0 messages leads to IndexOutOfBoundsException 
 - [QPID-6011](https://issues.apache.org/jira/browse/QPID-6011) - [Java Broker] Provide mechanism for disabling plugins or specific configured object types 
 - [QPID-6012](https://issues.apache.org/jira/browse/QPID-6012) - HA fix ACL notice log message about accounting for TX queues.
 - [QPID-6018](https://issues.apache.org/jira/browse/QPID-6018) - SimpleAuthenticationProvider offered as option through the Management UI
 - [QPID-6019](https://issues.apache.org/jira/browse/QPID-6019) - Queue added to model even if attribute resolution fails
 - [QPID-6023](https://issues.apache.org/jira/browse/QPID-6023) - [Java Broker] include AMQP 1.0 websocket plugin in broker binary assembly
 - [QPID-6024](https://issues.apache.org/jira/browse/QPID-6024) - Changes to Java Broker Model affected QMF2 plugin
 - [QPID-6031](https://issues.apache.org/jira/browse/QPID-6031) - [JMS 1.0 Client] If attempting to connect over SSL to a server whose certificate is not trusted, ensure a meaningful error message is generated.
 - [QPID-6038](https://issues.apache.org/jira/browse/QPID-6038) - [Java Broker] HTTP Management UI for exchange appears to be lacking "type"
 - [QPID-6048](https://issues.apache.org/jira/browse/QPID-6048) - [Java Broker] BDB HA intruder protection allows cluster to restart with an intruder
 - [QPID-6049](https://issues.apache.org/jira/browse/QPID-6049) - [AMQP 1.0] ssl broken over 1.0
 - [QPID-6050](https://issues.apache.org/jira/browse/QPID-6050) - [JMS AMQP 1.0 client] Setting system property qpid.sync_publish does not have the intended effect
 - [QPID-6052](https://issues.apache.org/jira/browse/QPID-6052) - [Java Client] The client does not correctly set the JMSDestination on a 0-9-1 message in ADDR mode
 - [QPID-6053](https://issues.apache.org/jira/browse/QPID-6053) - [Java AMQP 1.0] Codec fails with exception when passed a byte[] to encode
 - [QPID-6054](https://issues.apache.org/jira/browse/QPID-6054) - [Java Broker] [AMQP 1.0] Java Broker does not honour request for receiver settles first links when it is the receiver
 - [QPID-6066](https://issues.apache.org/jira/browse/QPID-6066) - [0-8..0-9-1] Client AMQSession#getQueueDepth() call fails against pre 0.30 java brokers
 - [QPID-6068](https://issues.apache.org/jira/browse/QPID-6068) - NPE encountered whilst editing JMX_CONNECTOR port
 - [QPID-6069](https://issues.apache.org/jira/browse/QPID-6069) - Does not compile under C++11 on FreeBSD
 - [QPID-6076](https://issues.apache.org/jira/browse/QPID-6076) - [Java Broker] Sending a 0-10 Message with no DeliveryProperties to the default exchange causes NPE
 - [QPID-6077](https://issues.apache.org/jira/browse/QPID-6077) - [Java AMQP 1.0] Receiving messages where sender settles first causes memory leak
 - [QPID-6079](https://issues.apache.org/jira/browse/QPID-6079) - Some python AlternateExchangeTests fail against Java broker (and leave behind an exchange that cannot be deleted)
 - [QPID-6080](https://issues.apache.org/jira/browse/QPID-6080) - Python MessageEchoTests fails against Java Broker
 - [QPID-6089](https://issues.apache.org/jira/browse/QPID-6089) - Qpidd doesn't correctly parse --known-hosts-url option
 - [QPID-6110](https://issues.apache.org/jira/browse/QPID-6110) - Python source distributions are missing license and notice files

## Tasks

 - [QPID-5048](https://issues.apache.org/jira/browse/QPID-5048) - [Java] Implement a Maven 3 build system 
 - [QPID-5664](https://issues.apache.org/jira/browse/QPID-5664) - [Java Broker] correct the broker docbook for max-delivery counting and DLQ to contain the proper client side option value
 - [QPID-5777](https://issues.apache.org/jira/browse/QPID-5777) - [Java] remove stale 'doc' directory
 - [QPID-5821](https://issues.apache.org/jira/browse/QPID-5821) - Remove message store settings from MessageStore/DurableConfigurationStore interfaces
 - [QPID-5822](https://issues.apache.org/jira/browse/QPID-5822) - Replace low-level JDBC/BDB attributes with context variables
 - [QPID-5851](https://issues.apache.org/jira/browse/QPID-5851) - [Java Broker] Add new test profiles for JSON config store and Persistent Message Store
 - [QPID-5913](https://issues.apache.org/jira/browse/QPID-5913) - Remove dependency on crypto-js