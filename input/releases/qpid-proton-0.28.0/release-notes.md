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

# Qpid Proton 0.28.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).

**Note**: An issue was identified preventing driving the Python binding container using an external event loop such as Tornado. This will be addressed in a future release.

## New features and improvements

 - [PROTON-1992](https://issues.apache.org/jira/browse/PROTON-1992) - [Python] Rework python binding to use only Proton Core library
 - [PROTON-2021](https://issues.apache.org/jira/browse/PROTON-2021) - [c] Make SSL/TLS usage more secure by default

## Bugs fixed

 - [PROTON-1467](https://issues.apache.org/jira/browse/PROTON-1467) - [python] setup.py script fails to build C sources on Windows
 - [PROTON-2007](https://issues.apache.org/jira/browse/PROTON-2007) - [python] Correct example tests for the case where the system python differs from the harness python
 - [PROTON-2015](https://issues.apache.org/jira/browse/PROTON-2015) - [cpp] listener::on_error() should throw by default
 - [PROTON-2019](https://issues.apache.org/jira/browse/PROTON-2019) - [Python] SSL Tests fail on Windows 10
 - [PROTON-2020](https://issues.apache.org/jira/browse/PROTON-2020) - [python] _io.py error path syntax error in python3
 - [PROTON-2023](https://issues.apache.org/jira/browse/PROTON-2023) - [cpp] [Windows] Json connect config file test won't build
 - [PROTON-2034](https://issues.apache.org/jira/browse/PROTON-2034) - [python] Selector string sent as illegal binary value if non-unicode string is used
 - [PROTON-2035](https://issues.apache.org/jira/browse/PROTON-2035) - [go] Inability to mock Golang interfaces
 - [PROTON-2038](https://issues.apache.org/jira/browse/PROTON-2038) - [Python] ubyte (and other unsigned types) can hold negative value
 - [PROTON-2039](https://issues.apache.org/jira/browse/PROTON-2039) - [python] set listener socket reuseaddr option

## Tasks

 - [PROTON-2025](https://issues.apache.org/jira/browse/PROTON-2025) - Azure Pipeline build definition