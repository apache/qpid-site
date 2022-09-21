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

# Qpid via Maven

The following dependencies can be added to the POM for your Maven build to utilise the artifacts via the [Maven central repository](http://search.maven.org/).

;; Fragments generated with 'pygmentize -l xml -f html ~/maven.xml > ~/maven.html'

## Qpid JMS

Jakarta Messaging 3.1 (jakarta.jms)

<div class="highlight"><pre>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.qpid<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>qpid-jms-client<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>{{current_jms_release}}<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>

Jakarta Messaging 2.0 (javax.jms)

<div class="highlight"><pre>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.qpid<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>qpid-jms-client<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>{{other_jms_release}}<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>

## Qpid ProtonJ2

Client

<div class="highlight"><pre>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.qpid<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>protonj2-client<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>{{current_protonj2_release}}<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>

Engine

<div class="highlight"><pre>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.qpid<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>protonj2<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>{{current_protonj2_release}}<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>

## Qpid Proton-J

<div class="highlight"><pre>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.qpid<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>proton-j<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>{{current_proton_j_release}}<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>


## Qpid AMQP 0-x JMS Client

<div class="highlight"><pre>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.qpid<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>qpid-client<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>{{current_jms_amqp_0_x_release}}<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.geronimo.specs<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>geronimo-jms_1.1_spec<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>1.0<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>

## More information

 - [Snapshot repository](https://repository.apache.org/content/repositories/snapshots/)
 - [Maven project](http://maven.apache.org/)
