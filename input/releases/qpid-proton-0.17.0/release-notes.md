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

# Qpid Proton 0.17.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [PROTON-1312](https://issues.apache.org/jira/browse/PROTON-1312) - BlockingConnection leaks Proton-C memory
 - [PROTON-1376](https://issues.apache.org/jira/browse/PROTON-1376) - [C, windows] Release 0.16 build fail - src/protocol.h clobbered
 - [PROTON-1377](https://issues.apache.org/jira/browse/PROTON-1377) - proton-c core library was not installed
 - [PROTON-1378](https://issues.apache.org/jira/browse/PROTON-1378) - Two reactor final events generated
 - [PROTON-1379](https://issues.apache.org/jira/browse/PROTON-1379) - Compile without warnings under g++ 7.0
 - [PROTON-1380](https://issues.apache.org/jira/browse/PROTON-1380) - Cyrus SASL accesses strings that have been freed
 - [PROTON-1382](https://issues.apache.org/jira/browse/PROTON-1382) - Remove bit fields initialization for bool fields
 - [PROTON-1383](https://issues.apache.org/jira/browse/PROTON-1383) - Add missing includes to fix Solaris compilation
 - [PROTON-1388](https://issues.apache.org/jira/browse/PROTON-1388) - client fails to decrypt after sasl encryption is negotiated with qpidd
 - [PROTON-1389](https://issues.apache.org/jira/browse/PROTON-1389) - PROTON-1325: Repair broken fix for python "buffer" type.
 - [PROTON-1390](https://issues.apache.org/jira/browse/PROTON-1390) - Go fixes to build with gccgo
 - [PROTON-1391](https://issues.apache.org/jira/browse/PROTON-1391) - Passing NULL as a SASL selected mechanism is crashing pn_do_error on Solaris
 - [PROTON-1392](https://issues.apache.org/jira/browse/PROTON-1392) - SWIG doesn't define how to export symbols on Solaris
 - [PROTON-1395](https://issues.apache.org/jira/browse/PROTON-1395) - go: testing with -race fails on some platforms 

## Tasks

 - [PROTON-1385](https://issues.apache.org/jira/browse/PROTON-1385) - make proton-j independently releasable
 - [PROTON-1386](https://issues.apache.org/jira/browse/PROTON-1386) - disable the PHP binding build by default
 - [PROTON-1396](https://issues.apache.org/jira/browse/PROTON-1396) - 0.17.0 release tasks