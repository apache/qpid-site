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

# Packages

## Debian

Use `apt-get` to install Qpid and its dependencies.

To install the C++ and Python
[Messaging]({{site_url}}/components/messaging-api/index.html) APIs:

    % apt-get install libqpidmessaging2-dev
    % apt-get install python-qpid

To install the
[C++ broker]({{site_url}}/components/cpp-broker/index.html) and
tools::

    % apt-get install qpidd qpid-tools

## Fedora

Use `yum` or `dnf` to install Qpid and its dependencies.

To install the C and Python [Proton]({{site_url}}/proton/index.html)
APIs:

    % yum install qpid-proton-c-devel
    % yum install python-qpid-proton

To install the C++ and Python
[Messaging]({{site_url}}/components/messaging-api/index.html) APIs:

    % yum install qpid-cpp-client-devel
    % yum install python-qpid

To install
[Dispatch router]({{site_url}}/components/dispatch-router/index.html)
and tools:

    % yum install qpid-dispatch-router qpid-dispatch-tools

To install the
[C++ broker]({{site_url}}/components/cpp-broker/index.html) and tools:

    % yum install qpid-cpp-server qpid-tools

## EPEL

Packages for RHEL 7 and CentOS 7 are available from the
[Fedora EPEL](https://fedoraproject.org/wiki/EPEL) repositories.
Install the EPEL release RPM to add the repository to your system.

    % rpm -i https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

Once installed, you can use the [Fedora instructions](#fedora) above
to install the packages.

