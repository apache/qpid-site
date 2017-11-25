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

# Qpid C++ 1.37.0 Release Notes

Qpid C++ offers a connection-oriented messaging API supporting many
programming languages and a message broker written in C++ that stores,
routes, and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7574](https://issues.apache.org/jira/browse/QPID-7574) - Make management libraries Python 3 compatible
 - [QPID-7629](https://issues.apache.org/jira/browse/QPID-7629) - Use CMake "SYSTEM" keyword when including headers
 - [QPID-7666](https://issues.apache.org/jira/browse/QPID-7666) - [linearstore] Enhancements to the write buffer default and per-queue options
 - [QPID-7677](https://issues.apache.org/jira/browse/QPID-7677) - [C++ broker] broker requires much more memory for AMQP1.0 subscription than for 0-10 one
 - [QPID-7698](https://issues.apache.org/jira/browse/QPID-7698) - Minor doc improvements
 - [QPID-7714](https://issues.apache.org/jira/browse/QPID-7714) - Suppress auto_ptr warnings
 - [QPID-7715](https://issues.apache.org/jira/browse/QPID-7715) - [linearstore] Documentation on upgrading from pre-partition to partitioned version of store
 - [QPID-7861](https://issues.apache.org/jira/browse/QPID-7861) - [cpp] Provide systemd scripts for Fedora
 - [QPID-7874](https://issues.apache.org/jira/browse/QPID-7874) - qpid-route performs an unnecessary link check when adding routes
 - [QPID-7875](https://issues.apache.org/jira/browse/QPID-7875) - qpid-route fetches links multiple times when deleting routes
 - [QPID-8041](https://issues.apache.org/jira/browse/QPID-8041) - [Messaging] Allow virtualhost to be specified when form an AMQP 0-10 connection

## Bugs fixed

 - [QPID-7595](https://issues.apache.org/jira/browse/QPID-7595) - [C++ Windows] CMake required version is too low for installation
 - [QPID-7651](https://issues.apache.org/jira/browse/QPID-7651) - [linearstore] Using write page cache sizes of 1 and 2 (kiB) cause floating point exception on startup
 - [QPID-7669](https://issues.apache.org/jira/browse/QPID-7669) - Unintended UI changes from switch to swigged Python client for management tools
 - [QPID-7671](https://issues.apache.org/jira/browse/QPID-7671) - Problem building on debian (unstable) distribution:
 - [QPID-7674](https://issues.apache.org/jira/browse/QPID-7674) - Broker bulid problem with GCC 7
 - [QPID-7693](https://issues.apache.org/jira/browse/QPID-7693) - SSL client socket leaks a file descriptor
 - [QPID-7702](https://issues.apache.org/jira/browse/QPID-7702) - Use of 'return NULL' in swig binding leaks memory
 - [QPID-7713](https://issues.apache.org/jira/browse/QPID-7713) - Clang build fails with link error
 - [QPID-7786](https://issues.apache.org/jira/browse/QPID-7786) - qpidd segfaults during startup when SSL certificate cant be read
 - [QPID-7788](https://issues.apache.org/jira/browse/QPID-7788) - Linearstore doesnt move to EFP latest journal files when deleting a durable queue
 - [QPID-7847](https://issues.apache.org/jira/browse/QPID-7847) - qmf.client.BrokerAgent does not provide reconnect support
 - [QPID-7859](https://issues.apache.org/jira/browse/QPID-7859) - [AMQP 1.0]: sending message to an exchange that exceeds the limit of a queue with reject policy results in connection being closed
 - [QPID-7860](https://issues.apache.org/jira/browse/QPID-7860) - [cpp] Build produces deprecation warnings on recent Fedora
 - [QPID-7871](https://issues.apache.org/jira/browse/QPID-7871) - Batch file for Windows is missing from qpid-tools setup package
 - [QPID-7876](https://issues.apache.org/jira/browse/QPID-7876) - qpid-route does not properly consider src-local when matching bridges
 - [QPID-7893](https://issues.apache.org/jira/browse/QPID-7893) - compilation failure on Fedora 26
 - [QPID-7895](https://issues.apache.org/jira/browse/QPID-7895) - [linearstore] Excessive CPU utilization for some kernel clocksources
 - [QPID-7901](https://issues.apache.org/jira/browse/QPID-7901) - Prevent endless detach cycle
 - [QPID-7929](https://issues.apache.org/jira/browse/QPID-7929) - [c++ broker] missing extern fails compile on Windows
 - [QPID-7975](https://issues.apache.org/jira/browse/QPID-7975) - [linearstore] Sending durable messages using AMQP 1.0 and 0-10 concurrently causes high latency for 1.0 messages
 - [QPID-7991](https://issues.apache.org/jira/browse/QPID-7991) - Segfault in broker while processing active bridges
 - [QPID-8037](https://issues.apache.org/jira/browse/QPID-8037) - Compile error on Windows, Visual Studio 2017

## Tasks

 - [QPID-7920](https://issues.apache.org/jira/browse/QPID-7920) - Qpid C++ 1.37.0 release tasks