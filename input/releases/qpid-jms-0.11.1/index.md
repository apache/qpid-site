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

# Qpid JMS 0.11.1

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol engine.

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service

## Download

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

| Content | Download | Verify |
|---------|----------|--------|
| Qpid JMS binaries | [apache-qpid-jms-0.11.1-bin.tar.gz](http://archive.apache.org/dist/qpid/jms/0.11.1/apache-qpid-jms-0.11.1-bin.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/jms/0.11.1/apache-qpid-jms-0.11.1-bin.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/jms/0.11.1/apache-qpid-jms-0.11.1-bin.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/jms/0.11.1/apache-qpid-jms-0.11.1-bin.tar.gz.sha1) |
| Qpid JMS source code | [apache-qpid-jms-0.11.1-src.tar.gz](http://archive.apache.org/dist/qpid/jms/0.11.1/apache-qpid-jms-0.11.1-src.tar.gz) | [ASC](http://archive.apache.org/dist/qpid/jms/0.11.1/apache-qpid-jms-0.11.1-src.tar.gz.asc), [MD5](http://archive.apache.org/dist/qpid/jms/0.11.1/apache-qpid-jms-0.11.1-src.tar.gz.md5), [SHA1](http://archive.apache.org/dist/qpid/jms/0.11.1/apache-qpid-jms-0.11.1-src.tar.gz.sha1) |

The client is also available [via Maven]({{site_url}}/maven.html).

## Documentation


<div class="two-column" markdown="1">

 - [API reference](http://docs.oracle.com/javaee/1.4/api/javax/jms/package-summary.html)
 - [Examples](https://github.com/apache/qpid-jms/tree/0.11.1/qpid-jms-examples)
 - [Configuration](docs/index.html)
 - [Building Qpid JMS](building.html)

</div>


## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/jms/0.11.1)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPIDJMS+AND+fixVersion+%3D+%270.11.1%27+AND+resolution+%3D+%27fixed%27+ORDER+BY+priority+DESC)
 - [Source repository tag](https://git-wip-us.apache.org/repos/asf/qpid-jms.git/tree/refs/tags/0.11.1)

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("0.11.1" === "{{current_jms_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>