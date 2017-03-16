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

# Qpid Python 1.36.0 Release Notes

Qpid Python includes an AMQP messaging library and a suite of tests
for AMQP conformance.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [QPID-7317](https://issues.apache.org/jira/browse/QPID-7317) - Deadlock on publish
 - [QPID-7423](https://issues.apache.org/jira/browse/QPID-7423) - [0-8...0-91] Chunk message content that exceeds the capacity of a single frame into multiple frames
 - [QPID-7424](https://issues.apache.org/jira/browse/QPID-7424) - [0-8..0-91] Consuming python client application is not notified of remotely closed connection
 - [QPID-7588](https://issues.apache.org/jira/browse/QPID-7588) - [Python Client 0-8..0-91] The received message ocasionally might not be dispatched into the application queue in timely manner