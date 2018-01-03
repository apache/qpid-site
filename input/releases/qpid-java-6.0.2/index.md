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

# Qpid Java 6.0.2

Qpid Java offers an AMQP-fluent implementation of JMS and a message
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
| Java broker, Qpid JMS, Qpid JCA | [qpid-java-6.0.2.tar.gz](http://archive.apache.org/dist/qpid/java/6.0.2/qpid-java-6.0.2.tar.gz) | [ASC](https://archive.apache.org/dist/qpid/java/6.0.2/qpid-java-6.0.2.tar.gz.asc), [MD5](https://archive.apache.org/dist/qpid/java/6.0.2/qpid-java-6.0.2.tar.gz.md5), [SHA1](https://archive.apache.org/dist/qpid/java/6.0.2/qpid-java-6.0.2.tar.gz.sha1) |

## Java binaries

| Content | Download | Verify |
|---------|----------|--------|
| Java broker | [qpid-broker-6.0.2-bin.tar.gz](http://archive.apache.org/dist/qpid/java/6.0.2/binaries/qpid-broker-6.0.2-bin.tar.gz) | [ASC](https://archive.apache.org/dist/qpid/java/6.0.2/binaries/qpid-broker-6.0.2-bin.tar.gz.asc), [MD5](https://archive.apache.org/dist/qpid/java/6.0.2/binaries/qpid-broker-6.0.2-bin.tar.gz.md5), [SHA1](https://archive.apache.org/dist/qpid/java/6.0.2/binaries/qpid-broker-6.0.2-bin.tar.gz.sha1) |
| Qpid JMS (AMQP 0-10, 0-9-1, 0-9, 0-8) | [qpid-client-6.0.2-bin.tar.gz](http://archive.apache.org/dist/qpid/java/6.0.2/binaries/qpid-client-6.0.2-bin.tar.gz) | [ASC](https://archive.apache.org/dist/qpid/java/6.0.2/binaries/qpid-client-6.0.2-bin.tar.gz.asc), [MD5](https://archive.apache.org/dist/qpid/java/6.0.2/binaries/qpid-client-6.0.2-bin.tar.gz.md5), [SHA1](https://archive.apache.org/dist/qpid/java/6.0.2/binaries/qpid-client-6.0.2-bin.tar.gz.sha1) |

## Components

| Component | Languages | Platforms | AMQP versions |
|-----------|-----------|-----------|---------------|
| [Java broker]({{site_url}}/components/java-broker/index.html) | Java | JVM | 1.0, 0-10, 0-9-1, 0-9, 0-8 |
| [Qpid JMS (AMQP 0-10, 0-9-1, 0-9, 0-8)]({{site_url}}/components/jms/amqp-0-x.html) | Java | JVM | 0-10, 0-9-1, 0-9, 0-8 |

## Documentation


<div class="two-column" markdown="1">

 - [Installing Qpid Java](java-broker/book/Java-Broker-Installation.html)
 - [Java broker book](java-broker/book/index.html)
 - [API reference](http://docs.oracle.com/javaee/1.4/api/javax/jms/package-summary.html)
 - [Using the Qpid JMS client (AMQP 0-10)](jms-client-0-10/book/index.html)
 - [Using the Qpid JMS client (AMQP 0-9-1, 0-9, 0-8)](jms-client-0-8/book/index.html)
 - [JMS examples (AMQP 0-10)](qpid-jms/examples/index.html)
 - [JMS examples (AMQP 0-9-1, 0-9, 0-8)](jms-client-0-8/book/JMS-Client-0-8-Examples.html)
 - [JCA examples](http://svn.apache.org/repos/asf/qpid/java/trunk/jca/example/)

</div>


## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/java/6.0.2)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+%3D+%27qpid-java-6.0.2%27+AND+resolution+%3D+%27fixed%27+ORDER+BY+priority+DESC)
 - [Source repository tag](http://svn.apache.org/repos/asf/qpid/java/tags/6.0.2)

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("6.0.2" === "{{current_java_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>
