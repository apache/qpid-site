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

<div id="-left-column" markdown="1">

# Qpid JMS

<div class="feature" markdown="1">

## JMS with the strength of AMQP

Qpid JMS is an AMQP 1.0 [Jakarta Messaging 3.0](https://jakarta.ee/specifications/messaging/3.0/jakarta-messaging-spec-3.0.html)
client built using [Qpid Proton]({{site_url}}/proton/index.html).

For a release using Jakarta Messaging 3.0 (jakarta.jms), see the [{{current_jms_release}} release]({{site_url}}/releases/qpid-jms-{{current_jms_release}}/index.html).

For a release using Jakarta Messaging 2.0 (javax.jms), see the [{{other_jms_release}} release]({{site_url}}/releases/qpid-jms-{{other_jms_release}}/index.html).

</div>

## Features

 - [Jakarta Messaging 3.0](https://jakarta.ee/specifications/messaging/3.0/jakarta-messaging-spec-3.0.html) API
 - Secure communication via SSL and SASL 
 - Producer flow control
 - Failover
 - Pure-Java implementation

## Documentation

<div class="two-column" markdown="1">
 - [API reference](https://jakarta.ee/specifications/messaging/3.0/apidocs/)
 - [Examples](https://github.com/apache/qpid-jms/tree/{{current_jms_release}}/qpid-jms-examples)
 - [Configuration]({{current_jms_release_url}}/docs/index.html)
 - [Building Qpid JMS]({{current_jms_release_url}}/building.html)

</div>

For details about the AMQP 0-x JMS client, look [here](amqp-0-x.html).

</div>

<div id="-right-column" class="right-column-adjusted" markdown="1">

## Releases

 - {{current_jms_release_link}}
 - [Qpid JMS {{other_jms_release}}]({{site_url}}/releases/qpid-jms-{{other_jms_release}}/index.html)
 - [Past releases]({{site_url}}/releases/index.html#past-releases)

## Issues

 - [Report a bug](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12314524&issuetype=1&priority=3&summary=[Enter%20a%20brief%20description])
 - [Request an improvement](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12314524&issuetype=4&priority=3)
 - <form id="-jira-goto-form">Go to issue <input name="jira" value="QPIDJMS-"/></form>
 - [JIRA project page](https://issues.apache.org/jira/browse/QPIDJMS)

## Source code

 - [Browse via GitHub](https://github.com/apache/qpid-jms)
 - [Git clone URL](https://gitbox.apache.org/repos/asf/qpid-jms.git)

## Resources

 - [Security](security.html)
 - [AMQP 0-x JMS Client](amqp-0-x.html)

</div>
