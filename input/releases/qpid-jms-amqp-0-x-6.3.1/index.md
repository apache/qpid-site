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

# Qpid JMS AMQP 0-x 6.3.1

Qpid JMS AMQP 0-x is JMS 1.1 compatible client which can speak AMQP 0-8,0-9,0-9-1 and 0-10.

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service

## Download

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

| Content | Download | Verify |
|---------|----------|--------|
| Qpid JMS binaries | [apache-qpid-jms-amqp-0-x-6.3.1-bin.tar.gz](http://archive.apache.org/dist/qpid/jms-amqp-0-x/6.3.1/binaries/apache-qpid-jms-amqp-0-x-6.3.1-bin.tar.gz) | [ASC](https://archive.apache.org/dist/qpid/jms-amqp-0-x/6.3.1/binaries/apache-qpid-jms-amqp-0-x-6.3.1-bin.tar.gz.asc), [SHA512](https://archive.apache.org/dist/qpid/jms-amqp-0-x/6.3.1/binaries/apache-qpid-jms-amqp-0-x-6.3.1-bin.tar.gz.sha512) |
| Qpid JMS binaries | [apache-qpid-jms-amqp-0-x-6.3.1-bin.zip](http://archive.apache.org/dist/qpid/jms-amqp-0-x/6.3.1/binaries/apache-qpid-jms-amqp-0-x-6.3.1-bin.zip) | [ASC](https://archive.apache.org/dist/qpid/jms-amqp-0-x/6.3.1/binaries/apache-qpid-jms-amqp-0-x-6.3.1-bin.zip.asc), [SHA512](https://archive.apache.org/dist/qpid/jms-amqp-0-x/6.3.1/binaries/apache-qpid-jms-amqp-0-x-6.3.1-bin.zip.sha512) |
| Qpid JMS source code | [apache-qpid-jms-amqp-0-x-6.3.1-src.tar.gz](http://archive.apache.org/dist/qpid/jms-amqp-0-x/6.3.1/apache-qpid-jms-amqp-0-x-6.3.1-src.tar.gz) | [ASC](https://archive.apache.org/dist/qpid/jms-amqp-0-x/6.3.1/apache-qpid-jms-amqp-0-x-6.3.1-src.tar.gz.asc), [SHA512](https://archive.apache.org/dist/qpid/jms-amqp-0-x/6.3.1/apache-qpid-jms-amqp-0-x-6.3.1-src.tar.gz.sha512) |

The client is also available [via Maven]({{site_url}}/maven.html).

## Documentation


<div class="two-column" markdown="1">

 - [API reference](http://docs.oracle.com/javaee/7/api/javax/jms/package-summary.html)
 - [Using the Qpid JMS AMQP 0-x - AMQP 0-10](jms-amqp-0-10-book/index.html)
 - [Using the Qpid JMS AMQP 0-x - AMQP 0-9-1, 0-9, 0-8](jms-amqp-0-8-book/index.html)
 - [Examples (AMQP 0-10)](examples/index.html)
 - [Examples (AMQP 0-9-1, 0-9, 0-8)](jms-amqp-0-8-book/JMS-Client-0-8-Examples.html)

</div>


## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/jms-amqp-0-x/6.3.1)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+%3D+%27qpid-java-client-0-x-6.3.1%27+AND+resolution+%3D+%27fixed%27+ORDER+BY+priority+DESC)
 - [Source repository tag](https://git-wip-us.apache.org/repos/asf/qpid-jms-amqp-0-x.git/tree/refs/tags/6.3.1)

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("6.3.1" === "{{current_jms_amqp_0_x_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>