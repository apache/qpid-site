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

# Qpid Proton 0.36.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2254](https://issues.apache.org/jira/browse/PROTON-2254) - Relative paths in CMake share
 - [PROTON-2382](https://issues.apache.org/jira/browse/PROTON-2382) - [cpp] An accessor on tracker for the delivery tag
 - [PROTON-2399](https://issues.apache.org/jira/browse/PROTON-2399) - Support Python 3.10
 - [PROTON-2405](https://issues.apache.org/jira/browse/PROTON-2405) - [Python] Make python examples python 3 only
 - [PROTON-2407](https://issues.apache.org/jira/browse/PROTON-2407) - [proton-python] add type annotations
 - [PROTON-2425](https://issues.apache.org/jira/browse/PROTON-2425) - Tweak pn_buffer code to use memcpy instead of memmove
 - [PROTON-2427](https://issues.apache.org/jira/browse/PROTON-2427) - Avoid using pn_message_id()/pn_message_correlation_id() APIs in examples and bindings
 - [PROTON-2429](https://issues.apache.org/jira/browse/PROTON-2429) - [C] Introduce pn_msgid_t as an alias for pn_atom_t
 - [PROTON-2430](https://issues.apache.org/jira/browse/PROTON-2430) - [python] Modify binding to stop using potentially inefficient pn_message_id et al
 - [PROTON-2445](https://issues.apache.org/jira/browse/PROTON-2445) - Make codec encoder use short forms for  ULONG &amp; UINT 0

## Bugs fixed

 - [PROTON-2403](https://issues.apache.org/jira/browse/PROTON-2403) - libuv based proactor test errors
 - [PROTON-2411](https://issues.apache.org/jira/browse/PROTON-2411) - Simultaneous idle timeout sequencing errors on 32bit system
 - [PROTON-2413](https://issues.apache.org/jira/browse/PROTON-2413) - Python binding example runner can't run python examples
 - [PROTON-2422](https://issues.apache.org/jira/browse/PROTON-2422) - Proton will sometimes fail to send empty frame if the idle timeout ratio between peers is greater than 2. 
 - [PROTON-2424](https://issues.apache.org/jira/browse/PROTON-2424) - C++ example runner fails when run using ctest with valgrind checking
 - [PROTON-2426](https://issues.apache.org/jira/browse/PROTON-2426) - Fix off by one error in pn_quote_data
 - [PROTON-2433](https://issues.apache.org/jira/browse/PROTON-2433) - The work for PROTON-2254 seems to have broken modern use of CMake
 - [PROTON-2443](https://issues.apache.org/jira/browse/PROTON-2443) - Workaround bug in cyrus-sasl that expects zero terminated clientid in EXTERNAL mechanism
 - [PROTON-2444](https://issues.apache.org/jira/browse/PROTON-2444) - Valgrind spotted use of an uninitialised value
 - [PROTON-2446](https://issues.apache.org/jira/browse/PROTON-2446) - Raw data dumps don't backslash quote quotemarks!