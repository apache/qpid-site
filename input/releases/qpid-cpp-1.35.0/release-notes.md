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

# Qpid C++ 1.35.0 Release Notes

Qpid C++ offers a connection-oriented messaging API supporting many
programming languages and a message broker written in C++ that stores,
routes, and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-2549](https://issues.apache.org/jira/browse/QPID-2549) - Port qpid to FreeBSD
 - [QPID-4397](https://issues.apache.org/jira/browse/QPID-4397) - C++ Broker Improve log statement for expired messages
 - [QPID-6391](https://issues.apache.org/jira/browse/QPID-6391) - [C++ Broker] [AMQP 1.0] add support for a 'no-local' filter
 - [QPID-6665](https://issues.apache.org/jira/browse/QPID-6665) - update hello_world.cpp example to use setContentObject
 - [QPID-6730](https://issues.apache.org/jira/browse/QPID-6730) - Make the journal flush timeout configurable in the C++ broker
 - [QPID-6757](https://issues.apache.org/jira/browse/QPID-6757) - [linearstore] Add qpid-txtest mode to qpid-qls-analyze which extracts message number from message body
 - [QPID-6783](https://issues.apache.org/jira/browse/QPID-6783) - qpidd should dynamically set the SASL service name based on protocol.
 - [QPID-7130](https://issues.apache.org/jira/browse/QPID-7130) - qpid C++ with SSL authentication returning dummy string from Connection::getAuthenticatedUsername()
 - [QPID-7171](https://issues.apache.org/jira/browse/QPID-7171) - Allow disable-auto-decode to be set via env var or conf file
 - [QPID-7281](https://issues.apache.org/jira/browse/QPID-7281) - Get the tests running on Windows

## Bugs fixed

 - [QPID-5855](https://issues.apache.org/jira/browse/QPID-5855) - JAVA Client Can not recieve message with qpid ha cluster "Session exception occured while trying to commit"
 - [QPID-6308](https://issues.apache.org/jira/browse/QPID-6308) - [C++ Messaging] Server example never sends utf8 responses
 - [QPID-6435](https://issues.apache.org/jira/browse/QPID-6435) - No error info logged for io errors with ssl
 - [QPID-6491](https://issues.apache.org/jira/browse/QPID-6491) - qpid-route map does not use any authentication when querying other brokers
 - [QPID-6577](https://issues.apache.org/jira/browse/QPID-6577) - HA - backup broker messages are larger than primary messages.
 - [QPID-6639](https://issues.apache.org/jira/browse/QPID-6639) - Incoming connection using "cut-through" ANONYMOUS SASL fails
 - [QPID-6648](https://issues.apache.org/jira/browse/QPID-6648) - Spelling, grammar errors in qpid::messaging::Receiver API doc
 - [QPID-6654](https://issues.apache.org/jira/browse/QPID-6654) - mgmt-disable option set to false causes segv on CentOS 6.3
 - [QPID-6659](https://issues.apache.org/jira/browse/QPID-6659) - [AMQP 1.0] qpid::messaging can't handle multi-frame transfers
 - [QPID-6660](https://issues.apache.org/jira/browse/QPID-6660) - [AMQP 1.0] broker attempts to process incoming messages for closed session
 - [QPID-6661](https://issues.apache.org/jira/browse/QPID-6661) - [AMQP 1.0] heartbeat anomalies
 - [QPID-6668](https://issues.apache.org/jira/browse/QPID-6668) - [C++] INSTALL-WINDOWS is out of date
 - [QPID-6698](https://issues.apache.org/jira/browse/QPID-6698) - [amqp1.0] connections drop when heartbeat is used and the time of day changes
 - [QPID-6714](https://issues.apache.org/jira/browse/QPID-6714) - Add support for JMSHeaders in selectors
 - [QPID-6717](https://issues.apache.org/jira/browse/QPID-6717) - selector can match incorrectly due to different type for values
 - [QPID-6718](https://issues.apache.org/jira/browse/QPID-6718) - parsing errors for integer literals in selectors
 - [QPID-6767](https://issues.apache.org/jira/browse/QPID-6767) - qpidd tools don't allow sasl service name to be changed
 - [QPID-6790](https://issues.apache.org/jira/browse/QPID-6790) - qpidd crashes in the interop_tests unit test.
 - [QPID-6834](https://issues.apache.org/jira/browse/QPID-6834) - allow lifetime of delete-on-close in queue policy
 - [QPID-6858](https://issues.apache.org/jira/browse/QPID-6858) - Port all python swig input files to support python 3 and 2
 - [QPID-6870](https://issues.apache.org/jira/browse/QPID-6870) - [AMQP 1.0]: qpidd does not honour the undeliverable-here field of MODIFIED disposition
 - [QPID-6924](https://issues.apache.org/jira/browse/QPID-6924) - Qpidd fails to compile against trunk 0.12-SNAPSHOT proton-c
 - [QPID-6966](https://issues.apache.org/jira/browse/QPID-6966) - C++ broker and client to support TLS1.1 and TLS1.2 by default
 - [QPID-7010](https://issues.apache.org/jira/browse/QPID-7010) - assertion failure if disposition sent for previously settled delivery
 - [QPID-7020](https://issues.apache.org/jira/browse/QPID-7020) - uint16 AMQP0-10 message properties decoded as uint8
 - [QPID-7100](https://issues.apache.org/jira/browse/QPID-7100) - qpid-perftest divide by zero when mode is shared and nsubs is zero
 - [QPID-7127](https://issues.apache.org/jira/browse/QPID-7127) - [C++ broker] Setting large idle timeout cause confuses timers in the C++ broker
 - [QPID-7131](https://issues.apache.org/jira/browse/QPID-7131) - snd-settle-mode advertised is always 'mixed'
 - [QPID-7134](https://issues.apache.org/jira/browse/QPID-7134) - [C++ client] Message::setContent("") does not work
 - [QPID-7137](https://issues.apache.org/jira/browse/QPID-7137) - Abi tests fail with new libstdc++ abi
 - [QPID-7145](https://issues.apache.org/jira/browse/QPID-7145) - auto_ptr is deprecated from C++11 and onwards and its use causes a warning with GCC 6
 - [QPID-7147](https://issues.apache.org/jira/browse/QPID-7147) - When compiling with C++11/14 bind() use gets found as std::bind()
 - [QPID-7149](https://issues.apache.org/jira/browse/QPID-7149) - [HA] active HA broker memory leak when ring queue discards overflow messages
 - [QPID-7182](https://issues.apache.org/jira/browse/QPID-7182) - [C++ broker] high CPU usage on backup brokers following QPID-7149 scenario
 - [QPID-7225](https://issues.apache.org/jira/browse/QPID-7225) - PriorityQueue doesn't check that released message is acquired
 - [QPID-7233](https://issues.apache.org/jira/browse/QPID-7233) - qpid-receive uses 0 prefetch unless an explicit message count is provided
 - [QPID-7234](https://issues.apache.org/jira/browse/QPID-7234) - client does not update credit for expired messages
 - [QPID-7235](https://issues.apache.org/jira/browse/QPID-7235) - Observers should have a virtual destructor
 - [QPID-7240](https://issues.apache.org/jira/browse/QPID-7240) - acquired messages are not evicted from priority-ring queue
 - [QPID-7250](https://issues.apache.org/jira/browse/QPID-7250) - Durable message that exceeds page queue size prevents broker restart
 - [QPID-7302](https://issues.apache.org/jira/browse/QPID-7302) - race between auto-delete and re-declare/consume 
 - [QPID-7306](https://issues.apache.org/jira/browse/QPID-7306) - Fix memory bugs and race conditions found in a Qpid HA deployment
 - [QPID-7324](https://issues.apache.org/jira/browse/QPID-7324) - [AMQP 1.0] support 'undeliverable-here' field for MODIFIED outcome
 - [QPID-7326](https://issues.apache.org/jira/browse/QPID-7326) - Memory bloat on HA primary broker
 - [QPID-7329](https://issues.apache.org/jira/browse/QPID-7329) - [AMQP 1.0]: support message-annotations field for MODIFIED outcome
 - [QPID-7357](https://issues.apache.org/jira/browse/QPID-7357) - c++ HA Backup crash during re-connect in failover
 - [QPID-7361](https://issues.apache.org/jira/browse/QPID-7361) - [AMQP-1.0] sender sometimes waits for credit without flushing buffered transfers to disk
 - [QPID-7373](https://issues.apache.org/jira/browse/QPID-7373) - memory leak in broker with idle worker threads
 - [QPID-7376](https://issues.apache.org/jira/browse/QPID-7376) - fetch with capacity=0 can hang or timeout if fetched message expires client-side
 - [QPID-7383](https://issues.apache.org/jira/browse/QPID-7383) - [linearstore] Overwrite-before-return causes latencies for clients
 - [QPID-7393](https://issues.apache.org/jira/browse/QPID-7393) - Unavailable buffers in Windows SSL