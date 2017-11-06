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

# Qpid Proton 0.18.1 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1622](https://issues.apache.org/jira/browse/PROTON-1622) - Add coverage reporting to CMake build
 - [PROTON-1663](https://issues.apache.org/jira/browse/PROTON-1663) - [ruby]  use cmake status messages, not warnings if ruby deps not found

## Bugs fixed

 - [PROTON-1176](https://issues.apache.org/jira/browse/PROTON-1176) - Core dump if reactor creation fails
 - [PROTON-1597](https://issues.apache.org/jira/browse/PROTON-1597) - Warnings when executing cmake in the examples/c directory
 - [PROTON-1620](https://issues.apache.org/jira/browse/PROTON-1620) - TLS / SSL thread safety with proactor
 - [PROTON-1628](https://issues.apache.org/jira/browse/PROTON-1628) - [cpp] Stopping container in on_container_start will hang
 - [PROTON-1639](https://issues.apache.org/jira/browse/PROTON-1639) - proton.c ipv6 test does not detect lack of ipv6 support
 - [PROTON-1650](https://issues.apache.org/jira/browse/PROTON-1650) - Missing extern "C" {} declaration in proton/netaddr.h
 - [PROTON-1652](https://issues.apache.org/jira/browse/PROTON-1652) - [Windows] C Example tests fail
 - [PROTON-1655](https://issues.apache.org/jira/browse/PROTON-1655) - go-test TestAuthPlain fails when SASL_IMPL is none
 - [PROTON-1659](https://issues.apache.org/jira/browse/PROTON-1659) - Some of the test python will not run under python  3
 - [PROTON-1660](https://issues.apache.org/jira/browse/PROTON-1660) - The gemspec dependency on "json ~&gt; 0" breaks anyone dependning on a recent version of json
 - [PROTON-1662](https://issues.apache.org/jira/browse/PROTON-1662) - Proton-c fails to compile with no cyrus SASL but OpenSSL
 - [PROTON-1664](https://issues.apache.org/jira/browse/PROTON-1664) - C++ binding examples fail to build stand lone
 - [PROTON-1666](https://issues.apache.org/jira/browse/PROTON-1666) - Erroneous fix for PROTON-1616 would trim final character of ANONYMOUS username
 - [PROTON-1667](https://issues.apache.org/jira/browse/PROTON-1667) - Fix most coverity errors remaining in proton-c 0.18

## Tasks

 - [PROTON-1668](https://issues.apache.org/jira/browse/PROTON-1668) - 0.18.1 release tasks