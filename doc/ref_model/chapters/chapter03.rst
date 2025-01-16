Modelling
=========

The infrastructure resources and their capabilities that a shared cloud infrastructure (a network function
virtualisation infrastructure or NFVI) provides for hosting workloads, including virtual network functions (VNFs) and
cloud-native network functions (CNFs), need to be clearly defined. A common understanding of which resources and their
corresponding capabilities a cloud infrastructure should provide will help to improve workload onboarding efficiency
and avoid issues that could negatively impact the length of time and the cost of onboarding and maintaining target
workloads and solutions on top of a virtualised infrastructure.

The abstraction model presented in this Reference Model (RM) specifies a common set of virtual infrastructure resources
that a cloud infrastructure will need to provide to be able to host most of the typical VNF/CNF Telco workloads. The
intention of this Reference Model is to adhere to the following principles:

- **Scope:** the model should describe the most relevant virtualised infrastructure resources, including acceleration
  technologies, that a cloud infrastructure needs to host the Telco workloads.
- **Separation of concern:** the model should support a clear distinction between the responsibilities related to
  maintaining the network function virtualisation infrastructure and the responsibilities related to managing the
  various VNF workloads.
- **Simplicity:** the amount of different types of resources, including their attributes and relationships to one
  another, should be kept to a minimum to reduce the configuration spectrum which needs to be considered.
- **Declarative**: the model should allow for the description of the intended state and the configuration of the cloud
  infrastructure resources for automated lifecycle management.
- **Explicit:** the model needs to be rich enough to cover the instantiation and the ongoing operation of the cloud
  infrastructure.
- **Lifecycle:** the model must distinguish between those resources which have independent lifecycles, but should group
  together those resources which share a common lifecycle.
- **Aligned:** the model should clearly highlight the dependencies between its components, to allow for a well-defined
  and simplified synchronisation of independent automation tasks.

**To summarise:**\ *the abstraction model presented in this document will build upon existing modelling concepts, and
simplify and streamline them to the needs of the Telco operators who intend to distinguish between infrastructure-related
and workload-related responsibilities.*

Model
-----

The abstraction model for the cloud infrastructure is divided into two logical layers:

- the virtual infrastructure layer
- the hardware infrastructure layer

The reason for this is that only the virtual infrastructure layer will be directly exposed to the workloads (VNFs/CNFs).

.. figure:: ../figures/ch03-model-overview.png
   :alt: Cloud infrastructure model overview
   :name: Cloud infrastructure model overview

   Cloud infrastructure model overview

The functionalities of each layer are as follows:

**Virtual infrastructure layer**

The virtual infrastructure layer comprises the following functionalities:

- **Virtual infrastructure resources:** These are all the infrastructure resources (compute, storage, and networks)
  which the cloud infrastructure provides to the VNF/CNF and other workloads. These virtual resources can be managed
  by the tenants and tenant workloads directly or indirectly via an application programming interface (API).
- **Virtual infrastructure manager:** This consists of the software components that manage the virtual resources and
  make those management capabilities accessible via one or more APIs. The responsibilities of this functionality
  include the management of logical constructs, such as tenants, tenant workloads, resource catalogues, identities,
  access controls, security policies, and so on.

**Hardware infrastructure layer**

The hardware infrastructure layer comprises the following functionalities:

- **Hardware infrastructure manager:** This is a logical block of functionality responsible for the management of the
  abstracted hardware resources (compute, network, and storage). As such, it is shielded from the direct involvement
  with server host software.
- **Hardware resources:** These consist of physical hardware components, such as servers (including random access
  memory, local storage, network ports, and hardware acceleration devices), storage devices, network devices, and the
  basic input output system (BIOS).

**Workload layer**

The workload layer comprises the workloads (VNFs/CNFs). The workloads are workload functions that are virtualized or
containerized, or both, which run within a virtual machine (VM) or as a set of containers.

Virtual infrastructure layer
----------------------------

Virtual resources
~~~~~~~~~~~~~~~~~

The virtual infrastructure resources provided by the cloud infrastructure can be grouped into four categories, as
shown in the following diagram:

.. figure:: ../figures/ch03-model-virtual-resources.png
   :alt: Virtual infrastructure resources provide virtual compute, storage, and networks in a tenant context

   Virtual infrastructure resources provide virtual compute, storage, and networks in a tenant context

- **Tenants:** The tenants represent an isolated and independently manageable elastic pool of compute, storage,
  and network resources.
- **Compute resources:** The compute resources represent virtualised computes for workloads and other systems, as
  necessary.
- **Storage resources:** The storage resources represent virtualised resources for persisting data.
- **Network resources:** The network resources represent virtual resources providing layer 2 and layer 3
  connectivity.

The virtualised infrastructure resources related to these categories are listed below.

Tenant
^^^^^^

A cloud infrastructure needs to be able to support multiple tenants and has to isolate sets of infrastructure
resources dedicated to specific workloads (VNFs and CNFs) from one another. Tenants represent an independently
manageable logical pool of compute, storage, and network resources abstracted from physical hardware.

**Example**\ *: a tenant within an OpenStack environment or a Kubernetes cluster.*

============ =======================================================================================================
Attribute    Description
============ =======================================================================================================
``name``     The name of the logical resource pool.
``type``     The type of tenant (for example, OpenStack tenant, Kubernetes cluster, and so on).
``vcpus``    The maximum number of virtual CPUs.
``ram``      The maximum random access memory size in GB.
``disk``     The maximum size of the ephemeral disk in GB.
``networks`` A description of external networks required for inter-domain connectivity.
``metadata`` The key/value pairs for selection of the appropriate physical context (for example, location,
             availability zone, and so on).
============ =======================================================================================================

**Table 3-1:** Attributes of a tenant

Virtual compute
^^^^^^^^^^^^^^^

A virtual compute is a virtual machine or container/pod that is can host the application components of the
workloads (VNFs/CNFs) of the tenant. A virtual compute, therefore, requires a tenant context and, since it
needs to communicate with other communication partners, it is assumed that the networks have been provisioned
in advance.

**Example**\ *: a virtual compute descriptor as defined in the TOSCA Simple Profile for NFV.*

================ =============================================================================
Attribute        Description
================ =============================================================================
``name``         The name of the virtual host.
``vcpus``        The number of virtual CPUs.
``ram``          The random access memory size, in GBs.
``disk``         The size of the root disk, in GBs.
``nics``         The sorted list of network interfaces connecting the host to the virtual
                 networks.
``acceleration`` The key/value pairs for the selection of the appropriate acceleration
                 technology.
``metadata``     The key/value pairs for the selection of the appropriate redundancy domain.
================ =============================================================================

**Table 3-2:** The attributes of the compute resources

Virtual storage
^^^^^^^^^^^^^^^

Virtual machines and containers can consume storage in a number of ways. The types of storage used include
the following:

- Storage that is managed via hypervisor and container runtime (hypervisor attached for virtual machines,
  and container persistent for containers), and is connected via the cloud infrastructure underlay network.
- Shared file storage and object storage, which is connected via the tenant/user overlay network. The
  details of the tenant storage consumption model are covered in `Storage for Tenant Consumption`_.

When managing the provision of virtual storage, the tenant should be able to request alternate performance
levels, capacity, and behaviours. The set of selectable attributes includes the following:

- Storage class: block, file, and object.
- Retention policy: persistent (storage volume/data) across the stop/start of the workload. With ephemeral
  storage, there is no data retention across the stop/start events for the workload.
- Underlying physical device type (HDD, SSD, and so on).
- Performance characteristics: these are defined as latency, input/output operations per second (IOPS), and
  throughput.
- Enhanced features: these are a set of selectable features, such as auto-replicate, encryption, and snapshot
  support.

..note::

  The approximate numeric ranges for the qualitative values used above are given in
  :ref:`chapters/chapter04:storage extensions`.

The storage resources have the following attributes, with metric definitions that support verification through
passive measurements (telemetry) where appropriate.

========================= ==============================================================================================
Attribute                 Description
========================= ==============================================================================================
``name``                  The name of the storage resources.
``data retention policy`` Persistent or ephemeral.
``performance``           Read-and-write (R/W) latency, the average amount of time to perform an R/W operation, in
                          milliseconds.
\                         Read-and-write IOPS, the average rate of performing R/W, in IO operations per second.
\                         Read-and-write throughput, the average rate of performing R/W operations, in bytes per
                          second.
``enhanced features``     Replication, encryption.
``type``                  Block, object, or file.
``size``                  The size, in GBs. Telemetry includes the amount of free, used, and reserved disk space, in
                          bytes.
========================= ==============================================================================================

**Table 3-3:** The attributes of the storage resources

Virtual network
^^^^^^^^^^^^^^^

This topic is covered in `Network <#network>`__.

Availability zone
^^^^^^^^^^^^^^^^^

An availability zone is a logical pool of physical resources, such as compute, block storage, and network).
These logical pools segment the physical resources of a cloud based on factors chosen by the cloud operator.
The cloud operator may create availability zones based on location, such as the rack or the datacenter, or
indirect failure domain dependencies, such as power sources. The workloads can leverage the availability zones
to utilise multiple locations or avoid sharing failure domains for a workload, thereby increasing the fault
tolerance of the workloads.

As a logical group with operator-specified criteria, the only mandatory attribute for an availability zone is
the name.

========= ==================================
Attribute Description
========= ==================================
``name``  The name of the availability zone.
========= ==================================

**Table 3-4:** The attributes of the availability zones

Virtual infrastructure manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The virtual infrastructure manager allows the operator to do the following:

- Set up, manage, and delete tenants.
- Set up, manage, and delete user and service accounts.
- Manage access privileges.
- Provision, manage, monitor, and delete virtual resources.

.. figure:: ../figures/ch03-model-virtual-manager.png
   :alt: Virtual infrastructure manager

   Virtual infrastructure manager

The virtual infrastructure manager needs to support the following functional aspects:

- **API/UI**: This is an application programming interface/user interface that provides access to the virtual resource
  management function.
- **Catalogue**: The catalogue manages the collection of available virtual resource templates that the cloud
  infrastructure can provide.
- **Inventory**: The inventory manages the information related to the virtual resources of a cloud infrastructure.
- **Scheduler**: The scheduler receives requests via the API/UI. It provisions and manages the virtual resources by
  coordinating the activities of the compute, storage, and network resource managers.
- **Monitoring**: This functionality monitors and collects information on all events and the current state of all the
  virtual resources.
- **Additional management functions**: these include identity management, access management, policy management (for
  example, to enforce security policies), and so on.
- **Compute resources manager**: This functionality provides a mechanism to provision the virtual resources with the
  help of the hardware compute resources.
- **Storage resources manager**: This functionality provides a mechanism to provision the virtual resources with the
  help of the hardware storage resources.
- **Network resources manager**: This functionality provides a mechanism to provision the virtual resources with the
  help of the hardware network resources.

Hardware infrastructure layer
-----------------------------

Hardware infrastructure resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The compute, storage, and network resources serve as the foundation of the cloud infrastructure. They are exposed to
and used by a set of networked host operating systems (OSs) in a cluster that normally handles the virtual infrastructure
layer, providing virtual machines or containers, where the application workloads (VNFs/CNFs) run.

.. figure:: ../figures/ch03-model-hardware-resources.png
   :alt: Cloud infrastructure hardware resources

   Cloud infrastructure hardware resources

In managed hardware infrastructure systems, these consumable compute, storage, and network resources can be provisioned
through operator commands or through software APIs. It is important to distinguish between the consumable resources
that are treated as leased resources from the actual physical hardware resources that are installed in the datacentre.
For this purpose, the hardware resource layer is conceptually split into a logical resource layer that exposes the
consumable resources to the software layer above, and the physical resource layer that is operated and managed by the
cloud infrastructure providers operations team from the hardware infrastructure management functions perspective.

Some installations might use a cluster of managed switches or storage components controlled by a switch fabric
controller or a storage fabric controller, or both, acting as an appliance system. This system should be federated
with the hardware infrastructure management system over an API to facilitate an exchange of configuration intent,
and status and telemetry information, allowing the hardware infrastructure management and management stack to automate
cloud infrastructure operations. These appliance systems normally also have their own equipment management APIs and
procedures for the hardware installation and maintenance staff.

An example of this is a cloud infrastructure stack federated with a commercial switch fabric, where the cloud
infrastructure can send (see the note below) networking configuration intent to the switch fabric and the switch
fabric can send status and telemetry information to the cloud infrastructure, for example, port/link status and
packet counters of many sorts. This allows the hardware infrastructure management stack and the cloud infrastructure
management stack to have network automation that includes the switches that are controlled by the federated switch
fabric. This would be a normal case for operators that have a separate networking department that owns and runs the
switch fabric separately from the datacentre.

..note::
  
  The word "send" is a loose definition of the action of getting a message across to the other side. It can be
  implemented in many different ways.

Hardware acceleration resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a given software network function and software infrastructure, hardware acceleration resources can be used to
achieve requirements, or improve cost and performance. The following table gives the reasons for using hardware
acceleration, together with examples of hardware acceleration use.

+--------------------------------+-------------------------------------------+-----------------------------------------+
| Reason for using hardware      | Example                                   | Comment                                 |
| acceleration                   |                                           |                                         |
+================================+===========================================+=========================================+
| To achieve technical           | Strict latency or timing accuracy.        | This must be done by optimizing the     |
| requirements.                  |                                           | compute node. It cannot be solved by    |
|                                |                                           | adding more compute nodes.              |
|                                |                                           |                                         |
+--------------------------------+-------------------------------------------+-----------------------------------------+
| To achieve technical           | Fit within power or space envelope.       | This is done by optimizing the cluster  |
| rrequirements.                 |                                           | of compute nodes.                       |
+--------------------------------+-------------------------------------------+-----------------------------------------+
| To improve cost and            | Lower costs and less power and cooling by | This is used when functionality can be  |
| performance.                   | improving the performance per node.       | achieved through the usage of the       |
|                                |                                           | accelerator, or by adding more          |
|                                |                                           | compute nodes.                          |
+--------------------------------+-------------------------------------------+-----------------------------------------+

**Table 3-5:** Reasons and examples for using hardware acceleration

Hardware accelerators can be used to offload the software execution for the purpose of accelerating the tasks to achieve
better performance, or offloading the tasks to another execution entity to achieve more predictable execution times,
efficient handling of the tasks, or separation of authority regarding who can control the execution of the tasks.

For further details about hardware acceleration, see `hardware acceleration abstraction`_.

Hardware infrastructure manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The hardware infrastructure manager supports the equipment management for all the managed physical hardware resources
of the cloud infrastructure.

In most deployments, the hardware infrastructure manager should also be the hardware infrastructure layer provisioning
manager of the compute, storage, and network resources that can be used by the virtualization infrastructure layer
instances. It provides an API enabling the vital resource recovery and control functions of the provisioned functions,
such as the reset and power control of the compute resources.

For deployments with more than one virtualization infrastructure layer instance that use a common pool of hardware
resources, it is necessary for the hardware infrastructure layer provisioning manager of the compute, storage, and
network resources to handle resource assignment and arbitration.

The resource allocation could be a simple record of which virtualization infrastructure layer instances have been
allocated physical hardware resources, or it could be a more advanced resource composition function that assembles
the consumed compute, storage, and network resources on demand from the physical hardware resource pools.

.. figure:: ../figures/ch03-model-hardware-manager.png
   :alt: Hardware infrastructure manager

   Hardware infrastructure manager

The hardware infrastructure manager allows you to do the following:

- Provision, manage, monitor, and delete hardware resources.
- Manage physical hardware resource discovery, monitoring, and topology.
- Manage hardware infrastructure telemetry and log collection services.

The hardware infrastructure manager must support the following functional aspects:

- **API/UI**: This is an application programming interface/user interface that provides access to the hardware resource
  management functions.
- **Discovery**: This functional aspect deals with discovering physical hardware resources and collecting relevant
  information about them.
- **Topology**: This deals with discovering and monitoring physical interconnections, such as cables, in between the
  physical hardware resources.
- **Equipment**: This functional aspect deals with managing the physical hardware resources in terms of configuration,
  firmware status, health/fault status, and autonomous environmental control functions, such as fan and power conversion
  regulations.
- **Resource allocation and composition**: This functional aspect deals with creating, modifying, and deleting logical
  compute, network, and storage resources through the composition of allocated physical hardware resources.
- **Underlay network resources manager**: This provides a mechanism to provision hardware resources and provide
  separation in between multiple virtualization infrastructure instances for the use of the underlay network, for
  example, switch fabric, switches, and SmartNICs.
- **Monitoring**: This functional aspect deals with monitoring and collecting information on events, current state, and
  telemetry data of the physical hardware resources and autonomous equipment control functions, as well as the switch
  and storage fabric systems.
- **Additional management functions**: These include software and configuration lifecycle management, identity management,
  access management, policy management (for example, the enforcement of security policies), and so on.

The Redfish® standard-based hardware infrastructure manager
-----------------------------------------------------------

This section proposes a Redfish-based hardware infrastructure manager for the Anuket project. Open Distributed
Infrastructure Management (ODIM) is an open-source software platform that delivers a means of distributed physical
infrastructure lifecycle management based on the industry standard DMTF Redfish API and model specification.

The :ref:`chapters/chapter09:configuration and lifecycle management` section of this reference model specifies the
Redfish standard for managing the infrastructure hardware. The GSMA's "Cloud Infrastructure Reference Model
(NG.126)" also specifies Redfish as the standard interface that should be made available by the infrastructure and
cloud infrastructure management components, in the infrastructure hardware layer.
 
Redfish is an internationally recognized standard: ISO/IEC 30115:2018 :cite:p:`iso-standard-83853`. The Redfish
interface specifies an HTTP RESTful interface that a client can use to manage conformant platforms. The Redfish
standard consists of a Redfish interface specification: Redfish Specification :cite:p:`redfish-specification` and
a model specification: Redfish Data Model Specification :cite:p:`redfish-data-model-specification-version`. The
interface specification defines the RESTful behaviour of the resources. The data model specification defines the
structure of the HTTP resources. The model is expressed as a schema using OpenAPI and json-schema formats. The
schema allows the implementation of Redfish clients using the OpenAPI and json-schema toolchains.

There are several open-source implementations of Redfish Clients and Redfish Services. A Redfish resource
aggregator can implement a scalable infrastructure manager which aggregates and exposes a standards-based Redfish
interface and services northbound to an orchestrator. 

The DMTF specifies the Redfish interface and model. It seeks to expand the manageability domains. The prescription
of what subset of the Redfish model needs to be implemented for a specific manageability domain is left to other
standards bodies. Redfish has defined a JSON syntax for the prescription, called a Redfish Profile, and
implemented an application which reads the Redfish Profile and tests for conformance of an implementation Interop
Validator :cite:p:`redfish-interop-validator`. The Redfish Profile mechanism is used by the Open Compute Project 
and Open Process Automation Forum.

Redfish fulfils the following requirements stated in the above hardware infrastructure manager section:

-	**API/UI**: Redfish specifies a programming interface. The HTTP interface is accessible remotely via an IP and
  locally via the Ethernet loopback mechanism.
-	**Discovery**: The Redfish schema provides a physical hardware resource model, including relevant information.
-	**Topology**: The Redfish schema contains a cable model.
-	**Equipment**: The Redfish schema contains a physical model and a functional model. The physical model
  expresses the chassis and the containers, and interconnects between them and environmental control functions.
  The functional model expresses the logical aspects and includes the configuration and firmware status. The
  physical and the functional model each has its own health/fault status information.
-	**Resource Allocation and Composition**: The Redfish schema has a composition model through which a client can
  compose a logical resource by allocating physical resources. FOr details, see the Redfish Composition
  Whitepaper :cite:p:`redfish-composition-whitepaper`.
-	**Underlay Network Resources Manager**: The Redfish schema has models for fabrics, switches, and SmartNICs.
-	**Monitoring**: The Redfish schema contains an event model for the client to receive hardware events and
  a telemetry model for collecting information across the entire model (physical and functional). For details,
  see the Redfish Telemetry Whitepaper :cite:p:`redfish-telemetry-whitepaper`.
-	**Additional Management Functions**: The Redfish schema has models for access management and identity
  management. For details, see the Redfish Data Model Specification
  :cite:p:`redfish-data-model-specification-version-2023.2`.

How Redfish fits into the ETSI NFV networking reference model
-------------------------------------------------------------

As shown in the figure below, a Redfish resource aggregator can play the role of hardware infrastructure manager
in the ETSI NFV networking reference model. Whereas this resource manager would expose a Redfish interface to
the northbound, the infrastructure pieces can themselves be managed using plugins.

.. figure:: ../figures/Chapter-3-ODIM-CloudInfraMgmt.png
   :alt: ODIM fitment in the ETSI NFV networking reference model 
   :name: ODIM fitment in the ETSI NFV networking reference model

The plugins may manage compute, storage, and network devices from multiple vendors.

Network
-------

Networking, alongside compute and storage, is an integral part of the cloud infrastructure (network function
virtualisation infrastructure). The general function of networking, in this context, is to provide the
connectivity between the various virtual and physical resources required for the delivery of a network service.
Such connectivity may manifest itself as a virtualized network between the virtual machines (VMs) and/or
containers (for example, overlay networks managed by SDN controllers, and/or programmable network fabrics), or
as an integration into the infrastructure hardware level for offloading some of the network service
functionality.

Normalization of the integration reference points between the different layers of the cloud infrastructure
architecture is one of the main concerns. In the networking context, the primary focus is directed on the packet
flow and control flow interfaces between the virtual resources (referred to as the software (SW) virtualization
layer) and the physical resources (referred to as the hardware (HW) infrastructure layer), as well as on related
integration into the various MANO reference points (hardware/network infrastructure management and orchestration).
The identification of these two different layers (the software virtualization layer and the hardware
infrastructure layer) remains in alignment with the separation of resources into virtual and physical resources,
generally used in this document. See, for example, :numref:`Cloud Infrastructure Model Overview`. The importance
of understanding the separation of concerns between the software virtualization layer and the hardware
infrastructure layer is important because without it, the cardinality of having multiple CaaS and IaaS instances
executing on their own private virtual resources from the single shared hardware infrastructure layer cannot be
expressed in separate administrative domains.

Network principles
~~~~~~~~~~~~~~~~~~

There are a number of principles that should be followed during the development and definition of the networking
scope for the Reference Model, Reference Architectures, Reference Implementations, and Reference Conformance test
suites. They are as follows:

- Abstraction: This is a standardized network abstraction layer between the virtualisation layers and the network
  physical resources layer that hides, or abstracts, the details of the network physical resources from the
  virtualization layers.

..

   **Note:** In deployment phases, this principle may be applied in many different ways, for example, depending on
   target use case requirements, workload characteristics, different algorithm implementations of pipeline stages,
   and available platforms. The network abstraction layer supports, for example, physical resources with or without
   programmable hardware acceleration, or programmable network switches.

- Agnosticism: This defines the network fabric concepts and models that can carry any type of traffic in terms of
  the following:

  - Control, user, and management traffic types.
  - Acceleration technologies that can support multiple types of infrastructure deployments and network function
    workloads.

- Automation: This enables end-to-end automation, from physical fabric installation and provisioning to the
  automation of the onboarding of the workloads (VNFs/CNFs).
- Openness: All networking is based on open-source or standardized APIs (northbound interfaces (NBIs) and
  southbound interfaces (SBIs)), and should enable the integration of open-source networking components, such as
  SDN controllers.
- Programmability: The network model enables a programmable forwarding plane controlled from a separately deployed
  control plane.
- Scalability: The network model enables scalability to handle all traffic traversing from north to south and east
  to west, enabling large and small deployments in a non-blocking manner.
- Workload agnostic: This network model is capable of providing connectivity to any type of workload, including
  VNF, CNF, and BareMetal workloads.
- Carrier-grade: This network model is capable of supporting deployments of the carrier-grade workloads.
- Future proof: This network model is extendible to support known and emerging technology trends, including
  SmartNICs, FPGAs, and programmable switches, integrated for multiclouds and Edge-related technologies.

Network layering and concepts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Cloud Infrastructure Networking Reference Model is an essential foundation that governs all Reference
Architectures and cloud infrastructure implementations to enable multiple cloud infrastructure virtualization
technology choices and their evolution. These include the following:

- single Infrastructure as a Service (IaaS)-based virtualization instances with virtual machines (VM)
- multi-IaaS-based virtualization instances
- cloud-native Container as a Service (CaaS)-based virtualization instances
- hybrid multi-IaaS- and CaaS-based virtualization instances

To retain the cloud paradigms of automation, scalability, and usage of shared hardware resources when introducing
CaaS instances, it is necessary to allow the co-deployment of multiple simultaneous IaaS and CaaS instances on a
shared pool of hardware resources.

Compute and storage resources are rarely shared between IaaS and CaaS instances. However, the underpinning
networking, most commonly implemented with Ethernet and IP, must be shared and managed as a shared pool of underlay
network resources, to enable the pooled usage of compute and storage from a managed shared pool.s

Throughout this section, a number of references to ETSI NFV are made. They are explicitly made towards the ETSI NFV
models in the architectural framework:

- ETSI GS NFV 002 V1.2.1 cite:p:`etsigsnfv002`
- ETSI GR NFV-IFA 029 V3.3.1 :cite:p:`etsigrnfvifa029`

Cloud and Telco networking are layered. It is important to keep the dependencies between the layers to a minimum,
to enable security, separation, and portability between multiple implementations and generations.

Before we start developing a deep model, we need to agree on some foundational concepts and layering that allow
the decoupling of implementations between the layers. We will pay particular attention to four concepts in this
section:

- underlay and overlay networking concepts
- hardware and virtual infrastructure layer concepts
- software-defined underlay and overlay networking concepts
- programmable networking fabric concepts

Underlay and overlay networking concepts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ETSI Network Functions Virtualization Architectural Framework, as mentioned above, describes how a virtual
infrastructure layer instance abstracts the hardware resources and separates the virtualization tenants (workload)
from each other. It also clearly states that the control and implementation of the hardware layer is out of scope
for that specification.

When having multiple virtual infrastructure layer instances on a shared hardware infrastructure, the networking
can be layered in an underlay and an overlay network layer. The purpose of this layering is to ensure the
separation of the overlay networks of the virtualization tenants (workload) from each other, while allowing the
traffic to flow on the shared underlay network between all the Ethernet-connected hardware devices.

The overlay networking separation is often done through the encapsulation of the tenants' traffic using overlay
protocols, for example, through VxLAN or EVPN on the underlay networks, based, for example, on L2 (VLAN) or L3
(IP) networks.

The overlay network for each cloud infrastructure deployment must support a basic primary tenant network between
the instances within each tenant. Due to the nature of the telecom applications handling of the networks and their
related network functions, they often need access to external non-translated traffic flows and have multiple
separated or secondary traffic channels with abilities for different traffic treatments.

In some instances, the virtualization tenants can bypass the overlay networking encapsulation to achieve better
performance, or network visibility or control. A common method to bypass the overlay networking encapsulation that
is normally done by the virtualization layer is the VNF/CNF usage of SR-IOV that effectively takes over the
physical and virtual functions of the NIC directly into the VNF/CNF tenant. In these cases, the underlay networking
must handle the separation, for example, through a virtual termination end point (VTEP) that encapsulates the
overlay network traffic.

   **Note:** Bypassing the overlay networking layer is a violation of the basic decoupling principles. However, in
   some cases it is unavoidable with existing technologies and available standards. Until suitable technologies and
   standards are developed, a set of agreed exemptions has been agreed that forces the underlay networking to handle
   the bypassed overlay networking separation.

A VTEP could be manually provisioned in the underlay networking, or be automated and controlled through a software-
defined networking controller interface, into the underlying networking in the hardware infrastructure layer.

Hardware and virtual infrastructure layer concepts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The cloud infrastructure, based on the ETSI NFV infrastructure with hardware extensions, is composed of two distinct
layers, referred to here as a hardware infrastructure layer and virtual infrastructure layer. When there are multiple
separated simultaneously deployed virtual infrastructure domains, the architecture and deployed implementations must
enable each of them to be in individual non-dependent administrative domains. The hardware infrastructure must then
also be enabled, to be an administrative domain fully separated from all of the virtualization domains.

For cloud infrastructure implementations of multiple separated simultaneous virtual infrastructure layer instances on
a shared hardware infrastructure, the hardware resources must also be separate. This means the servers, the storage,
and the underlay networking resources that interconnect the hardware resources, for example, through a switching
fabric.

To allow multiple separated simultaneous virtual infrastructure layer instances onto a shared switching fabric, it is
necessary to split the underlay networking resources into non-overlapping addressing domains on suitable protocols,
such as VxLAN with their VNI ranges. This separation must be done through an administrative domain that cannot be
compromised by any of the individual virtualization infrastructure layer domains, either by malicious or unintentional
underlay network mapping or configuration.

These concepts are similar to the way the hyperscaler cloud providers (HCPs) offer virtual private clouds for users of
bare-metal deployment on the HCP shared pool of servers, storage, and networking resources.

The separation of the administrative domains of the hardware and virtual infrastructure layers makes it important that
the Reference Architectures do not include direct management or dependencies of the pooled physical hardware resources
in the hardware infrastructure layer, such as servers, switches, and underlay networks from within the virtual
infrastructure layer. All automated interaction from the virtual infrastructure layer implementations towards the
hardware infrastructure with its shared networking resources in the hardware infrastructure Layer must go through a
common abstracted Reference Model interface.

Software-defined underlay and overlay networking concepts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A major point with a cloud infrastructures is to automate as much as possible. An important tool
for networking automation is software-defined networking (SDN). Doftware-defined networking comes
in many different forms and can act on multiple layers of the networking. In this section, we will
deal with the internal networking of a datacentre, and not how datacentres interconnect with each
other or gain access to the world outside.

When there are multiple simultaneously deployed instances of the virtual infrastructure layers on
the same hardware infrastructure, it is important to ensure underlay networking separation in the
hardware infrastructure layer. This separation can be done manually through the provisioning of a
statically configured separation of the underlay networking in the hardware infrastructure layer. A
better and more agile usage of the hardware infrastructure is to offer each instance of the virtual
infrastructure layer a unique instance of an SDN interface into the shared hardware infrastructure.
Since these SDN instances only deal with a well-separated portion, or slice, of the underlay
networking, we call this interface SDN underlay (SDNu).

The hardware infrastructure layer is responsible for keeping the different virtual infrastructure
layer instances separated in the underlay networking. This can be done through manual provisioning
methods or can be automated through a hardware infrastructure layer orchestration interface. The
separation responsibility is also valid between all instances of the SDNu interface, since each
virtual infrastructure layer instance does not know about the other virtual infrastructure
instances, and is therefore neither disturbed by them nor able to reach them.

An SDN overlay control interface (SDNo) is responsible for managing the virtual infrastructure 
layer virtual switching or routing, or both, as well as its encapsulation and its mapping onto the
underlay networks.

In cases where the VNF/CNF bypasses the virtual infrastructure layer virtual switching and its
encapsulation, as described above, the hardware infrastructure layer must perform the encapsulation
and mapping onto the underlay networking to ensure underlay networking separation. This should be a
prioritized capability in the SDNu control interface, since Anuket currently allows exemptions for
bypassing the virtual switching, for example, through SR-IOV.

SDNo controllers can request underlay networking encapsulation and mapping to be performed by
signalling to an SDNu controller. However, today there is no standardized way for this signalling.
Because of this, there is a missing reference point and API description in this architecture.

Multiple instances of Container as a Service (CaaS) virtual infrastructure layers running on an
Infrastructure as a Service (IaaS) virtual infrastructure layer could make use of the IaaS layer to
handle the required underlay networking separation. In these cases, the IaaS virtualization
infrastructure manager (VIM) could include an SDNu control interface enabling automation.

   **Note:** The Reference Model describes a logical separation of the SDNu and SDNo interfaces to
   clarify the separation of administrative domains where applicable. In real deployment cases, an
   operator can select to deploy a single SDN controller instance that implements all the necessary
   administrative domain separations or have separate SDN controllers for each administrative
   domain. A common deployment scenario today is to use a single SDN controller handling both the
   underlay and the overlay networking, which works well in implementations where there is only one
   administrative domain that owns both the hardware infrastructure and the single virtual
   infrastructure instance. However, a shared underlay network that ensures separation must be
   under the control of the shared hardware infrastructure layer. One consequence of this is that
   the Reference Architectures must not model collapsed SDNo and SDNu controllers, since each SDNo
   must remain unaware of other deployed implementations in the virtual infrastructure layer that
   are running on the same hardware infrastructure.

Programmable networking fabric concept
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The concept of a programmable networking fabric pertains to the ability to have an effective
forwarding pipeline (also known as a forwarding plane) that can be programmed or configured, or
both, without any risk of disruption to the shared underlay networking that is involved with the
reprogramming for the specific efficiency increase.

The forwarding plane is distributed by nature. It must be possible to implement it, both in switch
elements and on SmartNICs (managed outside the reach of the host software), so that both can be
managed from a logically centralised control plane, residing in the hardware infrastructure layer.

The logically centralized control plane is the foundation for the authoritative separation between
different virtualization instances or bare metal network function applications that are regarded as
untrusted, both from the shared layers and from each other.

Although the control plane is logically centralized, scaling and control latency concerns must
allow the implementation of the control plane to be distributed when required.

All VNF, CNF, and virtualization instance acceleration, as well as all specific support
functionalities that are programmable in the forwarding plane, must be confined to the
well-separated sections or stages of any shared underlay networking. A practical example could be a
virtualization instance or VNF/CNF that controls a NIC/SmartNIC, where the underlay networking
(switch fabric) ensures the separation in the same way as for SR-IOV cases today.

The nature of a shared underlay network that ensures separation and is robust is that all code in
the forwarding plane and in the control plane must be under the scrutiny and lifecycle management
of the hardware infrastructure layer.

This also implies that programmable forwarding functions in a programmable networking fabric are
shared resources. Therefore, they will have to obtain standardized interfaces over time, in order
to be useful for multiple VNF/CNF and multivendor architectures, such as ETSI NFV. An example of
such future extensions of shared functionalities implemented by a programmable networking fabric
are L3 as a Service, Firewall as a Service (FaaS), and Load Balancing as a Service (LBaaS).

   **Note:** Appliance-like applications that fully own their infrastructure layers (that is, they
   share nothing) could manage and use a programmable networking fabric in many ways. However, that
   is not a cloud infrastructure implementation and therefore falls outside the use cases for these
   specifications.

Networking reference model
~~~~~~~~~~~~~~~~~~~~~~~~~~

The cloud infrastructure networking reference model, depicted in
:numref:`Networking Reference Model based on the ETSI NFV`, is based on the ETSI NFV model
enhanced with container virtualization support and a strict separation of the hardware
infrastructure and virtualization infrastructure layers in the NFVI. It includes all the above
concepts, and enables multiple well-separated simultaneous virtualization instances and domains,
allowing a mix of IaaS, CaaS on IaaS, and CaaS on bare metal, on top of a shared hardware
infrastructure.

It is up to any deployment of the cloud infrastructure to decide what networking-related objects to
use. However, all Reference Architectures have to be able to map into this model.

.. figure:: ../figures/RM-Ch03_5-Networking-Reference-Model-based-on-the-ETSI-NFV.png
   :alt: Networking reference model based on the ETSI NFV
   :name: Networking reference model based on the ETSI NFV

   Networking reference model based on the ETSI NFV

Deployment examples based on the networking reference model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Switch fabric and SmartNIC examples for underlay networking separation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The hardware infrastructure layer can implement the underlay networking separation in any type of
packet handling component. This may be deployed in many different ways, depending on target use
case requirements, workload characteristics, and available platforms. Two of the most common ways
are the following:

1. Within the physical switch fabric.
2. In a SmartNIC connected to the server CPU which is controlled over a management channel that
   is not reachable from the server CPU and its host software.

In either way, the underlay networking separation is controlled by the hardware infrastructure
manager.

In both cases, the underlay networking can be externally controlled over the SDNu interface that
must be instantiated with the appropriate underlay networking separation for each of the
virtualization administrative domains.

   **Note:** The use of SmartNIC in this section pertains only to the underlay networking
   separation of virtual instances in separate overlay domains, an approach that is much the same
   as that of AWS with their Nitro SmartNIC. This is the important consideration for the Reference
   Model that enables multiple implementation instances from one or several reference architectures
   to be used on a shared underlay network. The use of SmartNIC components from any specific
   virtual instance, for example, for internal virtual switching control and acceleration, must be
   regulated by each reference architecture without interfering with the authoritative underlay
   separation laid out in the Reference Model.

Two examples of different common hardware realizations of underlay network separation in the
hardware infrastructure layer can be seen in :numref:`Underlay Networking separation examples`
below.

.. figure:: ../figures/RM-Ch03_5-Underlay-Networking-separation-examples.png
   :alt: Underlay networking separation examples
   :name: Underlay networking separation examples

   Underlay networking separation examples

Examples of the relationship between SDN overlay and SDN underlay layering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Two use case examples with both SDNo and SDNu control functions depicting a software-based virtual
switch instance in the virtual infrastructure layer and another high-performance-oriented virtual
infrastructure instance (for example, enabling SR-IOV) are described in
:numref:`SDN Controller relationship examples`, below. The examples show how the encapsulation and
mapping can be done in the virtual switch or in a SmartNIC, on top of a statically provisioned
underlay switching fabric. An alternative example could show the SDNu controlling the underlay
switching fabric without the usage of SmartNICs.

.. figure:: ../figures/RM-Ch03_5-SDN-Controller-relationship-examples.png
   :alt: SDN controller relationship examples
   :name: SDN controller relationship examples

   SDN controller relationship examples

Example of IaaS and CaaS virtualization infrastructure instances on a shared hardware infrastructure with SDN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:numref:`Networking Reference Model deployment example` depicts a networking reference model
deployment example to demonstrate the mapping to ETSI NFV reference points with additions of packet
flows through the infrastructure layers and other necessary reference points. The example
illustrates the individual responsibilities of a complex organization with multiple separated
administrative domains, represented with separate colours.

This example is, or will be, a common scenario for operators who modernize their network functions
during a lengthy period of migration from VNFs to cloud-native CNFs. Today, the network functions
are predominantly VNFs on IaaS environments. The operators are gradually moving a selection of
these into CNFs on CaaS that either sit on top of the existing IaaS or directly on bare metal. It
is expected that there will be multiple CaaS instances in most networks, since a generic standard
of CaaS implementation that will be capable of supporting all types of CNFs from any vendor is not
foreseen. It is also expected that many CNFs will have dependencies on a particular CaaS version or
a set of instances which will prohibit a separation of lifecycle management between individual CNFs
and CaaS instances.

.. figure:: ../figures/RM-Ch03_5-Networking-Reference-Model-deployment-example.png
   :alt: Networking reference model deployment example
   :name: Networking reference model deployment example

   Networking reference model deployment example

Service function chaining
~~~~~~~~~~~~~~~~~~~~~~~~~

Over the past few years, there has been a significant move towards decomposing network functions
into smaller sub-functions that can be independently scaled and potentially reused across multiple
network functions. A service chain allows the composition of network functions by passing selected
packets through multiple smaller services.

To support this capability in a sustainable manner, it is necessary to be able to model service
chains as a high-level abstraction. This is essential for ensuring that the underlying connection
setup, and direction or redirection of traffic flows can be performed in an automated manner. At a
high level, a service chain can be considered to be a directed acyclic graph with the composing
network functions being the vertices. Building on top of this, a service chain can be modelled by
defining two parameters:

-  An acyclic graph defining the service functions that need to be traversed for the service chain.
   This allows for multiple paths for a packet to traverse the service chain.
-  A set of packet/flow classifiers that determine which packets enter and exit a given service
   chain.

These capabilities need to be provided for both virtualized and containerized (cloud-native)
network functions, as it will be necessary to support both of them for the foreseeable future.
Since virtualized network functions have existed for a while, there is support, albeit partial, for
service chaining in virtualized environments, in orchestration platforms such as OpenStack.
Container orchestration platforms, such as Kubernetes, do not support service chaining and may
require development of new primitives, in order to support advanced networking functions.

It is expected that reference architectures will provide a service chain workflow manager that
accepts the service function acyclic graph and can identify or create the necessary service
functions, and the networking between them, in order to instantiate such a chain.

It is also necessary to provide specialized tools to aid the troubleshooting of individual services
and the communication between them, in order to investigate issues in the performance of composed
network functions. At the very least, there needs to be a provision of packet-level and byte-level
counters and statistics, as the packets pass through the service chain, in order to ascertain any
issues with forwarding and performance. Mechanisms to trace the paths of selected subsets of
traffic as they flow through the service chain are also required.

Service function chaining model introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Service function chaining (SFC) can be seen as a layered structure where the service function plane
(the SFC data plane consists of a service function forwarder, a classifier, a service function, and
a service function proxy) resides over a service function overlay network. SFC uses a
service-specific overlay that creates the service topology. The service overlay provides service
function connectivity built on top of the existing network topology. It leverages various overlay
network technologies, such as the Virtual eXtensible Local Area Network (VXLAN), for
interconnecting SFC data plane elements, and allows the establishment of service function paths
(SFPs).

In a typical overlay network, packets are routed according to networking principles and use a
suitable path for the packet to be routed from a source to its destination.

However, in a service-specific overlay network, packets are routed according to policies. This
requires specific support at the network level, such as at CNI in the CNF environment, to provide
such a specific routing mechanism.

Service function chaining architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The service function chaining (SFC) architecture is composed of functional management, control, and
data components, as categorized in Table 3-6.

The following table highlights areas under which common SFC functional components can be
categorized.


+------------+------------------------+--------------------------------------------------------------------------------+
| Components | Example                | Responsibilities                                                               |
+============+========================+================================================================================+
| Management | SFC orchestrator       | This is a high level of orchestrator. It orchestrate the SFC based on SFC      |
|            |                        | models and policies, with the help of control components.                      |
|            +------------------------+--------------------------------------------------------------------------------+
|            | SFC OAM components     | These are responsible for the SFC OAM functions.                               |
|            +------------------------+--------------------------------------------------------------------------------+
|            | VNF MANO               | The NFVO, VNFM, and VIM are responsible for the lifecycle of the SFC data      |
|            |                        | components.                                                                    |
|            +------------------------+--------------------------------------------------------------------------------+
|            | CNF MANO               | The CNF DevOps components are responsible for the lifecycle of the SFC data    |
|            |                        | components.                                                                    |
+------------+------------------------+--------------------------------------------------------------------------------+
| Control    | SFC SDN controller     | The SDNC is responsible for creating the service-specific overlay network. It  |
|            |                        | deploys different techniques stitch the wiring. However, It provides the same  |
|            |                        | functionality, for example, 12xconn, SRv6, segment routing, and so on.         |
|            +------------------------+--------------------------------------------------------------------------------+
|            | SFC renderer           | The SFC renderer creates and wires the ports and interfaces for the SF data    |
|            |                        | path.                                                                          |
+------------+------------------------+--------------------------------------------------------------------------------+
| Data       | Core components\SF,    | These are responsible for steering the traffic for the intended service        |
|            | SFF, SF proxy          | functionalities based on policies.                                             |
+------------+------------------------+--------------------------------------------------------------------------------+

**Table 3-6:** SFC architecture components

   **Note:** These are logical components and are listed for their functionalities only.

The SFC architecture components can be viewed according to Figures 3.10 and 3.11.

:numref:`SFC Architecture for VNF based SFs` shows the simple architecture of an SFC with multiple
VNFs, as SF data plane components, along with the SFC management and NFV MANO components.

.. figure:: ../figures/ch03-model-sfc-architecture-vnf-2.png
   :alt: SFC architecture for VNF-based SFs
   :name: SFC architecture for VNF-based SFs

   SFC architecture for VNF-based SFs

:numref:`SFC Architecture for CNF based SFs` shows the simple architecture of an SFC with multiple
CNFs, as SF data plane components, along with the SFC management and CNF MANO components.

.. figure:: ../figures/ch03-model-sfc-architecture-cnf-2.png
   :alt: SFC architecture for CNF-based SFs
   :name: SFC architecture for CNF-based SFs

   SFC architecture for CNF-based SFs

The SFC management components, together with the control components, are responsible for rendering
SFC requests to service function paths. For this they convert the requisite SFC policies into
network topology-dependent paths and forward steering policies. The relevant SFC data components -
classifiers and service function forwarders - are responsible for managing the steering policies.

Information flows in service function chaining
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creation of service function chain
''''''''''''''''''''''''''''''''''

The creation of the SFC might include a design or preparation phase comprising the following:

- The service functions that are included in the SFC.
- The routing order in the service function, if the SFC is composed of more than one service
  function.

:numref:`Creation of Service Function Chain` shows an SFC creation call flow, separated logically
in two steps.

.. figure:: ../figures/ch03-model-sfc-info-create-flow.png
   :alt: Creation of a service function chain
   :name: Creation of a service function chain

   Creation of a service function chain

1. Creation of the service functions of the SFC.

- The flow of steps to enable the SFC creation can be as follows:

  a. The SFC orchestrator creates the SFs with the help of the VNF MANO or the CNF MANO.
  b. The SFC Renderer attaches the SFC-aware interfaces at the SFs to enable the service plane.
  c. The NFVO boots up the relevant SF configurations at the SF.

     **Note:** These steps are optional, if the SFC orchestrator discovers that the SFs have
     already been created.

2. Creation of the service function path (SFP) using the created SFs and associated interfaces.

- A service function path consists of the following:

   - A set of ports (in the VNF environment) or interfaces (in the CNF environment) that define the
     sequence of the service functions.
   - A set of flow classifiers that specify the classified traffic flows entering the chain.

- This step creates a new chain policy with chain rules. The chain rules can include the identifier
  of a traffic flow, the service characteristics, the SFC identifier, and related information to
  route the packets along the chain. The service characteristics can be application layer matching
  information, such as URLs. The traffic flow identifier identifies the kind of traffic flow, such
  as video, TCP, or HTTP, that needs to be serviced. It can be a specific subscriber who is
  applying the service (for example, parental control). The SFC identifier steers the matched
  traffic along the SFP with SFC encapsulation.

  a. The SFC orchestrator creates an SFP with the help of the SDNC.
  b. The SDNC pushes the SFC traffic steering policies to the SFF or SFFs.
  c. The SFC classifier policy is provided for the SFP to the SFC classifier by the SFC controller.
  
  **Note:** This is not shown in the call flow.

Updating the service function chain
'''''''''''''''''''''''''''''''''''

The SFP or the SFC can be updated for various reasons. Some of these reasons include the following:

- The SFC controller monitors the SFP status and alerts the SFC controller if the SFP does not meet
  the service-level agreement (SLA), or there is some other type of anomaly.
- The SFC design changes to update the SF order, and the inclusion or removal of SFs.
- There are changes in the SFC policy rules.

Data steering in the service function chain
'''''''''''''''''''''''''''''''''''''''''''

:numref:`DataSteering` shows traffic steering along the SFP.

.. figure:: ../figures/ch03-model-sfc-data-flow.png
   :alt: Data steering in the service function chain
   :name: DataSteering

   Data steering in the service function chain

- The SFC classifier detects the traffic flow based on the classification policies. For example, to
  enable the SGi-Lan feature as the SFC, the 5G user plane function (UPF) acts as the SFC
  classifier. The UPF receives the classification policies from the 5G policy control function
  (PCF) as traffic steering policies.
- The SFC classifier applies the SFC encapsulation (for example, SCH or NSH) and routes the traffic
  towards the SFF, acting as an entry point to the SFP. The SFC encapsulation provides, at a
  minimum, SFP identification, and is used by the SFC-aware functions, such as the SFF and
  SFC-aware SFs.
- The SFF, based on the SFC encapsulation, routes the traffic to the SF for service
  functionalities.
- The SF updates the SFC encapsulation, based on its policies, for further services.
- At the end of the SFP, the SFC encapsulation is removed and the packet is routed out of the SFP.


Time-sensitive networking
~~~~~~~~~~~~~~~~~~~~~~~~~

Many network functions have time sensitivity for processing and require a high-precision
synchronized clock for the cloud infrastructure. A subset of these workloads, such as RAN, also
require support for synchronous Ethernet.

+--------------------------------+-----------------------------------+-------------------------------------------------+
| Reason for using synchronous   | Example                           | Comment                                         |
| precision clock                |                                   |                                                 |
+================================+===================================+=================================================+
| To achieve technical           | Strict latency or timing          | Must be done for precise low-latency            |
| requirements.                  | accuracy.                         | communication between the data source and the   |
|                                |                                   | receiver.                                       |
+--------------------------------+-----------------------------------+-------------------------------------------------+
| To achieve technical           | Separation of the processing      | Ability to separate RAN into RU, DU, and CU on  |
| requirements.                  | pipeline.                         | different or stretched clusters.                |
+--------------------------------+-----------------------------------+-------------------------------------------------+

**Table 3-7:** Reasons and examples for precise clock and synchronization

Precise synchronization requires a specialized card that can be on a server or a network device
motherboard, or can be part of an NIC, or both.

OpenStack and Kubernetes clusters use Network Time Protocol (NTP)
(Protocol and Algorithms Specification :cite:p:`rfc5905`,
Autokey Specification :cite:p:`rfc5906`,
Managed Objects :cite:p:`rfc5907`,
Server Option for DHCPv6 :cite:p:`rfc5908`)
as the default time synchronization for the cluster. Such a level of synchronization is
insufficient for some network functions. Precision Time Protocol version 2 PTP
:cite:p:`precision-time-protocol-version-2` __ :cite:p:`ieee1588dash2019` is commonly used for
time-sensitive networking. This allows synchronization in microsecond range, rather than the
millisecond range that the NTP provides.

Some setwork functions, such as vDU or vRAN, also require SyncE :cite:p:`syncE` :cite:p:`itutg8262`.
The Control, User, and Synchronization (CUS) plane specification defines different topology options
that provide a Lower Layer Split Control plane 1-4 (LLS-C1 - LLS-C4) with different synchronization
requirements (ITU-T G.8275.2 :cite:p:`itutg82752`).

SyncE was standardized by the ITU-T, in cooperation with the IEEE, with the following three
recommendations:

- ITU-T Rec. G.8261: this defines aspects about the architecture and the wander performance of
  SyncE networks.
- ITU-T Rec. G.8262: this specifies synchronous Ethernet clocks for SyncE.
- ITU-T Rec. G.8264: this describes the specification of Ethernet Synchronization Messaging Channel
  (ESMC) SyncE architecture. It requires, at minimum, the replacement of the internal clock of the
  Ethernet card by a phase-locked loop, in order to feed the Ethernet PHY.

Load balancer
~~~~~~~~~~~~~

Load balancing is the process of distributing a set of tasks over a set of resources (computing
units), with the goal of improving the overall scalability and availability of the system. Load
balancing can optimize the response time and avoid overloading certain compute nodes, while other
compute nodes are left idle.

The two main approaches to load balancing are as follows:

- Static algorithms: these do not consider the state of different machines.
- Dynamic algorithms: these are usually more general and more efficient. However, they require 
  exchanges of information between the different compute units, with a possible tradeoff of
  integration complexity and reduced efficiency.

Load balancers can be categorized or configured in following ways:

-	Based on hardware devices or written in software.
-	Operating on network Layer 4 or 7.
-	Balancing incoming traffic/requests using target selection, such as:

  - Static: random, round robin, based on the performance of the target, the client IP address, the
    URL path, or the hash.
  - Dynamic: the minimum number of connections and the minimum response time.

To increase redundancy, multiple replicas of load balancers are placed into a load balancing
cluster.

Kubernetes networking semantics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The support for traditional network orchestration is non-existent in Kubernetes, as it is first and
foremost a Platform as a Service (PaaS) environment and not an Infrastructure as a Service (Iaas)
component. There is no network orchestration API, as there is in Neutron in OpenStack, and there is
no way to create L2 networks, instantiate network services, such as L3aaS and LBaaS, and then
connect them all together, as can be done using Neutron.

Kubernetes networking can be divided into two parts:

- Built-in network functionality, available through the pod’s mandatory primary interface.
- Network functionality, available through the pod’s optional secondary interfaces.

Built-in Kubernetes network functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kubernetes currently only allows for one network, the cluster network, and one network attachment
for each pod. Each pod and container has an eth0 interface. This interface is created by
Kubernetes at pod creation and is attached to the cluster network. All communication to and from
the pod is done through this interface. To allow for only one interface in a pod removes the need
for traditional networking tools, such as VRFs, and additional routes and routing tables, inside
the pod network namespace.

Multiple networks and advanced configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently Kubernetes does not in itself support multi-networks, pod multi-network attachments, or
network orchestration. This is supported by using a container network interface
:cite:p:`container-network-interface` multiplexer, such as Multus :cite:p:`multus`. The Network
Plumbing Working Group :cite:p:`network-plumbing-working-group` has produced the Kubernetes Network
Custom Resource Definition De Facto Standard
:cite:p:`kubernetes-network-custom-resource-definition-de-facto-standard`. This document describes
how secondary networks can be defined and attached to pods.

Storage
-------

Introduction to storage
~~~~~~~~~~~~~~~~~~~~~~~

The general function of the storage subsystem is to provide the persistent data storage required
for the delivery of a network service. In the context of the cloud infrastructure, the storage
subsystem needs to accommodate the needs of the tenanted applications and platform management. Each
of the following has common and specific needs for storage, in terms of performance, capacity, and
consumption models:

- Underlying compute host boot and virtual machine hosting.
- Control plane configuration and management plane storage for fault and performance management and
  automation, and capacity management and reporting.
- Tenant application and VNF storage needs.

The combination of common but diverse needs, in conjunction with the differences in the hosting
environments (from large datacentres to small edge deployments), has resulted in the proliferation
of storage technologies and their deployment architectures. To address this, the Reference Model
outlines a general cloud storage model (see :numref:`General Cloud Storage Model` - General cloud
storage model). The model outlines the different types of storage technologies and how they can be
used to meet the need for the following across large datacentres and small edge deployments:

- Provision of storage via dedicated storage systems.
- Multitenant cloud storage.
- Control and management plane storage needs.

This model can then be used for implementing reference architectures.

.. figure:: ../figures/rm-chap3.6-general-cloud-storage-model-01.png
   :alt: General cloud storage model
   :name: General Cloud storage model

   General cloud storage model

Storage is multifaceted. Therefore, it can be classified based on the following criteria:

- cost
- performance (IOPS, throughput, latency)
- the capacity and consumption model (platform-native, network-shared, object, or archival)
- the underlying implementation model (in-chassis, software-defined, appliance)

The objective of the model, and the set of stereotypes and perspectives, is to provide guidance to
architects and implementers in establishing storage solutions for the cloud infrastructure.

The following principles apply to the storage scope for the Reference Model, Reference
Architectures, Reference Implementations, and Reference Conformance test suites:

- Abstraction: This refers to a standardized storage abstraction layer between the virtualization
  layers and the storage physical resources layer that hides, or abstracts, the details of the
  storage physical resources from the virtualization layers.
- Agnosticism: This defines the storage subsystem concepts and models that can provide various
  storage types and performance requirements. For further information, see `Virtual Storage`_.
- Automation: This enables end-to-end automation, from physical storage installation and
  provisioning to the automation of the onboarding of the workloads (VNFs/CNFs).
- Openness: All storage is based on open-source or standardized APIs (northbound interfaces (NBIs)
  and southbound interfaces (SBIs)), and should enable the integration of storage components, such
  as software-defined storage controllers.
- Scalability: The storage model enables scalability to allow small-scale to large-scale
  deployments.
- Workload-agnostic: This storage model can provide a storage functionality to any type of
  workloads, including the following:

  - tenant VNFs
  - CNFs and infrastructure management, via bare-metal or virtualized deployments

- Operationally amenable: The storage must be amenable to a consistent set of operational processes
  for the following:

  - non-disruptive capacity expansion and contraction
  - backup and restoration
  - archive and performance management

  Where applicable (for example, backup, restoration, and archive), these processes should also be
  provided to tenants for their own delegated management.    

- Security policy-amenable: The storage subsystems must be amenable to policy-based security
  controls covering areas such as the following:

  - encryption for data at rest or in flight
  - delegated tenant security policy management
  - platform management security policy override
  - secure erase on device removal

- Future-proof: This storage model can be extended to support known and emerging technology trends,
  covering a range of memory-storage technologies, including software-defined storage with a mix of
  SATA- and NVMe-based SSDs, DRAM and persistent memory, integrated for multiclouds, and
  Edge-related technologies.

The above-mentioned principles should be understood as storage-specific specializations of the
:ref:`common/chapter00:anuket general principles`.

Storage implementation stereotypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following set of storage implementations outlines some of the most prevalent stereotypical
storage implementations.

The first of these are for datacentre storage cases, with stereotypes of the following:

- Dedicated storage appliance (:numref:`Storage Appliance Stereotype`): This provides network-based
  storage via iSCSI (2) and NFS/CIFS (3), with potentially virtual NAS (vNAS) (4) capability.
  Having virtual network software (4) allows the establishment of storage tenancies, where storage
  tenancies have their own virtual storage services which are exposed on their own network.
- Software-defined storage (:numref:`Software Defined Storage Stereotype`): This can provide
  capabilities similar to the dedicated storage appliance (see (3),(4), and (5) in the diagram). In
  this case, this is provided as a software solution on top of a hyper-converged infrastructure.

.. figure:: ../figures/rm-chap3.6-general-cloud-storage-appliance-sterotype-01.png
   :alt: Storage appliance stereotype
   :name: Storage appliance stereotype

   Storage appliance stereotype

.. figure:: ../figures/rm-chap3.6-general-cloud-storage-software-defined-sterotype-01.png
   :alt: Software-defined storage stereotype
   :name: Software-defined storage stereotype

   Software-defined storage stereotype

Both of these stereotypes can be used to support a wide range of storage needs. These needs include
the following:

- Machine boot (via iSCSI).
- Provision of storage to the cloud platform control and management planes.
- Platform-native (that is, hypervisor attached and container persistence storage, as defined in
  :ref:`chapters/chapter03:storage for tenant consumption`").
- Application/VNF/CNF-managed network storage.

To meet these needs requires connectivity within the cloud infrastructure underlay and tenant
overlay networks.

Successful management of the cloud infrastructure requires high levels of automation, including the
ability to rapidly set up new storage and hosting infrastructure. This cloud infrastructure
bootstrapping process is managed through infrastructure automation tooling. A typical part of the
bootstrap process is the use of PXE boot to manage the deployment of initial images to physical
hosts. A similar approach is used for Bare Metal-as-a-Service provisioning. The storage stereotype
that covers this use case is infrastructure automation
(:numref:`Infrastructure Automation - PXE Boot Server Stereotype`). In this storage stereotype, the
PXE boot server provides a cache of boot images that are stored in local storage (2). These images
are conditionally served up as PXE boot images (3). The PXE boot server can run within bootstrap
management hosting in a data centre or within the routing/switch layer for an edge deployment case
aimed at minimizing the physical footprint. The infrastructure automation PXE server is aware of
the provisioning status of the physical infrastructure and will serve specific images or even not
respond to PXE boot requests for hosts which have already been provisioned and are considered to be
in service.

.. figure:: ../figures/rm-chap3.6-general-cloud-storage-infrastructure-automation-pxe-server-sterotype-01.png
   :alt: Infrastructure automation - PXE boot server stereotype
   :name: Infrastructure automation - PXE boot server stereotype

   Infrastructure automation - PXE boot server stereotype

To provide the PXE boot service to the underlying resource hosts, the PXE server must be connected
to the same network as the NIC that is configured for the PXE boot. The infrastructure automation -
PXE server stereotype is also applicable to booting tenant virtual machines. In this case, the PXE
server is on the same network as one of the machines' vNICs. For tenant use, this is provided as
part of the tenant-consumable boot infrastructure services.

For each of the defined stereotypes, the storage service uses physical block storage for boot (see
Physical Layer - Block Consumption -> OS File Systems Exposure (1) in the stereotype diagrams).
This is the primary use case for use in the chassis physical storage that is not being used for
consumption and exposure as network-based storage. In general, it is desirable to use a
network-based storage solution for the provision of cloud infrastructure storage. The
infrastructure automation - PXE server is an exception to the preferential use of network-based
storage. As it is managing the bootstrap process, it cannot be dependent on a separate storage
system for maintaining its image cache.

Storage for tenant consumption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Storage is made available for tenant consumption through a number of models. A simplified view of
this is provided in the following illustrative model.

.. figure:: ../figures/rm-ch3.6-storage-model-02.png
   :alt: Storage model: cost versus performance with consumption model overlay

   Storage model: cost versus performance with consumption model overlay

Details of the terms used in figure 3.18 are as follows:

- (Comparative) Cost: this is the monetary value or unit of the end-user storage capacity.
- Performance: this is defined by IOPS/latency/throughput, as typically each of them increases with
  successive generations of storage.
- Capacity: consumption needs are represented by the width of the ultra-high performance,
  enterprise-transactional, value, and capacity storage options that you can see in figure 3.18.
- Storage types: the storage is accessed and used according to different storage types. There are
  four storage types:

  - Platform Native: this storage type is managed by the hypervisor/platform (examples include a
    virtual disk volume from which a VNF boots, and can write back to, the storage interface that is
    exposed by the container runtime). This storage type is typically not shared across running
    VNF/CNF instances.
  - Shared File Storage: this storage type is accessed through a file systems interface (for
    example, network-based storage, such as CIFS or NFS), where the storage volumes can be accessed
    and shared by multiple VNF/CNF instances.
  - Object Storage: this storage type is accessed via API interfaces (the most common example being
    the HTTP RESTful services API), which support the GET/PUT functions of structured objects.
  - Archival: this storage type is targeted for the provision of long-term storage for the purpose
    of disaster recovery, meeting legal requirements, or other historical recordings, where the
    storage mechanism may go through multiple stages before finally landing at rest.

The storage models provide a relatively simple way for the storage consumer to specify their
storage needs. This is shown in the following table, which highlights the key attributes and
features of the storage classes and epic use cases for common usage patterns.

+-----------+-----------------------+-----------------------+---------+-----------------------+------------------------+
| Storage   | Consumption model     | Performance and       | Cost    | Infrastructure        | Use case               |
| type      |                       | capacity              |         | strategy              |                        |
+===========+=======================+=======================+=========+=======================+========================+
| Platform- | Managed by the VIM/   | Ultra-high            | High to | - Always part of the  | Boot/start VNF/CNF.    |
| native    | hypervisor and        | performance and very  | very    |   VIM deployment.     | Live migration of the  |
|           | attached as part of   | high performance,     | high    | - Storage is directly | workload within and    |
|           | the VNF/CNF start-up  | Capacity: 10 GB -     |         |   next to the vCPU.   | across VIMs.           |
|           | via the VNF           | 5 TB, Tier 1          |         | - Able to support the |                        |
|           | descriptor.           |                       |         |   highest performance |                        |
|           | Shareability of       |                       |         |   use cases.          |                        |
|           | volumes across VNF/   |                       |         | - Always available to |                        |
|           | CNF instances is      |                       |         |   support VNF/CNF     |                        |
|           | determined by         |                       |         |   boot/startup.       |                        |
|           | platform and storage  |                       |         |                       |                        |
|           | capabilities.         |                       |         |                       |                        |                                                                                                                                               
+-----------+-----------------------+-----------------------+---------+-----------------------+------------------------+
| Shared    | - Access via the      | Enterprise            | High -  | - Leverage existing   | The VNFs and CNFs      |
| file      |   network file        | transactional         | mid     |   capabilities.       | are able to share the  |
| storage   |   system.             | performance (real-    |         | - Only build if       | same file content.     |
|           | - Concurrent          | time transaction      |         |   necessary (this is  |                        |
|           |   consumption across  | processing).          |         |   not required by     |                        |
|           |   multiple VNFs/CNFs. | Capacity: 5 GB -      |         |   many data plane     |                        |
|           | - Sharing can be      | 100 TB, selectable    |         |   VNFs/CNFs).         |                        |
|           |   constrained to      | Tier 1 to Tier 3.     |         | - If required for     |                        |
|           |   tenancy and cross   |                       |         |   Edge deployment,    |                        |
|           |   tenancy, and is     |                       |         |   then aim to unify   |                        |
|           |   externally          |                       |         |   with a platform-    |                        |
|           |   accessible.         |                       |         |   native deployment.  |                        |
+-----------+-----------------------+-----------------------+---------+-----------------------+------------------------+
| Object    | Consumed via the      | - Highly              | High to | Primarily the         | Cloud-native           |
| storage   | HTTP/S RESTful        |   distributable       | mid     | responsibility of     | geo-distributed        |
|           | services.             |   and scalable.       |         | the tenant            | VNFs/CNFs.             |
|           |                       | - Provided by the     |         | application.          |                        |
|           |                       |   serving application |         |                       |                        |
|           |                       |   which manages the   |         |                       |                        |
|           |                       |   storage needs.      |         |                       |                        |
|           |                       | - Location-           |         |                       |                        |
|           |                       |   independent.        |         |                       |                        |
+-----------+-----------------------+-----------------------+---------+-----------------------+------------------------+
| Capacity  | Typically accessed    | Very low              | Low     | Use the cheapest      | Archival storage for   |
|           | according to Shared   | transactional         |         | storage available     | tenant/platform        |
|           | Storage, but will     | performance.          |         | that meets the        | backup/restore, and    |
|           | likely have           | Throughput is         |         | capacity and security | disaster recovery      |
|           | additional storage    | needed to accommodate |         | needs.                | (DR).                  |
|           | stages. Not suitable  | the large data flow.  |         |                       |                        |
|           | for real-time         | Tier 5.               |         |                       |                        |
|           | processing.           |                       |         |                       |                        |
+-----------+-----------------------+-----------------------+---------+-----------------------+------------------------+

**Table 3-8:** Tenant storage types

In :ref:`Storage implementation stereotypes`, the general cloud storage model is used to
illustrate the provision of storage. The model can also be used to illustrate the consumption of
storage for use by the tenants. See below for the platform-native stereotypes:

- Platform-Native: Hypervisor-Attached Consumption Stereotype
  (:numref:`Platform Native: Hypervisor Attached Consumption Stereotype`): where the hypervisor
  consumes the software-defined storage via the network (RA-1 - Cinder backend (2)) and the block
  image is attached to the virtual machine (the RAW or QCOW file within the file system), which is
  used for boot and exposure to the virtual machine operating system (OS) as block storage (3). The
  virtual machine operating system, in turn, consumes this for use by the tenant application via
  the file system.
- Platform-Native: Container-Persistent Consumption Stereotype
  (:numref:`Platform Native: Container Persistent Consumption Stereotype`): this is a simpler case
  with container runtime consuming software-defined storage (via the reliable autonomic distributed
  object store (RADOS) backend (2)), and exposes this to the container as a file system mount (3).

.. figure:: ../figures/rm-chap3.6-general-cloud-storage-hypervisor-attached-stereotype-01.png
   :alt: Platform-Native: Hypervisor-Attached Consumption Stereotype
   :name: Platform-Native: Hypervisor-Attached Consumption Stereotype

   Platform-Native: Hypervisor-Attached Consumption Stereotype

.. figure:: ../figures/rm-chap3.6-general-cloud-storage-container-persistent-stereotype-01.png
   :alt: Platform-Native: Container-Persistent Consumption Stereotype
   :name: Platform-Native: Container-Persistent Consumption Stereotype

   Platform-Native: Container-Persistent Consumption Stereotype

..note::
  
  A stereotype for network file storage consumption is not illustrated, as this is managed by the
  tenant application, by performing a file systems mount.

In the cloud infrastructure, the storage types may manifest in various ways with substantive
variations in the architecture models being used. Examples of this are provided in
`Storage Implementation Stereotypes`_, with stereotypes for dedicated storage appliance and
software-defined storage. In the consumption case, again, in-chassis storage is used to support the
hypervisor and container host operating system/runtime boot, and is not used for tenant/user plane
storage consumption.

Storage scenarios and architecture fit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The storage model and stereotypical usage scenarios illustrate the key storage uses cases and how
they apply to the support of storage requirements from across a range of cloud deployments. This
set of storage uses cases is summarized in the following tables, including how the stereotypes can
support the Anuket Reference Architectures, followed by the key areas for consideration in such a
deployment scenario. The structure of the table is as follows:

- Use Case: the target storage use case that is being covered (large datacentre, small datacentre,
  standalone cloud, Edge, and so on).
- Stereotype: which of the defined stereotypes is used.
- Infra/Ctrl/Mgmt: the ability of the storage stereotype to support the following:

  - Infrastructure: for host computer boot (from either the local host storage or the PXE).
  - Control plane: for cloud infrastructure control (such as the OpenStack (RA1) or the Kubernetes
    (RA2) control functions).
  - Management plane needs: for infrastructure automation, tenant VNF/CNF orchestration, and cloud
    infrastructure monitoring and assurance.
- Tenant/user: the ability of the storage stereotype to support the tenant/user plane needs,
  including the following:

  - Platform-Native
  - shared file storage
  - object storage (in accordance with `Storage for Tenant Consumption`_)

Where:

- Y: yes, almost always provided.
- O: optional, readily accommodated.
- N: no, not available.
- NA: not applicable for this use case or stereotype.

+-------------------------------+-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
|                                                                                          | Tenant/user                                                    |
+===============================+=====================================+======+======+======+============+============+========+=======+=====+======+========+
|                                                                     | Infra/Ctrl/Mgmt    | Platform-native         | Shared file                 | Object |
+-------------------------------+-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
| Use case                      | Stereotype                          | Boot | Ctrl | Mgt  | Hypervisor-| Container- | Within | Cross | Ext | vNAS | Object |
|                               |                                     |      |      |      | attached   | persistent |        |       |     |      |        |
+-------------------------------+-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
| Datacentre storage            | Dedicated network storage appliance | Y    | Y    | Y    | Y          | Y          | O      | O     | O   | O    | O      |
|                               +-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
|                               | Dedicated software-defined storage  | O    | O    | O    | Y          | Y          | O      | O     | O   | O    | O      |
|                               +-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
|                               | Traditional SAN                     | Y    | Y    | Y    | N          | N          | N      | N     | N   | N    | N      |
+-------------------------------+-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
| Satellite datacentre storage  | Small software-defined storage      | O    | O    | O    | Y          | Y          | O      | O     | O   | O    | O      |
+-------------------------------+-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
| Small datacentre storage      | Converged software-defined storage  | O    | O    | O    | Y          | Y          | O      | O     | O   | O    | O      |
+-------------------------------+-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
| Edge cloud                    | Edge cloud for VNF/CNF storage      | NA   | O    | NA   | Y          | Y          | O      | O     | O   | O    | O      |
|                               +-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
|                               | Edge cloud for apps storage         | NA   | O    | NA   | Y          | Y          | O      | O     | O   | O    | Y      |
|                               +-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
|                               | Edge cloud for content management   | NA   | O    | NA   | Y          | Y          | O      | O     | O   | O    | Y      |
|                               | storage                             |      |      |      |            |            |        |       |     |      |        |
+-------------------------------+-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
| Split control plane/user      | Split Edge control plane storage    | NA   | N    | NA   | Y          | Y          | O      | O     | O   | O    | O      |
| plane                         +-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+
| Edge cloud                    | Split Edge user plane storage       | NA   | N    | NA   | N          | N          | N      | N     | N   | N    | N      |
+-------------------------------+-------------------------------------+------+------+------+------------+------------+--------+-------+-----+------+--------+

**Table 3-9:** Storage use cases and stereotypes

The storage subsystem is a foundational part of any cloud infrastructure. As such, it is important
to identify the storage needs, based on target tenant use cases, at inception. This allows the
right set of considerations to be addressed for the deployment. A set of typical considerations is
provided for the following purposes:

- For various use cases to meet the functional and performance needs.
- To avoid the need for significant reworking of the storage solution and the likely ripple-through
  impact on the broader cloud infrastructure.

These considerations will help to guide the build and deployment of the storage solution for the
various use cases and stereotypes outlined in the summary table.

+----+----+----+----------+-----------------------------------------------------------+
| Use case                | Description                                               |
+====+====+====+==========+===========================================================+
| **Datacentre**          | This provides a reliable and scalable storage capability  |
| **Storage**             | that has flexibility to meet diverse needs.               |
+----+----+----+----------+-----------------------------------------------------------+
|    | Meets the needs    | The cloud infrastructure control plane (tenant virtual    |
|    | of:                | machine and container lifecycle management and control).  |
|    |                    +-----------------------------------------------------------+
|    |                    | The cloud infrastructure management plane (cloud          |
|    |                    | infrastructure fault and performance management, and      |
|    |                    | platform automation).                                     |
|    |                    +-----------------------------------------------------------+
|    |                    | The cloud infrastructure tenant/user plane.               |
+----+----+----+----------+-----------------------------------------------------------+
|    | General considerations: What are the general considerations, irrespective of   |
|    | the deployment stereotype/technology used in the storage subsystem?            |
+----+----+----+----------+-----------------------------------------------------------+
|    | 1  | Can storage support virtual machine (RA-1) and container (RA-2) hosting   |
|    |    | cases from single instance? Bearring in mind that, if you wish to have a  |
|    |    | single storage instance providing storage across multiple clusters and/or |
|    |    | availability zones within the same datacentre, then this needs to be      |
|    |    | factored into the underlay network design.                                |
+----+----+----+----------+-----------------------------------------------------------+
|    | 2  | Can the storage system support live migration/multi-attach within and     |
|    |    | across the availability zones (applicable to virtual machine hosting      |
|    |    | (RA-1))? How does the cloud infrastructure solution support the migration |
|    |    | of virtual machines between the availability zones in general?            |
+----+----+----+----------+-----------------------------------------------------------+
|    | 3  | Can the storage system support the full range of shared-file storage use  |
|    |    | cases? This would include the ability to control how network-exposed      |
|    |    | shared-file storage is visible: within tenancy, across tenancy (bearing   |
|    |    | in mind that a tenancy can operate across availability zones) and         |
|    |    | externally.                                                               |
+----+----+----+----------+-----------------------------------------------------------+
|    | 4  | Can the storage system support alternate performance tiers to allow       |
|    |    | tenant selection of best cost/performance options? For high-performance   |
|    |    | storage provision, meeting throughput and IOP needs can be achieved by    |
|    |    | using the following:                                                      |
|    |    |                                                                           |
|    |    | - very high IOP flash storage                                             |
|    |    | - higher bandwidth networking                                             |
|    |    | - performance-optimized replication design                                |
|    |    | - storage pool host distribution                                          |
+----+----+----+----------+-----------------------------------------------------------+
|    | Specific considerations: in selecting a particular stereotype/technology, this |
|    | can bring with it considerations that are specific to this choice.             |
+----+----+----+----------+-----------------------------------------------------------+
|    | Dedicated software-defined storage                                             |
+----+----+----+----------+-----------------------------------------------------------+
|         | 1  | It is necessary to establish the physical disk data layout/encoding  |
|         |    | scheme choice. The options could be either of the following:         |
|         |    |                                                                      |
|         |    |  - replication/mirroring of data across multiple storage hosts       |
|         |    |  - CRC-based redundancy management encoding (such as erasure         |
|         |    |    encoding)                                                         |
|         |    |                                                                      |
|         |    | This typically has performance/cost implications, as replication has |
|         |    | a lower performance impact but consumes a larger number of physical  |
|         |    | disks. If you use replication, then increasing the number of         |
|         |    | replicas provides greater data loss prevention, but consumes more    |
|         |    | disk system backend network bandwidth, with bandwidth needs          |
|         |    | proportional to the number of replicas.                              | 
|         +----+----------+-----------------------------------------------------------+
|         | 2  | In general, with the software-defined storage solution, it is not    |
|         |    | advisable to use hardware RAID controllers. This is because they     |
|         |    | impact the scope of recovery on failure, since the failed device     |
|         |    | replacement can only be managed within the RAID volume of which the  |
|         |    | disk is a part. With software-defined storage, failure recovery can  |
|         |    | be managed within the host in which the disk failed, but also across |
|         |    | the physical storage hosts.                                          |
|         +----+----------+-----------------------------------------------------------+
|         | 3  | Can storage be consumed optimally, irrespective of whether this is   |
|         |    | on the control, management, or tenant/user plane? An example of this |
|         |    | is iSCSI/NFS, which, while it is available and provides a common     |
|         |    | technical capability, does not provide best achievable performance.  |
|         |    | The best performance is achieved using a provided OS layer driver    |
|         |    | that matches the particular software-defined storage implementation  |
|         |    | (for example, using a RADOS driver in the Ceph case versus the Ceph  |
|         |    | ability to expose iSCSI).                                            |
+----+----+----+----------+-----------------------------------------------------------+
|    | Dedicated network storage appliance                                            |
+----+----+----+----------+-----------------------------------------------------------+
|         | 1  | Macro choices are made according to vendor/model selection and the   |
|         |    | available configuration choices.                                     |
+----+----+----+----------+-----------------------------------------------------------+
|    | Traditional SAN                                                                |
+----+----+----+----------+-----------------------------------------------------------+
|         | 1  | This is generally made available via Fibre Channel Arbitrated Loop   |
|         |    | (FC-AL)/SCSI connectivity. It therefore requires specific            |
|         |    | connectivity. To provide the features required for the cloud         |
|         |    | infrastructure (shared-file storage, object storage, and             |
|         |    | Multi-tenancy support), SAN storage systems need to be augmented     |
|         |    | with other gateways to provide an IP network-consumable capability.  |
|         |    | This is often seen with current deployments where the NFS/CIFS (NAS) |
|         |    | gateway is connected by the FC-AL (for storage backend) and the IP   |
|         |    | network for cloud infrastructure consumption (frontend). This model  |
|         |    | helps to extend the use of SAN storage investment.                   |
|         |    |                                                                      |
|         |    | **Note:** This applies to SANs which use SAS/SATA physical disk      |
|         |    | devices, as direct-connect FC-AL disk devices are no longer          |
|         |    | manufactured.                                                        |
+----+----+----+----------+-----------------------------------------------------------+
| **Satellite**           | Satellite datacentres are smaller regional deployments    |
| **Datacentre storage**  | which have connectivity to and use resources available    |
|                         | from the main datacentre. Therefore, they only provide    |
|                         | support for a subset of requirements.                     |
+----+----+----+----------+-----------------------------------------------------------+
|    | Meets the needs    | The cloud infrastructure control plane (tenant virtual    |
|    | of                 | machine, and container lifecycle management and control). |
|    |                    +-----------------------------------------------------------+
|    |                    | The cloud infrastructure tenant/user plane.               |
|    +----+----+----------+-----------------------------------------------------------+
|    | General considerations: What are the general considerations, irrespective      |
|    | of the deployment stereotype/technology used in the storage subsystem?         |
|    +----+----+----------+-----------------------------------------------------------+
|    | 1  | Is there a need to support multiple clusters/availability zones at the    |
|    |    | same site? If so, then use the Datacentre Storage use case. Otherwise,    |
|    |    | consider how to put the virtual machine and container hosting control     |
|    |    | plane, and the storage control plane on the same set of hosts, to reduce  |
|    |    | the footprint.                                                            |
|    +----+----+----------+-----------------------------------------------------------+
|    | 2  | Can the establishment of shared file storage be avoided by using          |
|    |    | the capabilities provided by large datacentre storage?                    |
|    +----+----+----------+-----------------------------------------------------------+
|    | 3  | Can very large capacity storage needs be moved to larger datacentre       |
|    |    | storage capabilities?                                                     |
|    +----+----+----------+-----------------------------------------------------------+
|    | Specific considerations: In selecting a particular stereotype or technology,   |
|    | this can bring with it considerations that are specific to this choice.        |
+----+----+----+----------+-----------------------------------------------------------+
|    | Small software-defined storage                                                 |
+----+----+----+----------+-----------------------------------------------------------+
|         | 1  | Leverage the same technology as the Dedicated Software-Defined       |
|         |    | Storage scenarios, but avoid, or limit, infrastructure boot and      |
|         |    | management plane support, and network storage support.               |
|         +----+----------+-----------------------------------------------------------+
|         | 2  | Avoid having dedicated storage instances per cluster/availability    |
|         |    | zone.                                                                |
|         +----+----------+-----------------------------------------------------------+
|         | 3  | Resilience through rapid rebuild (N+1 failure scenario).             |
+----+----+----+----------+-----------------------------------------------------------+
| **Small datacentre**    | Small datacentre storage deployment is used in cases      |
| **storage**             | where software-defined storage and virtual machine/       |
|                         | container hosting are running on a converged              |
|                         | infrastructure footprint, with the aim of reducing the    |
|                         | overall size of the platform. This solution behaves as a  |
|                         | standalone cloud infrastructure platform.                 |
+----+----+----+----------+-----------------------------------------------------------+
|    | Meets the needs    | The cloud infrastructure control plane (tenant virtual    |
|    | of                 | machine and container lifecycle management and control).  |
|    |                    +-----------------------------------------------------------+
|    |                    | The cloud infrastructure management plane (cloud          |
|    |                    | infrastructure fault and performance management, and      |
|    |                    | platform automation).                                     |
|    |                    +-----------------------------------------------------------+
|    |                    | The cloud infrastructure tenant/user plane.               |
|    +----+----+----------+-----------------------------------------------------------+
|    | General considerations: What are the general considerations, irrespective of   |
|    | the deployment stereotype/technology used in the storage subsystem?            |
|    +----+----+----------+-----------------------------------------------------------+
|    | 1  | Is there a need to support multiple clusters/availability zones at the    |
|    |    | same site? See the guidance for the Satellite Datacentre Storage use      |
|    |    | case (1).                                                                 |
|    +----+----+----------+-----------------------------------------------------------+
|    | 2  | Is shared file storage required? Check the sharing scope carefully, as    |
|    |    | the fully virtualized NF solution adds complexity and increases the       |
|    |    | resource needs.                                                           |
|    +----+----+----------+-----------------------------------------------------------+
|    | 3  | Is there a need for large local capacity? With the large-capacity flash   |
|    |    | (15-30 TB per device), the solution can hold significant storage          |
|    |    | capacity. However, it is important to consider carefully the data loss    |
|    |    | prevention needs and the impact on rebuild/recovery times.                |
|    +----+----+----------+-----------------------------------------------------------+
|    | Specific considerations: In selecting a particular stereotype or technology,   |
|    | this can bring with it considerations that are specific to this choice.        |
+----+----+----+----------+-----------------------------------------------------------+
|    | Converged software-defined storage                                             |
+----+----+----+----------+-----------------------------------------------------------+
|         | 1  | Leverage the same technology as in the Dedicated Software-Defined    |
|         |    | Storage scenarios, but on converged infrastructure. To meet the      |
|         |    | capacity needs, provision three hosts for storage and the rest for   |
|         |    | virtual infrastructure and storage control, and management and       |
|         |    | tenant workload hosting.                                             |
|         +----+----------+-----------------------------------------------------------+
|         | 2  | If the solution needs to host two clusters/availability zones, then  |
|         |    | have shareable storage instances.                                    |
|         +----+----------+-----------------------------------------------------------+
|         | 3  | Resilience through rapid rebuild (N+0 or N+1).                       |
+----+----+----+----------+-----------------------------------------------------------+
| **Edge cloud for app**  | This supports the deployment of applications at the edge, |
| **storage**             | which tend to have greater storage needs than a network   |
|                         | VNF/CNF.                                                  |
+----+----+----+----------+-----------------------------------------------------------+
|    | Meets the needs    | The cloud infrastructure control plane (tenant virtual    |
|    | of                 | machine, and container lifecycle management and control). |
|    |                    +-----------------------------------------------------------+
|    |                    | The cloud infrastructure tenant/user plane: limited       |
|    |                    | configuration storage.                                    |
+----+----+----+----------+-----------------------------------------------------------+
| **Edge cloud for**      | This supports the deployment of VNFs/CNFs at the edge.    |
| **VNF/CNF storage**     |                                                           |
+----+----+----+----------+-----------------------------------------------------------+
|    | Meets the needs    | The cloud infrastructure control plane (tenant virtual    |
|    | of                 | machine, and container lifecycle management and control). |
|    |                    +-----------------------------------------------------------+
|    |                    | The cloud infrastructure tenant/user plane: limited       |
|    |                    | configuration storage.                                    |
+----+----+----+----------+-----------------------------------------------------------+
| **Edge cloud for**      | This supports the deployment of media content caches at   |
| **content storage**     | the edge. This is a common content distribution network   |
|                         | (CDN) use case.                                           |
+----+----+----+----------+-----------------------------------------------------------+
|    | Meets the needs    | The cloud infrastructure control plane (tenant virtual    |
|    | of                 | machine, and container lifecycle management and control). |
|    |                    +-----------------------------------------------------------+
|    |                    | The cloud infrastructure tenant/user plane: media content |
|    |                    | storage.                                                  |
|    +----+----+----------+-----------------------------------------------------------+
|    | General considerations: What are the general considerations, irrespective of   |
|    | the deployment stereotype/technology used in the storage subsystem?            |
|    +----+----+----------+-----------------------------------------------------------+
|    | 1  | Consuming and exposing object storage through the tenant application.     |
|    +----+----+----------+-----------------------------------------------------------+
|    | 2  | Using embedded shared file storage for control and tenant storage needs.  |
|    +----+----+----------+-----------------------------------------------------------+
|    | Specific considerations: In selecting a particular stereotype/technology, this |
|    | can bring with it considerations that are specific to this choice.             |
|    +----+----+----------+-----------------------------------------------------------+
|    | Embedded shared file storage                                                   |
+----+----+----+----------+-----------------------------------------------------------+
|         | 1  | What is the best way to achieve some level of data resilience, while |
|         |    | minimizing the required infrastructure (for example, in situations   |
|         |    | in which you do not have the luxury of having host VMs dedicated to  |
|         |    | supporting the storage control and storage data needs)?              |
+----+----+----+----------+-----------------------------------------------------------+

The General Storage Model illustrates that at the bottom of any storage solution there is always
the physical storage layer and a storage operating system of some sort. In the cloud infrastructure
environment, what is generally consumed is some form of network storage which can be provided by
the following:

- The infrastructure platform underlay network for the control plane and platform native -
  hypervisor attached and container runtime managed.
- Tenant/user overlay network for shared file storage and object storage.

In general, for the provision of storage as a shared resource, it is not desirable to use
in-chassis storage for anything other than in the storage devices for the platform hypervisor/OS
boot or for the hosts providing the storage subsystems deployment itself. This is due to
difficulties in the resulting operational management (see the principles section
`Introduction to Storage`_ - "Operationally Amenable").

For cloud-based storage, ephemeral storage (hypervisor-attached or container images which are
disposed of when the VNF/CNF is stopped) is often distinguished from other persistent storage.
However, this is a behaviour variation that is managed via the VNF descriptor, rather than a
specific storage type.

Storage also follows the alignment of separated virtual and physical resources of the virtual
infrastructure layer and the hardware infrastructure layer. The reasons for such an alignment are
described in more detail in `Network`_.

While new storage technologies are being made available and there is a trend towards the use of
flash for all physical storage needs, the core storage architecture for the cloud infrastructure is
likely, for the near future, to remain consistent with the network-based consumption model, as
described through the stereotypes.


Sample reference model realization
----------------------------------

The following diagram shows an example of the realization of the reference model, in which a
virtual infrastructure layer contains three coexisting but different types of implementation:

- A typical IaaS using VMs and a hypervisor for virtualization.
- A CaaS on a VM/hypervisor.
- A CaaS on bare metal.

This diagram is presented for illustration purposes only. It does not preclude the validity of
other different combinations of implementation types. The model enables several potentially
different controllers orchestrating different types of resources (virtual or hardware, or both).
Management clients can manage virtual resources via the virtual infrastructure manager (container
infrastructure service manager for CaaS, or virtual infrastructure manager for IaaS) or,
alternatively, hardware infrastructure resources via the hardware infrastructure manager. The
latter situation may occur, for example, when an orchestrator (an example of a management client)
is involved in provisioning the physical network resources with the assistance of the controllers.
This realization example also enables the implementation of a programmable fabric.


.. figure:: ../figures/ch03-model-realization-diagram-2.png
   :alt: Reference model realization example
   :name: reference model realization example

   Reference model realization example

The terms container infrastructure service instance and container infrastructure service manager
should be understood as defined in ETSI GR NFV-IFA 029 V3.3.1 :cite:p:`etsigrnfvifa029`. More
detailed deployment examples can be found in `network`_ of this Reference Model chapter.

Hardware acceleration abstraction
---------------------------------

The purpose of a hardware accelerator is either to accelerate the execution of an application or to
offload functions from the generic CPU, to make the application and/or cloud infrastructure more
efficient from one or more aspects.

Hardware accelerators are often used in Telco clouds for a number of reasons. Some applications
require a hardware accelerator to perform tasks that a generic CPU cannot perform with sufficient
speed or timing accuracy, or handle the traffic that must be kept in a single context. Other
applications may be properly served with a generic CPU in some deployment cases, while being
inefficient in other situations. The cloud infrastructure might also benefit from specialized
accelerated hardware devices to perform its tasks with less power, space, or cost than a generic
CPU.

The accelerators are specialized resources and are generally not expected to exist in large
quantities. Therefore, it is important that these limited hardware accelerators are carefully
assigned to areas where they can be used most efficiently for most of the time. In general, this
requires there to be software-based alternative functions that can be used for occasions when
hardware accelerators cannot be assigned to accelerate or offload applications or cloud
infrastructure tasks.

The preferred scenario is one in which the accelerated or offloaded functions have abstracted
interfaces, since that would hide the different implementations from a functional point of view and
make orchestrator choices simpler and more transparent to deploy. It would also allow support for
multiple different hardware accelerators, as well as the reduction of the operator’s integration
and test efforts of the accelerators and their applications, and/or the cloud infrastructure.

Types of accelerators
~~~~~~~~~~~~~~~~~~~~~

Accelerator technologies can be categorized depending on where they are realized in the hardware
product and how they are activated, how their lifecycles are managed, and how they are supported in
running the infrastructure.

+-----------------------------+-----------------------------+----------------------------+-----------------------------+
| Acceleration                | Example implementation      | Activation/LCM/support     | Usage by application tenant |
| technology/hardware         |                             |                            |                             |
+=============================+=============================+============================+=============================+
| CPU instructions            | Within the CPU cores.       | None for hardware.         | Application for loading a   |
|                             |                             |                            | software library that       |
|                             |                             |                            | recognizes and uses CPU     |
|                             |                             |                            | instructions.               |
+-----------------------------+-----------------------------+----------------------------+-----------------------------+
| Fixed-function accelerator  | Crypto, vRAN-specific       | Rare updates.              | Application for loading a   |
|                             | adapter.                    |                            | software library or driver  |
|                             |                             |                            | that recognizes and uses    |
|                             |                             |                            | the accelerator.            |
+-----------------------------+-----------------------------+----------------------------+-----------------------------+
| Firmware-programmable       | Network/storage adapter     | Rare updates.              | The application is normally |
| adapter                     | with the programmable part  |                            | not modified or aware.      |
|                             | of the firmware image.      |                            |                             |
+-----------------------------+-----------------------------+----------------------------+-----------------------------+
| SmartNIC                    | Programmable accelerator    | Programmable by            | There are three operational |
|                             | for the vSwitch/vRouter,    | infrastructure operators   | modes:                      |
|                             | network function, or        | or application tenants, or | - Non-programmable,         |
|                             | hardware infrastructure, or | both.                      |   normally with unaware     |
|                             | all three.                  |                            |   applications.             |
|                             |                             |                            | - Programmable once for     |
|                             |                             |                            |   activation.               |
|                             |                             |                            | - Reprogrammable.           |
+-----------------------------+-----------------------------+----------------------------+-----------------------------+
| SmartSwitch-based           | Programmable switch fabric  | Programmable by            | There are three operational |
|                             | or TOR switch.              | infrastructure operators   | modes:                      |
|                             |                             | or application tenants,    | - Non-programmable,         |
|                             |                             | or both.                   |   normally with unaware     |
|                             |                             |                            |   applications.             |
|                             |                             |                            | - Programmable once for     |
|                             |                             |                            |   activation.               |
|                             |                             |                            | - Reprogrammable.           |
+-----------------------------+-----------------------------+----------------------------+-----------------------------+

**Table 3-10:** Hardware acceleration categories, implementation, and activation/LCM/support and usage

.. figure:: ../figures/ch03-examples-of-server-and-smartswitch-based-nodes.png
   :alt: Examples of server- and SmartSwitch-based nodes (for illustration only)

   Examples of server- and SmartSwitch-based nodes (for illustration only)

Infrastructure and application-level acceleration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:numref:`Hardware Acceleration in RM Realization Diagram` gives examples for the hardware
accelerators shown in :numref:`Reference model realization example`
(the :ref:`chapters/chapter03:sample reference model realization` diagram).

.. figure:: ../figures/ch03-hardware-acceleration-in-rm-realization-diagram.png
   :alt: Hardware acceleration in the Reference Model realization diagram
   :name: Hardware acceleration in the Reference Model realization diagram

   Hardware acceleration in the Reference Model realization diagram

The hardware accelerators are part of the hardware infrastructure layer. Those hardware
accelerators that need to be activated or programmed expose the management interfaces and have
accelerator management software managing them in-band, from the host operating system (OS), or
out-of-band (OOB), over a network to the adapter, without going through the host OS. For more
flexibility in management, such accelerator management can be carried over the appropriate service
with an authentication mechanism before being exposed to the cloud infrastructure operator or the
application tenant, or both.

The application uses a software library supporting the hardware acceleration and running on generic
CPU instructions. Mapping the workload to the acceleration hardware is performed with Cyborg in
OpenStack or the device plugin framework in Kubernetes. The hardware accelerator supports in-band
or out-of-band management, or both, with the service exposing it to the cloud infrastructure
operator or application tenant roles.

Hardware accelerators can have the following uses:

-  Virtualization infrastructure layer acceleration: an example of this is vSwitch, which can be
   leveraged agnostically by the VNFs, if standard host interfaces, such as VirtIO, are used.
-  Application layer acceleration: an example of this is the software library/framework (for
   example, DPDK) in the virtual machine, providing application-level acceleration with (where
   available) hardware-abstracted APIs to access platform hardware acceleration, and providing
   software-equivalent libraries when hardware assistance is not available.
-  Hardware infrastructure layer offload: an example of this is an underlay network separation
   managed out-of-band, providing network separation secured from the host OS to reach any
   provisioned transport switch infrastructure.

There are two levels of consumption for underlay separation or overlay acceleration. Underlay
separation ensures that multiple different virtualization infrastructure instances are kept in
separate underlay network access domains. Overlay acceleration offloads the virtualization
infrastructure instances to the vSwitch/vRouter, or to virtual termination endpoints, for
applications that bypass the virtual infrastructure layer.

Application or infrastructure acceleration can benefit from underlying hardware acceleration, yet
still be decoupled from it by using open multivendor APIs for hardware acceleration devices such as:

- For Linux IO virtualization: VirtIO.
- For network functions using DPDK libraries: Crypto devices, EthDev, event devices, and base band
  devices.
- For O-RAN network functions: the O-RAN acceleration abstraction layer interface.

Example of the O-RAN acceleration abstraction layer interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O-RAN Alliance’s Cloudification and Orchestration Workgroup (WG6) defines the acceleration
abstraction layer (AAL), an application-level interface, as the recommended way of decoupling
the software vendors’ network functions from the different hardware accelerator implementations.

.. figure:: ../figures/ch03-hardware-acceleration-in-rm-realization-diagram_AAL.png
   :alt: AAL interface in Reference Model realization diagram

   AAL interface in Reference Model realization diagram

The “O-RAN Acceleration Abstraction Layer General Aspects and Principles 1.0” document
:cite:p:`oranwg6aalganp` and the latest O-RAN WG6 Cloudification and Orchestration Workgroup
specifications :cite:p:`oranwg6cloudorchwg` do the following:

- Describe the functions conveyed over the AAL interface, including configuration and management
  functions.
- Identify the requirements, as well as the general procedures and operations.
- Introduce the initial set of O-DU/O-CU AAL profiles.

Workload placement
~~~~~~~~~~~~~~~~~~

Workload placement can be done by a combination of filters or selectors to find the appropriate
compute resources and subsystems to manage the assignment of scheduled workloads to the hardware
accelerator, and intelligence in the workload to detect the presence of hardware accelerators.

For initial limited cloud deployments of network functions on private clouds, it is possible to
have a workload placement orchestrator that handles optimizations of selected virtualization
clusters and available hardware resources. However, with the increasing number of acceleration
devices, hardware composability, and hybrid multicloud deployments, this will soon become too
complex.

Growing lists of individual optimizations, including hardware acceleration during scheduling, make
the mapping of the workloads to the lists of individual optimizations more complicated. Therefore,
such optimizations are grouped together into higher-level categories. An example of this is to have
a real-time and a data plane-optimized category, instead of specifying the required individual
optimizations.

With a further growth in the size of the clusters and the variety of types of hardware
acceleration, it will be necessary, in a hybrid or multicloud deployment, to enable separate
optimization levels for the workload placement and each cloud infrastructure provider. The workload
placement orchestrator will operate on one or several cloud infrastructure resources to satisfy the
workloads according to service-level agreements (SLAs) that do not specify all implementation and
resource details. Each cloud infrastructure provider will make internal infrastructure
optimizations towards their own internal optimization targets while fulfilling the SLAs.

CPU instructions
~~~~~~~~~~~~~~~~

The CPU architecture often includes instructions and execution blocks for the most common
compute-heavy algorithms, such as block cyphers (for example, AES-NI), random number generators, or
vector instructions. These functions are normally consumed in the infrastructure software or
applications by using enabled software libraries that run faster when custom CPU instructions for
the execution of such functions are available in the hardware, and slower when these instructions
are not available in the hardware, as only the general CPU instructions are used. Custom CPU
instructions do not need to be activated or have their lifecycles managed. When scheduling the
workloads, compute nodes with such custom CPU instructions can be found by applications or by an
orchestrator using OpenStack Nova filters or Kubernetes Node Feature Discovery labels, or directly
from the hardware management layer.

Fixed-function accelerators
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fixed-function accelerators are either of the following:

- Adapters with in-line functionality (typically, PCIe adapters with Ethernet ports or storage
  drives).
- Adapters with look-aside functionality (typically, PCIe adapters without any external ports).

Each adapter has an additional chip on the motherboard. This chip is included in the server
chipsets, or packaged or embedded in the main CPU. Fixed-function accelerators can accelerate
cryptographic functions, and other algorithms in parallel. Initial activation and rare lifecycle
management events (such as updating firmware images) can typically be done from the host OS (such
as the OS driver or a library), the hardware infrastructure manager (from a library), or the
network function (mostly through a library).

Beyond finding such compute nodes while scheduling the workloads, the workloads also need to be
mapped to the accelerator, both of which can be done with the device plugin framework in Kubernetes.
Once mapped to the application, the application can use enabled software libraries or device
drivers, or both, that will use hardware acceleration. If hardware acceleration is used to improve
cost and performance, then the application can also run on generic compute nodes without the
hardware accelerator, when the application uses the same software library to run on generic CPU
instructions.

Firmware-programmable adapters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Firmware-programmable network adapters with programmable pipelines are types of network adapters
where the usual Ethernet controller functionality (accelerating common network overlays, checksums,
or protocol termination) can be extended with partially programmable modules, so that additional
protocols can be recognized, parsed, and put into specific queues. This helps to increase
performance and reduce load on the main CPU.

Firmware-programmable storage adapters can offload some of the storage functionality and include
storage drive emulation to enable partial drive assignments up to the accessing host OS. These
adapters can, over time, include more supported storage offload functions or support more drive
emulation functions.

Before being used, such adapters have to be activated by loading a programmable module that
typically accelerates the virtualization infrastructure. Doing this in multivendor environments can
lead to complications because the adapter hardware is typically specified, installed, and supported
by the server vendor while the programmable image on the adapter is managed by the SDN, the storage
controller, or the software infrastructure vendor.

SmartNICs
~~~~~~~~~

Programmable SmartNIC accelerators are either of the following:

- Programmable in-line adapters (typically, PCIe adapters with Ethernet ports).
- Network-connected pooled accelerators, such as forms of GPU or FPGA where the normal CPU PCIe
  connection is extended with an Ethernet hop.

There are two main types of SmartNIC that can accelerate network functions in-line between the CPUs 
and the Ethernet ports of the servers. The simpler types have a configurable or programmable packet
pipeline that can implement offload for the infrastructure virtual switching or part of an
application functions data plane. The more advanced type, often called a data processing unit (DPU),
has a programmable pipeline and a number of strong CPU cores that can simultaneously implement
underlay networking separation and trusted forwarding functions, infrastructure virtual switching
data and control plane, as well as part of an application functions control plane.

.. figure:: ../figures/ch03-example-smartnic-deployment-model.png
   :alt: Example SmartNIC deployment model that accelerates two workloads and has OOB management

   Example SmartNIC deployment model that accelerates two workloads and has OOB management

Simple SmartNIC
^^^^^^^^^^^^^^^

The preferred usage of a simple SmartNIC is for the virtualization infrastructure usage that
typically implements the data (forwarding) plane of the virtual switch or router. These deployments
can offer a standardized higher level abstract interface towards the application tenants, such as
VirtIO, that supports good portability and is therefore the preferred usage method.

The direct usage of simple SmartNICs by the application tenant (VNF or CNF), where the application
tenant acts as a dedicated accelerator appliance, requires the application tenant to manage the
loading and the function that is loaded into the SmartNIC. Such a deployment is similar to the NIC
PCI Pass-Through in that it bypasses the virtualization infrastructure layer’s virtual switching,
which requires all network encapsulation, mapping, and separation to be done by the underlay
network, often by manual provisioning. Therefore, it is not a preferred usage method.

Data processing unit
^^^^^^^^^^^^^^^^^^^^

The data processing unit (DPU) can accelerate software infrastructure functions (vSwitch/vRouter)
from the main CPU and simultaneously offer networking services, such as load balancers, firewalls,
and application tenant offload functions. Through out-of-band management, the DPU can also ensure
underlay separation and map a selected part of the underlay network to the specific virtualization
infrastructure instance that the server on which it is mounted requires, allowing the selected parts
to be used on any statically provisioned underlay network.

The forwarding path (data plane) needs to be installed and controlled by the hardware infrastructure
manager through an isolated out-of-band management channel, into the DPU control and operating
system, out of reach for the main CPU host software. All the content in the forwarding path must
come from the trusted code of the hardware infrastructure operator, since any fault or malicious
content can seriously disturb the entire network for all the connected devices.

The trusted forwarding functions must be handled through a hardware infrastructure management
repository and must have APIs for their respective control functions. These APIs must be able to
handle some version differences, since the lifecycle management of the forwarding and control
planes is not atomic. The offload functions that should be offered as
services must have published and preferably standardized open APIs. However, the application-
specific forwarding functions do not have to be open APIs, since they will only communicate with
the control functions provided by the application tenant. P4
:cite:p:`p4-open-source-programming-language` and OpenConfig :cite:p:`openConfig` are examples of
suitable languages and models, with different levels of flexibility, usable for these forwarding
and control functions.

The separated management channel can either come in through the BMC, a direct management port on
the DPU, or through a management VPN on the switch ports. This enables the hardware infrastructure
management to automate its networking through the DPU without the need to dynamically manage the
switch fabric. This enables a free choice of switch fabric vendor. These deployments allow the
switch fabric to be statically provisioned by the operator's networking operation unit, as is often
required.

The DPU can offload the control and data plane of the virtual switching to the DPU, as well as
offloading the trusted hardware for virtualized packet core and radio data plane networking, and
transport-related functionalities in a power-efficient way. It can also offload relevant application
tenant control functions, if the DPU offers an execution environment for virtual machines or
containers, and there is space and performance headroom. In such cases, the DPU must also set up a
communication channel in the respective application tenant environment.

Smart switches
~~~~~~~~~~~~~~

Smart switches fall into two categories:

- configurable smart switches
- programmable smart switches

Configurable smart switches run generic smart configurable network operating systems offering a
full range of network functionalities. Configurable smart switches are flexible enough to support
most network solutions. The most common such network operating system is Linux-based SONiC
:cite:p:`sonic`. SONiC allows hardware and software disaggregation by running on switches from
multiple switch vendors with different types of vendor fixed-function ASICs. However, today SONiC
cannot implement new types of data plane functionalities or patch/modify/correct an ASIC, which is
the type of support offered by programmable smart switches.

Programmable smart switches enable the support of new protocols and network functions. They also
enable the correcting or modifying of existing protocols and network functions, allow customers to
implement network functions, and to implement and load only those functionalities that are required.
Such switches contain one or more programmable switch ASICs of the same or different types. The two
most used programming languages are P4 :cite:p:`p4-open-source-programming-language` and NPL
:cite:p:`npl`. Both can be used with vendor-specific toolchains to program their switch ASICs or
FPGAs, or both. The Open Networking Foundation Stratum :cite:p:`stratum` is an example of a network
operating system that offers generic lifecycle management control services for the P4 components,
and a management API. The control API for the individual network functions are not part of the
Stratum APIs.

Based on smart switches, products exist for fully integrated Edge and fabric solutions from vendors
such as Arista, Cisco, and Kaloom.

Decoupling applications from the infrastructure and platform with hardware acceleration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Decoupling :ref:`common/glossary:cloud platform abstraction related terminology:` applications from
hardware accelerators are normally accomplished using drivers that, if available, are preferred
with standardized interfaces across vendors and their products, or, if not available, then through
drivers specific to the vendor hardware device in question. Decoupling infrastructure software from
hardware accelerators using standard interfaces is also preferred. If they are not available for
the target hardware accelerator, coupling one or a limited number of software infrastructures is
less of an issue compared to coupling multiple applications.

Taking advantage of Reference Model and Reference Architecture environments with common
capabilities, applications can be developed and deployed more rapidly, providing more service
agility and easier operations. The extent to which this can be achieved depends on the levels of
decoupling between the application and the infrastructure, or the platform underneath the
application.

Infrastructure
^^^^^^^^^^^^^^

- Application functionality or application control requires infrastructure components beyond the
  Reference Model profiles, or infrastructure configuration changes beyond the APIs specified by
  the Reference Architecture. Generally, such an application is tightly coupled with the
  infrastructure. This results in an appliance deployment model (see
  :ref:`common/glossary:cloud platform abstraction related terminology:`).
- Application control using APIs specified by the Reference Architecture finds nodes, already
  configured in support of the profiles, with the required infrastructure components. In those
  nodes using APIs specified by the Reference Architecture, the application control configures the
  infrastructure components that make the application work. An example of this is an application
  that, to achieve the latency requirements, needs certain hardware acceleration available in the
  Reference Model profile and is exposed through the APIs specified by the Reference Architecture.
- Application control using APIs specified by the Reference Architecture finds nodes, already
  configured in support of the profiles, with optional infrastructure components. In those nodes
  using APIs specified by the Reference Architecture, the application control configures the
  infrastructure components that make the application work more effectively than it would without
  that infrastructure component. An example of this is an application that is more cost-effective
  with certain acceleration adapters, but can also work without them.
- Application control using APIs specified by the Reference Architecture finds general profile
  nodes without any specific infrastructure components.

Platform services
^^^^^^^^^^^^^^^^^

- An application functionality or application control can work only with its own components, instead
  of using defined platform services. An example of this is an application that has its own load
  balancer.
- With a custom integration effort, an application can be made to use defined platform services. An
  example of this is an application that, with a custom integration effort, can use a defined load
  balancer which can be accelerated with hardware acceleration in a way that is fully decoupled
  from the application (that is, the application does not have awareness of the load balancer being
  hardware-accelerated).
- The application is designed and can be configured for running with defined platform services. An
  example of this is an application that can be configured to use a defined load balancer which can
  be accelerated with hardware acceleration.


Address Family For XDP (AF_XDP)
-------------------------------

Address Family For XDP (AF_XDP) :cite:p:`address-family-for-xdp` is optimized for high-performance
packet processing and is introduced in Linux kernel v4.18. This new socket type leverages the
eXpress Data Path (XDP) :cite:p:`eXpress-dataa-path-xdp` in-kernel fast-path to transfer traffic
frames from the NIC driver directly to userspace without the need for a full network stack. XDP is
an Extended Berkley Packet Filter :cite:p:`extended-berkley-packet-filter` (eBPF) software program.

By using the XDP_REDIRECT action from the XDP program, ingress frames can be redirected to other
XDP-enabled network devices. The fastest working mode of operation is Zero-Copy mode in enabled XDP
drivers.

.. figure:: ../figures/ch03-afxdp-arch.png
   :alt: AF_XDP architecture
   :name: AF_XDP architecture

   AF_XDP architecture

Linux-native applications can open an AF_XDP socket to receive raw packets directly from the NIC by
using libbpf :cite:p:`libbpf` library functions to register a packet buffer area where packets are
located, and to create and bind the socket to a networking interface. DPDK-based applications can
use the AF_XDP Poll Mode Driver :cite:p:`AF_XDP-poll-mode-driver`. VPP-based applications can use
the AF_XDP Device Driver :cite:p:`AF_XDP-device-driver`.

In virtualized environments, AF_XDP could be used as interface between guest Kernel and user space
applications. However, it would still need SR-IOV or virtio to get traffic to the virtual machine.


Energy efficiency
-----------------

Energy efficiency should be an overall requirement for the cloud infrastructure itself, the
workloads hosted by this infrastructure, and the interface layer between them. 

For telecommunication networks, energy efficiency is defined by ITU-T L.1330 :cite:p:`itutl1330`
as "the relation between the useful output and energy consumption", the useful output being a
metric which represents the capacity provided by the service whose energy efficiency is assessed.
As an example, the useful output of a traffic forwarding function can be the data volume forwarded
(for example, measured in bytes). The assessment of its energy efficiency is then based on the
ratio between this volume and the energy consumed for processing it (measured in Watt-hours, for
example): energy efficicency (B/Wh) = traffic volume/consumed energy.

As elaborated in the Next Generation Alliance's whitepaper NGA Green G :cite:p:`ngagreeng`,
with the global migration from 4G to 5G, one can observe the rise in datacentre power consumption
with the simultaneous reduction in the energy consumption of the core network elements. This
observation emphasizes the importance of energy efficiency on the infrastructure and workload
levels, and on the interface layer between them. 

Examples of opportunities for the energy demand and cost reductions for the telecommunications
operators are classified below.

- Optimization based on workload demand, enhanced by AI-based smart monitoring:
  - Smart sleep and shutdowns of infrastructure elements.
  - Adaptive power consumption.
  - Time of usage optimization.
  - Multiple input and output muting.
  - Cross base station optimization.

- Optimization based on technology advancements:
  - 2G/3G legacy shutdowns.
  - 3G/4G/5G optimization.
  - Cooling optimization.
  - Improved insulation.

- Energy sources:
  - Sustainable energy generation.
  - Procurement of green energy.
  - Fuel usage optimization.

In this Reference Model, the focus is on the first group, which is related to the optimization on
the workload to infrastructure interface level.

The method for assessing energy efficiency depends on the service targeted and the objectives. For
NFV, ETSI proposes a method for production environments in ETSI EN 303 471 :cite:p:`etsien303sp471`
and another method for laboratory environments in ETSI ES 203 539 :cite:p:`etsies203sp539` (this is
a common effort with the ITU-T which was published as ITU-T L.1361 :cite:p:`itutl1361`).

Whatever the method and the service, it requires the cloud infrastructure to provide some **energy
consumption metrics** for different parts of the infrastructure hardware (such as the server, the
CPU and so on), as included in :ref:`chapters/chapter04:internal performance measurement capabilities`.
These metrics can be an amount of consumed energy (measured in Joules or Watt-hours) or a real-time
power utilization (measured in Watt-seconds or Joules per second), as proposed by the DMTF Redfish
DSP0268 2022.2 :cite:p:`dmtfredfish` which specifies the metrics EnergykWh and PowerWatts for this
purpose.

Some relevant information regarding NFV energy efficiency can also be found in the Open RAN
Technical Priority - Focus on Energy Efficiency (March 2022) :cite:p:`oranenergyeff` and the QuEST
Forum - NFV Workload Efficiency Whitepaper (October 2016) :cite:p:`questnfvwlenergyeff`.


