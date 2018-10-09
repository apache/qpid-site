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

# Qpid Proton 0.26.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1888](https://issues.apache.org/jira/browse/PROTON-1888) - [python] Allow configuration of connection details via a simple config file
 - [PROTON-1935](https://issues.apache.org/jira/browse/PROTON-1935) - [cpp] Read a config file to get default connection parameters 
 - [PROTON-1940](https://issues.apache.org/jira/browse/PROTON-1940) - [c] normalize encoding of multiple="true" fields

## Bugs fixed

 - [PROTON-1928](https://issues.apache.org/jira/browse/PROTON-1928) - install static libraries
 - [PROTON-1929](https://issues.apache.org/jira/browse/PROTON-1929) - [c] library prints directly to stderr/stdout
 - [PROTON-1934](https://issues.apache.org/jira/browse/PROTON-1934) - [Python] Backoff class is not exported by reactor
 - [PROTON-1942](https://issues.apache.org/jira/browse/PROTON-1942) - [c] decoding a message does not set the inferred flag.