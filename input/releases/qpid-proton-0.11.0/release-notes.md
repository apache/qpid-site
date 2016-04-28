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

# Qpid Proton 0.11.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-948](https://issues.apache.org/jira/browse/PROTON-948) - remove deprecated methods on the Message
 - [PROTON-964](https://issues.apache.org/jira/browse/PROTON-964) - Proton-J extensible event types
 - [PROTON-972](https://issues.apache.org/jira/browse/PROTON-972) - Support the heartbeat option in BlockingConnection
 - [PROTON-980](https://issues.apache.org/jira/browse/PROTON-980) - Enable handler processing the event after child handlers have processed it
 - [PROTON-981](https://issues.apache.org/jira/browse/PROTON-981) - Make JythonTest extendable
 - [PROTON-982](https://issues.apache.org/jira/browse/PROTON-982) - Make proton python tests compatible with unittest
 - [PROTON-984](https://issues.apache.org/jira/browse/PROTON-984) - Document proton-j time units
 - [PROTON-997](https://issues.apache.org/jira/browse/PROTON-997) - Allow proton-j handler to be extended by a jython class
 - [PROTON-1011](https://issues.apache.org/jira/browse/PROTON-1011) - Go example of plain event-driven broker.
 - [PROTON-1016](https://issues.apache.org/jira/browse/PROTON-1016) - Jython implements long with a BigInteger
 - [PROTON-1036](https://issues.apache.org/jira/browse/PROTON-1036) - c++: engine API for integration with external IO frameworks

## Bugs fixed

 - [PROTON-892](https://issues.apache.org/jira/browse/PROTON-892) - pn_data_t capacity does not grow above 32768 items
 - [PROTON-937](https://issues.apache.org/jira/browse/PROTON-937) - LinkImpl.localOpen() does not initialize source and target
 - [PROTON-949](https://issues.apache.org/jira/browse/PROTON-949) - proton doesn't build with ccache swig
 - [PROTON-952](https://issues.apache.org/jira/browse/PROTON-952) - Building Proton with python 2.6 and python 3.4 on Travis CI finds and links wrong libpython
 - [PROTON-971](https://issues.apache.org/jira/browse/PROTON-971) - [proton-j] multi-frame deliveries may be broken when sent if buffered along with a futher delivery for the same link
 - [PROTON-974](https://issues.apache.org/jira/browse/PROTON-974) - single symbol for mechanisms in sasl-mechanisms not recognised
 - [PROTON-977](https://issues.apache.org/jira/browse/PROTON-977) - handler appears to get ignored
 - [PROTON-990](https://issues.apache.org/jira/browse/PROTON-990) - [C++ binding] Examples fail to link in Visual Studio 2012, 2015
 - [PROTON-1003](https://issues.apache.org/jira/browse/PROTON-1003) - ssl transport layer does not define an error handler
 - [PROTON-1006](https://issues.apache.org/jira/browse/PROTON-1006) - Sending pre-settled messages over the python blocking api waits indefinetly
 - [PROTON-1008](https://issues.apache.org/jira/browse/PROTON-1008) - Using a blank mech_list disables authentication
 - [PROTON-1010](https://issues.apache.org/jira/browse/PROTON-1010) - BlockingConnection leaks sockets after close() is called
 - [PROTON-1013](https://issues.apache.org/jira/browse/PROTON-1013) - Documentation: CyruSASL missing as an optional dependency
 - [PROTON-1015](https://issues.apache.org/jira/browse/PROTON-1015) - Documentation: typos in the C++ tutorial
 - [PROTON-1018](https://issues.apache.org/jira/browse/PROTON-1018) - Crash in pn_transport_finalize(transport.c) when logging level set to PN_TRACE_DRV
 - [PROTON-1019](https://issues.apache.org/jira/browse/PROTON-1019) - Documentation: typos in the C++ API documentation
 - [PROTON-1023](https://issues.apache.org/jira/browse/PROTON-1023) - Incorrect handling of failed attach for BlockingConnection
 - [PROTON-1024](https://issues.apache.org/jira/browse/PROTON-1024) - Disconnect during close not handled correctly in BlockingConnection
 - [PROTON-1028](https://issues.apache.org/jira/browse/PROTON-1028) - BlockingConnection leaks due to cyclical reference
 - [PROTON-1029](https://issues.apache.org/jira/browse/PROTON-1029) - Do not fail hard if strerror_r fails.
 - [PROTON-1030](https://issues.apache.org/jira/browse/PROTON-1030) - Reactor never freed if handler/global_handler set
 - [PROTON-1031](https://issues.apache.org/jira/browse/PROTON-1031) - [python] Bump the module version to 0.11.0
 - [PROTON-1033](https://issues.apache.org/jira/browse/PROTON-1033) - Update the revision of the libqpid-proton library to 4
 - [PROTON-1034](https://issues.apache.org/jira/browse/PROTON-1034) - [Go binding] Windows build fails if Go language is installed but no gcc tool kit
 - [PROTON-1042](https://issues.apache.org/jira/browse/PROTON-1042) - Can't distinguish between null target and null address on a target