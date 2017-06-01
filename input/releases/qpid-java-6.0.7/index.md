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

#Qpid for Java 6.0.7

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.  More about [Qpid]({{site_url}}/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

## Source archives

| Content | Download | Verify |
|---------|----------|--------|
| Qpid Broker for Java, Qpid JMS for AMQP 0-9-1/0-10 | [qpid-java-6.0.7.tar.gz](http://archive.apache.org/dist/qpid/java/6.0.7/qpid-java-6.0.7.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/java/6.0.7/qpid-java-6.0.7.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/java/6.0.7/qpid-java-6.0.7.tar.gz.md5), [SHA512](http://archive.apache.org/dist/qpid/java/6.0.7/qpid-java-6.0.7.tar.gz.sha) |

## Binaries

| Content | Download | Verify |
|---------|----------|--------|
| Qpid Broker for Java | [qpid-broker-6.0.7-bin.tar.gz](http://archive.apache.org/dist/qpid/java/6.0.7/binaries/qpid-broker-6.0.7-bin.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/java/6.0.7/binaries/qpid-broker-6.0.7-bin.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/java/6.0.7/binaries/qpid-broker-6.0.7-bin.tar.gz.md5), [SHA512](http://archive.apache.org/dist/qpid/java/6.0.7/binaries/qpid-broker-6.0.7-bin.tar.gz.sha) |
| Qpid JMS for AMQP 0-9-1/0-10 | [qpid-client-6.0.7-bin.tar.gz](http://archive.apache.org/dist/qpid/java/6.0.7/binaries/qpid-client-6.0.7-bin.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/java/6.0.7/binaries/qpid-client-6.0.7-bin.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/java/6.0.7/binaries/qpid-client-6.0.7-bin.tar.gz.md5), [SHA512](http://archive.apache.org/dist/qpid/java/6.0.7/binaries/qpid-client-6.0.7-bin.tar.gz.sha) |

## Components

| Component | Languages | Platforms | AMQP versions |
|-----------|-----------|-----------|---------------|
| [Qpid Broker for Java]({{site_url}}/components/java-broker/index.html) | Java | JVM | 1.0, 0-10, 0-9-1, 0-9, 0-8 |
| [Qpid JMS for AMQP 0-9-1/0-10]({{site_url}}/components/jms/amqp-0-x.html) | Java | JVM | 0-10, 0-9-1, 0-9, 0-8 |

## Documentation


<div class="two-column" markdown="1">

 - [Installing Qpid Broker for Java](java-broker/book/Java-Broker-Installation.html)
 - [Broker book](java-broker/book/index.html)
 - [API reference](http://docs.oracle.com/javaee/1.4/api/javax/jms/package-summary.html)
 - [Using the Qpid JMS client for AMQP 0-10](jms-client-0-10/book/index.html)
 - [Using the Qpid JMS client for AMQP 0-9-1](jms-client-0-8/book/index.html)
 - [JMS examples for AMQP 0-10](qpid-jms/examples/index.html)
 - [JMS examples for AMQP 0-9-1, 0-9, 0-8](jms-client-0-8/book/JMS-Client-0-8-Examples.html)

</div>


## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/java/6.0.7)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+%3D+%27qpid-java-6.0.7%27+AND+resolution+%3D+%27fixed%27+ORDER+BY+priority+DESC)
 - [Source repository tag](http://svn.apache.org/repos/asf/qpid/java/tags/6.0.7)

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("6.0.7" === "{{current_java_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>