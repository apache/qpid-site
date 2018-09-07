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

# Qpid Proton 0.25.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).

NOTE: Dispatch 1.3.0 builds against Proton 0.25.0, but a number of tests will
fail due to import errors. A patch can be found on
[DISPATCH-1108](https://issues.apache.org/jira/browse/DISPATCH-1108)
to resolve these test failures until a newer release of Dispatch is available.

## New features and improvements

 - [PROTON-1816](https://issues.apache.org/jira/browse/PROTON-1816) - [c] deprecate old netaddr function names
 - [PROTON-1878](https://issues.apache.org/jira/browse/PROTON-1878) - Improve cmake modularity - split out library detection code
 - [PROTON-1879](https://issues.apache.org/jira/browse/PROTON-1879) - Update cmake so that it uses the easier to use imported target feature
 - [PROTON-1885](https://issues.apache.org/jira/browse/PROTON-1885) - [python] move tests/python to python/tests
 - [PROTON-1886](https://issues.apache.org/jira/browse/PROTON-1886) - Expose diagnostic information from the openssl error queue when SSL_new fails.
 - [PROTON-1918](https://issues.apache.org/jira/browse/PROTON-1918) - Make CMake tests use more modern idiomatic cmake
 - [PROTON-1919](https://issues.apache.org/jira/browse/PROTON-1919) - [Python] Remove all use of messenger symbols
 - [PROTON-1921](https://issues.apache.org/jira/browse/PROTON-1921) - Various doc updates
 - [PROTON-1922](https://issues.apache.org/jira/browse/PROTON-1922) - [Python] Further restrict symbols exported by python binding

## Bugs fixed

 - [PROTON-1842](https://issues.apache.org/jira/browse/PROTON-1842) - [c] Dispatch/Proton crashes when opening/closing connections
 - [PROTON-1874](https://issues.apache.org/jira/browse/PROTON-1874) - Valgrind complains about epoll_ctl accessing uninitialised data
 - [PROTON-1875](https://issues.apache.org/jira/browse/PROTON-1875) - [Ruby] Error running ruby-test-container on Raspbian Jesse
 - [PROTON-1877](https://issues.apache.org/jira/browse/PROTON-1877) - rubygem doc is not multilib-clean for x86_64 vs i686
 - [PROTON-1880](https://issues.apache.org/jira/browse/PROTON-1880) - "make install" doesn't install pdbs for proton-core and proton-proactor libs
 - [PROTON-1881](https://issues.apache.org/jira/browse/PROTON-1881) - C++ code is not built with warning flags
 - [PROTON-1882](https://issues.apache.org/jira/browse/PROTON-1882) - [cpp] cannot send message properties with null values
 - [PROTON-1884](https://issues.apache.org/jira/browse/PROTON-1884) - [c] example broker does not configure SASL correctly
 - [PROTON-1896](https://issues.apache.org/jira/browse/PROTON-1896) - Python binding doesn't work correctly with IPv6 literals on python 2.6.6
 - [PROTON-1903](https://issues.apache.org/jira/browse/PROTON-1903) - Bugs found by the OSS Fuzz project
 - [PROTON-1912](https://issues.apache.org/jira/browse/PROTON-1912) - [ruby] gem build fails with very recent versions of cmake
