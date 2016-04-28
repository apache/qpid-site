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

# Qpid 0.28 Release Notes

Qpid is a cross-platform AMQP messaging system.  It provides message
brokers written in C++ and Java, and clients for C++, Java, Perl,
Python, Ruby, and .NET.  More about [Qpid]({{site_url}}/index.html).

The full list of changes in the Qpid 0.28 release incorporates
both the issues worked on during the 0.27 development
stream and any final touches made during the 0.28 release
process. A list of these JIRA issues can be found below.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-5073](https://issues.apache.org/jira/browse/QPID-5073) - [Java Broker] Refactor DurableConfigurationStore recovery to allow for additional configured object children other than just Exchange/Binding/Queue
 - [QPID-5210](https://issues.apache.org/jira/browse/QPID-5210) - [AMQP 1.0 JMS client] add support for providing SSL configuration other than the JVM default
 - [QPID-5333](https://issues.apache.org/jira/browse/QPID-5333) - Implement a find_proton function for cmake
 - [QPID-5347](https://issues.apache.org/jira/browse/QPID-5347) - Web Management console should display queue attributes exclusive/owner
 - [QPID-5348](https://issues.apache.org/jira/browse/QPID-5348) - [AMQP 1.0] Add option to automatically set the to field on sent messages based on senders address
 - [QPID-5374](https://issues.apache.org/jira/browse/QPID-5374) - Contribute JMS client docbook for 0-8..0-9-1
 - [QPID-5396](https://issues.apache.org/jira/browse/QPID-5396) - Windows certificate store name mismatch
 - [QPID-5408](https://issues.apache.org/jira/browse/QPID-5408) - [AMQP 1.0 JMS] Connection URLs which contain unrecognised options should throw exception
 - [QPID-5437](https://issues.apache.org/jira/browse/QPID-5437) - [Java Broker] Allow HTTP Management port to be bound to specific interfaces
 - [QPID-5452](https://issues.apache.org/jira/browse/QPID-5452) - Change installation directory to /usr/bin for qpid-receive and qpid-send
 - [QPID-5459](https://issues.apache.org/jira/browse/QPID-5459) - [Java Broker] Add WebSocket transport support
 - [QPID-5470](https://issues.apache.org/jira/browse/QPID-5470) - Improve QMF README documentation and update JavaDocs to reflect new location of QMF2 API docs
 - [QPID-5472](https://issues.apache.org/jira/browse/QPID-5472) - Exception messages used to report bind port failures should include port id/name/number too
 - [QPID-5474](https://issues.apache.org/jira/browse/QPID-5474) - [Java Broker] add clientid and client version to the web ui connection screen, stop displaying unimplemented attributes
 - [QPID-5475](https://issues.apache.org/jira/browse/QPID-5475) - [Java Broker] Add SSL client auth support to HTTP Management
 - [QPID-5516](https://issues.apache.org/jira/browse/QPID-5516) - C++ build tries to build systemtap (DTrace compatible) probes where they won't work
 - [QPID-5519](https://issues.apache.org/jira/browse/QPID-5519) - ACL property/properties for paged queues
 - [QPID-5527](https://issues.apache.org/jira/browse/QPID-5527) - Upgrade to Jetty 8
 - [QPID-5539](https://issues.apache.org/jira/browse/QPID-5539) - Provide Windows SslCredential class
 - [QPID-5549](https://issues.apache.org/jira/browse/QPID-5549) - Windows SSL client support for AMQP 1.0
 - [QPID-5551](https://issues.apache.org/jira/browse/QPID-5551) - [Java Broker] Improve use of exceptions throughout the broker
 - [QPID-5555](https://issues.apache.org/jira/browse/QPID-5555) - [Java Broker] Modify Queue implementation of lifetime / exclusivity policies
 - [QPID-5558](https://issues.apache.org/jira/browse/QPID-5558) - [Java Broker] Update implementation of draft AMQP Management to conform with WD06
 - [QPID-5559](https://issues.apache.org/jira/browse/QPID-5559) - [Java Broker] Remove unused methods from the AMQQueue interface and implementations 
 - [QPID-5562](https://issues.apache.org/jira/browse/QPID-5562) - [Java Broker] Make all ACL assertions throw AccessControlException on failure
 - [QPID-5563](https://issues.apache.org/jira/browse/QPID-5563) - [Java Broker] [AMQP 1.0] Use hostname field in open to select virtualhost
 - [QPID-5566](https://issues.apache.org/jira/browse/QPID-5566) - [JMS AMQP 1.0] DestinationImpl implements both Queue and Topic, which confuses some other JMS implementations
 - [QPID-5567](https://issues.apache.org/jira/browse/QPID-5567) - [Java Broker] Remove SecurityManager "CurrentSubject" thread local, and always use the subject from the current AccessControlContext
 - [QPID-5574](https://issues.apache.org/jira/browse/QPID-5574) - [AMQP 1.0 JMS Client] Allow sync-publish option to override default behaviour
 - [QPID-5582](https://issues.apache.org/jira/browse/QPID-5582) - [Java Broker] Enforce 0-10 restriction on uniqueness of binding keys 
 - [QPID-5593](https://issues.apache.org/jira/browse/QPID-5593) - Adapt gen-release-books etc to publish jms-client-0-8 too
 - [QPID-5601](https://issues.apache.org/jira/browse/QPID-5601) - [Java Broker] The default exchange is not really an exchange
 - [QPID-5605](https://issues.apache.org/jira/browse/QPID-5605) - [Java Broker] [AMQP 1.0] Allow for addresses of the form &lt;exchange&gt;/&lt;routing-key&gt; to be used for both publishing and consuming
 - [QPID-5606](https://issues.apache.org/jira/browse/QPID-5606) - [Java Broker] Add a Principal representing the connection to HTTP and JMX management driven actions
 - [QPID-5612](https://issues.apache.org/jira/browse/QPID-5612) - JMS benchmarking tool
 - [QPID-5621](https://issues.apache.org/jira/browse/QPID-5621) - [C++ broker] userId is not passed to ACL when DIGEST-MD5 is used while creating link
 - [QPID-5632](https://issues.apache.org/jira/browse/QPID-5632) - Export idiomatic cmake files for external cmake projects to use
 - [QPID-5657](https://issues.apache.org/jira/browse/QPID-5657) - Upgrade geronimo JMS jar dependency from v1.0 to v1.1.1
 - [QPID-5723](https://issues.apache.org/jira/browse/QPID-5723) - Java 8 support
 - [QPID-5741](https://issues.apache.org/jira/browse/QPID-5741) - Now that Proton 0.7 has released don't warn if we try to build with it

## Bugs fixed

 - [QPID-2294](https://issues.apache.org/jira/browse/QPID-2294) - The Unix python client can erroneously throw exceptions from select due to interrupted system call
 - [QPID-4877](https://issues.apache.org/jira/browse/QPID-4877) - Consumers created using BURLs without named exchange fail with "Cannot add bindings to the default exchange [error code 403: access refused]"
 - [QPID-5264](https://issues.apache.org/jira/browse/QPID-5264) - Can't change maxprefetch limit with JMS AMQP 1.0
 - [QPID-5336](https://issues.apache.org/jira/browse/QPID-5336) - Script interpreters need to be found on the path and not have hardcoded locations
 - [QPID-5356](https://issues.apache.org/jira/browse/QPID-5356) - Windows can provide an unspecified client certificate in SSL negotiation
 - [QPID-5372](https://issues.apache.org/jira/browse/QPID-5372) - [Java Broker] An excessive amount of debug logging is generated for PreferencesProviderFactory when a Broker tab is opened in web management console
 - [QPID-5373](https://issues.apache.org/jira/browse/QPID-5373) - [Java Broker] SSL negotiation is being performed in the accepting thread
 - [QPID-5378](https://issues.apache.org/jira/browse/QPID-5378) - [AMQP 1.0] zero capacity receiver does not reissue credit on reconnect
 - [QPID-5379](https://issues.apache.org/jira/browse/QPID-5379) - [AMQP 1.0] Sasl layer with encryption is broken
 - [QPID-5383](https://issues.apache.org/jira/browse/QPID-5383) - [AMQP 1.0] string valued properties for queues created on attach lose encoding
 - [QPID-5384](https://issues.apache.org/jira/browse/QPID-5384) - [AMQP 1.0] can't assert on autodelete property
 - [QPID-5394](https://issues.apache.org/jira/browse/QPID-5394) - Qpid cpp build always builds swig python binding code even when not necessary
 - [QPID-5395](https://issues.apache.org/jira/browse/QPID-5395) - [AMQP 1.0] direct proton tracing into qpids own logging
 - [QPID-5416](https://issues.apache.org/jira/browse/QPID-5416) - [AMQP 1.0] sending a qmfv2 getTimestampConfig request over 1.0 causes broker crash
 - [QPID-5418](https://issues.apache.org/jira/browse/QPID-5418) - qpidd loading both linear and legacy store succeeds without a warning/error
 - [QPID-5420](https://issues.apache.org/jira/browse/QPID-5420) - Creating consumer for Destination specifying the no-name exchange in binding url syntax fails against Java Broker.
 - [QPID-5427](https://issues.apache.org/jira/browse/QPID-5427) - It is possible to mask critical logging messages
 - [QPID-5428](https://issues.apache.org/jira/browse/QPID-5428) - heartbeats not in use when attempting to connect
 - [QPID-5429](https://issues.apache.org/jira/browse/QPID-5429) - Java Broker does not always write the reason it cannot start-up to qpid.log
 - [QPID-5434](https://issues.apache.org/jira/browse/QPID-5434) - [AMQP 1.0] timestamps sent with incorrect typecode
 - [QPID-5435](https://issues.apache.org/jira/browse/QPID-5435) - [AMQP 1.0] modify qpid-send to use get-/set- ContentObject() for strings as well as maps
 - [QPID-5440](https://issues.apache.org/jira/browse/QPID-5440) - [AMQP 1.0] display alternate-exchange property for topic
 - [QPID-5446](https://issues.apache.org/jira/browse/QPID-5446) - [AMQP 1.0] 'group sequence id' field is exposed via incorrect property name
 - [QPID-5447](https://issues.apache.org/jira/browse/QPID-5447) - Link detached by peer with amqp:precondition-failed: Exchange of different type already exists
 - [QPID-5451](https://issues.apache.org/jira/browse/QPID-5451) - [AMQP 1.0] overly verbose logging at notce level for message sequence annotations over AMQP 1.0
 - [QPID-5455](https://issues.apache.org/jira/browse/QPID-5455) - [AMQP 1.0 JMS client] Client looses persistent messages violating JMS delivery guarantee
 - [QPID-5457](https://issues.apache.org/jira/browse/QPID-5457) - [AMQP 1.0] broker doesn't handle messages composed from multiple transfers 
 - [QPID-5458](https://issues.apache.org/jira/browse/QPID-5458) - [Java Broker] the View Message dialog does not show CorrelationID or Size
 - [QPID-5461](https://issues.apache.org/jira/browse/QPID-5461) - [Java Broker] Downgrade the severity of broker log messages like java.io.IOException: Connection reset by peer for 0-8/9/9-1 connections
 - [QPID-5467](https://issues.apache.org/jira/browse/QPID-5467) - [AMQP 1.0] delete-on-closed not handled correctly
 - [QPID-5468](https://issues.apache.org/jira/browse/QPID-5468) - [AMQP 1.0] delete-if-unused doesn't work for initial sender
 - [QPID-5469](https://issues.apache.org/jira/browse/QPID-5469) - [AMQP 1.0] don't override autodeletion if implied by topic policy
 - [QPID-5471](https://issues.apache.org/jira/browse/QPID-5471) - [Java Broker] fix / enhance the message group documentation
 - [QPID-5476](https://issues.apache.org/jira/browse/QPID-5476) - ABI check script isn't robust enough
 - [QPID-5478](https://issues.apache.org/jira/browse/QPID-5478) - [Java Common] IoSender may throw a timeout related SenderException earlier than it should
 - [QPID-5481](https://issues.apache.org/jira/browse/QPID-5481) - C++ .NET Messaging binding does not expose recent Messaging additions
 - [QPID-5485](https://issues.apache.org/jira/browse/QPID-5485) -  Deleting paged queue does not remove underlying file
 - [QPID-5486](https://issues.apache.org/jira/browse/QPID-5486) - Creating paged queue can overwrite existing qpidd files
 - [QPID-5497](https://issues.apache.org/jira/browse/QPID-5497) - [AMQP 1.0] Session::sync() not implemented.
 - [QPID-5498](https://issues.apache.org/jira/browse/QPID-5498) - paged out messages loses expiration
 - [QPID-5499](https://issues.apache.org/jira/browse/QPID-5499) - Ruby/Perl bindings fail to compile with -Werror=format-security
 - [QPID-5501](https://issues.apache.org/jira/browse/QPID-5501) - [AMQP 1.0] create topic doesn't fail if topic of same name already exists
 - [QPID-5502](https://issues.apache.org/jira/browse/QPID-5502) - [AMQP 1.0] implement qmf operations for closing connection and ending (detaching) session
 - [QPID-5503](https://issues.apache.org/jira/browse/QPID-5503) - [AMQP 1.0] implement Session::nextReceiver()
 - [QPID-5504](https://issues.apache.org/jira/browse/QPID-5504) - [Java Broker] Allow other routing/storage node types than Queues and Exchanges
 - [QPID-5506](https://issues.apache.org/jira/browse/QPID-5506) - c++ sasl_fed_ex tests fail on FreeBSD because /usr/bin/certutil doesn't exist
 - [QPID-5509](https://issues.apache.org/jira/browse/QPID-5509) - [AMQP 1.0] release prefetched messages on closing receiver
 - [QPID-5512](https://issues.apache.org/jira/browse/QPID-5512) - suppress exception sometimes seen in IoReceiver due to race while closing the socket on Windows
 - [QPID-5513](https://issues.apache.org/jira/browse/QPID-5513) - HA backup fails if number of replicated queues exceeds number of channels.
 - [QPID-5520](https://issues.apache.org/jira/browse/QPID-5520) - qpid-python-test should not fail for skipped tests.
 - [QPID-5522](https://issues.apache.org/jira/browse/QPID-5522) - TransactionController endless wait when the TCP/IP connection is lost
 - [QPID-5524](https://issues.apache.org/jira/browse/QPID-5524) - Missing ssl-cert-name connection argument processing in AMQP 1.0. cpp client
 - [QPID-5529](https://issues.apache.org/jira/browse/QPID-5529) - [AMQP 1.0] invalid property type not handled correctly
 - [QPID-5530](https://issues.apache.org/jira/browse/QPID-5530) - [legacystore] store_chk raises "Operation on non-existent record: operation=unlock; rid=.." on aborted DTX transaction in TplStore 
 - [QPID-5531](https://issues.apache.org/jira/browse/QPID-5531) - [C++ broker] Set timeout for every DTX transaction
 - [QPID-5532](https://issues.apache.org/jira/browse/QPID-5532) - [C++ broker] Add debug log when timeouting DTX transaction
 - [QPID-5534](https://issues.apache.org/jira/browse/QPID-5534) - [C++ broker] Headers exchange can route a message to one queue multiple times
 - [QPID-5541](https://issues.apache.org/jira/browse/QPID-5541) - HA incorrect options for expected-backups in qpid-ha tool.
 - [QPID-5544](https://issues.apache.org/jira/browse/QPID-5544) - HA memory leak in backup broker after shutdown.
 - [QPID-5546](https://issues.apache.org/jira/browse/QPID-5546) - Perl bindings use encode/decode instead of getContentObject/setContentObject
 - [QPID-5547](https://issues.apache.org/jira/browse/QPID-5547) - [Java Broker] When handling rejects in 0-8/9/9-1 treat queues with no max delivery set as having infinite max delivery, rather than max delivery of 1
 - [QPID-5548](https://issues.apache.org/jira/browse/QPID-5548) - C++ Messaging API does not specify the connection Connection URL format
 - [QPID-5552](https://issues.apache.org/jira/browse/QPID-5552) - Client abrupt stop causes QPID Server crash
 - [QPID-5556](https://issues.apache.org/jira/browse/QPID-5556) - Update qpid.pm and qpid_messaging.pm to export the proper package
 - [QPID-5557](https://issues.apache.org/jira/browse/QPID-5557) - Can't disambiguate name for which both queue and exchange exist
 - [QPID-5565](https://issues.apache.org/jira/browse/QPID-5565) - [C++ broker] ACL queue create rules to take zero as unlimited value
 - [QPID-5568](https://issues.apache.org/jira/browse/QPID-5568) - HA C++ qpid::messaging AMQP 1.0 client failover logging is not clear.
 - [QPID-5569](https://issues.apache.org/jira/browse/QPID-5569) - NullPointerException if message prop's userId is null
 - [QPID-5570](https://issues.apache.org/jira/browse/QPID-5570) - [JMS AMQP 1.0 Client] Client incorrectly acknowledges pre-fetched messages with CLIENT_ACK
 - [QPID-5571](https://issues.apache.org/jira/browse/QPID-5571) - [Java Broker] [AMQP 1.0] Broker can deadlock if a consumer is closed while it is sending messages
 - [QPID-5575](https://issues.apache.org/jira/browse/QPID-5575) - C++ .NET Binding csharp.map.receiver example throws referencing connectionOptions arg
 - [QPID-5576](https://issues.apache.org/jira/browse/QPID-5576) - javax.naming.NamingException in org.apache.qpid.amqp_1_0.jms.jndi.PropertiesFileInitialContextFactory.getInitialContext()
 - [QPID-5584](https://issues.apache.org/jira/browse/QPID-5584) - [AMQP 1.0] LinkError thrown when NotFound is expected
 - [QPID-5586](https://issues.apache.org/jira/browse/QPID-5586) - qpid::messaging::Session::nextReceiver needs to be able to throw a distinct exception if the session is closed
 - [QPID-5587](https://issues.apache.org/jira/browse/QPID-5587) - QMF to track queue owner (userId)
 - [QPID-5588](https://issues.apache.org/jira/browse/QPID-5588) - Python client fails if socket fd &gt; FD_SETSIZE
 - [QPID-5589](https://issues.apache.org/jira/browse/QPID-5589) - C++ Windows install fails for qmfgen when Python is in "C:\Program Files"
 - [QPID-5594](https://issues.apache.org/jira/browse/QPID-5594) - [amqp1.0] missing first-acquirer property support in C++ broker
 - [QPID-5596](https://issues.apache.org/jira/browse/QPID-5596) - [Java Broker] Address bugs identified by Findbugs
 - [QPID-5597](https://issues.apache.org/jira/browse/QPID-5597) - [C++ client] Topic subscriptions should not ignore auto-delete x-declare flag
 - [QPID-5602](https://issues.apache.org/jira/browse/QPID-5602) - reduce severity and improve IOException logging in IoSender
 - [QPID-5608](https://issues.apache.org/jira/browse/QPID-5608) -  [amqp1.0] delete-on-close policy do not work for producers to exchanges
 - [QPID-5613](https://issues.apache.org/jira/browse/QPID-5613) - C++ ACL self test fails when broker doesn't start (missing --interface option)
 - [QPID-5623](https://issues.apache.org/jira/browse/QPID-5623) - [C++ Messaging Client - amqp1.0] throws qpid::Exception instead of qpid::types::Exception
 - [QPID-5630](https://issues.apache.org/jira/browse/QPID-5630) - Windows C++ broker never finds modules in module directory
 - [QPID-5631](https://issues.apache.org/jira/browse/QPID-5631) - Adjust Cmake build files to change in detecting proton
 - [QPID-5633](https://issues.apache.org/jira/browse/QPID-5633) - [Java Broker] Setting of attribute on http management plugin corrupts the broker configuration store
 - [QPID-5637](https://issues.apache.org/jira/browse/QPID-5637) - Python client does not reset the Selector singleton when the process id changes.
 - [QPID-5640](https://issues.apache.org/jira/browse/QPID-5640) - JsonFileConfigStore does not save bindings
 - [QPID-5641](https://issues.apache.org/jira/browse/QPID-5641) - [legacystore] Valgrind reports memory leaks on older store tests
 - [QPID-5646](https://issues.apache.org/jira/browse/QPID-5646) - Can't build against any released version of proton
 - [QPID-5648](https://issues.apache.org/jira/browse/QPID-5648) - basic C++ AMQP 1.0 ssl client connections broken
 - [QPID-5652](https://issues.apache.org/jira/browse/QPID-5652) - RDMA dependencies are not listed in INSTALL
 - [QPID-5658](https://issues.apache.org/jira/browse/QPID-5658) - C++ code not compiling with libc++
 - [QPID-5659](https://issues.apache.org/jira/browse/QPID-5659) - C++ not compiling (correctly) as C++11
 - [QPID-5669](https://issues.apache.org/jira/browse/QPID-5669) - "SSL negotiation failed" spurious error on connection close (Windows C++)
 - [QPID-5673](https://issues.apache.org/jira/browse/QPID-5673) - [Java Broker] NPE when attempting to connect to an unknown Virtual Host using AMQP 1.0
 - [QPID-5681](https://issues.apache.org/jira/browse/QPID-5681) - c++ broker: Fix core dump interlink tests
 - [QPID-5694](https://issues.apache.org/jira/browse/QPID-5694) - Windows C++ broker SSL sends non-existent negotiation token on shutdown
 - [QPID-5696](https://issues.apache.org/jira/browse/QPID-5696) - perl qpid client's qpid::messaging::Message() does not handle properly floats (non-quoted) in message properties
 - [QPID-5697](https://issues.apache.org/jira/browse/QPID-5697) - An exchange is deleted by a request for topic removal
 - [QPID-5700](https://issues.apache.org/jira/browse/QPID-5700) - heartbeat interleaved with message frames causes decode error
 - [QPID-5739](https://issues.apache.org/jira/browse/QPID-5739) - [AMQP 1.0 JMS Client] Hello example configuration does not work.
 - [QPID-5764](https://issues.apache.org/jira/browse/QPID-5764) - [Java] add a note detailing the move to the Maven build for future releases

## Tasks

 - [QPID-5065](https://issues.apache.org/jira/browse/QPID-5065) - [Java] tests do not run on Windows
 - [QPID-5581](https://issues.apache.org/jira/browse/QPID-5581) - [Java Broker] Rename SimpleAMQQueue to AbstractQueue
 - [QPID-5674](https://issues.apache.org/jira/browse/QPID-5674) - 0.28 beta1 'java release' includes test output
 - [QPID-5675](https://issues.apache.org/jira/browse/QPID-5675) - [Java Broker] remove unused xalan dependency
 - [QPID-5676](https://issues.apache.org/jira/browse/QPID-5676) - [Java Broker] change the BCEL dependency to match the Ant build
 - [QPID-5677](https://issues.apache.org/jira/browse/QPID-5677) - [Java] update the LICENSE and NOTICE files in various release artifacts