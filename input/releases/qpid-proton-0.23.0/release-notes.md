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

# Qpid Proton 0.23.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-636](https://issues.apache.org/jira/browse/PROTON-636) - remove confusing default for session capacity and allow disabling it
 - [PROTON-1823](https://issues.apache.org/jira/browse/PROTON-1823) - [c] make it easier to send a message
 - [PROTON-1826](https://issues.apache.org/jira/browse/PROTON-1826) - [go] Add Messge.String() method for human-readable message printing

## Bugs fixed

 - [PROTON-1514](https://issues.apache.org/jira/browse/PROTON-1514) - [proton-c] When last frame of multi-frame transfer has settled=true, Proton still considers delivery as unsettled
 - [PROTON-1809](https://issues.apache.org/jira/browse/PROTON-1809) - [python, ruby] Unable to receive messages when max-frame-size is set to more than 2^20
 - [PROTON-1815](https://issues.apache.org/jira/browse/PROTON-1815) - [C++ binding]  Complex types: List containing array of std::nullptr_t fails compilation
 - [PROTON-1818](https://issues.apache.org/jira/browse/PROTON-1818) - [C++ binding] Complex types: list of nulls causes SIGABRT
 - [PROTON-1820](https://issues.apache.org/jira/browse/PROTON-1820) - [ruby] Container#schedule does not work if called from handler
 - [PROTON-1821](https://issues.apache.org/jira/browse/PROTON-1821) - link name is not correctly set from sender or receiver options
 - [PROTON-1822](https://issues.apache.org/jira/browse/PROTON-1822) - Running C/C++ Example tests under python 3 produces warnings
 - [PROTON-1825](https://issues.apache.org/jira/browse/PROTON-1825) - PyPI package python-qpid-proton doesn't pip install on MacOS X or FreeBSD
 - [PROTON-1830](https://issues.apache.org/jira/browse/PROTON-1830) - [ruby] sporadic failure of ruby tests
 - [PROTON-1832](https://issues.apache.org/jira/browse/PROTON-1832) - [c] duplicate link names cause invalid read in pn_transport_unbind_handles
 - [PROTON-1841](https://issues.apache.org/jira/browse/PROTON-1841) - [cpp] add missing ostream&lt;&lt; and to_string for proton::message
 - [PROTON-1844](https://issues.apache.org/jira/browse/PROTON-1844) - Windows proactor memory corruption on cleanup
 - [PROTON-1845](https://issues.apache.org/jira/browse/PROTON-1845) - [c] Treat attach received after detach as implying new link 
 - [PROTON-1847](https://issues.apache.org/jira/browse/PROTON-1847) - container:schedule used from an external thread can stop container::run loop processing other events
