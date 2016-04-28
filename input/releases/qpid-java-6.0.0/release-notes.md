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

# Qpid Java 6.0.0 Release Notes

Qpid Java 6.0 release brings with it the following headline changes

* Fully reimplemented AMQP IO layer utilising Java NIO
 * Improved messaging performance - messages kept in direct memory throughout their traversal of the Broker.
 * IO processing now takes place thread pools mean Broker's resource utilisation can be constrained 
 * TCP/IP back pressure from struggling consuming application will cause the Broker to route messages elsewhere until application recovers
 * Improved fairness in message distribution between competing consumers
* End to end encryption
* Logging now fully manageable from the UI/REST API
 * Ability to log to Syslog, Stdout and produce a per virtual host log file.

For more information about this release, including download links and
documentation, see the [release overview](index.html).



## New features and improvements

 - [QPID-6514](https://issues.apache.org/jira/browse/QPID-6514) - Implement plugin that warns and/or disconnects a client if the Qpid Client is too old.
 - [QPID-6525](https://issues.apache.org/jira/browse/QPID-6525) - Allow temporary queue name prefix to be specified by the Broker
 - [QPID-6591](https://issues.apache.org/jira/browse/QPID-6591) - [Java Broker] Add ability to generate a virtualhost specific log
 - [QPID-6630](https://issues.apache.org/jira/browse/QPID-6630) - Add SyslogLogger for Broker and VirtualHost
 - [QPID-6643](https://issues.apache.org/jira/browse/QPID-6643) - Enhance BrokerConsoleLogger to allow logging to stderr
 - [QPID-6732](https://issues.apache.org/jira/browse/QPID-6732) - Change performance test framework to use a rate limiter/hill climbing algorithm to determine a sustainable throughput for a given testcase 
 - [QPID-6756](https://issues.apache.org/jira/browse/QPID-6756) - [Java Client] Allow Client to make connection over a provided Socket
 - [QPID-6843](https://issues.apache.org/jira/browse/QPID-6843) - [Java Broker] Implement Broker side heartbeating in 1.0 AMQP implementation
 - [QPID-2836](https://issues.apache.org/jira/browse/QPID-2836) - [Java Broker] Use slf4j rather than log4j for logging operations
 - [QPID-5818](https://issues.apache.org/jira/browse/QPID-5818) - AMQP model mutating actions should use task executors
 - [QPID-6262](https://issues.apache.org/jira/browse/QPID-6262) - Utilise NIO for AMQP in Java Broker
 - [QPID-6412](https://issues.apache.org/jira/browse/QPID-6412) - Declare variables as ConcurrentMap not ConcurrentHashMap to avoid issues after compiling on Java 8
 - [QPID-6423](https://issues.apache.org/jira/browse/QPID-6423) - [Java Broker] Allow plugin of custom user queue reports using the REST API
 - [QPID-6425](https://issues.apache.org/jira/browse/QPID-6425) - [Java Broker] Allow for local and global name equivalence on virtual hosts
 - [QPID-6428](https://issues.apache.org/jira/browse/QPID-6428) - [Java Broker] Use StoreConfigurationChangeListener to manage storage of all configured objects
 - [QPID-6429](https://issues.apache.org/jira/browse/QPID-6429) - IO refactoring - use single pooled thread to service each connection
 - [QPID-6434](https://issues.apache.org/jira/browse/QPID-6434) - [Java Client] Update existing JMS client documentation for AMQP 0.8/0.9.x to cover the effect of setting maxprefetch to 0
 - [QPID-6436](https://issues.apache.org/jira/browse/QPID-6436) - [Java Broker] Move ACL functionality scattered over the configured objects into SecurityManager and AbstractConfiguredObjects
 - [QPID-6438](https://issues.apache.org/jira/browse/QPID-6438) - [Java Broker] Extend REST interfaces to result in errors when object already exist on create and when object does not exist on update
 - [QPID-6443](https://issues.apache.org/jira/browse/QPID-6443) - Broker should have a default VHN rather than default VH
 - [QPID-6449](https://issues.apache.org/jira/browse/QPID-6449) - [Java Broker] Change REST interfaces to return 422 status code from create/update requests when provided attribute values are invalid or required attributes are missing
 - [QPID-6450](https://issues.apache.org/jira/browse/QPID-6450) - [Java Broker] Use separate configuration thread for each virtual host node
 - [QPID-6453](https://issues.apache.org/jira/browse/QPID-6453) - [Java Broker] Add documentation Queue attributes for defaultFilters and ensureNondestructiveConsumers
 - [QPID-6454](https://issues.apache.org/jira/browse/QPID-6454) - [Java Broker] Provide mechanism to view REST API interface definition
 - [QPID-6457](https://issues.apache.org/jira/browse/QPID-6457) - [Java Broker] Implement asynchronous commits for Derby/JDBC message stores
 - [QPID-6477](https://issues.apache.org/jira/browse/QPID-6477) - Make 0-10 implementation ignore all received frames except ConnectionCloseOk once ConnectionClose is sent
 - [QPID-6485](https://issues.apache.org/jira/browse/QPID-6485) - Remove superfluous find/get methods from the Broker configured object
 - [QPID-6494](https://issues.apache.org/jira/browse/QPID-6494) - Remove redundant configuration change listener from BrokerAdapter
 - [QPID-6507](https://issues.apache.org/jira/browse/QPID-6507) - Eliminate HelperServlet from web management console
 - [QPID-6512](https://issues.apache.org/jira/browse/QPID-6512) - Exception chaining is handled inconsistently
 - [QPID-6515](https://issues.apache.org/jira/browse/QPID-6515) - Eliminate dependencies that require commons-logging (beanutils and collections)
 - [QPID-6516](https://issues.apache.org/jira/browse/QPID-6516) - Tactically switch Broker from Log4j to Logback
 - [QPID-6522](https://issues.apache.org/jira/browse/QPID-6522) - [Java] Remove dependencies on commons-lang, commons-codec
 - [QPID-6523](https://issues.apache.org/jira/browse/QPID-6523) - [Java] Update dependency on guava library to latest version
 - [QPID-6527](https://issues.apache.org/jira/browse/QPID-6527) - [Java Broker Web management Console] Introduce a management service facade to hide the details of REST communication between console and the broker
 - [QPID-6528](https://issues.apache.org/jira/browse/QPID-6528) - Multiple starving suspended consumers on a single session might hold the reference to old deleted queue entry via QueueContext#_lastSeenEntry causing accumulation of deleted queue entries in Broker memory which can eventually lead to OOM
 - [QPID-6530](https://issues.apache.org/jira/browse/QPID-6530) - Enable connection close from the Web Management UI
 - [QPID-6533](https://issues.apache.org/jira/browse/QPID-6533) - [Java Broker] Store logging configuration within broker config
 - [QPID-6534](https://issues.apache.org/jira/browse/QPID-6534) - [Java Client] Add a pooled connection factory
 - [QPID-6538](https://issues.apache.org/jira/browse/QPID-6538) - [Java Broker] Allow TrustStores to be used to distribute public keys to clients
 - [QPID-6540](https://issues.apache.org/jira/browse/QPID-6540) - Add ability to disable one or more of an authentication provider's mechanisms
 - [QPID-6542](https://issues.apache.org/jira/browse/QPID-6542) - [Java Broker] Add additional logging when errors occur during management actions
 - [QPID-6543](https://issues.apache.org/jira/browse/QPID-6543) - Coalesce multi attribute updates into single store write
 - [QPID-6546](https://issues.apache.org/jira/browse/QPID-6546) - EXH-1003 Message should put quotes around the exchange name and routing key
 - [QPID-6552](https://issues.apache.org/jira/browse/QPID-6552) - [Java Client] Allow client to use certificate/key files as an alternative to JKS files for keystores/truststores
 - [QPID-6569](https://issues.apache.org/jira/browse/QPID-6569) - Begin capturing logback logging events at startup and replay those events once the BrokerLoggers are ready
 - [QPID-6573](https://issues.apache.org/jira/browse/QPID-6573) - Add broker connection close guard to protect against a client that does not respond to the connection close command in a timely manner
 - [QPID-6575](https://issues.apache.org/jira/browse/QPID-6575) - Log subscription state change message (SUB-1003) only when a subscription has been suspended for an unusally long period of time
 - [QPID-6576](https://issues.apache.org/jira/browse/QPID-6576) - [Java Client] Provide easy-to-use mechanism for end-to-end encryption of messages
 - [QPID-6578](https://issues.apache.org/jira/browse/QPID-6578) - [Java Broker] Add the ability for logging filters to be added/removed/changed dynamically
 - [QPID-6579](https://issues.apache.org/jira/browse/QPID-6579) - [Java Broker] Add the ability to dynamically add and remove broker loggers
 - [QPID-6580](https://issues.apache.org/jira/browse/QPID-6580) - [Java Broker] Improve fairness between connections (limit the amount of bytes read per thread before yielding)
 - [QPID-6581](https://issues.apache.org/jira/browse/QPID-6581) - [Java Broker] The binding of the rest servlet to model objects should use meta data
 - [QPID-6582](https://issues.apache.org/jira/browse/QPID-6582) - Implement fairness amongst session/consumer on a single connection
 - [QPID-6584](https://issues.apache.org/jira/browse/QPID-6584) - Properly clean up after tests
 - [QPID-6585](https://issues.apache.org/jira/browse/QPID-6585) - [Java Broker] Allow omission of SASL layer for AMQP 1.0 where anonymous or external auth is desired
 - [QPID-6586](https://issues.apache.org/jira/browse/QPID-6586) - [Java Broker] Allow configured objects to define 'ManagedOperations' and expose these through the REST api
 - [QPID-6589](https://issues.apache.org/jira/browse/QPID-6589) - [Java Broker] Use separate io thread pools for each virtual host
 - [QPID-6594](https://issues.apache.org/jira/browse/QPID-6594) - [Java Broker] Remove ConnectionRegistry and move responsibility to the VirtualHost
 - [QPID-6595](https://issues.apache.org/jira/browse/QPID-6595) - Allow ConfiguredObject context variables to be resolved in terms of their ancestor's attributes
 - [QPID-6597](https://issues.apache.org/jira/browse/QPID-6597) - [Java Broker] Port / Connection remodelling
 - [QPID-6598](https://issues.apache.org/jira/browse/QPID-6598) - [Java Broker] Allow configuration encryption provider to be updated dynamically
 - [QPID-6600](https://issues.apache.org/jira/browse/QPID-6600) - [Java] Refactor and remove unnecessary interfaces/dependencies
 - [QPID-6601](https://issues.apache.org/jira/browse/QPID-6601) - CHN messages 1002/1004 are logged for every receive call if prefetch zero is used
 - [QPID-6603](https://issues.apache.org/jira/browse/QPID-6603) - Allow model to express that an attribute is immutable
 - [QPID-6604](https://issues.apache.org/jira/browse/QPID-6604) - [Java Broker] Add new keystore type which generates a self signed certificate on first use
 - [QPID-6605](https://issues.apache.org/jira/browse/QPID-6605) - [Java Broker] Add new TrustStore type which trusts the certificate from a given URL
 - [QPID-6606](https://issues.apache.org/jira/browse/QPID-6606) - Document the Java Broker's AuthenticationProviders' behaviour regarding authentication mechanisms
 - [QPID-6609](https://issues.apache.org/jira/browse/QPID-6609) - [Java Broker] Add into Web Management Console UI to add/edit/delete loggers and filters
 - [QPID-6612](https://issues.apache.org/jira/browse/QPID-6612) - [Java Broker] Refactor Connection(Adapter), ProtocolEngine and AMQConnectionModel
 - [QPID-6613](https://issues.apache.org/jira/browse/QPID-6613) - Simplify creation of per-test log file using Logback's SiftAppender
 - [QPID-6614](https://issues.apache.org/jira/browse/QPID-6614) - [Java Broker] Make BrokerFileLogger implementation expose content of the current file and the names/content of any previously rolled files
 - [QPID-6616](https://issues.apache.org/jira/browse/QPID-6616) - Rename TypedContent into Content, introduce ContentHeader annotation to mark methods returning values for content headers and move responsibility to write content to the implementations
 - [QPID-6618](https://issues.apache.org/jira/browse/QPID-6618) - Allow on-line access to the log cached by BrokerMemoryLogger
 - [QPID-6620](https://issues.apache.org/jira/browse/QPID-6620) - [Java Broker] Restore the behaviour of the if(LOGGER.isDebugEnabled()) idiom (but restrict its use)
 - [QPID-6622](https://issues.apache.org/jira/browse/QPID-6622) - [Java Broker] Add statistics to Broker/VhostLoggers to count the number of errors/warnings logged
 - [QPID-6623](https://issues.apache.org/jira/browse/QPID-6623) - [Java Broker] Log a warning before creating a new configuration secret key file
 - [QPID-6624](https://issues.apache.org/jira/browse/QPID-6624) - [Java Broker] If a port does not support the default protocol reply, it should not error but revert to sending the highest supported version
 - [QPID-6626](https://issues.apache.org/jira/browse/QPID-6626) - [Java Broker] Provide a mechanism for the REST API to communicate which versions are supported
 - [QPID-6627](https://issues.apache.org/jira/browse/QPID-6627) - [Java Broker] REST API should respond with 404 NOT FOUND when the path to a requested object contains an object name which does not exist
 - [QPID-6628](https://issues.apache.org/jira/browse/QPID-6628) - [Java Broker] Update dependency on Jackson JSON library from v1.9 to v2.5
 - [QPID-6629](https://issues.apache.org/jira/browse/QPID-6629) - [Java] Remove all deprecated constants from the public API
 - [QPID-6631](https://issues.apache.org/jira/browse/QPID-6631) - [Java Broker] Add option to fail the Broker if logging fails
 - [QPID-6632](https://issues.apache.org/jira/browse/QPID-6632) - [Java] Refactor AMQException to split out exceptions which carry a protocol error constant 
 - [QPID-6635](https://issues.apache.org/jira/browse/QPID-6635) - Improve JMS Client functionality around Container JNDI integration
 - [QPID-6636](https://issues.apache.org/jira/browse/QPID-6636) - Prevent possibility of malicious manipulation of the content-disposition header
 - [QPID-6637](https://issues.apache.org/jira/browse/QPID-6637) - Replace gson dependency with jackson in perf test framework
 - [QPID-6638](https://issues.apache.org/jira/browse/QPID-6638) - Logging UI improvements
 - [QPID-6642](https://issues.apache.org/jira/browse/QPID-6642) - Improve Logging robustness
 - [QPID-6644](https://issues.apache.org/jira/browse/QPID-6644) - Add operational logging for creation/deletion of several objects
 - [QPID-6646](https://issues.apache.org/jira/browse/QPID-6646) - [Java Broker] Add meta data on ManagedStatistics
 - [QPID-6652](https://issues.apache.org/jira/browse/QPID-6652) - [Java Broker] Make remaining REST service calls to be model based operations
 - [QPID-6655](https://issues.apache.org/jira/browse/QPID-6655) - Refactor slow authentication detection to use a Ticker
 - [QPID-6657](https://issues.apache.org/jira/browse/QPID-6657) - Add operational message to record a operator initiated connection close
 - [QPID-6658](https://issues.apache.org/jira/browse/QPID-6658) - Add derived attribute protocol to Connection model object
 - [QPID-6662](https://issues.apache.org/jira/browse/QPID-6662) - Use direct byte buffers
 - [QPID-6663](https://issues.apache.org/jira/browse/QPID-6663) - Stop using system property amqj.protocol.logging.level to control clients logging [0-8..0-91]
 - [QPID-6692](https://issues.apache.org/jira/browse/QPID-6692) - Minor corrections to the Java Broker and JMS client documentation
 - [QPID-6695](https://issues.apache.org/jira/browse/QPID-6695) - Make model tasks have useful toStrings so that task submit/completion debug logs are useful
 - [QPID-6697](https://issues.apache.org/jira/browse/QPID-6697) - Give IO thread pools a minimum/maximum size and provide advice to user to help them select sensible values
 - [QPID-6705](https://issues.apache.org/jira/browse/QPID-6705) - Add logging to RestServlet to report URL, method and user of each REST call (at debug)
 - [QPID-6706](https://issues.apache.org/jira/browse/QPID-6706) - PropertiesFileInitialContextFactory should accept PROVIDER_URLS with schemes other than file:
 - [QPID-6715](https://issues.apache.org/jira/browse/QPID-6715) - Model to be versioned by major Qpid release (x.y)
 - [QPID-6716](https://issues.apache.org/jira/browse/QPID-6716) - Rename LoggerFilter to LogInclusionRule
 - [QPID-6721](https://issues.apache.org/jira/browse/QPID-6721) - Produce operation log message for unrecognised AMQP protocol initiations
 - [QPID-6728](https://issues.apache.org/jira/browse/QPID-6728) - Upgrade SLF4J dependency from 1.6 to 1.7
 - [QPID-6734](https://issues.apache.org/jira/browse/QPID-6734) - [Java Broker] [BDB Store] Correctly set cache mode for BDB store to not needlessly store message data
 - [QPID-6736](https://issues.apache.org/jira/browse/QPID-6736) - Rewrite 0-8..0-91 connection / session units tests
 - [QPID-6737](https://issues.apache.org/jira/browse/QPID-6737) - Allow message auth to be enabled from context variable
 - [QPID-6739](https://issues.apache.org/jira/browse/QPID-6739) - Allow setting and overriding Qpid client version suffix in qpid-common.properties
 - [QPID-6745](https://issues.apache.org/jira/browse/QPID-6745) - Upgrade Jetty dependency to 8.1.17.v20150415
 - [QPID-6746](https://issues.apache.org/jira/browse/QPID-6746) - Default direct memory settings in Java Broker's start scripts
 - [QPID-6747](https://issues.apache.org/jira/browse/QPID-6747) - Change BRK-1011 operation log message to log direct memory too
 - [QPID-6749](https://issues.apache.org/jira/browse/QPID-6749) - [Java Broker] [BDB Store] Log to slf4j loggers with same name as intended jul logger
 - [QPID-6750](https://issues.apache.org/jira/browse/QPID-6750) - [Java Broker] Use Guava ListenableFuture rather than invent our own future class for store interaction
 - [QPID-6760](https://issues.apache.org/jira/browse/QPID-6760) - Make connection metadata provide useful provider version information
 - [QPID-6761](https://issues.apache.org/jira/browse/QPID-6761) - Broken pipe in http management results in alerting error messages in the logs
 - [QPID-6763](https://issues.apache.org/jira/browse/QPID-6763) - Better representation of errors on login screen of WebManagement
 - [QPID-6777](https://issues.apache.org/jira/browse/QPID-6777) - [Java] Change parent pom for qpid-java-build to apache-parent
 - [QPID-6781](https://issues.apache.org/jira/browse/QPID-6781) - Replace use of Subject#doAs with calls to AccessController#doPrivileged and cache AccessControlContext
 - [QPID-6785](https://issues.apache.org/jira/browse/QPID-6785) - Improve performance of QpidLoggerTurboFilter
 - [QPID-6787](https://issues.apache.org/jira/browse/QPID-6787) - Prevent unnecessary buffer copies/buffer allocations when storing metadata (0-8..0-91)
 - [QPID-6789](https://issues.apache.org/jira/browse/QPID-6789) - [Java Broker] Avoid waking up the selector when there is no need to do so
 - [QPID-6792](https://issues.apache.org/jira/browse/QPID-6792) - Enqueue path should report flow to disk state change too
 - [QPID-6794](https://issues.apache.org/jira/browse/QPID-6794) - [Java Broker] Reduce latency in IO by processing work immediately after select()
 - [QPID-6797](https://issues.apache.org/jira/browse/QPID-6797) - [Java Broker] Minor performance improvements
 - [QPID-6801](https://issues.apache.org/jira/browse/QPID-6801) - Documentation for new Broker's new Logging sub-system
 - [QPID-6802](https://issues.apache.org/jira/browse/QPID-6802) - Document how the Broker uses memory
 - [QPID-6806](https://issues.apache.org/jira/browse/QPID-6806) - Remove configuration for minimum thread pool size for port/virtualhost
 - [QPID-6807](https://issues.apache.org/jira/browse/QPID-6807) - Add ability to configure the number of selectors for AMQP ports and virtualhost
 - [QPID-6816](https://issues.apache.org/jira/browse/QPID-6816) - [Java Broker] Add warning when a port reaches its maximum connection count
 - [QPID-6818](https://issues.apache.org/jira/browse/QPID-6818) - Include ephemeral port number in client logs
 - [QPID-6819](https://issues.apache.org/jira/browse/QPID-6819) - Schedule socket accepts on the thread pool
 - [QPID-6824](https://issues.apache.org/jira/browse/QPID-6824) - Include Broker host/port number in CON-1001 message
 - [QPID-6831](https://issues.apache.org/jira/browse/QPID-6831) - Remove logging from constructor of ConnectionScopedRuntimeException
 - [QPID-6840](https://issues.apache.org/jira/browse/QPID-6840) - [Java Broker] Interleave calls to processPending with attempts to write outstanding data
 - [QPID-6871](https://issues.apache.org/jira/browse/QPID-6871) - Make accepting port socket backlog configurable
 - [QPID-6876](https://issues.apache.org/jira/browse/QPID-6876) - [Java Broker] Provide easy mechanism to download certificate for auto generated keys
 - [QPID-6906](https://issues.apache.org/jira/browse/QPID-6906) - [Java Broker] Allow addition / removal of certificates from ManagedPeerCertificatesTrustStore instances
 - [QPID-6908](https://issues.apache.org/jira/browse/QPID-6908) - Add Broker model operation to shutdown the Broker
 - [QPID-6912](https://issues.apache.org/jira/browse/QPID-6912) - Enumerate model operations in the auto generated apidocs
 - [QPID-6913](https://issues.apache.org/jira/browse/QPID-6913) - Remove JMX from default configuration
 - [QPID-6919](https://issues.apache.org/jira/browse/QPID-6919) - Limit number of acceptors on HttpPort to avoid Jetty WARNing
 - [QPID-4446](https://issues.apache.org/jira/browse/QPID-4446) - Add support for joram JMS tests
 - [QPID-6481](https://issues.apache.org/jira/browse/QPID-6481) - Move java source tree to top-level
 - [QPID-6556](https://issues.apache.org/jira/browse/QPID-6556) - Document how to bind JMS client destinations and connection factories into Tomcat JNDI 
 - [QPID-6742](https://issues.apache.org/jira/browse/QPID-6742) - [Java Broker] Determine heap and direct memory consumption by Java Broker with JDK 1.7/1.8

## Bug Fixed
 - [QPID-3521](https://issues.apache.org/jira/browse/QPID-3521) - failover process for the 0-8 client does not clear the pre-dispatch queue
 - [QPID-3541](https://issues.apache.org/jira/browse/QPID-3541) - Broker closes socket immediately after sending 0-8/0-9/0-9-1 ConnectionClose whilst closing ConnectionRegistry
 - [QPID-5076](https://issues.apache.org/jira/browse/QPID-5076) - [Java Broker] Durable auto-delete queues leave behind orphaned bindings
 - [QPID-5847](https://issues.apache.org/jira/browse/QPID-5847) - Closing 0-8..0-9-1 messaging connection from management occasionally ends with 409 conflict
 - [QPID-5856](https://issues.apache.org/jira/browse/QPID-5856) - Closing 0-10 messaging connection from management leads to spurious exception and timeout
 - [QPID-6094](https://issues.apache.org/jira/browse/QPID-6094) - [0-8..0-9-1] Java Broker can interleave other frames (for the same channel) amongst content frames
 - [QPID-6234](https://issues.apache.org/jira/browse/QPID-6234) - (0-10) Absence of destination argument to the message.subscribe command causes Java Broker to NPE
 - [QPID-6283](https://issues.apache.org/jira/browse/QPID-6283) - FileSystemSpaceChecker can generate java.lang.ArithmeticException / by zero
 - [QPID-6302](https://issues.apache.org/jira/browse/QPID-6302) - InitialContextFactory implementations modify the provided environment
 - [QPID-6373](https://issues.apache.org/jira/browse/QPID-6373) - Change qpid-server.bat default work folder to %APPDATA%\Qpid
 - [QPID-6382](https://issues.apache.org/jira/browse/QPID-6382) - [Java Broker] REST API and Management UI should allow management of objects with '/' in their name
 - [QPID-6385](https://issues.apache.org/jira/browse/QPID-6385) - [Java Broker] documentation of HTTP management API is out of date, using old API gives misleading output
 - [QPID-6442](https://issues.apache.org/jira/browse/QPID-6442) - HA: Connection to virtual host fails if virtual host name not explicitly specified in connection url 
 - [QPID-6446](https://issues.apache.org/jira/browse/QPID-6446) - [Java Broker] Existing virtual host/node derby database is shutdown on attempt to create a virtual host/node with duplicate name
 - [QPID-6451](https://issues.apache.org/jira/browse/QPID-6451) - ProtocolVersionException exception logged at error as Java Client downgrades from 0-10
 - [QPID-6452](https://issues.apache.org/jira/browse/QPID-6452) - [Java Broker] Allow time sensitive filters to be used in queue default filters
 - [QPID-6456](https://issues.apache.org/jira/browse/QPID-6456) - [AMQP 0-8] Java Broker sends wrong connection close ok method identifier (51 rather than 61)
 - [QPID-6458](https://issues.apache.org/jira/browse/QPID-6458) - Clients sends channel flow or message stop even if channel is already closed
 - [QPID-6460](https://issues.apache.org/jira/browse/QPID-6460) - JMS ExceptionListener potentially invoked concurrently 
 - [QPID-6461](https://issues.apache.org/jira/browse/QPID-6461) - Closing a connection in a JMS ExceptionListener logs an InterruptedException
 - [QPID-6464](https://issues.apache.org/jira/browse/QPID-6464) - HA hangs for duration of replica consistency policy timeout if the node changes role whilst recovery is in flight
 - [QPID-6465](https://issues.apache.org/jira/browse/QPID-6465) - ArrayIndexOutOfBoundsException is thrown on attempt to authenticate with MD5AuthenticationProvider
 - [QPID-6466](https://issues.apache.org/jira/browse/QPID-6466) - Client may send duplicate basic.rejects (or messageRelease) during consumer close
 - [QPID-6469](https://issues.apache.org/jira/browse/QPID-6469) - Improve AMQProtocolEngine#exception to guard against an exception whilst trying to send response to client from the method
 - [QPID-6478](https://issues.apache.org/jira/browse/QPID-6478) - [Java Broker] The state of newly created file based user managing authentication providers is set to UNINITIALIZED
 - [QPID-6487](https://issues.apache.org/jira/browse/QPID-6487) - [Java Broker] [AMQP 1.0] Deadlock in Java Broker AMQP 1.0 with new IO model
 - [QPID-6488](https://issues.apache.org/jira/browse/QPID-6488) - [Java Broker] HTTP management may use wrong authentication provider
 - [QPID-6489](https://issues.apache.org/jira/browse/QPID-6489) - Test FailoverBehaviourTest.testFlowControlFlagResetOnFailover fails because it manages to send more messages than expected before flow is blocked 
 - [QPID-6495](https://issues.apache.org/jira/browse/QPID-6495) - Ensure that closing a 0-10 connection from management releases the protocol layer's session resources too
 - [QPID-6496](https://issues.apache.org/jira/browse/QPID-6496) - PropertiesFileInitialContextFactory logs properties at INFO which may allow a password to be logged in clear
 - [QPID-6497](https://issues.apache.org/jira/browse/QPID-6497) - Web Management Console serves contents of index.html for REST API requests containing double slashes in the REST request URL
 - [QPID-6498](https://issues.apache.org/jira/browse/QPID-6498) - BDB HA VHN on transition from Master to Replica attempts to save VH in Replica configuration store causing ReplicaWriteException
 - [QPID-6502](https://issues.apache.org/jira/browse/QPID-6502) - Close connection in response to a CSRE condition rather than sending an execution exception
 - [QPID-6503](https://issues.apache.org/jira/browse/QPID-6503) - IllegalStateException can be reported on Broker shutdown due to an attempt to submit a configuration task into shutdown executor service
 - [QPID-6506](https://issues.apache.org/jira/browse/QPID-6506) - PropertiesFileInitialContextFactory pollutes system properties with values that may contain passwords
 - [QPID-6508](https://issues.apache.org/jira/browse/QPID-6508) - PropertiesFileInitialContextFactory silences important exceptions and is non-compliant with the InitialContext interface
 - [QPID-6510](https://issues.apache.org/jira/browse/QPID-6510) - [0.8/0.9.x/0.10 JMS Client] An instance initializer in org.apache.qpid.filter.PropertyExpression may cause an indefinite loop in HashMap.put() when instances of PropertyExpression are created from different threads at the same time
 - [QPID-6513](https://issues.apache.org/jira/browse/QPID-6513) - Null Pointer Exception on connection.close() in @PreDestroy
 - [QPID-6531](https://issues.apache.org/jira/browse/QPID-6531) - [Java AMQP 1-0 Client] Move the legacy AMQP 1.0 Java client from the Java tree
 - [QPID-6535](https://issues.apache.org/jira/browse/QPID-6535) - java.lang.OutOfMemoryError: unable to create new native thread
 - [QPID-6536](https://issues.apache.org/jira/browse/QPID-6536) - [Java Broker] UI tabs should inform user when the underlying object disappears i.e. starts to return 404
 - [QPID-6539](https://issues.apache.org/jira/browse/QPID-6539) - [Java Broker] ConcurrentModificationException can occur in StandardEnvironmentFacadeFactory.buildEnvironmentConfiguration on BDB VH start-up causing the ERRORED state of the object
 - [QPID-6541](https://issues.apache.org/jira/browse/QPID-6541) - [Java Broker] In rare cases it is possible for newly arrived messages to be enqueued ahead of recovering messages in asynchronous recovery
 - [QPID-6545](https://issues.apache.org/jira/browse/QPID-6545) - malformed cyrillic strings that passed as TextMessage's property
 - [QPID-6547](https://issues.apache.org/jira/browse/QPID-6547) - [Java Client] Client should not attempt to make explicit bindings against the default exchange
 - [QPID-6550](https://issues.apache.org/jira/browse/QPID-6550) - [Java Broker] BrokerStoreUpgraderAndRecoverer incorrectly adds vhostaliases to non-AMQP ports which do not have protocols
 - [QPID-6555](https://issues.apache.org/jira/browse/QPID-6555) - Unable to create non-durable queues and exchanges from the web management console
 - [QPID-6560](https://issues.apache.org/jira/browse/QPID-6560) - [Java Broker] BDB HA JE environment close on intruder detection might block the execution of VHN children tasks thus causing unnecessary delays in shutdown of ReplicatedEnvironmentFacade executors
 - [QPID-6561](https://issues.apache.org/jira/browse/QPID-6561) - Create VHN/VH dialogue cancel button causes Javascript error
 - [QPID-6562](https://issues.apache.org/jira/browse/QPID-6562) - Test BDBHAVirtualHostNodeRestTest.testMutateStateOfOneNode fails sporadically
 - [QPID-6565](https://issues.apache.org/jira/browse/QPID-6565) - [Java Broker] On startup the broker makes a directory called config.json rather than a file
 - [QPID-6566](https://issues.apache.org/jira/browse/QPID-6566) - [Java Broker] Fix issues highlighted by running Joram JMS tests against AMQP 1.0
 - [QPID-6570](https://issues.apache.org/jira/browse/QPID-6570) - Auto delete exchanges are not deleted automatically after the last binding is removed
 - [QPID-6583](https://issues.apache.org/jira/browse/QPID-6583) - [Java Client] AMQSession_0_10 should use connection task pool rather than a Timer
 - [QPID-6587](https://issues.apache.org/jira/browse/QPID-6587) - Qpid crash when trying to convert a message
 - [QPID-6588](https://issues.apache.org/jira/browse/QPID-6588) - HTTP Management writes JSON responses using the platform's default encoding rather than UTF-8
 - [QPID-6593](https://issues.apache.org/jira/browse/QPID-6593) - [Java Client] Improve BURL validation to detect illegal names such as '/a/b/c/d'
 - [QPID-6596](https://issues.apache.org/jira/browse/QPID-6596) - [Java Broker] Add ability for virtualhost events to be excluded from the Broker log
 - [QPID-6599](https://issues.apache.org/jira/browse/QPID-6599) - Attempting to actively declare a reserved exchange causes existing exchange to be partially removed from the in memory model 
 - [QPID-6607](https://issues.apache.org/jira/browse/QPID-6607) - Messages causing a runtime selector error may halt the broker 
 - [QPID-6608](https://issues.apache.org/jira/browse/QPID-6608) - Unexpected exceptions occurring within virtualhost housekeeping thread are not logged and do not cause the Broker to fail
 - [QPID-6617](https://issues.apache.org/jira/browse/QPID-6617) - Exceptions in handling of GET requests are reported as internal server error (500)
 - [QPID-6619](https://issues.apache.org/jira/browse/QPID-6619) - NPEs when creating consumers / queues
 - [QPID-6621](https://issues.apache.org/jira/browse/QPID-6621) - [Java Broker] Slow performance of Shared Groups message grouping on large queues
 - [QPID-6625](https://issues.apache.org/jira/browse/QPID-6625) - [Java Broker] Wire up the existing JMX logging interface to the new model
 - [QPID-6634](https://issues.apache.org/jira/browse/QPID-6634) - Model may signal state change to listeners even though the state change failed
 - [QPID-6645](https://issues.apache.org/jira/browse/QPID-6645) - VHN/VH add dialogue incorrectly defaults visibility file upload widget
 - [QPID-6647](https://issues.apache.org/jira/browse/QPID-6647) - Thread Leak when Connection is closed while a MessageConsumer is in a receive()
 - [QPID-6649](https://issues.apache.org/jira/browse/QPID-6649) - Client initiated connection close can race with Broker shutdown (or VH mastership change) leading to exception and unclosed socket
 - [QPID-6650](https://issues.apache.org/jira/browse/QPID-6650) - [Java Broker] RMI and JMX ports do not behave sensibly when configured as port 0
 - [QPID-6656](https://issues.apache.org/jira/browse/QPID-6656) - Ensure target size is assigned to newly created queues
 - [QPID-6664](https://issues.apache.org/jira/browse/QPID-6664) - Connection#close may hang awaiting failover to exhaust retries
 - [QPID-6667](https://issues.apache.org/jira/browse/QPID-6667) - [Java Broker] Unusued temporary queues are not deleted on connection disconnect
 - [QPID-6670](https://issues.apache.org/jira/browse/QPID-6670) - Exchange deletion does not await binding deletion leading to possibility of a IllegalStateException : Task executor is not in ACTIVE state
 - [QPID-6671](https://issues.apache.org/jira/browse/QPID-6671) - java.util.NoSuchElementException whilst trying to deregister a connection mbean
 - [QPID-6672](https://issues.apache.org/jira/browse/QPID-6672) - Message dispatching after dispatcher close can cause thread to terminate with IllegalStateException
 - [QPID-6677](https://issues.apache.org/jira/browse/QPID-6677) - Invocation of Connection#stop from MessageListener with 0-10 AMQP client might result in hang of operation
 - [QPID-6678](https://issues.apache.org/jira/browse/QPID-6678) - Deleting an exchange that is referenced as alternate apparently succeeds but marks the exchange as DELETED
 - [QPID-6681](https://issues.apache.org/jira/browse/QPID-6681) - Disallow the changing of an object's type
 - [QPID-6682](https://issues.apache.org/jira/browse/QPID-6682) - [Java Tests] SSLTest and ExternalAuthenticationTest always use AMQP 0-10 no matter which test profile is used
 - [QPID-6683](https://issues.apache.org/jira/browse/QPID-6683) - Jetty thread seemingly spins if many HTTP ports are defined on hosts with large numbers of core
 - [QPID-6684](https://issues.apache.org/jira/browse/QPID-6684) - Asynchronous state change exceptions not passed back to caller
 - [QPID-6685](https://issues.apache.org/jira/browse/QPID-6685) - ServerScopedRuntimeExceptions occurring during the Broker's initial open phase are ignored, 
 - [QPID-6686](https://issues.apache.org/jira/browse/QPID-6686) - NPE is thrown on evaluating BrokerFileLogger#logFiles when BrokerFileLogger is in ERRORED state due to attribute value resolution errors
 - [QPID-6687](https://issues.apache.org/jira/browse/QPID-6687) - NPE is thrown on stop of Broker and VirtualHost FileLoggers when Logger is in ERRORED state due to attribute value resolution errors
 - [QPID-6688](https://issues.apache.org/jira/browse/QPID-6688) - [Java Broker] Add port state check in HTTP and JMX management plugins whilst iterating through ports in order to avoid NPE thrown for Ports in ERRORED state having uninitialized protocols
 - [QPID-6689](https://issues.apache.org/jira/browse/QPID-6689) - [Java Broker] QpidTurboFilter prevents any log messages from being logged until NameAndLevelFilters are activated
 - [QPID-6690](https://issues.apache.org/jira/browse/QPID-6690) - [Java Broker] Errors like NoClassDefFoundError do not interrupt ListenableFuture.get() in ACO#doSync(ListenableFuture)  blocking the configuration thread and hanging the Broker on creation of BDB VHN/VH when JE library is not available in classpath
 - [QPID-6691](https://issues.apache.org/jira/browse/QPID-6691) - If AccessControlProvider is in errored state we should default to DENY
 - [QPID-6694](https://issues.apache.org/jira/browse/QPID-6694) - Ensure that future wiring within async model operations preserves exceptions
 - [QPID-6696](https://issues.apache.org/jira/browse/QPID-6696) - [Java Broker] Newly added durable preferences provider is not persisted into configuration store for children managing authentication providers Base64MD5PasswordFile and PlainPasswordFile
 - [QPID-6701](https://issues.apache.org/jira/browse/QPID-6701) - [Regression btw 0.30 - 0.32] If address doesn't resolve an exception is not thrown
 - [QPID-6704](https://issues.apache.org/jira/browse/QPID-6704) - [Java Broker] Broker fails to start on windows partition mounted with SUBST 
 - [QPID-6707](https://issues.apache.org/jira/browse/QPID-6707) - Kill the Broker on invocation of store mutation operation ending with ServerScopedRuntimeException
 - [QPID-6708](https://issues.apache.org/jira/browse/QPID-6708) - Changing LoggingLevel on an existing filter does not always take immediate effect
 - [QPID-6709](https://issues.apache.org/jira/browse/QPID-6709) - SUB-1001 operation log message for consumers with noLocal/arrivaltime filters contain an object identity
 - [QPID-6710](https://issues.apache.org/jira/browse/QPID-6710) - NPE masks IOException on running out of disk space
 - [QPID-6712](https://issues.apache.org/jira/browse/QPID-6712) - Queue Runner may observe a message after it has been dequeued/deleted
 - [QPID-6713](https://issues.apache.org/jira/browse/QPID-6713) - [Java Broker] A message still being processed by a QueueBrowser or management function should not be removed from the store
 - [QPID-6719](https://issues.apache.org/jira/browse/QPID-6719) - qpid-client.properties not loaded by client
 - [QPID-6720](https://issues.apache.org/jira/browse/QPID-6720) - Replace calls to o.a.q.t.Logger with direct calls to SLF4J
 - [QPID-6723](https://issues.apache.org/jira/browse/QPID-6723) - [Java Broker] Stop caching AMQShortStrings
 - [QPID-6724](https://issues.apache.org/jira/browse/QPID-6724) - Stop writing all usernames within an external password database to the log
 - [QPID-6726](https://issues.apache.org/jira/browse/QPID-6726) - Change flow to disk trigger to consider direct memory occupancy
 - [QPID-6731](https://issues.apache.org/jira/browse/QPID-6731) - HttpManagement operational logging does not log actual port bound when the system-allocated port is used (port=0)
 - [QPID-6733](https://issues.apache.org/jira/browse/QPID-6733) - [Java Broker] Stop swallowing or ignoring ServerScopeRuntimeException thrown in threads of BDB HA executor services
 - [QPID-6735](https://issues.apache.org/jira/browse/QPID-6735) - [Java Broker] Out of memory when consuming messages in very large transaction
 - [QPID-6741](https://issues.apache.org/jira/browse/QPID-6741) - ThreadPoolExecutors used for virtual host IO / port IO do not scale above minimum pool size
 - [QPID-6743](https://issues.apache.org/jira/browse/QPID-6743) - Java client may log a spurious SSLPeerUnverifiedException warning during SSL connection handshake
 - [QPID-6744](https://issues.apache.org/jira/browse/QPID-6744) - Java client 0-8..0-91 sends queue.delete with nowait true but then awaits a reply
 - [QPID-6751](https://issues.apache.org/jira/browse/QPID-6751) - [Java Broker] Set adequate JE cache sizes for multiple JE environments created in Broker BDB virtual host nodes and virtual hosts
 - [QPID-6752](https://issues.apache.org/jira/browse/QPID-6752) - Downgrade 'Average cleaner backlog ..' from ERROR to INFO
 - [QPID-6755](https://issues.apache.org/jira/browse/QPID-6755) - Release tasks for qpid-java-6.0
 - [QPID-6758](https://issues.apache.org/jira/browse/QPID-6758) - Race condition can lead to referenceCount on messages being below zero
 - [QPID-6759](https://issues.apache.org/jira/browse/QPID-6759) - Java client 0-8..0-91 sends exchange.delete but then awaits the wrong response (ExchangeDeclareOk)
 - [QPID-6762](https://issues.apache.org/jira/browse/QPID-6762) - Contrary to the documentation sorted queues put messages without a sorting key at the head of the queue
 - [QPID-6765](https://issues.apache.org/jira/browse/QPID-6765) - [Java Broker] Java Broker leaks instances of org.apache.qpid.server.virtualhost.AbstractSystemMessageSource.Consumer on 0.10 path
 - [QPID-6768](https://issues.apache.org/jira/browse/QPID-6768) - Avoid unnecessary message payload copy during send (0-8...0-91)
 - [QPID-6769](https://issues.apache.org/jira/browse/QPID-6769) - [Java Broker] Excessive number of instances of NonPooledByteBufferRef is created in destruction tests to exercise memory consumption by persistent messages breaching the limits of max heap and direct memory to start flowing to disk
 - [QPID-6772](https://issues.apache.org/jira/browse/QPID-6772) - [Java] logback license is reported as incompatible
 - [QPID-6775](https://issues.apache.org/jira/browse/QPID-6775) - [Java Broker] Metadata are being cleaned and immediately reloaded from disk on meesage enqueuing when flow to disk is enabled
 - [QPID-6780](https://issues.apache.org/jira/browse/QPID-6780) - Sessions are not closed when connection drops
 - [QPID-6782](https://issues.apache.org/jira/browse/QPID-6782) - [Java Broker] AbstractVirtualHost does not block existing connections when disk usage is over maximum allowed value
 - [QPID-6784](https://issues.apache.org/jira/browse/QPID-6784) - Client may send frames that are too large and broker does wrong frame size validation for AMQP 0-91
 - [QPID-6786](https://issues.apache.org/jira/browse/QPID-6786) - (0-10) ServerAssembler fails with IndexOutOfBoundsException on receipt of message with large headers
 - [QPID-6788](https://issues.apache.org/jira/browse/QPID-6788) - NetworkConnection can occupy large amounts of direct memory causing the broker to go OutOfMemory
 - [QPID-6791](https://issues.apache.org/jira/browse/QPID-6791) - Unsafe usage of WeakHashMap in ACL module can cause the broker to dead lock
 - [QPID-6795](https://issues.apache.org/jira/browse/QPID-6795) - Virtual host should close thread pools before transitioning to error state
 - [QPID-6798](https://issues.apache.org/jira/browse/QPID-6798) - Broker decompressing a message on behalf of a client who cannot produces stack trace to Broker log
 - [QPID-6800](https://issues.apache.org/jira/browse/QPID-6800) - Use cached direct buffers for message compression/decompression
 - [QPID-6810](https://issues.apache.org/jira/browse/QPID-6810) - [Java Broker] WebSockets plugin needs to work with new IO threading model
 - [QPID-6813](https://issues.apache.org/jira/browse/QPID-6813) - Consumer tasks may run on the Broker thread leading to deadlock
 - [QPID-6814](https://issues.apache.org/jira/browse/QPID-6814) - IO Selector deadlock
 - [QPID-6820](https://issues.apache.org/jira/browse/QPID-6820) - [Java Broker] State change listeners on non-acquired messages do not get removed when consumers are closed
 - [QPID-6823](https://issues.apache.org/jira/browse/QPID-6823) - [Java Broker] On failures to open ACL rules file the cause exception is not chained to the thrown IllegalConfigurationException making it is difficult to understand what exactly caused the failure to open ACL file
 - [QPID-6828](https://issues.apache.org/jira/browse/QPID-6828) - [Java Broker] Consumers on SystemMessageSources are not notified on suspension of message assignment
 - [QPID-6829](https://issues.apache.org/jira/browse/QPID-6829) - [Java Broker] SystemMessageSources$Consumer needs to implement flush()
 - [QPID-6830](https://issues.apache.org/jira/browse/QPID-6830) - Ensure QueueConsumerImpl#_stateListener is published safely between threads
 - [QPID-6832](https://issues.apache.org/jira/browse/QPID-6832) - [Java Broker] AMQP 1.0 implementation leaks direct memory 
 - [QPID-6833](https://issues.apache.org/jira/browse/QPID-6833) - [Java Broker] Operational log message  SUB-1003  is not logged by SuspendedConsumerLoggingTicker causing failures of ConsumerLoggingTest#testSubscriptionSuspend
 - [QPID-6841](https://issues.apache.org/jira/browse/QPID-6841) - [Java Broker] Calling recover on a subscription to a Sorted or Priority Queue may cause messages to become stuck
 - [QPID-6844](https://issues.apache.org/jira/browse/QPID-6844) - [Java Broker] [AMQP1.0] Link credit not being allocated correctly leading to messages not being sent
 - [QPID-6845](https://issues.apache.org/jira/browse/QPID-6845) - [Java Broker] [AMQP1.0] Abruptly closing a connection leaves orphaned consumers and acquired messages
 - [QPID-6846](https://issues.apache.org/jira/browse/QPID-6846) - [Java Broker] IdleTimeoutTicker causes I/O network thread spinning on AMQP 1.0 due to unimplemented heartbeating
 - [QPID-6850](https://issues.apache.org/jira/browse/QPID-6850) - AMQP 1.0 connections remain associated with virtualhost after connection close.
 - [QPID-6851](https://issues.apache.org/jira/browse/QPID-6851) - AMQP 1.0 TemporaryQueues not deleted on connection close
 - [QPID-6853](https://issues.apache.org/jira/browse/QPID-6853) - [Java Broker] Messages in consumerTarget _queue may be deleted before they are sent
 - [QPID-6854](https://issues.apache.org/jira/browse/QPID-6854) - Fix screen label for Broker#connection_heartBeatDelay attribute (wrong time units)
 - [QPID-6859](https://issues.apache.org/jira/browse/QPID-6859) - [Java Broker] Web Management console Plain SASL mechanism 'response' request is sent as JSON instead of being encoded as 'application/x-www-form-urlencoded'
 - [QPID-6860](https://issues.apache.org/jira/browse/QPID-6860) - [Java Broker] Web Management Console for Simple LDAP Authentication provider is not rendered properly
 - [QPID-6861](https://issues.apache.org/jira/browse/QPID-6861) - Avoid unsafe read of AMQPConnection_0_8#_channelMap
 - [QPID-6872](https://issues.apache.org/jira/browse/QPID-6872) - [Java Broker] Configured Objects with the same names under one parent can be created via management interfaces
 - [QPID-6873](https://issues.apache.org/jira/browse/QPID-6873) - [Java Broker] Creation of SiteSpecificTrustStore with invalid site url results in broken REST interfaces due to NPE thrown on generation of REST data
 - [QPID-6877](https://issues.apache.org/jira/browse/QPID-6877) - [Java Broker] In Web Management Console in Edit Broker Dialog the config encryption field is not set to 'None' when config encryption is not used and prevents Edit form from submitting unless explicitly selected
 - [QPID-6878](https://issues.apache.org/jira/browse/QPID-6878) - [Java Broker] In web Management Console on BDB VHN tab Edit button is not enabled after VHN stop
 - [QPID-6884](https://issues.apache.org/jira/browse/QPID-6884) - [Java Broker] Adding a BrokerLogger with a relative path without a slash fails
 - [QPID-6885](https://issues.apache.org/jira/browse/QPID-6885) - [Java Broker] When adding a ConsoleLogger one must explicitly set the target stream
 - [QPID-6887](https://issues.apache.org/jira/browse/QPID-6887) - [Java Broker] The UI for adding BrokerLogbackSocket is broken
 - [QPID-6889](https://issues.apache.org/jira/browse/QPID-6889) - [Java Broker] Entering relative path without parent for JSON VHN store in web UI fails
 - [QPID-6898](https://issues.apache.org/jira/browse/QPID-6898) - [Java Broker] Entering relative path for DERBY VHN in web UI fails
 - [QPID-6899](https://issues.apache.org/jira/browse/QPID-6899) - [Java Broker] Adding AuthenticationProvider with FileSystemPreferences with relative path partially fails
 - [QPID-6900](https://issues.apache.org/jira/browse/QPID-6900) - Address unsafe publication issue in AMQConnection_0_8
 - [QPID-6902](https://issues.apache.org/jira/browse/QPID-6902) - [Java Broker] In web UI adding a GroupProvider with relative path without parent fails
 - [QPID-6903](https://issues.apache.org/jira/browse/QPID-6903) - [Java Broker] In web UI for queues the label for the alerting threshold for max queue size is wrong
 - [QPID-6904](https://issues.apache.org/jira/browse/QPID-6904) - [Java Broker] In web UI in the copy message dialogue the button says 'move message'
 - [QPID-6909](https://issues.apache.org/jira/browse/QPID-6909) - Durability model attribute should be immutable in all cases
 - [QPID-6911](https://issues.apache.org/jira/browse/QPID-6911) - Broker is missing from the apidocs
 - [QPID-6914](https://issues.apache.org/jira/browse/QPID-6914) - [Java Broker] Setting a relative path without a parent for encrypter.key.file leads to NPE
 - [QPID-6918](https://issues.apache.org/jira/browse/QPID-6918) - Creating AutoGeneratedSelfSigned keystore fails on JDK 1.8
 - [QPID-6922](https://issues.apache.org/jira/browse/QPID-6922) - Trying to edit shipped authentication provider 'passwordFile' leads to 404
 - [QPID-6923](https://issues.apache.org/jira/browse/QPID-6923) - Make AutoGeneratedSelfSigned default to SHA256WithRSA rather than SHA1WithRSA to help users comply with SHA-1 sunset
 - [QPID-6926](https://issues.apache.org/jira/browse/QPID-6926) - [Java Broker] [AMQP 1.0] Detach sent after session ended
 - [QPID-6928](https://issues.apache.org/jira/browse/QPID-6928) - [Java Broker] [AMQP 1.0] Broker should not NPE if target address is null

