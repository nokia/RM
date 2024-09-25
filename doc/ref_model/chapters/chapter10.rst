Challenges and Gaps
===================

Introduction
------------

This section is dedicated to identifying the challenges and gaps found in the course of the development of the
Reference Model to ensure that it continues to be of strategic and tactical value for the long term. Should a
challenge or gap not be identified that has not already been addressed in the model itself, the community may assume
that it will remain an unknown. Therefore, the community is encouraged to engage with and raise an issue with the
appropriate working groups to close the gap. In this manner, the Reference Model can continuously improve.

Challenges
----------

The continuous challenge is to finalize a stable version from which all the stakeholders in the application value
chain can derive the intended value of a common cloud infrastructure. This maturity level is reached when the released
Reference Model version is adopted by the stakeholders into their application development and deployment cycles.

Gaps
----

This section addresses the major open issues identified in the development of the Reference Model, the Reference
Architecture, and the Reference Implementation of the Common Cloud Infrastructure Lifecycle Framework.

Discovery
~~~~~~~~~

The workloads (VNFs and CNFs) and the cloud infrastructure should be able to discover each other and exchange their
capabilities as required or offered. One of the key pain points for most of the operators is the VNF/CNF onboarding,
in terms of time and complexity. It could take weeks or months to onboard a VNF or a CNF. A lot of static and
laborious checks have to be performed to ensure the compatibility of the workloads with the corresponding cloud
infrastructure. The onboarding of the workloads (network functions) should be automated as much as possible. The
workloads and cloud infrastructure should be able to discover and negotiate their capabilities. The following needs
to be supported:

- Discovery and advertising of capabilities:

  - The cloud infrastructure should be able to publish the capabilities it offers to the workloads or network
    functions.
  - The workloads should be able to query the cloud infrastructure for specific capabilities, such as the number of
    cores and performance parameters.

- Negotiation of capabilities/handshake API:

  - The workloads and cloud infrastructure should be able to negotiate on certain capabilities. For example, a
    workload desires hardware acceleration for high throughput, but should be able to fall back to high throughput
    offered by the cloud infrastructure via a DPDK offering, and vice versa.

Supporting the load balancing of VNF/CNFs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ability to dynamically scale a network function by load balancing across multiple instances or replicas of the
same VNF or CNF is essential. New architectures and application patterns, such as microservices, make this even more
crucial. It must not only be possible to load balance and scale each service layer independently, it is also essential
to provide support for chaining the different layers together through Service Function Chaining.

The load balancing and scaling needed for typical enterprise applications is well supported in OpenStack by the Octavia
v2 API. The Octavia v2 API is a backwards-compatible superset of the Neutron LBaaS v2 API that it is replacing.

The built-in mechanism in Kubernetes for scaling enterprise-type services and PODs is also sufficient for applications
that only use one interface.

What is not supported either in OpenStack or Kubernetes is the scaling and load balancing of a typical VNF or CNF. There
is no support in OpenStack to scale stateful L3 applications such as SCTP, QUIC, mTCP, and gRPC. In Kubernetes it is even
worse. The built-in Kubernetes network support is tied to the first POD/container interface. Support for the secondary
interfaces is managed through the Container Network Interface (CNI) and by CNI plugins, such as Multus, that support the
“Kubernetes Network Customs Resource Definition”, specified by the Kubernetes Network Plumbing Group. This specification
supports the attachment of network endpoints to PODs, IP address management, and the ability to define interface-specific
static routes. There is no support for network orchestration and functions, such as load balancing, routing, ACL, and
firewalls.

Closed-loop automation
~~~~~~~~~~~~~~~~~~~~~~

The state of a system is defined by a set of variables that fully describe the system and determine the response of the
system to any given set of inputs. A closed-loop automation system automatically maintains the specified desired state
of the controlled system.

Closed-loop automation is evolving as a major advancement in telecommunication network automation. In the context of
telecommunications systems, closed-loop automation is a system that, in a continuous loop, programmatically validates
the state of the cloud infrastructure against the declared desired state. In the case of deviation from the desires
state, it automatically takes remediation actions necessary for bringing the actual state to the desired state. The
Reference Model specification will address this important area in the next releases.

Hybrid multicloud: APIs
~~~~~~~~~~~~~~~~~~~~~~~

Section "8.5 Multi-Cloud Interactions Model" defines several core roles within the multicloud model and discusses
stereotypical interactions between them. However, the model realises that a federated cloud requires the definition
of, and agreement on, a set of APIs. The current fragmentation in the industry is caused by the following factors:

- Proprietary APIs, some of which have been adopted as default industry standards.
- A number of open-source community projects aiming to provide abstract interfaces to wrap proprietary APIs.
- Vendors offering to act as brokers.
- Standards and industry APIs to address specific subsets of interactions.

AF_XDP
~~~~~~

Linux-native AF_XDP promises high enough packet processing performance and simplification, compared to what SR-IOV
and DPDK require for initial installation and later lifecycle management. Nevertheless, it will take time until
AF_XDP-based solutions are financially invested and have matured enough in both virtualization infrastructure and
network functions.
