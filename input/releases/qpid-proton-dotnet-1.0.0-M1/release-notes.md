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

# Qpid Proton Dotnet 1.0.0-M1 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2549](https://issues.apache.org/jira/browse/PROTON-2549) - [dotnet] Add a next receiver API to the connection and session 

## Tasks

 - [PROTON-2548](https://issues.apache.org/jira/browse/PROTON-2548) - Initial release tasks

# Errata note on building the 1.0.0-M1 release

The examples and unit tests included in the 1.0.0-M1 release will only
build and run on platforms with the .NET 5.0 Framework installed. The
next release will update the project files for the examples and tests 
to allow them to roll forward and work with later .NET installations

 - [PROTON-2560](https://issues.apache.org/jira/browse/PROTON-2560) - Running tests or examples can fail on system with only .NET 6 installed
