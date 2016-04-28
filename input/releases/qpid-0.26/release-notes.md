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

# Qpid 0.26 Release Notes

Qpid is a cross-platform AMQP messaging system.  It provides message
brokers written in C++ and Java, and clients for C++, Java, Perl,
Python, Ruby, and .NET.  More about [Qpid]({{site_url}}/index.html).

The full list of changes in the Qpid 0.26 release incorporates
both the issues worked on during the 0.25 development
stream and any final touches made during the 0.26 release
process. A list of these JIRA issues can be found below.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-4265](https://issues.apache.org/jira/browse/QPID-4265) - It's hardly possible to close a receiver that waits for incoming message with Duration::FOREVER
 - [QPID-4463](https://issues.apache.org/jira/browse/QPID-4463) - SimpleLDAPAuthenticationManager should accept truststore and truststore password configuration
 - [QPID-4534](https://issues.apache.org/jira/browse/QPID-4534) - Unify client side heartbeat system properties/broker url options 
 - [QPID-4640](https://issues.apache.org/jira/browse/QPID-4640) - Deprecate autoconf/automake build system.
 - [QPID-4927](https://issues.apache.org/jira/browse/QPID-4927) - C++ CMake tests need to use valgrind the same way that the autotools build does
 - [QPID-4940](https://issues.apache.org/jira/browse/QPID-4940) - Remove unmaintained/obsolete QMF code
 - [QPID-4941](https://issues.apache.org/jira/browse/QPID-4941) - Remove obsolete/deprecated C++ example code
 - [QPID-4942](https://issues.apache.org/jira/browse/QPID-4942) - We should only export/install headers files for current C++ APIs
 - [QPID-4952](https://issues.apache.org/jira/browse/QPID-4952) - Rename the Python swig bindings to qpid_messaging
 - [QPID-5003](https://issues.apache.org/jira/browse/QPID-5003) - set expiration time on durable subscription queues
 - [QPID-5012](https://issues.apache.org/jira/browse/QPID-5012) - [Java Broker] update optional BDB store to use version 5.0.84 of BDB JE 
 - [QPID-5037](https://issues.apache.org/jira/browse/QPID-5037) - [Java Broker- Web Management Console] Move log viewer into a separate tab and add abilities to download logs and filter log entries in the logs table
 - [QPID-5079](https://issues.apache.org/jira/browse/QPID-5079) - Only export necessary symbols from the supported client API libraries
 - [QPID-5087](https://issues.apache.org/jira/browse/QPID-5087) - [Java Broker] Allow the use of separate message stores and configuration stores for the (nonHA) virtualhost
 - [QPID-5111](https://issues.apache.org/jira/browse/QPID-5111) - Improve handling of library dependencies in cmake build
 - [QPID-5112](https://issues.apache.org/jira/browse/QPID-5112) - Don't bother to look for libraries on windows that are never present there
 - [QPID-5133](https://issues.apache.org/jira/browse/QPID-5133) - Add an option to the spout examples to enable durable messages
 - [QPID-5138](https://issues.apache.org/jira/browse/QPID-5138) - [Java Broker] Implement web management console preferences
 - [QPID-5144](https://issues.apache.org/jira/browse/QPID-5144) - Include the Python examples with the python-qpid_messaging sources
 - [QPID-5158](https://issues.apache.org/jira/browse/QPID-5158) - extract the code generation process in the common and broker modules into dedicated build files
 - [QPID-5159](https://issues.apache.org/jira/browse/QPID-5159) - [Java Broker] create broker-core module
 - [QPID-5160](https://issues.apache.org/jira/browse/QPID-5160) - [Java] add a qpid-test-utils module instead of making tests in every module rely on the tests dir from the common module
 - [QPID-5166](https://issues.apache.org/jira/browse/QPID-5166) - Lazily create dispatcher thread in JMS Session implementation
 - [QPID-5167](https://issues.apache.org/jira/browse/QPID-5167) - Allow sync_publish flag to be controlled from the ConnectionFactory connection string
 - [QPID-5178](https://issues.apache.org/jira/browse/QPID-5178) - Flow detail from Rejected outcome though to MessageRejectedException
 - [QPID-5199](https://issues.apache.org/jira/browse/QPID-5199) - include headers when calculating message size
 - [QPID-5202](https://issues.apache.org/jira/browse/QPID-5202) - [Java Broker] Improve exchange documentation in java broker docbook
 - [QPID-5222](https://issues.apache.org/jira/browse/QPID-5222) - [Java Broker] update optional BDB store to use version 5.0.97 of BDB JE 
 - [QPID-5223](https://issues.apache.org/jira/browse/QPID-5223) - [Java 0-x Client] add system property to set message expiration header as raw TTL value for users of RabbitMQ
 - [QPID-5237](https://issues.apache.org/jira/browse/QPID-5237) - Self-contained C++ source distribution
 - [QPID-5245](https://issues.apache.org/jira/browse/QPID-5245) - [AMQP 1.0 JMS] Provide additional information through exceptions
 - [QPID-5260](https://issues.apache.org/jira/browse/QPID-5260) - Miscellaneous CMake Improvements
 - [QPID-5261](https://issues.apache.org/jira/browse/QPID-5261) - Install DLLs and import libs to more usual place for windows SDK
 - [QPID-5263](https://issues.apache.org/jira/browse/QPID-5263) - Fix installed boost files on windows
 - [QPID-5274](https://issues.apache.org/jira/browse/QPID-5274) - CMake in cpp/src is cluttered with windows-specific functions
 - [QPID-5277](https://issues.apache.org/jira/browse/QPID-5277) - Add ability create, delete and list objects of arbitrary types
 - [QPID-5306](https://issues.apache.org/jira/browse/QPID-5306) - Improve cmake testing structure
 - [QPID-5308](https://issues.apache.org/jira/browse/QPID-5308) - Make C++ test results reports output XML
 - [QPID-5316](https://issues.apache.org/jira/browse/QPID-5316) - add paging-dir option to control location of page file for paged queues
 - [QPID-5325](https://issues.apache.org/jira/browse/QPID-5325) - [Java Broker] Add ability to save web management console open tabs in user preferences

## Bugs fixed

 - [QPID-4582](https://issues.apache.org/jira/browse/QPID-4582) - C++ Broker legacystore self tests fail
 - [QPID-4670](https://issues.apache.org/jira/browse/QPID-4670) - [AMQP 1.0] dynamic flag on source/target is not handled correctly
 - [QPID-4708](https://issues.apache.org/jira/browse/QPID-4708) - [AMQP 1.0] failover support (i.e. reconnect=true)
 - [QPID-4711](https://issues.apache.org/jira/browse/QPID-4711) - [AMQP 1.0] translation of structured content between 0-10 and 1.0 encoding
 - [QPID-4730](https://issues.apache.org/jira/browse/QPID-4730) - Bug for qpid perl binding. The object is overwritten by the return value when a function return an integer.
 - [QPID-4875](https://issues.apache.org/jira/browse/QPID-4875) - [Java] The parsing logic for certificate subjects doesn't work properly in all cases
 - [QPID-4901](https://issues.apache.org/jira/browse/QPID-4901) - [JMS AMQP 1.0] QueueBrowser hangs on reaching end of the queues
 - [QPID-4907](https://issues.apache.org/jira/browse/QPID-4907) - qpid-tool displays duplicate entries for objects managed by the broker.
 - [QPID-4924](https://issues.apache.org/jira/browse/QPID-4924) - Python language examples based on the Python language bindings
 - [QPID-4944](https://issues.apache.org/jira/browse/QPID-4944) - HA Sporadic failure in ha_tests:  test_failover_send_receive and test_expected_backup_timeout
 - [QPID-4948](https://issues.apache.org/jira/browse/QPID-4948) - [AMQP 1.0] browsing queues not supported
 - [QPID-4978](https://issues.apache.org/jira/browse/QPID-4978) - [AMQP 1.0] support reliability link option
 - [QPID-5002](https://issues.apache.org/jira/browse/QPID-5002) - durable link should not create autodelete subscription queue by default
 - [QPID-5011](https://issues.apache.org/jira/browse/QPID-5011) - C++ Broker ACL allows one connection when user quota is zero
 - [QPID-5015](https://issues.apache.org/jira/browse/QPID-5015) - QueueFlowLimit tests occassionally fail
 - [QPID-5016](https://issues.apache.org/jira/browse/QPID-5016) - Legacy store not correctly initialising rmgr
 - [QPID-5025](https://issues.apache.org/jira/browse/QPID-5025) - DeliveryRecord::committed() doesn't check if delivery is already ended
 - [QPID-5026](https://issues.apache.org/jira/browse/QPID-5026) - [AMQP 1.0] set address for 'local' terminus in attach
 - [QPID-5029](https://issues.apache.org/jira/browse/QPID-5029) - WinSDK build tries to handle components that have been removed
 - [QPID-5038](https://issues.apache.org/jira/browse/QPID-5038) - [Java Broker] some message store system tests leak resources (including bdb threads)
 - [QPID-5039](https://issues.apache.org/jira/browse/QPID-5039) - C++ broker compile issue in VS2012
 - [QPID-5040](https://issues.apache.org/jira/browse/QPID-5040) - [AMQP 1.0] Support for AmqpValue sections
 - [QPID-5041](https://issues.apache.org/jira/browse/QPID-5041) - adding annotations to durable messages causes persistence id to be lost
 - [QPID-5050](https://issues.apache.org/jira/browse/QPID-5050) - Clients calling Connection#stop() (or #close()) from within an ExceptionListener have potential for deadlock
 - [QPID-5051](https://issues.apache.org/jira/browse/QPID-5051) - swigged ppython tests fail on RHEL5
 - [QPID-5058](https://issues.apache.org/jira/browse/QPID-5058) - QPID JCA 0.22 on JBoss 5.1 Examples Throw Errors
 - [QPID-5071](https://issues.apache.org/jira/browse/QPID-5071) - The CMake build system does not rebuild when the Swig descriptors change
 - [QPID-5072](https://issues.apache.org/jira/browse/QPID-5072) - [C++ broker] SessionManager does not forget sessions when broker drops connection after journal error, leading to memory leak
 - [QPID-5077](https://issues.apache.org/jira/browse/QPID-5077) - [AMQP 1.0] SASL layer for interlinks assumes synchronous interaction
 - [QPID-5083](https://issues.apache.org/jira/browse/QPID-5083) - [AMQP 1.0] if sasl implementation is not available client (and interlinking) will fail
 - [QPID-5084](https://issues.apache.org/jira/browse/QPID-5084) - Track durable queue ownership across broker restarts
 - [QPID-5086](https://issues.apache.org/jira/browse/QPID-5086) - rollback can stall message delivery
 - [QPID-5089](https://issues.apache.org/jira/browse/QPID-5089) - Remove Personalized User/Pass from EAP6/JBoss7 Example
 - [QPID-5090](https://issues.apache.org/jira/browse/QPID-5090) - In 0-10, setting content 'object' to utf8 encoded string should cause content-type to be set to text/plain
 - [QPID-5098](https://issues.apache.org/jira/browse/QPID-5098) - [AMQP 1.0] Connection::close() doesn't handle failed sessions or links properly
 - [QPID-5101](https://issues.apache.org/jira/browse/QPID-5101) - C++ Broker windows build is missing SaslFactory::createServer
 - [QPID-5102](https://issues.apache.org/jira/browse/QPID-5102) - C++ Broker windows build needs many xxx_EXTERNs when PROTON is included
 - [QPID-5104](https://issues.apache.org/jira/browse/QPID-5104) - Python Swig bindings do not expose Message properties in the same manner as the pure Python bindings
 - [QPID-5106](https://issues.apache.org/jira/browse/QPID-5106) - Queue level message sequencing doesn't work with 1.0 client
 - [QPID-5108](https://issues.apache.org/jira/browse/QPID-5108) - session statistics Tx* not updated any time
 - [QPID-5109](https://issues.apache.org/jira/browse/QPID-5109) - qpid-config refers to policies no longer supported (ring-strict and flow-to-disk)
 - [QPID-5110](https://issues.apache.org/jira/browse/QPID-5110) - [AMQP 1.0] make handling of incorrectly typed properties more robust
 - [QPID-5113](https://issues.apache.org/jira/browse/QPID-5113) - JMS Client - JMS Connection exception listener is not notified when AMQ broker is killed
 - [QPID-5114](https://issues.apache.org/jira/browse/QPID-5114) - WinSDK should deliver qpid-send and qpid-receive executables
 - [QPID-5122](https://issues.apache.org/jira/browse/QPID-5122) - Error compling on ARM platforms: cast from 'const char*' to 'const size_t* {aka const unsigned int*}' increases required alignment of target type [-Werror=cast-align]
 - [QPID-5124](https://issues.apache.org/jira/browse/QPID-5124) - durable LVQ raises journal error when only transient messages are sent
 - [QPID-5126](https://issues.apache.org/jira/browse/QPID-5126) - Unable to compile legacy store on ARM platforms
 - [QPID-5129](https://issues.apache.org/jira/browse/QPID-5129) - Legacy store fails to compile on ARM due to alignment issues
 - [QPID-5130](https://issues.apache.org/jira/browse/QPID-5130) - [AMQP 1.0] x-declare for node ignores the exchange type
 - [QPID-5131](https://issues.apache.org/jira/browse/QPID-5131) - [AMQP 1.0] xml exchange can't see 1.0 content
 - [QPID-5132](https://issues.apache.org/jira/browse/QPID-5132) - HA crash in test_tx_join_leave caused by double delete of queue. 
 - [QPID-5139](https://issues.apache.org/jira/browse/QPID-5139) - HA transactions block a thread, can deadlock the broker.
 - [QPID-5140](https://issues.apache.org/jira/browse/QPID-5140) - Python swig bindings - Message.properties missing get/set methods
 - [QPID-5141](https://issues.apache.org/jira/browse/QPID-5141) - Message::getContentObject() returns void for 0-10 unless content is a map or a list
 - [QPID-5142](https://issues.apache.org/jira/browse/QPID-5142) - Don't want to pick up swigged client in python tests unless explicitly requested
 - [QPID-5143](https://issues.apache.org/jira/browse/QPID-5143) - default url shouldn't specify transport
 - [QPID-5146](https://issues.apache.org/jira/browse/QPID-5146) - [AMQP 1.0] capabilities not handled correctly
 - [QPID-5147](https://issues.apache.org/jira/browse/QPID-5147) - [AMQP 1.0] improve failure handling
 - [QPID-5148](https://issues.apache.org/jira/browse/QPID-5148) - [AMQP 1.0] ttl not handled
 - [QPID-5149](https://issues.apache.org/jira/browse/QPID-5149) - [AMQP 1.0] translation from 1.0 to 0-10 should truncate routing key if necessary
 - [QPID-5150](https://issues.apache.org/jira/browse/QPID-5150) - [AMQP 1.0] Sending messages over 1.0 to QMF agent crashes broker
 - [QPID-5151](https://issues.apache.org/jira/browse/QPID-5151) - [AMQP 1.0] messages sent to exchange over 1.0 are not rerouted to alternate exchange
 - [QPID-5152](https://issues.apache.org/jira/browse/QPID-5152) - [AMQP 1.0] exchange arguments aren't set when created on attach
 - [QPID-5153](https://issues.apache.org/jira/browse/QPID-5153) - [AMQP 1.0] specific message properties not read by broker for 1.0 messages
 - [QPID-5154](https://issues.apache.org/jira/browse/QPID-5154) - Correct errors in python client API doc
 - [QPID-5155](https://issues.apache.org/jira/browse/QPID-5155) - CMake does not package Proton library on windows
 - [QPID-5156](https://issues.apache.org/jira/browse/QPID-5156) - [AMQP 1.0] assert should check node properties
 - [QPID-5165](https://issues.apache.org/jira/browse/QPID-5165) - No mapping from JMS JMSXGroupID property to AMQP message group-id
 - [QPID-5168](https://issues.apache.org/jira/browse/QPID-5168) - [AMQP 1.0] make handling of reply-to less sensitive to different schemes
 - [QPID-5169](https://issues.apache.org/jira/browse/QPID-5169) - qpid-tools help typos (CRAM-MD -&gt; CRAM-MD5)
 - [QPID-5170](https://issues.apache.org/jira/browse/QPID-5170) - [AMQP 1.0] outgoing deliveries that are settled without an explicit disposition are not dequeued
 - [QPID-5172](https://issues.apache.org/jira/browse/QPID-5172) - Thread safety issue in StringTypeConstructor.construct and SymbolTypeConstructor.construct
 - [QPID-5177](https://issues.apache.org/jira/browse/QPID-5177) - producer.send with sync_publish=true set against activemq blocks and doesn't return
 - [QPID-5182](https://issues.apache.org/jira/browse/QPID-5182) - The details of custom error-conditions are not being preserved up to the Error object
 - [QPID-5183](https://issues.apache.org/jira/browse/QPID-5183) - Python client does not release acquired messages on consumer close when session persists
 - [QPID-5184](https://issues.apache.org/jira/browse/QPID-5184) - [Java 0-x Client] queueSender.send() to RabbitMQ V3.1.3 generates invalid expiration '': no_integer response
 - [QPID-5187](https://issues.apache.org/jira/browse/QPID-5187) - WinSDK does not package amqpc library
 - [QPID-5188](https://issues.apache.org/jira/browse/QPID-5188) - WinSDK uses hard-coded qpid directory for source pool
 - [QPID-5190](https://issues.apache.org/jira/browse/QPID-5190) - Client consistently locks up in both producer.send and connection.close if broker fails at the right moment
 - [QPID-5192](https://issues.apache.org/jira/browse/QPID-5192) - [Java common and broker-core] add the generated protocol and logging files to the tree, make re-generation triggered upon request
 - [QPID-5194](https://issues.apache.org/jira/browse/QPID-5194) - Occasionally see ERROR (221): Caught Exception: java.lang.IllegalArgumentException: timeout value is negative
 - [QPID-5195](https://issues.apache.org/jira/browse/QPID-5195) - [AMQP 1.0 JMS] Client does not properly handle the case where there are not enough channels
 - [QPID-5197](https://issues.apache.org/jira/browse/QPID-5197) - Remove obsolete --cluster-durable/persistLastNode options
 - [QPID-5198](https://issues.apache.org/jira/browse/QPID-5198) - wrong exception is thrown if protocol is not recognised
 - [QPID-5200](https://issues.apache.org/jira/browse/QPID-5200) - Can't disable size limit on individual queue
 - [QPID-5203](https://issues.apache.org/jira/browse/QPID-5203) - Python client unexpected exception after ACL denial
 - [QPID-5205](https://issues.apache.org/jira/browse/QPID-5205) - Viewing an exchange with alternate exchange through the Management UI causes exception in Broker logs.
 - [QPID-5206](https://issues.apache.org/jira/browse/QPID-5206) - [AMQP 1.0 JMS] Occasional null pointer exception seen in org.apache.qpid.amqp_1_0.client.Sender$1.remoteDetached(Sender.java:181)
 - [QPID-5215](https://issues.apache.org/jira/browse/QPID-5215) - Legacystore: Import rest of tests and utilities
 - [QPID-5224](https://issues.apache.org/jira/browse/QPID-5224) - [Java 0-x Client] connection is abruptly closed when creating consumers against RabbitMQ
 - [QPID-5227](https://issues.apache.org/jira/browse/QPID-5227) - redelivered flag not always set correctly
 - [QPID-5228](https://issues.apache.org/jira/browse/QPID-5228) - [AMQP 1.0] can't set alternate-exchange for subscription queue
 - [QPID-5229](https://issues.apache.org/jira/browse/QPID-5229) - [AMQP 1.0] release and reject not implemented
 - [QPID-5230](https://issues.apache.org/jira/browse/QPID-5230) - explicitly release message is not marked as redelivered on subsequent delivery
 - [QPID-5231](https://issues.apache.org/jira/browse/QPID-5231) - A few tools still reference the old Qpid Swig binding name (cqpid) rather than the new qpid_messaging name
 - [QPID-5232](https://issues.apache.org/jira/browse/QPID-5232) - [AMQP 1.0] receiver links from exchanges should be unreliable by default
 - [QPID-5233](https://issues.apache.org/jira/browse/QPID-5233) - [AMQP 1.0] default sender capacity for 1.0 is different from that for 0-10
 - [QPID-5235](https://issues.apache.org/jira/browse/QPID-5235) - [AMQP 1.0] store settings aren't passed through for queues created on attach of 1.0 links
 - [QPID-5236](https://issues.apache.org/jira/browse/QPID-5236) - [AMQP 1.0]: testing for incorrect symbolic descriptor for value sections
 - [QPID-5239](https://issues.apache.org/jira/browse/QPID-5239) - annotations are always sent as strings over 0-10
 - [QPID-5240](https://issues.apache.org/jira/browse/QPID-5240) - [Java Broker] ExternalAuthenticationManager NPEs/abruptly closes connection when connection attempt made by misconfigured client
 - [QPID-5241](https://issues.apache.org/jira/browse/QPID-5241) - [Java Broker] JMX Management can cause NPE in case of premature shutdown
 - [QPID-5242](https://issues.apache.org/jira/browse/QPID-5242) - [Java Broker] The queue adapter does not return correct values for attributes "messageGroupKey" and "messageGroupSharedGroups"
 - [QPID-5244](https://issues.apache.org/jira/browse/QPID-5244) - Remove old QMFv1 example agent
 - [QPID-5246](https://issues.apache.org/jira/browse/QPID-5246) - ACL treats DeleteQueue as a Reject Queue
 - [QPID-5247](https://issues.apache.org/jira/browse/QPID-5247) - [AMQP 1.0] Receiver::isClosed() is not implemented
 - [QPID-5248](https://issues.apache.org/jira/browse/QPID-5248) - [AMQP 1.0] non-autodeleted,non-shared subscription queues should be deleted when receiver is explicitly closed
 - [QPID-5251](https://issues.apache.org/jira/browse/QPID-5251) - [AMQP 1.0] allow create-on-demand through broker configuration
 - [QPID-5253](https://issues.apache.org/jira/browse/QPID-5253) - [AMQP 1.0] delivery-count is incorrect for browsed message that has never been previously delivered
 - [QPID-5256](https://issues.apache.org/jira/browse/QPID-5256) - Calling Message::getContentSize() throws InvalidConversion
 - [QPID-5259](https://issues.apache.org/jira/browse/QPID-5259) - cmake legacy store and linear store messages aren't very helpful if dependencies are missing.
 - [QPID-5262](https://issues.apache.org/jira/browse/QPID-5262) - Install debug versions of MS runtime DLLs
 - [QPID-5265](https://issues.apache.org/jira/browse/QPID-5265) - [Java Broker] the client version is only logged for 0-8/9/9-1 connections if a clientid is also set
 - [QPID-5266](https://issues.apache.org/jira/browse/QPID-5266) - [Java Broker] the client product is not logged in the connection open message
 - [QPID-5276](https://issues.apache.org/jira/browse/QPID-5276) - [AMQP 1.0] node resolution doesn't take into account requested type
 - [QPID-5279](https://issues.apache.org/jira/browse/QPID-5279) - [AMQP 1.0] 1.0 receiver can consume from someone else's exclusive queue
 - [QPID-5280](https://issues.apache.org/jira/browse/QPID-5280) - exclusivity of queue not enforced for bind/unbind
 - [QPID-5282](https://issues.apache.org/jira/browse/QPID-5282) - Sender timeouts may allow the peer to suffer an AMQFrameDecodingException
 - [QPID-5283](https://issues.apache.org/jira/browse/QPID-5283) - exclusive declare granted even if queue has existing consumer
 - [QPID-5284](https://issues.apache.org/jira/browse/QPID-5284) - timestamp is not persisted
 - [QPID-5286](https://issues.apache.org/jira/browse/QPID-5286) - [AMQP 1.0] Receiver::get() doesn't replenish credit
 - [QPID-5287](https://issues.apache.org/jira/browse/QPID-5287) - .NET binding does not set Assembly version number
 - [QPID-5288](https://issues.apache.org/jira/browse/QPID-5288) - [AMQP 1.0] Sender::close() hangs when coinciding with connection close by peer
 - [QPID-5289](https://issues.apache.org/jira/browse/QPID-5289) - [AMQP 1.0] error descriptions are not given in exceptions by client
 - [QPID-5290](https://issues.apache.org/jira/browse/QPID-5290) - Attempt to enqueue message larger than page size should not end connection
 - [QPID-5291](https://issues.apache.org/jira/browse/QPID-5291) - [AMQP 1.0] set connection properties from management schema if available
 - [QPID-5292](https://issues.apache.org/jira/browse/QPID-5292) - connection event not raised, authIdentity not set in mgmt props
 - [QPID-5293](https://issues.apache.org/jira/browse/QPID-5293) - [AMQP 1.0 JMS] Thread deadlock when closing connection
 - [QPID-5294](https://issues.apache.org/jira/browse/QPID-5294) - [AMQP 1.0 JMS] Thread deadlock due to JVM bug JDK-8022788
 - [QPID-5295](https://issues.apache.org/jira/browse/QPID-5295) - [AMQP 1.0 JMS] Thread deadlock
 - [QPID-5297](https://issues.apache.org/jira/browse/QPID-5297) - [Java Broker] make the 1.0 protocol plugin use a single ProtocolEngineCreator
 - [QPID-5299](https://issues.apache.org/jira/browse/QPID-5299) - [AMQP 1.0] ACL rules should be checked before checking node's existence and returning amqp:not-found error
 - [QPID-5300](https://issues.apache.org/jira/browse/QPID-5300) - [AMQP 1.0] Some ACL errors are returned as internal error instead of unauthorized error
 - [QPID-5301](https://issues.apache.org/jira/browse/QPID-5301) - support autodeletion of exchanges
 - [QPID-5304](https://issues.apache.org/jira/browse/QPID-5304) - Unit test program has bad failure mode if XML_LIB is not set
 - [QPID-5305](https://issues.apache.org/jira/browse/QPID-5305) - Valgrind reports uninitialised values sent to system call in legacystore
 - [QPID-5309](https://issues.apache.org/jira/browse/QPID-5309) - PagedQueue page file created as executable
 - [QPID-5312](https://issues.apache.org/jira/browse/QPID-5312) - Paged queue does not deliver all messages
 - [QPID-5314](https://issues.apache.org/jira/browse/QPID-5314) - Don't include full path for paging file in paged queue exceptions
 - [QPID-5315](https://issues.apache.org/jira/browse/QPID-5315) - paging out of memory loses persistence id for messages
 - [QPID-5326](https://issues.apache.org/jira/browse/QPID-5326) - [Java Broker] Authentication provider attributes data float down whilst scrolling the web management console page
 - [QPID-5327](https://issues.apache.org/jira/browse/QPID-5327) - [Java Broker] Javascript errors are reported in IE7 and IE11 on opening log viewer tab and preferences dialog
 - [QPID-5328](https://issues.apache.org/jira/browse/QPID-5328) - browse mode should imply unreliable delivery over 0-10
 - [QPID-5330](https://issues.apache.org/jira/browse/QPID-5330) - Queue flow limit tests try to invoke a missing qpid-python-test
 - [QPID-5331](https://issues.apache.org/jira/browse/QPID-5331) - [AMQP 1.0] Connection::close() hangs if a sender link has failed
 - [QPID-5341](https://issues.apache.org/jira/browse/QPID-5341) - Allow use of proton 0.6
 - [QPID-5342](https://issues.apache.org/jira/browse/QPID-5342) - Java client ignores missing heartbeats
 - [QPID-5344](https://issues.apache.org/jira/browse/QPID-5344) - [AMQP 1.0 JMS] Thread deadlock related to session close
 - [QPID-5349](https://issues.apache.org/jira/browse/QPID-5349) - C++ windows packaging does not install qpid-proton.dll library
 - [QPID-5354](https://issues.apache.org/jira/browse/QPID-5354) - [AMQP 1.0] durable node property not signalled if specified on its own
 - [QPID-5363](https://issues.apache.org/jira/browse/QPID-5363) - C++ HelloWorld messaging client crash closing AMQP 1.0 connection on Windows
 - [QPID-5385](https://issues.apache.org/jira/browse/QPID-5385) - Create/Close session in a loop causing connection to be closed and connection.close to hang after that
 - [QPID-5386](https://issues.apache.org/jira/browse/QPID-5386) - message not coverted correctly if it contains a delivery-annotation section
 - [QPID-5389](https://issues.apache.org/jira/browse/QPID-5389) - ConnectionHandler may stop writting pending frames if close is called right after the connection is started
 - [QPID-5390](https://issues.apache.org/jira/browse/QPID-5390) - ConcurrentModificationException when closing a connection
 - [QPID-5401](https://issues.apache.org/jira/browse/QPID-5401) - Linearstore: ARM compile error: cast ... increases required alignment of target type
 - [QPID-5402](https://issues.apache.org/jira/browse/QPID-5402) - Disable default build of linearstore in cmake
 - [QPID-5417](https://issues.apache.org/jira/browse/QPID-5417) - ClassCastException when using amqp-1-0-jms-0.24 client
 - [QPID-5419](https://issues.apache.org/jira/browse/QPID-5419) - [JMS Client] The JMS Client fails to start a dispatcher thread for Durable Consumer's
 - [QPID-5421](https://issues.apache.org/jira/browse/QPID-5421) - HA replication error in stand-alone replication.
 - [QPID-5422](https://issues.apache.org/jira/browse/QPID-5422) - [Java Broker] maven artifacts for broker-core module not being copied by release.sh
 - [QPID-5423](https://issues.apache.org/jira/browse/QPID-5423) - [Java Broker] binary release packaging  duplicates some plugin dependencies
 - [QPID-5430](https://issues.apache.org/jira/browse/QPID-5430) - HA primary broker does not go active if there are no replicated queues.
 - [QPID-5431](https://issues.apache.org/jira/browse/QPID-5431) - Qpid c++ client hangs / crashes during reception failover in HA environment (mutual recursion) 
 - [QPID-5439](https://issues.apache.org/jira/browse/QPID-5439) - [AMQP 1.0 JMS client] Client hangs during connection.close()
 - [QPID-5445](https://issues.apache.org/jira/browse/QPID-5445) - Make install writes to OS-reserved location despite setting prefix
 - [QPID-5450](https://issues.apache.org/jira/browse/QPID-5450) - [Java Broker] shared message group race between acquiring new messages and acking delivered messages can lead to concurrent delivery
 - [QPID-5453](https://issues.apache.org/jira/browse/QPID-5453) - Subscription sessions linger
 - [QPID-5456](https://issues.apache.org/jira/browse/QPID-5456) - [AMQP 1.0] client refuses frames smaller than the frame size it indicated was acceptable
 - [QPID-5463](https://issues.apache.org/jira/browse/QPID-5463) - [AMQP 1.0] assume auto-delete if dynamic flag is set and no lifetime policy supplied
 - [QPID-5488](https://issues.apache.org/jira/browse/QPID-5488) - Apparent corruption of SSL connection

## Tasks

 - [QPID-4989](https://issues.apache.org/jira/browse/QPID-4989) - Java performance tests - add documentation
 - [QPID-5046](https://issues.apache.org/jira/browse/QPID-5046) - Change release.sh to use cmake instead of autotools to build the cpp tree
 - [QPID-5157](https://issues.apache.org/jira/browse/QPID-5157) - remove unused test and build code
 - [QPID-5163](https://issues.apache.org/jira/browse/QPID-5163) - [Java Broker] move generation of the ACL log messages alongside all the other log message generation in broker-core
 - [QPID-5164](https://issues.apache.org/jira/browse/QPID-5164) - [Java] remove use of qpid-all.jar from scripts, use classpath wildcard expansion instead
 - [QPID-5193](https://issues.apache.org/jira/browse/QPID-5193) - [Java] update the source and target values for javac to 1.6
 - [QPID-5207](https://issues.apache.org/jira/browse/QPID-5207) - [Java Broker] use the Dojo release binary for the management-http plugin build instead of extracting the war
 - [QPID-5243](https://issues.apache.org/jira/browse/QPID-5243) - [Java Broker] Upgrade dojo toolkit to the latest version (1.9.1)
 - [QPID-5255](https://issues.apache.org/jira/browse/QPID-5255) - 0.26 release tasks