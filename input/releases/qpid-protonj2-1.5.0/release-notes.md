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

# Qpid ProtonJ2 1.5.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [PROTON-2993](https://issues.apache.org/jira/browse/PROTON-2993) - [protonj2] Binary decoder should not allow long references to pooled buffer slices
 - [PROTON-2995](https://issues.apache.org/jira/browse/PROTON-2995) - [protonj2] Closing a link blocks until the close timeout when the remote ends the session instead of answering the detach
 - [PROTON-2996](https://issues.apache.org/jira/browse/PROTON-2996) - [protonj2] Connection default session is not replaced after the remote ends it
 - [PROTON-2997](https://issues.apache.org/jira/browse/PROTON-2997) - [protonj2] Timestamp encoder writing incorrect encoding code for arrays
 - [PROTON-3001](https://issues.apache.org/jira/browse/PROTON-3001) - [protonj2] Symbol InputStream based decoder fails on size greater than 127
 - [PROTON-3002](https://issues.apache.org/jira/browse/PROTON-3002) - [protonj2] Encoder and Decoder not fully thread safe 

## Tasks

 - [PROTON-2998](https://issues.apache.org/jira/browse/PROTON-2998) - [protonj2] Clean up of API docs, error messages and logging
 - [PROTON-2999](https://issues.apache.org/jira/browse/PROTON-2999) - [protonj2] Update netty to latest release
 - [PROTON-3000](https://issues.apache.org/jira/browse/PROTON-3000) - [protonj2] Update jacoco plugin to 0.8.16