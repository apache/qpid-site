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

# Download

*In addition to the source artefacts below, we offer
[Qpid packages](packages.html) and [Qpid via Maven](maven.html).*

Qpid's source artefacts are produced as part of our community release
process. The downloads on this page are from our
[current releases]({{site_url}}/releases/index.html#current-releases).

It is important to [verify the integrity](#verify-what-you-download) of the files you download.

## Messaging APIs

| Content | Download | Verify |
| ------- | -------- | ------ |
| [Qpid Proton]({{site_url}}/proton/index.html) | [qpid-proton-{{current_proton_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/proton/{{current_proton_release}}/qpid-proton-{{current_proton_release}}.tar.gz.sha1) |
| [Qpid Proton-J]({{site_url}}/proton/index.html) | [apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz)\* | [ASC](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz.md5), [SHA512](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-bin.tar.gz.sha) |
| [Qpid JMS]({{site_url}}/components/jms/index.html) (AMQP 1.0) | [apache-qpid-jms-{{current_jms_release}}-bin.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz)\* | [ASC](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-bin.tar.gz.sha1) |
| [Qpid AMQP 0-x JMS Client]({{site_url}}/components/jms/amqp-0-x.html) | [qpid-client-{{current_java_release}}-bin.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/java/{{current_java_release}}/binaries/qpid-client-{{current_java_release}}-bin.tar.gz)\* | [ASC](http://www.apache.org/dist/qpid/java/{{current_java_release}}/binaries/qpid-client-{{current_java_release}}-bin.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/java/{{current_java_release}}/binaries/qpid-client-{{current_java_release}}-bin.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/java/{{current_java_release}}/binaries/qpid-client-{{current_java_release}}-bin.tar.gz.sha1) |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) (C++, bindings) | [qpid-cpp-{{current_cpp_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.sha1) |
| [Qpid Messaging API]({{site_url}}/components/messaging-api/index.html) (Python) | [qpid-python-{{current_python_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/python/{{current_python_release}}/qpid-python-{{current_python_release}}.tar.gz.sha1) |

## Messaging servers

| Content | Download | Verify |
| ------- | -------- | ------ |
| [Broker for Java]({{site_url}}/components/java-broker/index.html) | [qpid-broker-{{current_java_release}}-bin.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/java/{{current_java_release}}/binaries/qpid-broker-{{current_java_release}}-bin.tar.gz)\* | [ASC](http://www.apache.org/dist/qpid/java/{{current_java_release}}/binaries/qpid-broker-{{current_java_release}}-bin.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/java/{{current_java_release}}/binaries/qpid-broker-{{current_java_release}}-bin.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/java/{{current_java_release}}/binaries/qpid-broker-{{current_java_release}}-bin.tar.gz.sha1) |
| [C++ broker]({{site_url}}/components/cpp-broker/index.html) | [qpid-cpp-{{current_cpp_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.sha1) |
| [Dispatch router]({{site_url}}/components/dispatch-router/index.html) | [qpid-dispatch-{{current_dispatch_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/dispatch/{{current_dispatch_release}}/qpid-dispatch-{{current_dispatch_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/dispatch/{{current_dispatch_release}}/qpid-dispatch-{{current_dispatch_release}}.tar.gz.asc), [SHA1](http://www.apache.org/dist/qpid/dispatch/{{current_dispatch_release}}/qpid-dispatch-{{current_dispatch_release}}.tar.gz.sha1) |

\*These Java artefacts are presented as compiled bytecode.  We also
offer the source as part of our
[Qpid Proton-J source release](http://www.apache.org/dyn/closer.lua/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz)
\[[ASC](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz.asc),
[MD5](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz.md5),
[SHA512](http://www.apache.org/dist/qpid/proton-j/{{current_proton_j_release}}/apache-qpid-proton-j-{{current_proton_j_release}}-src.tar.gz.sha)\]
and
[Qpid JMS source release](http://www.apache.org/dyn/closer.lua/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz)
\[[ASC](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz.asc),
[MD5](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz.md5),
[SHA1](http://www.apache.org/dist/qpid/jms/{{current_jms_release}}/apache-qpid-jms-{{current_jms_release}}-src.tar.gz.sha1)\]
and
[Qpid for Java source release](http://www.apache.org/dyn/closer.lua/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz)
\[[ASC](http://www.apache.org/dist/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz.asc),
[MD5](http://www.apache.org/dist/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz.md5),
[SHA1](http://www.apache.org/dist/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz.sha1)\].

;; ## Other components
;;
;; | Content | Download | Verify |
;; | ------- | -------- | ------ |
;; | [Interop Test]({{site_url}}/components/interop-test/index.html) | [qpid-interop-test-{{current_interop_test_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/interop-test/{{current_interop_test_release}}/qpid-interop-test-{{current_interop_test_release}}.tar.gz) | [ASC](http://www.apache.org/dist/qpid/interop-test/{{current_interop_test_release}}/qpid-interop-test-{{current_interop_test_release}}.tar.gz.asc), [SHA](http://www.apache.org/dist/qpid/interop-test/{{current_interop_test_release}}/qpid-interop-test-{{current_interop_test_release}}.tar.gz.sha) |

## Verify what you download

It is essential that you verify the integrity of the downloaded files
using the ASC signatures, MD5 checksums, or SHA1 checksums.

The signatures can be verified using PGP or GPG. First download
the [`KEYS`](http://www.apache.org/dist/qpid/KEYS) file as well as the
`.asc` signature file for the relevant artefact. Make sure you get
these files from the relevant subdirectory of the
[main distribution directory](http://www.apache.org/dist/qpid/),
rather than from a mirror. Then verify the signatures using one of the
following sets of commands.

    % pgpk -a KEYS
    % pgpv <artifact-name>.asc

    % pgp -ka KEYS
    % pgp <artifact-name>.asc

    % gpg --import KEYS
    % gpg --verify <artifact-name>.asc

Alternatively, you can verify the MD5 or SHA1 checksums of the
files. Unix programs called `md5sum` and `sha1sum` (or `md5` and
`sha1`) are included in many unix distributions.  They are also
available as part of
[GNU Coreutils](http://www.gnu.org/software/coreutils/). For
Windows users, [FSUM](http://www.slavasoft.com/fsum/) supports MD5 and
SHA1. Ensure your generated checksum string matches the string
published in the `.md5` or `.sha1` file included with each release
artefact. Again, make sure you get this file from the relevant
subdirectory of the
[main distribution directory](http://www.apache.org/dist/qpid/),
rather than from a mirror.

## More information

 - [Components]({{site_url}}/components/index.html)
 - [Releases]({{site_url}}/releases/index.html)
 - [Packages](packages.html)
 - [Qpid via Maven](maven.html)
