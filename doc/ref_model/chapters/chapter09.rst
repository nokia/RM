Infrastructure Operations and Lifecycle Management
==================================================

Introduction to Infrastructure Operations and Lifecycle Management
------------------------------------------------------------------

The purpose of this section is to define the capabilities required of the infrastructure to ensure that it is
effectively supported, maintained, and otherwise lifecycle-managed by the operations teams. This includes
requirements relating to the need to be able to maintain infrastructure services "in-service" without impacting
the applications and workloads, while minimising human labour. It must also capture any exceptions and related
assumptions.

There are three main business operating frameworks that are commonly known and used across the telecommunications
industry and that are related to the topics in this section:

-  FCAPS: the ISO model for network management.
-  The TM Forum Business Process Framework (eTOM).
-  ITIL: ITIL 4.0 attempts to adapt IT service management practices to the needs of the cloud environment.

The sections below roughly map to these frameworks as follows:

====================================== ================== ========== ==============================
Chapter title                           FCAPS              eTOM       ITIL
====================================== ================== ========== ==============================
Configuration and lifecycle management Configuration      Fulfilment Configuration, release, change
Assurance                              Performance, fault Assurance  Event, incident
Capacity management                    Configuration      Fulfilment capacity management
====================================== ================== ========== ==============================

**Table 9-1:** Operating Frameworks

   **Note:** The above mapping is provided for general orientation purposes only. Detailed mapping of the required
   Cloud Infrastructure Lifecycle Management capabilities to any of these frameworks is beyond the scope of this
   document.

Infrastructure lifecycle model
------------------------------

The model discussed in this chapter is focused on the cloud infrastructure lifecycle. It provides a complementary
view to the cloud consumption model presented in Chapter 8.

The following diagrams provide mapping between the different stages of the infrastructure lifecycle across all
the layers of the stack, to the owners of the infrastructure and the cloud, and the tenant as the consumer of the
cloud services, in three different scenarios:

- Applications running as containers within virtual machines (the CaaS on IaaS scenario).
- Applications running as containers on bare metal (the CaaS on BM scenario).
- Applications running as VNFs within virtual machines (the IaaS scenario).

The diagrams also define also the scope of the Infrastructure LCM Automation for each of these scenarios. The dotted
lines symbolise the interactions between the layers of each of the models.

.. figure:: ../figures/RM-Ch09-LCM-Automation-CaaS-on-IaaS.png
   :name: Infrastructure automation in the CaaS on IaaS scenario
   :alt: "Infrastructure automation in the CaaS on IaaS scenario"

   Infrastructure LCM in CaaS on IaaS scenario

In the CaaS on IaaS scenario, the Infrastructure LCM scope covers the site/physical layer, the IaaS layer, and the CaaS
layer. From the lifecycle perspective (on the left-hand side of the diagram), the site/physical layer is entirely owned
by the infrastructure owner. The virtualised infrastructure layer (IaaS) is shared between the infrastructure owner and
the cloud provider. Similarly, the container orchestration layer (CaaS) is shared between the cloud provider and the
cloud consumer/tenant. These relationships can be illustrated by a scenario in which a telecom operator owns the
physical infrastructure on which an external cloud provider runs the virtualisation software (hypervisor).

Sharing the CaaS layer between the cloud provider and the cloud consumer reflects the fact that the container
management/orchestration software, like Kubernetes, is lifecycled by the cloud provider (for example, when scaling out
containers), but also by the cloud consumer, due to the close lifecycle relationship between an application and a
container in this model. For example, destroying an application means also destroying related containers. Therefore,
CaaS can be also considered as a part of the Application Orchestration layer.

.. figure:: ../figures/RM-Ch09-LCM-Automation-CNF-on-BM.png
   :name: Infrastructure automation in the CaaS on BM scenario
   :alt: "Infrastructure automation in the CaaS on BM scenario"

   Infrastructure LCM in the CaaS on BM scenario

The main difference in the CaaS on BM scenario is the absence of the IaaS layer. Therefore, the scope of the
Infrastructure LCM and its automation is limited to only two layers: the site/physical layer and the CaaS layer.
From the lifecycle ownership perspective, the CaaS layer is now shared not only between the cloud provider and the
cloud consumer (for the same reasons as in the CaaS on IaaS scenario), but also with the infrastructure owner. The
latter observation is related to the fact that in the bare-metal deployments lacking the hypervisor separation, the
CaaS layer is much more dependent on the underlying physical infrastructure.

.. figure:: ../figures/RM-Ch09-LCM-Automation-VNF-on-IaaS.png
   :name: Infrastructure Automation in IaaS scenario
   :alt: "Infrastructure Automation in IaaS scenario"

   Infrastructure LCM in IaaS scenario

In this "classical" scenario, the scope of the Infrastructure LCM and its automation is defined by the site/physical
layer and the IaaS layer. From the lifecycle perspective, the ownership of IaaS is shared between the infrastructure
owner and the cloud provider. This scenario is characterised by a clear separation between the lifecycle (and hence
its automation) of the infrastructure, and the application lifecycle owned by the cloud consumer/tenant in the role
of the application owner.

Configuration and lifecycle management
--------------------------------------

Configuration management is concerned with defining the configuration of infrastructure and its components, and
tracking or observing the running configuration of that infrastructure and any changes that take place. Modern
configuration management practices, such as desired state configuration management, also mean that any changes from
the desired state that are observed (also known as the delta) are rectified by an orchestration/fulfilment component
of the configuration management system. This closed loop mitigates the configuration drift in the infrastructure and
its components. Our recommendation is to keep these closed loops as small as possible to reduce complexity and the
risk of error. :numref:`Configuration and Lifecycle Management` shows the configuration management loop and how it
relates to lifecycle management.

.. figure:: ../figures/ch09_config_mgmt.png
   :name: Configuration and lifecycle management
   :alt: "Configuration and lifecycle management"

   Configuration and lifecycle management

The initial desired state might be for 10 hosts with a particular set of configuration attributes, including the
version of the hypervisor and any management agents. The configuration management system takes that as input (1) and
configures the infrastructure as required (2). It then observes the current state periodically (3) and, in case of a
difference between the desired state and the observed state, it calculates the delta (4) and reconfigures the
infrastructure (5). This loop takes place for each lifecycle stage (create, update, and delete). For example, if an
update to the hypervisor version is defined in the desired state, the configuration management system calculates the
delta (for example, v1 --> v2) and reconfigures the infrastructure as required.

However, the key requirements for the infrastructure and for infrastructure management are those interfaces and
reference points in the red box, where the configuration is **set**, and where it is **observed**. Table 9-2 lists
the main components and capabilities required to manage the configuration and lifecycle of those components.

+---------------------------------+---------------+---------------------------------+-----------------------------+
| Component                       | Set/Observe   | Capability                      | Example                     |
+=================================+===============+=================================+=============================+
| Cloud infrastructure management | Set           | Target software/firmware        | Software: v1.2.1            |
| software                        |               | version                         |                             |
|                                 |               +---------------------------------+-----------------------------+
|                                 |               | Desired configuration attribute | dhcp_lease_time: 86400      |
|                                 |               +---------------------------------+-----------------------------+
|                                 |               | Desired component quantities    | # hypervisor hosts: 10      |
|                                 +---------------+---------------------------------+-----------------------------+
|                                 | Observe       | Observed software/firmware      | Software: v1.2.1            |
|                                 |               | version                         |                             |
|                                 |               +---------------------------------+-----------------------------+
|                                 |               | Observed configuration          | dhcp_lease_time: 86400      |
|                                 |               | attribute                       |                             |
|                                 |               +---------------------------------+-----------------------------+
|                                 |               | Observed component quantities   | # hypervisor hosts: 10      |
+---------------------------------+---------------+---------------------------------+-----------------------------+
| Cloud infrastructure software   | Set           | Target software version         | Hypervisor software: v3.4.1 |
|                                 |               +---------------------------------+-----------------------------+
|                                 |               | Desired configuration attribute | management_int: eth0        |
|                                 |               +---------------------------------+-----------------------------+
|                                 |               | Desired component quantities    | # NICs for data: 6          |
|                                 +---------------+---------------------------------+-----------------------------+
|                                 | Observe       | Observed software/firmware      | Hypervisor software: v3.4.1 |
|                                 |               | version                         |                             |
|                                 |               +---------------------------------+-----------------------------+
|                                 |               | Observed configuration          | management_int: eth0        |
|                                 |               | attribute                       |                             |
|                                 |               +---------------------------------+-----------------------------+
|                                 |               | Observed component quantities   | # NICs for data: 6          |
+---------------------------------+---------------+---------------------------------+-----------------------------+
| Infrastructure hardware         | Set           | Target software/firmware        | Storage controller          |
|                                 |               | version                         | firmware: v10.3.4           |
|                                 |               +---------------------------------+-----------------------------+
|                                 |               | Desired configuration attribute | Virtual disk 1: RAID1       |
|                                 |               |                                 | [HDD1,HDD2]                 |
|                                 +---------------+---------------------------------+-----------------------------+
|                                 | Observe       | Observed software/firmware      | Storage controller          |
|                                 |               | version                         | firmware: v10.3.4           |
|                                 |               +---------------------------------+-----------------------------+
|                                 |               | Observed configuration          | Virtual disk 1: RAID1       |
|                                 |               | attribute                       | [HDD1,HDD2]                 |
+---------------------------------+---------------+---------------------------------+-----------------------------+

**Table 9-2:** Configuration and lifecycle management capabilities

Table 9-3 below defines the standard interfaces that should be made available by the infrastructure and cloud
infrastructure management components to allow for successful Configuration Management.

========================= ================================ ===============================
Component                 Interface standard               Link
========================= ================================ ===============================
Infrastructure management Defined in the RA specifications RA-1, RA-2
Infrastructure software   Defined in the RA specifications RA-1, RA-2
Infrastructure hardware   Redfish API                      DMTF RedFish specification :cite:p:`dmtfredfish`
========================= ================================ ===============================

**Table 9-3:** Interface standards for configuration management

Capacity management
-------------------

Capacity management is a potentially wide-ranging process that includes taking demands across lines of business,
analysing data about the infrastructure that is running, and calculating when additional infrastructure might be
required, or when infrastructure might need to be decommissioned.

As such, the requirements for capacity management on the infrastructure are covered by the Assurance, and the
Configuration and Lifecycle Management sections below. The Assurance section deals with the collection of data.
There is no reason to consider that this would be done by a different mechanism for capacity management, as it is
for assurance. The Configuration and Lifecycle Management section deals with the changes being made to the
infrastructure hardware, software, and management components (for example, changing of the number of hypervisor
hosts from 10 to 12).


Assurance
---------

Assurance is concerned with the following:

- The proactive and reactive maintenance activities that are required to ensure that the infrastructure services
  are available, in accordance with the defined performance and availability levels.
- The continuous monitoring of the status and performance of the individual components, and of the service as a
  whole.
- The collection and analysis of performance data, which is used to identify potential issues, including the
  ability to resolve the issue with no customer impact.

The requirement types are as follows:

1. Data collection from all the components, such as:

   - The ability to collect data relating to events (transactions, security events, physical interface up/down
     events, warning events, error events, and so on).
   - The ability to collect data relating to component status (up/down, physical temperature, disk speed, and
     so on).
   - The ability to collect data relating to component performance (used CPU resources, storage throughput,
     network bandwidth in/out, API transactions, transaction response times, and so on).

2. Capabilities of the infrastructure management software to allow for the in-service maintenance of the
   infrastructure software and hardware under its management, for example:

   - The ability to mark a physical compute node as being in a kind of "maintenance mode" and for the
     infrastructure management software to ensure that all the running workloads are moved off or rescheduled
     on to other available nodes (after checking that there is sufficient capacity), before marking the node as
     being ready for whatever maintenance activity needs to be performed.
   - The ability to coordinate, automate, and allow the declarative input of in-service software component
     upgrades, such as internal orchestration and scheduler components in the infrastructure management
     software.

.. Note::
  The above only refers to the components. It is expected that any service-level assurance does not add any
  further requirements to the infrastructure, but rather takes the extracted data and builds service models based
  on the knowledge it has of the services being offered.

Telemetry and observability
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Operating complex distributed systems, such as a Telco network, is a task that is becoming increasingly
challenging as the network complexity and the production excellence requirements grow. There are multiple
reasons for this, although they originate in the nature of the system concept. To be able to provide Telco
services, a complex system is decomposed into multiple different functional blocks called network functions.
Internal communication between the diverse network functions of a distributed system is based on message
exchange. To formalize this communication, clearly defined interfaces are introduced, and protocols designed.
Even though the architecture of a Telco network is systematically formalized on the worldwide level,
heterogeneity of services, functions, interfaces, and protocols cannot be avoided. By adding the multivendor
approach in the implementation of Telco networks, the outcome is a system with a remarkably high level of
complexity that requires significant effort for managing and operating it.

A large and complex ecosystem of end-user services requires a formalized approach for achieving high
reliability and scalability. The discipline which applies the well-known practices of software engineering
to operations is known as Site Reliability Engineering. It was conceived at Google as a means of overcoming
the limitations of the common DevOps approach.

The requirements of the common support system (comprising the Operation Support System (OSS) and the Business
Support System (BSS)) are redefined. They are driven by the introduction of new technologies in computing
infrastructure and modern data centres, with the abstraction of resources, known as virtualization and cloud
computing. This brings many advantages, such as easy scaling, error recovery, reaching a high level of
operational autonomy, and so on. It also brings many new challenges in the Telecom network management space.
These challenges are mostly directed towards the dynamic nature of the system, the orientation towards
microservices instead of a silo approach, and huge amounts of data which have to be processed, in order to
understand the internal status of the system. Therefore, the need arises for improved ways to monitor the
systems: observability.

Why observability?
^^^^^^^^^^^^^^^^^^

Knowing the status of all the services and functions at all levels in a cloud-based service offering is
essential, in order to act fast and proactively before the users notice any issues and, most importantly,
before they call the help desk.

A common approach to understanding the aforementioned Telco network status in conventional non-cloud
environments is referred to as monitoring. Usually it would include metric information related to resources,
such as CPUs, memory, HDD, Network I/O, as well as business-related technical key performance indicators
(KPIs), such as the number of active users, the number of registrations, and so on. This monitoring data is
represented as a time series, retrieved at regular intervals, usually with granulation of five to 30 minutes.
In addition, asynchronous messages, such as alarms and notifications, are exposed by the monitored systems,
in order to provide information about foreseen situations. It is worth noting that metric data provides
an approximation of the health of the system, while the alarms and notifications supply more information
about the problem. In general, they provide information about known unknowns: anticipated situations
occurring at random time. However, such information is rarely sufficient for understanding the problem
(root cause analysis (RCA)). Therefore, it is necessary to retrieve more data related to the problem, such
as logs and network signalization. Logs are an invaluable means with which to obtain more granular
information about the code execution. Network packet captures and traces are useful, since telecommunication
networks are distributed systems where components communicate using various protocols, and the communication
can be examined, in order to obtain details of the problem.

As the transition towards cloud environments takes place simultaneously with the introduction of the DevOps
mindset, the conventional monitoring approach becomes suboptimal. Cloud environments allow greater flexibility
as the microservice architecture is embraced to bring improvements in operability. Therefore, the automation
can be used to a greater extent than ever before. Automation in telecom networks usually supposes actions based
on decisions derived from the system output data (system observation). To derive useful decisions, data with a
rich context is necessary. The conventional monitoring approach has to be improved, in order to retrieve
sufficient data, not only from the wider context, but also without delays, as soon as the data is produced or
available. The new, enhanced approach was introduced as a concept of observability, borrowed from the control
theory which states that it is possible to draw conclusions about a system’s internal state based on external
outputs.

This requires the collection of alarms and telemetry data from the physical layer (wires), the cloud
infrastructure up to the network, and applications and services (virtualized network functions (VNFs)) running
on top of the cloud infrastructure, typically isolated by tenants.

Long-term trending data is essential for capacity planning purposes. It is typically collected, aggregated,
and retained over the full lifespan. To keep the amount of collected data manageable, automatic data reduction
algorithms are typically used, for example, by merging the data points from the smallest intervals to more
granular intervals.

The Telco cloud infrastructure typically consists of one or more regional data centres, central offices, and
edge sites. These are managed from the redundant central management sites, each hosted in their own data
centres.

The network services and applications deployed on a Telco cloud, and the Telco cloud infrastructure, are
usually managed by separate teams. Therefore, the monitoring solution must be able to keep the access to the
monitoring data isolated between the tenants and the cloud infrastructure operations. Some monitoring data from
the cloud infrastructure layer must be selectively available to the tenant monitoring applications, in order to
correlate, for example, the Network Functions/Services data with the underlying cloud infrastructure data.

What to observe
^^^^^^^^^^^^^^^

Typically, when it comes to data collection, the following three questions arise:

1. What kind of data should be collected?
2. Where should the data be sent?
3. Which protocol, interface, and format should be used?

What kind of data to collect
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An assessment of the kind of data that needs to be collected should begin by iterating over the following
physical and virtual infrastructure components:

- Network Services across sites and tenants.
- Virtualized functions per site and tenant.
- Individual virtual machines and containers.
- Virtualization infrastructure components.
- Physical servers (compute) and network elements.
- Tool servers with their applications (DNS, identity management, Zero-Touch Provisioning, and so on).
- Cabling.

Data categories
^^^^^^^^^^^^^^^

There are four main observability categories. They are as follows:

1. **Metrics**: Metrics, or telemetry report counters and gauge levels, can either be pulled periodically, for
   example, via SNMP or REST, or pushed as streams, using gRPC or NETCONF. Receivers of the published data can
   register for certain sensors, or for a certain publisher to a message broker. These messages must be
   structured, in order to be parsed successfully.
2. **Events**: Events indicate state variance beyond a specified threshold. They are categorized by severity,
   often with a description of what happened. The most common transport protocol is SNMP with its trap-and-inform
   messages. These messages are generated by physical and logical network elements. The messages can also be
   generated by monitoring applications with statically configured thresholds, or dynamically by Machine Learning
   (ML) algorithms. Generally, they are describing anomalies.
3. **Logs**: Logs are a record of the messages generated by the software for most devices (compute and network)
   and virtual applications. Logs are transported over SYSLOG and tend to come in high volumes.
4. **Traces**: Traces are end-to-end signalling messages (events) created to fulfil the execution of requests on
   the distributed system services. In other words, traces are action points executed to provide responses to the
   requests set to the distributed system service. Even the call can be thought of as a request which begins with
   a SIP INVITE message.

Where to send the data
^^^^^^^^^^^^^^^^^^^^^^

If the observability data has to be sent from its sources, or producers, to specific destinations, or consumers,
then this creates a high degree of dependency between the producers and the consumers. It is prone to errors,
especially in the case of configuration changes. Ideally, the data producers must not be impacted by any change in
the data consumers and vice versa. This is achieved by decoupling the data producers from the data consumers
through the use of brokers. The producers always send their data to the same endpoint: the broker. The consumers
register with the broker for data that is of interest to them and always receive their data from the broker.

Which protocol, interface, and format to use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While the protocols and interfaces are dictated by the selection of the message broker (common data bus) system,
the data format is usually customizable according to the users' needs. The concept of the Schema Registry mechanism,
well known in the world of big data, is helpful here to make sure that the message structures and formats are
consistently used.

The architecture
^^^^^^^^^^^^^^^^

In geographically dispersed large cloud deployments, a given Telco cloud may have several cloud infrastructure
components, as well as a large set of virtualized workloads (VNFs/CNFs). It is important to monitor all of these
workloads and infrastructure components. It is even more important to be able to distinguish between the metrics
provided by these entities to determine the performance and/or issues in such deployments.

The cloud deployment tends to shrink and expand according to customer demand. Therefore, an architecture is
required that can scale on demand and does not force a strong tie between various entities. This means that the
workloads and cloud infrastructure components that provide telemetry and performance metrics must not be burdened
to discover each other. The capacity (for example, speed and storage) of one component must not force overrun or
underrun situations that could cause critical data to be lost or delayed to a point where they become useless.

Operators in charge of the cloud infrastructure (physical infra plus virtualization platform) require detailed
alarms and metrics to run their platform efficiently. While they need indicators as to how well or poorly
individual virtual machines and containers are running, they do not need a view inside these workloads. In fact,
information on what the workloads are doing and how they are performing should not be accessible to the NFVI
operators. The architecture must allow for different consumers to grant or deny access to available resources.

Multiple workloads or network services can be deployed on one or more sites. These workloads require logical
separation, for security and privacy reasons, or to avoid an accidental mixing up of their respective metrics.
This can be achieved by deploying these workloads within their own tenant spaces. All virtualization platforms
offer such isolation down to virtual networks per tenant.

.. _push-vs-pull:

Push versus pull
^^^^^^^^^^^^^^^^

Push and pull are two widely deployed models for providing telemetry data.

Pull model
''''''''''

The following characteristics are typical of the pull model:

- The consumers are required to identify the producers of the data.
- Once the producers have been identified, there should be a tight relationship (synchronization) between the
  producer and the consumer. This makes the systems very complex in terms of configuration and management. For
  example, if a producer moves to a different location, or restarts, then the consumer must rediscover the
  producer and bind their relationship again.
- Data is pulled explicitly by the consumer. The consumer must have the appropriate bandwidth, compute power,
  and storage to deal with this data, for example, SNMP pull or walk.
- One problem with the pull model is that both consumers and producers have to have the means for load/
  performance regulation in cases where the set of consumers overload the pull request serving capabilities of
  the producer.

Push model
''''''''''

The following characteristics are typical of the push model:

- A declarative definition of destination: the data producers know explicitly where to stream or push their data.
- A well-known data broker is used: all the consumers and producers know about it through declarative definition.
  The data broker can be a bus, such as RabitMQ, Apache Kafka, or Apache Pulsar.
- There are no restrictions on the bandwidth or data storage for the producers or consumers. The producers produce
  the data, and stream or push it to the broker. The consumers pull the data from the broker. No explicit
  synchronisation is required between the producers and the consumers.
- Lifecycle Management (LCM) events, such as moves and reboots or restarts, of the consumers or producers have no
  impact on others.
- Producers and consumers can be added or removed at will. There is no impact on the system. This makes this model
  flexible and scalable, and better suited for large or small geographically dispersed Telco clouds.
- Examples of push model include gRPC, SNMP traps, and syslogs.

Producers, consumers, and message brokers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In an ideal case, the observability data is sent directly to the message broker in an agreed format, so that
consumers can then take the data and understand it without additional logic. The message brokers do not impose
limits on the data types.

Enforcing the correct message structures (carrying the data) is performed using Schema Registry concepts. Although
it is not necessary to use a Schema Registry, it is recommended.

.. figure:: ../figures/RM-Ch09-Fig-Producers-Consumers.png
   :name: Producers and consumers
   :alt: Producers and consumers

   Producers and consumers

.. figure:: ../figures/RM-Ch09-Fig-Broker-Service.png
   :alt: Figure 9-3: Broker services
   :name: Broker services

   Broker services
   
   
Automation
----------

Infrastructure lifecycle management automation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a typical telecom operator environment, infrastructure lifecycle management (LCM) is complex and error-prone.
The environment, with its multiple vendors and products, is expensive to maintain, in terms of time and costs,
owing to the need for complex planning, testing, and the out-of-business-hours execution required to perform
disruptive maintenance, such as upgrades, and to mitigate outages to mission-critical applications. Processes
and tooling for infrastructure management across hybrid environments create additional complexity due to the
different levels of access to infrastructure: hands-on access to the on-premise infrastructure, but only
restricted access to consumable services offered by public clouds.

Lifecycle operations, such as software or hardware upgrades (including complex and risky firmware updates),
typically involve time-consuming manual research and substantive testing to ensure that an upgrade is available
or required, and does not conflict with the current versions of other components. In a complex and at-scale
hybrid multicloud environment, consisting of multiple on-premise and public clouds, such a manual process is
ineffective and, in many cases, impossible to execute in a controlled manner. Hence the need for automation.

The goals of LCM are to provide a reliable administration of a system from its provisioning, through its
operational stage, to its final retirement.

The key functions of infrastructure LCM are as follows:

- Hybrid multicloud support. This means that LCM works across physical, virtual, and cloud environments,
  supporting on-premise, cloud, and distributed environments.
- Complete system lifecycle control (plan/design, build, provision, operate/manage, retire, and recycle/scrap).
- Enablement for the automation of most system maintenance tasks.

The key benefits of infrastructure LCM automation are as follows:

- Agility: standardisation of the LCM process by writing and running IaaC allows you to develop, stage, and
  produce environments quickly and easily.
- Operational consistency: automation of the lifecycle results in consistently maintaining the desired state.
  It reduces the possibility of errors and decreases the chances of incompatibility issues within the
  infrastructure.
- Mitigation of human-related risks: automation reduces risks related to human error and rogue activities,
  and safeguards against leakage of information about the company, in the event of an employee leaving the
  organization.
- Higher efficiency: this is achieved by minimizing human inaccuracies and eliminating the lack of knowledge
  about the infrastructure installed base and its configuration, using the CI/CD techniques adapted to
  infrastructure.
- Cost/time saving: engineers save on time and cost. This can be wisely invested in performing higher-value
  jobs. Additional cost savings can be made in the cloud with better use of cloud resources using LCM
  automation.
 
Infrastructure LCM Automation Framework
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The essential building blocks for infrastructure LCM automation are as follows:
 
- representation model
- repository functions
- available software versions and dependencies
- orchestration engine

Automated LCM uses the representation model to do the following:

- Abstract various automation technologies.
- Promote evolution from automation understood as automation of human tasks, to autonomous systems using
  intent-based, declarative automation, supported by evolving AI/ML technologies.

Automated LCM uses the repository functions to do the following:

- Store and manage configuration data.
- Store and manage metrics-related data, such as event data, alert data, and performance data.
- Maintain currency of data through the use of the discovery of current versions of software modules.
- Track and account for all systems, assets, and subscriptions (monitoring).
- Provide an inventory of all virtual and physical assets.
- Provide a topological view of interconnected resources.
- Support network design functions.

Automated LCM uses the available IAC software versions and dependencies component to do the following:

- Store information about the available software versions, software patches, and dependency expectations.
- Determine the recommended version of a software item, such as firmware, as well as dependencies on
  other items in the node, to ensure compliance, and to maintain system integrity.
- Determine the recommended versions of the foundation software running on the cluster.

Automated LCM uses the orchestration engine to do the following:

- Dynamically remediate dependencies during the change process, to optimise the outcome.
- Ensure that the system is consistent across its lifecycle by maintaining it in accordance with the
  intent templates.

LCM automation principles and best practices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Infrastructure LCM automation best practices should be guided by the following principles:

- Everything Codified: use explicit coding to configure files not only for initial provisioning but also as a
  single source of truth for the whole infrastructure lifecycle, to ensure consistency with the intended
  configuration templates, and to eliminate configuration drift.
- Version Controlled: use stringent version control for the infrastructure code to allow proper lifecycle
  automation.
- Self-Documentation: the code itself represents the updated documentation of the infrastructure, to minimise
  the documentation maintenance burden and to ensure the currency of the documentation.
- Code Modularisation: this applies to the IaaC principles of the microservices architecture where the modular
  units of the code can be independently deployed and lifecycled in an automated fashion.
- Immutability: IT infrastructure components are required to be replaced for each deployment during the system
  lifecycle, to be consistent with immutable infrastructure, to avoid configuration drift, and to restrict the
  impact of undocumented changes in the stack.
- Automated Testing: this is the key to error-free post-deployment lifecycle processes and to the elimination
  of lengthy manual testing processes.
- Unified Automation: this uses the same Infrastructure LCM Automation templates, toolsets, and procedures
  across different environments such as Dev, Test, QA, and Prod, to ensure the consistency of the lifecycle
  results and to reduce operational costs.
- Security Automation: the security of the infrastructure is critical to the overall security, dictating the
  use of consistent automated security procedures for threat detection, investigation, and remediation through
  all infrastructure lifecycle stages and all environments.

Software onboarding automation and CI/CD requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software onboarding automation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For software deployment, as far as cloud infrastructure services and workloads are concerned, automation is the
core of the DevOps concept. Automation allows the elimination of manual processes, thereby reducing human errors
and speeding up software deployments. The prerequisite is to install the CI/CD tools chain to do the following:

-  Build, package, and test the application/software.
-  Store environment's parameters and configurations.
-  Automate the delivery and deployment.

The CI/CD pipeline is used to deploy, test, and update the cloud infrastructure services, as well as to onboard
workloads hosted on the infrastructure. Typically, this business process consists of the following key phases:

1. Tenant engagement and software evaluation:

   - In this phase, the request from the tenant to host a workload on the cloud infrastructure platform is
     assessed and a decision is made on whether or not to proceed with the hosting request.
   - If the cloud infrastructure software needs to be updated or installed, an evaluation is made of the impact
     (including to tenants), and whether or not it is all right to proceed.
   - This phase may also involve the tenant accessing a prestaging environment to perform their own evaluation
     or prestaging activities, or both, in preparation for later onboarding phases.

2. Software packaging:

   - The main outcome of this phase is to produce the software-deployable image and the deployment manifests,
     such as TOSCA blueprints, HEAT templates, or Helm charts, that will define the service attributes of the
     cloud infrastructure.
   - The software packaging can be automated or performed by designated personnel, through self-service
     capabilities (for tenants), or by the cloud infrastructure operations team.

3. Software validation and certification:

   - In this phase, the software is deployed and tested, to validate it against the service design and other
     operator-specific acceptance criteria, as required.
   - Software validation and certification should be automated using CI/CD toolsets/pipelines, and
     Test-as-a-Service (TaaS) capabilities.

4. Publish software:

   - Tenant workloads: after the software is certified, the final onboarding process phase is for it to be
     published in the cloud infrastructure production catalogue, from where it can be instantiated on the cloud
     infrastructure platform by the tenant.
   - Cloud infrastructure software: after the software is certified, it is scheduled for deployment in concurrence
     with the user community.

All the phases described above can be automated using technology-specific toolsets and procedures. Therefore,
details of such automation are left for the technology-specific Reference Architecture and Reference Implementation
specifications.

Software CI/CD requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The requirements, including for CI/CD for ensuring software security scans, image integrity checks, OS version checks,
and so on, prior to deployment, are listed in Table 9-4 (below).

..Note::
  The tenant processes for application LCM, such as updates, are out of scope. For the purpose of these requirements,
  CI includes Continuous Delivery, and CD refers to Continuous Deployment.

.. list-table:: Automation CI/CD
  :widths: 10 20 30
  :header-rows: 1

  * - Ref #
    - Description
    - Comments/Notes
  * - auto.cicd.001
    - The CI/CD pipeline must support deployment on any cloud and cloud infrastructures, including different hardware
      accelerators.
    - CI/CD pipelines automate CI/CD best practices into repeatable workflows for integrating code and configurations
      into builds, testing builds including validation against design and operator-specific criteria, and delivery of
      the product onto a runtime environment. Example of an open-source cloud native CI/CD framework is the Tekton
      project (:cite:p:`tekton-project`)
  * - auto.cicd.002
    - The CI/CD pipelines must use event-driven task automation
    - 
  * - auto.cicd.003
    - The CI/CD pipelines should avoid scheduling tasks
    - 
  * - auto.cicd.004
    - The CI/CD pipeline is triggered by a new or updated software release being loaded into a repository
    - The software release can be source code files, configuration files, images, manifests. Operators may support a
      single or multiple repositories and may specify which repository is to be used for these releases. An example of
      an open source repository is the CNCF Harbor (:cite:p:`cncf-harbor`)
  * - auto.cicd.005
    - The CI pipeline must scan source code and manifests to validate compliance with design and coding best practices.
    - 
  * - auto.cicd.006
    - The CI pipeline must support the build and packaging of images and deployment manifests from source code and
      configuration files.
    - 
  * - auto.cicd.007
    - The CI pipeline must scan images and manifests to validate for compliance with security requirements.
    - See section 7.10 (:ref:`chapters/chapter07:consolidated security requirements`). Examples of such security
      requirements include only ingesting images, source code, configuration files, etc., only from trusted sources.
  * - auto.cicd.008
    - The CI pipeline must validate images and manifests
    - Example: different tests
  * - auto.cicd.009
    - The CI pipeline must validate with all hardware offload permutations and without hardware offload
    - 
  * - auto.cicd.010
    - The CI pipeline must promote validated images and manifests to be deployable.
    - Example: promote from a development repository to a production repository
  * - auto.cicd.011
    - The CD pipeline must verify and validate the tenant request
    - Example: RBAC, request is within quota limits, affinity/anti-affinity, etc.
  * - auto.cicd.012
    - The CD pipeline after all validations must turn over control to orchestration of the software
    - 
  * - auto.cicd.013
    - The CD pipeline must be able to deploy into Development, Test, and Production environments
    - 
  * - auto.cicd.014
    - The CD pipeline must be able to automatically promote software from Development to Test and Production
      environments
    - 
  * - auto.cicd.015
    - The CI pipeline must run all relevant Reference Conformance test suites
    - 

**Table 9-4:** Automation CI/CD

CI/CD design requirements
^^^^^^^^^^^^^^^^^^^^^^^^^

A number of CI/CD pipeline properties and rules must be agreed between the different actors to allow the smooth
deployment and testing of the cloud infrastructures and the hosted network functions, irrespective of whether the
jobs operate open-source or proprietary software. These properties and rules prevent a specific deployment or
testing operation from forcing a particular CI/CD design or, worse, from requesting the deployment of a fully
dedicated CI/CD toolchain for a particular network service.

At first glance, the deployment and test job must not request specific CI/CD tools, such as
:cite:p:`jenkins` or :cite:p:`ci/cd-gitlab`. However, there are many
other ways where deployment and test jobs can constrain the end users, from the build servers to artefact management.
Any manual operation is discouraged, regardless of whether it is about the deployment or the test resources.

The following requirements also aim to deploy all CI/CD toolchains smoothly and easily via simple playbooks, as
targeted by the Reference Conformance suites currently leveraging :cite:p:`xtestingCI`.

+-----------------+---------------------------------------------------+------------------------------------------------+
| Ref #           | Description                                       | Comments/Notes                                 |
+=================+===================================================+================================================+
| design.cicd.001 | The pipeline must allow the chaining of           | For example, all deployment and test           |
|                 | independent CI/CD jobs.                           | operations, from bare metal to Kubernetes and  |
|                 |                                                   | OpenStack, and to network services.            |
+-----------------+---------------------------------------------------+------------------------------------------------+
| design.cicd.002 | The pipeline jobs should be modular.              | This allows the execution of jobs              |
|                 |                                                   | independently of others, for example, starting |
|                 |                                                   | with an existing OpenStack deployment.         |
+-----------------+---------------------------------------------------+------------------------------------------------+
| design.cicd.003 | The pipeline must decouple the deployment and the |                                                |
|                 | test steps.                                       |                                                |
+-----------------+---------------------------------------------------+------------------------------------------------+
| design.cicd.004 | The pipeline should leverage the job artefacts    |                                                |
|                 | specified by the CI/CD tools, provided by the     |                                                |
|                 | operator.                                         |                                                |
+-----------------+---------------------------------------------------+------------------------------------------------+
| design.cicd.005 | The pipeline must execute all the relevant        |                                                |
|                 | Reference Conformance suites without              |                                                |
|                 | modification.                                     |                                                |
+-----------------+---------------------------------------------------+------------------------------------------------+
| design.cicd.006 | The software vendors/providers must use CI/CD     |                                                |
|                 | tools provided by the operator.                   |                                                |
+-----------------+---------------------------------------------------+------------------------------------------------+
| design.cicd.007 | All jobs must be packaged as containers.          |                                                |
+-----------------+---------------------------------------------------+------------------------------------------------+
| design.cicd.008 | All jobs must leverage a common execution to      |                                                |
|                 | allow the templating of all the deployment and    |                                                |
|                 | test steps.                                       |                                                |
+-----------------+---------------------------------------------------+------------------------------------------------+
| design.cicd.009 | The deployment jobs must publish all outputs as   | For example, OpenStack RC, kubeconfig, yaml,   |
|                 | artefacts in a specified format.                  | and so on. Anuket specifies the formats in the |
|                 |                                                   | RC.                                            |
+-----------------+---------------------------------------------------+------------------------------------------------+
| design.cicd.010 | The test jobs must pull all the inputs as         | For example, OpenStack RC, kubeconfig, yaml,   |
|                 | artefacts in a specified format.                  | and so on. Anuket specifies the formats in the |
|                 |                                                   | RC.                                            |
+-----------------+---------------------------------------------------+------------------------------------------------+
| design.cicd.011 | The test jobs must conform to the Reference       |                                                |
|                 | Conformance test case integration requirements.   |                                                |
+-----------------+---------------------------------------------------+------------------------------------------------+

**Table 9-5:** CI/CD design

Tenant creation automation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Pretenant creation requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Topics related to pretenant creation requirements include the following:

1. Tenant Approval: use, capacity, data centres, and so on.

   - Validate that the Tenant's planned use meets the Operators Cloud Use policies
     (see :ref:`common/glossary:operational and administrative terminology`).
   - Validate that the capacity available within the requested cloud sites can satisfy the tenant requested quota
     for the vCPU, RAM, disk, and network bandwidth.
   - Validate that the cloud infrastructure can meet the tenant’s performance requirements (for example, I/O,
     latency, jitter, and so on).
   - Validate that the cloud infrastructure can meet tenant’s resilience requirements.

2. For environments that support :ref:`chapters/chapter04:profiles and workload flavours`:

   - Verify that any requested private flavours have been created.
   - Verify that the metadata for these private flavours has been created.
   - Verify that the tenant has the necessary permissions to use the requested private flavours.
   - Validate that host aggregates are available for the specified flavours (public and private).
   - Verify that the metadata matches the requested new flavours and host aggregates.

3. Tenant networks

   - Verify that the networks requested by the tenant exist.
   - Verify that the security policies are correctly configured to approved ingress and egress only.

4. Tenant admin, tenant member, and other tenant role approvals for user by role

   - Add all the tenant members and configure their assigned roles in the Enterprise Identity and Access management
     system (for example, LDAP).
   - Verify that these roles have been created for the tenant.

5. Approvals of the tenants' images and manifests

   - Verify and validate the tenants' images and manifests using virus scans, verifying the correct OS version and
     patch, and so on.

   ..Note::
    Tenants may also add new images or replace existing images after their environments are created and will be
    subject to image security measures.

6. Create, verify, and validate the tenant

   - Create the tenant.
   - Use a proto- or tenant-provided HEAT template or Helm chart for an NF, and perform a sanity test (for example,
     by using scripts to test the creation of the VM or container, ping tests, and so on).

