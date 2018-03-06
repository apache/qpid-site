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

# Qpid Proton 0.21.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1762](https://issues.apache.org/jira/browse/PROTON-1762) - [ruby] gem does not contain examples or tests
 - [PROTON-1768](https://issues.apache.org/jira/browse/PROTON-1768) - Allow tox tests of pyPI dist packaging on all platforms

## Bugs fixed

 - [PROTON-927](https://issues.apache.org/jira/browse/PROTON-927) - absolute-expiry-time, creation-time are encoded as 0 if not set rather than null
 - [PROTON-1174](https://issues.apache.org/jira/browse/PROTON-1174) - Proton C encodes Open.channel-max 0 as a null and not as a uint.
 - [PROTON-1505](https://issues.apache.org/jira/browse/PROTON-1505) - Message header defaults only work if no header present
 - [PROTON-1734](https://issues.apache.org/jira/browse/PROTON-1734) - [cpp] container.stop() doesn't work when called from non-proactor thread.
 - [PROTON-1738](https://issues.apache.org/jira/browse/PROTON-1738) - [ruby-binding] incompatible with ruby 2.0.0
 - [PROTON-1757](https://issues.apache.org/jira/browse/PROTON-1757) - pn_netaddr_host_port() fails on FreeBSD
 - [PROTON-1758](https://issues.apache.org/jira/browse/PROTON-1758) - [Python binding] Check message application property keys, convert binary to string
 - [PROTON-1766](https://issues.apache.org/jira/browse/PROTON-1766) - [cpp] seg fault in reconnect test
 - [PROTON-1769](https://issues.apache.org/jira/browse/PROTON-1769) - PyPI package python-qpid-proton doesn't pip install on MacOS X
 - [PROTON-1772](https://issues.apache.org/jira/browse/PROTON-1772) - Remove thread race in proactor locking of listener_context
 - [PROTON-1773](https://issues.apache.org/jira/browse/PROTON-1773) - Access after free in pn_proactor_disconnect
 - [PROTON-1776](https://issues.apache.org/jira/browse/PROTON-1776) - [ruby] on_sender/receiver_open/close events are not generated

## Tasks

 - [PROTON-1752](https://issues.apache.org/jira/browse/PROTON-1752) - 0.21.0 release tasks