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

# Qpid Proton 0.29.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2040](https://issues.apache.org/jira/browse/PROTON-2040) - [cpp] Allow connection options to be updated for automatic reconnect.
 - [PROTON-2048](https://issues.apache.org/jira/browse/PROTON-2048) - Proton-C build process compiles a lot of files twice
 - [PROTON-2068](https://issues.apache.org/jira/browse/PROTON-2068) - Allow CMake builds using proton-c clients to import targets

## Bugs fixed

 - [PROTON-1473](https://issues.apache.org/jira/browse/PROTON-1473) - [cpp] Cryptic error message when connection fails because server end requires SASL
 - [PROTON-1977](https://issues.apache.org/jira/browse/PROTON-1977) - 'EndPointHandler' object has no attribute 'log_error'
 - [PROTON-1993](https://issues.apache.org/jira/browse/PROTON-1993) - Tests fail on Windows for release builds (without debug symbols)
 - [PROTON-2056](https://issues.apache.org/jira/browse/PROTON-2056) - [proton-python]  on_settled callback not called when disposition arrives in 2 frames
 - [PROTON-2061](https://issues.apache.org/jira/browse/PROTON-2061) - [C++] Sender auto settlement should only happen after receiving a settlement from the receiver
 - [PROTON-2062](https://issues.apache.org/jira/browse/PROTON-2062) - [ruby] Sender auto settlement should only happen after receiving a settlement from the receiver
 - [PROTON-2063](https://issues.apache.org/jira/browse/PROTON-2063) - [go] Sender auto settlement should only happen after receiving a settlement from the receiver
 - [PROTON-2067](https://issues.apache.org/jira/browse/PROTON-2067) - Enable linktime optimization by default
 - [PROTON-2073](https://issues.apache.org/jira/browse/PROTON-2073) - Travis CI build test fails on Ubuntu 1604
 - [PROTON-2074](https://issues.apache.org/jira/browse/PROTON-2074) - Using a connection url with characters that need to be urlencoded can cause a hang
 - [PROTON-2079](https://issues.apache.org/jira/browse/PROTON-2079) - Coverity issues related to printf on master branch
 - [PROTON-2081](https://issues.apache.org/jira/browse/PROTON-2081) - Hang in Windows proactor during connect
 - [PROTON-2087](https://issues.apache.org/jira/browse/PROTON-2087) - [Python] Detection of tox caches failure instaead of trying again if not initially found
 - [PROTON-2088](https://issues.apache.org/jira/browse/PROTON-2088) - [Python] Changing a python file and building does not ensure the changed file ends up in the installable

## Tasks

 - [PROTON-2053](https://issues.apache.org/jira/browse/PROTON-2053) - [Python] [C++] The Python and C++ bindings have different defaults for SASL