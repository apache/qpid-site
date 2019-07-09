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

# Qpid Broker-J 7.0.8

[Qpid Broker-J]({{site_url}}/components/broker-j/index.html) is a message broker written in Java that stores, routes,
and forwards messages using AMQP 1.0, 0-10, 0-9-1, 0-9 and 0-8.  More about
[Qpid]({{site_url}}/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

## Source archives

| Content | Download | Verify |
|---------|----------|--------|
| Qpid Broker-J | [apache-qpid-broker-j-7.0.8-src.tar.gz](http://archive.apache.org/dist/qpid/broker-j/7.0.8/apache-qpid-broker-j-7.0.8-src.tar.gz) | [ASC](https://archive.apache.org/dist/qpid/broker-j/7.0.8/apache-qpid-broker-j-7.0.8-src.tar.gz.asc), [SHA512](https://archive.apache.org/dist/qpid/broker-j/7.0.8/apache-qpid-broker-j-7.0.8-src.tar.gz.sha512) |

## Binaries

| Content | Download | Verify |
|---------|----------|--------|
| Qpid Broker-J | [apache-qpid-broker-j-7.0.8-bin.tar.gz](http://archive.apache.org/dist/qpid/broker-j/7.0.8/binaries/apache-qpid-broker-j-7.0.8-bin.tar.gz) | [ASC](https://archive.apache.org/dist/qpid/broker-j/7.0.8/binaries/apache-qpid-broker-j-7.0.8-bin.tar.gz.asc), [SHA512](https://archive.apache.org/dist/qpid/broker-j/7.0.8/binaries/apache-qpid-broker-j-7.0.8-bin.tar.gz.sha512) |
| Qpid Broker-J | [apache-qpid-broker-j-7.0.8-bin.zip](http://archive.apache.org/dist/qpid/broker-j/7.0.8/binaries/apache-qpid-broker-j-7.0.8-bin.zip) | [ASC](https://archive.apache.org/dist/qpid/broker-j/7.0.8/binaries/apache-qpid-broker-j-7.0.8-bin.zip.asc), [SHA512](https://archive.apache.org/dist/qpid/broker-j/7.0.8/binaries/apache-qpid-broker-j-7.0.8-bin.zip.sha512) |

## Documentation


<div class="two-column" markdown="1">

 - [Installing Qpid Broker-J](book/Java-Broker-Installation.html)
 - [Broker book](book/index.html)

</div>


## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/broker-j/7.0.8)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+%3D+%27qpid-java-broker-7.0.8%27+AND+resolution+%3D+%27fixed%27+ORDER+BY+priority+DESC)
 - [Source repository tag](https://gitbox.apache.org/repos/asf/qpid-broker-j.git/tree/refs/tags/7.0.8)

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("7.0.8" === "{{current_broker_j_release}}" || "7.0.8" === "{{other_broker_j_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>