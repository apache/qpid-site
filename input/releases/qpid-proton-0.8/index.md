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

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("0.8" === "{{current_proton_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>

# Qpid Proton 0.8

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

## Downloads

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

| Content | Download | Signature |
| ------- | -------- | --------- |
| AMQP Messenger, AMQP Protocol Engine | [qpid-proton-0.8.tar.gz](http://archive.apache.org/dist/qpid/proton/0.8/qpid-proton-0.8.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/proton/0.8/qpid-proton-0.8.tar.gz.asc) |

## Components

| Component | Languages | Platforms | AMQP versions |
| --------- | --------- | --------- | ------------- |
| [AMQP Messenger]({{site_url}}/proton/messenger.html) | C, Java, Perl, PHP, Python, Ruby | Linux, OS X, JVM | 1.0 |
| [AMQP Protocol Engine]({{site_url}}/proton/index.html) | C, Java, Perl, PHP, Python, Ruby | Linux, OS X, JVM | 1.0 |

## Documentation

<div class="two-column" markdown="1">
<div class="column" markdown="1">

### Installation

 - [Installing Qpid Proton](http://svn.apache.org/repos/asf/qpid/proton/branches/0.8/README)

### AMQP Protocol Engine

 - [C API reference](protocol-engine/c/api/files.html)
 - [Java API reference](protocol-engine/java/api/index.html)
 - [Python API reference](protocol-engine/python/api/index.html)

</div>
<div class="column" markdown="1">

### AMQP Messenger

 - [C API reference](protocol-engine/c/api/messenger_8h.html)
 - [C examples](messenger/c/examples/index.html)
 - [Java API reference](protocol-engine/java/api/org/apache/qpid/proton/messenger/Messenger.html)
 - [Perl examples](messenger/perl/examples/index.html)
 - [PHP examples](messenger/php/examples/index.html)
 - [Python API reference](protocol-engine/python/api/proton.Messenger-class.html)
 - [Python examples](messenger/python/examples/index.html)
 - [Ruby examples](messenger/ruby/examples/index.html)

</div>
</div>

## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/proton/0.8)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+PROTON+AND+fixVersion+%3D+%270.8%27+ORDER+BY+priority+DESC)
 - [Source repository branch](http://svn.apache.org/repos/asf/qpid/proton/branches/0.8)
 - [Source repository tag](http://svn.apache.org/repos/asf/qpid/proton/tags/0.8)
