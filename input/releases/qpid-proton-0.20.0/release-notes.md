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

# Qpid Proton 0.20.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1706](https://issues.apache.org/jira/browse/PROTON-1706) - pn_listener_t provide access to actual listening port
 - [PROTON-1733](https://issues.apache.org/jira/browse/PROTON-1733) - [cpp] Provide access to actual listening port for listen(":0")
 - [PROTON-1742](https://issues.apache.org/jira/browse/PROTON-1742) - there is no send example that works well with selected_recv
 - [PROTON-1749](https://issues.apache.org/jira/browse/PROTON-1749) - Add a C++ example demonstrating the use of the SASL APis
 - [PROTON-1751](https://issues.apache.org/jira/browse/PROTON-1751) - Various doc improvements

## Bugs fixed

 - [PROTON-1644](https://issues.apache.org/jira/browse/PROTON-1644) - [FreeBSD] Scheme for reusing ports in testing does not work for FreeBSD
 - [PROTON-1682](https://issues.apache.org/jira/browse/PROTON-1682) - SASL auth with GSSAPI fails: hostname is not set
 - [PROTON-1705](https://issues.apache.org/jira/browse/PROTON-1705) - [go] binding puts build artifacts in the source tree
 - [PROTON-1726](https://issues.apache.org/jira/browse/PROTON-1726) - Using PN_TRACE_RAW causes segv
 - [PROTON-1727](https://issues.apache.org/jira/browse/PROTON-1727) - [epoll proactor] segfaults, hangs and leaked FDs around failed connect
 - [PROTON-1741](https://issues.apache.org/jira/browse/PROTON-1741) - selected_recv example doesn't work
 - [PROTON-1745](https://issues.apache.org/jira/browse/PROTON-1745) - [proton-c] PN_CONNECTION_BOUND event is emitted too soon
 - [PROTON-1747](https://issues.apache.org/jira/browse/PROTON-1747) - Building C++ binding fails if proton-c built without openssl and without cyrus-sasl

## Tasks

 - [PROTON-1719](https://issues.apache.org/jira/browse/PROTON-1719) - Extend compiler coverage in Windows CI