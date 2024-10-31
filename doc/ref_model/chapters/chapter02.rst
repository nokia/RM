.. _workload-requirements--analysis:

Workload Requirements and Analysis
==================================

The cloud infrastructure is the totality of all the hardware and software components which build up the environment in
which the VNFs and CNFs (workloads) are deployed, managed, and executed. It is, therefore, inevitable that different
workloads will require different capabilities and have different expectations from the cloud infrastructure.

Among the main targets of the Reference Model is to define an agnostic cloud infrastructure, to remove any dependencies
between the workloads and the deployed cloud infrastructure, and to offer infrastructure resources to the workloads in
an abstracted way, with defined capabilities and metrics.

This means that operators will be able to host their Telco workloads (VNFs/CNFs) with different traffic types and
behaviours, and will be able to buy from any vendor on a unified consistent cloud infrastructure.

Additionally, a well-defined cloud infrastructure is needed for other types of workloads such as IT, machine
learning, and artificial intelligence.

This chapter analyses various Telco workloads and their requirements, and recommends certain cloud infrastructure
parameters necessary to specify the desired performance expected by these workloads.

Workloads collateral
--------------------

There are different ways in which workloads can be classified, for example:

-  **By function type:**

   -  Data plane (also known as user plane, media plane, and forwarding plane)
   -  Control plane (also known as signalling plane)
   -  Management plane

   ..

      **Note**\ *: Data plane workloads also include control and management plane functions. Control plane
      workloads also include management plane functions.*

- **By service offered:**

  - mobile broadband service
  - fixed broadband service
  - voice service
  - value-added services

-  **By technology:** 2G, 3G, 4G, 5G, IMS, FTTx, WiFi, and so on.

The following list of network functions most likely to be virtualised, covering almost 95% of the Telco workloads,
is organised by network segment and function type.

- **Radio Access Network (RAN)**

  - Data plane

    - BaseBand Unit (BBU)
    - Centralised Unit (CU)
    - Distributed Unit (DU)

- **2G/3G/4G mobile core network**

  - Control plane

    - Mobility Management Entity (MME)
    - Authentication, Authorisation, and Accounting (3GPP AAA)
    - Policy and Charging Rules Function (PCRF)
    - Online Charging system (OCS)
    - Offline Charging System (OFCS)
    - Home Subscriber Server (HSS)
    - Diameter Routing Agent (DRA)
    - Home Location Register (HLR)
    - Serving GateWay Control plane (SGW-C)
    - Packet data network GateWay Control plane (PGW-C)

  - Data plane

    - Serving GateWay (SGW)
    - Serving GateWay User plane (SGW-U)
    - Packet data network GateWay (PGW)
    - Packet data network GateWay User plane (PGW-U)
    - Evolved Packet Data GateWay (ePDG)
    - Mobile Switching Center (MSC)
    - Serving GPRS Support Node (SGSN)
    - Gateway GPRS Support Node (GGSN)
    - Short Message Service Center (SMSC)

- **5G core network**

  5G core nodes are virtualisable by design and are a strong candidate for onboarding into the Telco cloud as
  cloud-native applications.

  - Data plane

    - User Plane Function (UPF)

  - Control plane

    - Access and Mobility management Function (AMF)
    - Session Management Function (SMF)
    - Policy Control Function (PCF)
    - Authentication Server Function (AUSF)
    - Network Slice Selection Function (NSSF)
    - Unified Data Management (UDM)
    - Unified Data Repository (UDR)
    - Network Repository Function (NRF)
    - Network Exposure Function (NEF)
    - Charging Function part of the Converged Charging System (CHF)

      ..

         **Note:**\ *for Service-based Architecture (SBA), all network functions are stateless. That is, they
         store all sessions or states on unified data repository (UDR).*

- **IP Multimedia Subsystem (IMS)**

  - Data plane

    - Media GateWay (MGW)
    - Session Border Controller (SBC)
    - Media Resource Function (MRF)

  - Control plane

    - Call Session Control Function (CSCF)
    - Mobile Telephony Application Server (MTAS)
    - Border Gateway Control Function (BGCF)
    - Media Gateway Control Function (MGCF)

- **Fixed network**

  - Data plane

    - MultiService Access Node (MSAN)
    - Optical Line Termination (OLT)
    - WLAN Controller (WLC)
    - Broadband Network Gateway (BNG)
    - Broadband Remote Access Server (BRAS)
    - Residential GateWay (RGW)
    - Customer Premises Equipment (CPE)

  - Control plane

    - Authentication, Authorisation, and Accounting (AAA)

- **Other network functions**

  - Data plane

    - Label Switching Router (LSR)
    - Deep Packet Inspection (DPI)
    - Carrier-Grade Network Address Translation (CG-NAT)
    - Application Delivery Controller (ADC)
    - FireWall (FW)
    - Security GateWay (Sec-GW)
    - Content Delivery Network (CDN)

  - Control plane

    - Route Reflector (RR)
    - Domain Name System (DNS)

  - Management plane

    - Network Management System (NMS)

Use cases
---------

The intent of this section is to describe some important use cases that are pertinent to this Reference Model. We will
start with some typical Edge-related use cases. The list of use cases will be extended in future releases.

Telco Edge is commonly coupled with 5G use cases, seen as one of the ingredients of the Ultra-Reliable Low-latency
Communication (URLLC) and Enhanced Mobile Broadband (eMBB) network slicing. The requirements for user plane local
breakout/termination are common. They stipulate that value-added services (VASs) and any Gi-LAN applications are
locally hosted at the Edge. The Telco Edge is a perfect fit for centralized vRAN deployments and vDU/vCU hosting that
satisfy the latency requirements.

It is expected that with the technology evolution (for example, 6G), the use cases will be more demanding. For
example, to achieve either less than 1 ms latency or an ultrafast data rate, it will be required to evolve the
architecture. These use cases, once available, can be used for life saving decisions, such as for remote
automation in environments not supporting life (for example, in deep space communication), to ensure that the car
autonomous driving can be done in real time, and even for holographic communications. Such use cases can be seen as
the evolution of 5G use cases, where such requirements cannot be met due to technology constraints.

Use case no. 1: Edge CDN with eMBB core network slicing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Business objectives**

  Monetizing 5G by provisioning eMBB network slices with a distributed content delivery network (CDN) as a service
  that enables ultra-HD (UHD) streaming, video optimization, caching for large files, and other capabilities that can
  either be bundled by the network slice offering or implicitly enabled by the operator.

- **Targeted segments**

  - B2C: targeting high-tier packages and bundles
  - content owners: potential revenue sharing model
  - mobile virtual network operators (MVNOs): wholesale
  - stadiums and venues

- **Architecture**

.. figure:: ../figures/Fig2-1-uc1.png
  :alt: Edge CDN with eMBB Core Network Slicing

  Edge CDN with eMBB core network slicing

Use case no. 2: Edge private 5G with core network slicing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Business objectives**

  Private 5G is considered to be one of the most eagerly awaited business use cases in the coming years. It will
  enable mobile operators to provide a standalone private mobile network to enterprises that may include all the
  ingredients of the PLMN, such as radio, core, infrastructure, and services covering business requirements in terms
  of security, performance, reliability, and availability.

- **Targeted segments**

  - governmental sectors and public safety (mission-critical applications)
  - factories and the industry sector
  - enterprises with business-critical applications
  - enterprises with strict security requirements, with respect to the reachability of assets
  - enterprises with strict KPI requirements that mandate the on-premise deployment

- **Architecture**

  - There are multiple flavours for private 5G deployments or for the non-public network (NPN), as defined by 3GPP.
  - This use case addresses the technical realization of the NPN as a network slice of a PLMN, according to Annex D –
    3GPP TS 23.501 R16. It does not cover the other scenarios of deployment.
  - Thise use case assumes a network slice that is constructed from a single UPF deployed on customer premises, while
    sharing the 5G control plane (AMF, SMF, and other CP network functions) with the PLMN.
  - This use case does not cover the requirements of the private application servers (ASs), as they may vary with
    each customer setup.
  - Hosting the CU/DU on-customer infrastructure depends on the enterprise offering by the mobile operator and the
    selected private 5G setup.
  - The Edge cloud infrastructure can be governed by the client or handled by the service provider (mobile operator)
    as part of managed-services model.

.. figure:: ../figures/Fig2-2-uc2.png
  :alt: Edge private 5G with core network slicing

  Edge private 5G with core network slicing.

Use case no. 3: Edge automotive (V2X) with uRLLC core network slicing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Business objectives**

    The vehicle-to-everything (V2X) set of use cases provides a 5G monetization framework for mobile operators
    developing 5G URLLC business use cases targeting the automotive industry, smart city regulators, and public
    safety.

- **Targeted segments**

  - the automotive industry
  - governmental departments (smart cities, transport, police, emergency services, and so on)
  - private residences (compounds, hotels, and resorts)
  - enterprise and industrial campuses

- **Architecture**

  - 5G NR-V2X is a work item in 3GPP Release 16 that has not been completed at the time of writing this document.

    - Cellular V2X (C-V2X) has two modes of communication:

      - Direct mode, commonly described by Sidelink (SL), by 3GPP: this includes the V2V, V2I, and V2P using a
        direct interface (PC5) operating in ITS and intelligent transport bands (for example, 5.9 GHZ).
      - Network mode (UL/DL): this covers the V2N while operating in the common telecom-licensed spectrum. This use
        case capitalizes on this mode.

    - The potential use cases that may consume services from the Edge are the network model (V2N) and potentially
      the V2I (according to how the infrastructure will be mapped to an Edge level).

.. figure:: ../figures/Fig2-3-uc3.png
  :alt: Edge automotive (V2X) with uRLLC core network slicing

  Edge automotive (V2X) with uRLLC core network slicing

Use case no. 4: Edge vRAN deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Business objectives**
  vRAN is one of the trending RAN deployment technologies that fits all radio access technologies. vRAN helps to
  provide coverage for rural and uncovered areas with a compelling CAPEX reduction, compared to traditional and
  legacy RAN deployments. This coverage can be extended to all area types with 5G greenfield deployments as a
  typical example.

- **Targeted segments**

  - Private 5G customers: vRAN can be part of the non-public network (NPN).
  - B2B customers and MVNOs: vRAN can be part of E2E network slicing.
  - B2C: the mobile consumers segment.

- **Architecture**

  - There are multiple deployment models for the centralized unit (CU) and the distributed unit (DU). This use
    case covers the placement case of having the DU and the CU co-located and deployed on the Telco Edge. For
    details, see the NGMN Overview on 5GRAN Functional Decomposition ver 1.0 :cite:p:`ngmn5granfnldecomp`.
  - This use case covers the 5G vRAN deployment. However, this can be extended to cover 4G vRAN, as well.
  - Following Split Option 7.2, the average market latency for RU-DU (fronthaul) is 100 microseconds to 200
    microseconds, while the latency for DU-CU (midhaul) is tens of milliseconds. For details, see
    ORAN-WG4.IOT.0-v01.00 :cite:p:`oranwg4iot0`.

.. figure:: ../figures/Fig2-4-uc4.png
  :alt: Edge vRAN deployments

  Edge vRAN deployments

Use case no. 5: Telepresence experience
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Business objectives**

  This service allows communication with one or more persons and creates the impression of being present in the
  same location without being physically in a virtual environment. This service makes use of eMBB and URLLC
  network slices, and a distributed deployment which would offload processing.

- **Targeted segments**

  - B2B customers and MVNOs
  - B2C: the mobile consumers segment
  - enterpises which use of communication platforms
  
- **Architecture**

  - The architecture takes the form of distributed deployment models across the ecosystem. It should be possible
    to deploy the workloads at the extreme edge, which would allow real-time processing for video, and would
    offload processing for network load prediction. This would in turn support the quality of experience that is
    defined for such a use case.
  - This use case covers the placement at the management plane and the control plane (for example, the Core and
    the Edge domain).
  - There are high-level requirements for such a use case, such as a latency of 1ms, and an available bandwidth of
    8 Gbps.
      
Use case no. 6: Digital twins for manufacturing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Business Objectives**

  The business objectives are to provide the ability to design and create a product/service as a digital twin
  which can be tested before moving into the production environment. Therefore, only once acceptance is achieved
  in the digital world does the service become available. This leads to an extreme reduction of the total cost of
  ownership (TCO), and minimizes the risks that are commonly associated with the design and testing of a service
  for the industrial environment.

- **Targeted segments**

  - private networks
  - enterprise
  - factories (making extensive use of automation)
  
  - **Architecture**

  - This use case demands low latency (less than 1 ms) and high reliability.
  - The trustworthiness of the feature needs to be guaranteed. This is usually associated with performance,
    security, and resource efficiency/cost, and, subsequently, productivity.
  - This use case can process massive volumes of data.
    
Analysis
--------

Studying the various requirements of the workloads helps us to understand what expectations they will have
from the underlying cloud infrastructure. Some of the requirement types on which various workloads may have
different expectation levels are set out below:

- **Computing**

  - speed (for example, the CPU clock and the number of physical cores)
  - predictability (for example, CPU and RAM sharing level; real-time pre-emptive scheduling and/or settings
    for BIOS, kernel and OS services)
  - specific processing (for example, cryptography and transcoding)

- **Networking**

  - throughput (that is, bit rate or packet rate, or both)
  - latency and time-sensitive networking (TSN)
  - platform synchronization (such as GNSS, PTP, and SyncE)
  - the number of connection points or interfaces (that is, vNICs and VLANs)
  - specific traffic control (for example, firewalling, NAT, and cyphering)
  - specific external network connectivity (for example, MPLS and VXLAN)

- **Storage**

  - IOPS (that is, input/output rate or byte rate, or both)
  - volume
  - ephemeral or persistent
  - specific features (for example, object storage and local storage)

In trying to sort workloads into different categories based on the observed requirements, we have identified
two different profiles, detailed below. These profiles are mainly driven by the expected performance levels.

- **Profile One**

  - Workload types:

    - control plane functions without specific needs, and management plane functions
    - *examples: OFCS, AAA, and NMS*

  - Requirements:

    - There are no specific requirements.

- **Profile Two**

  - Workload types

    - data plane functions (that is, functions with specific networking and computing needs)
    - *examples: BNG, S/PGW, UPF, Sec-GW, DPI, CDN, SBC, MME, AMF, IMS-CSCF, and UDR*

  - Requirements:

    - predictable computing
    - high network throughput
    - low network latency

.. _profiles-profile-extensions--flavours:

Profiles, profile extensions, and flavours
------------------------------------------

**Profiles** are used to tag infrastructure, such as hypervisor hosts or Kubernetes worker nodes, and associate it with
a set of capabilities that are exploitable by the workloads.

There are two profile *layers*:

- Top-level **profiles**: The top-level profiles represent macro-characteristics that partition the infrastructure into
  separate pools. This means that an infrastructure object can belong to one profile only, and workloads can only be
  created using a single profile. Workloads requesting a given profile **must** be instantiated on the infrastructure of
  that same profile.
- Profile extensions: For a given profile, **profile extensions** represent small variations of the profile, such as
  infrastructure sizing differences (for example, memory size), that do not require the partitioning of the infrastructure
  into separate pools, but that have specifications with a finer granularity of the profile. Profile extensions can be
  *optionally* requested by workloads that want a more granular control over the infrastructure on which they run, that is,
  an infrastructure resource can have **more than one profile extension label** attached to it, and workloads can request
  resources to be instantiated on infrastructure with a certain profile extension. Workloads requesting a given profile
  extension **must** be instantiated on infrastructure with the same profile extension. The operator may instantiate
  workloads on infrastructure tagged with more profile extensions than requested, as long as the minimum requirements are
  satisfied.

The workloads specify infrastructure capability requirements as workload metadata, indicating what kind of
infrastructure they must run on to achieve functionality or the intended level of performance, or both. The workloads
request resources, specifying the profiles and profile extensions, and a set of sizing metadata that may be expressed
as flavours that are required for the workload to run as intended.
A resource request by a workload can be met by any infrastructure node that has the same or a more specialised profile,
and the necessary capacity to support the requested flavour or resource size.

Profiles, profile extensions, and flavours are considered in greater detail in
:ref:`chapters/chapter04:profile extensions`.

Profiles (top-level partitions)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Based on the analysis in Profiles, profile extensions, and flavours, the following cloud infrastructure profiles are as
follows (see also :numref:`Infrastructure profiles proposed based on VNFs categorisation`):

- **Basic**: this is for workloads that can tolerate resource over-subscription and variable latency.
- **High-performance**: this is for workloads that require predictable computing performance, high network throughput,
and low network latency.

.. figure:: ../figures/RM-ch02-node-profiles.png
   :alt: Infrastructure profiles based on the categorisation of the VNFs
   :name: Infrastructure profiles based on the categorisation of the VNFs

   Infrastructure profiles based on the categorisation of the VNFs

In :ref:`chapters/chapter04:infrastructure capabilities, measurements and catalogue`
these **Basic (B)** and **High-performance (H)** infrastructure profiles are defined in greater detail for use by the
workloads.

Profiles partition the infrastructure: an infrastructure object (host/node) **must** have only one profile associated
to it.

Profile extensions (specialisations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Profile extensions are intended to be used as labels for infrastructure. They identify the nodes that implement
special capabilities that go beyond the profile baseline. Certain profile extensions may only be relevant for some
profiles. The **profile extensions** are detailed in the following table.

+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Profile extension | Mnemonic                | Applicable to | Applicable to | Description            | Notes         |
| name              |                         | the basic     | the high-     |                        |               |
|                   |                         | profile       | performance   |                        |               |
|                   |                         |               | profile       |                        |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Compute-intensive | compute-high-perf-cpu   | ❌            | ✅           | Nodes that have        | May use       |
| high-performance  |                         |               |               | predictable computing  | vanilla       |
| CPU               |                         |               |               | performance and higher | VIM/K8S       |
|                   |                         |               |               | clock speeds.          | scheduling    |
|                   |                         |               |               |                        | instead.      |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Storage-intensive | storage-high-perf       | ❌            | ✅           | Nodes that have low    |               |
| high-performance  |                         |               |               | storage latency or     |               |
| storage           |                         |               |               | high storage IOPS, or  |               | 
|                   |                         |               |               | both.                  |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Compute-intensive | compute-high-memory     | ❌            | ✅           | Nodes that have high   | May use       |
| high memory       |                         |               |               | amounts of RAM.        | vanilla       |
|                   |                         |               |               |                        | VIM/K8S       |
|                   |                         |               |               |                        | scheduling    |
|                   |                         |               |               |                        | instead.      |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Compute-intensive | compute-gpu             | ❌            | ✅           | For compute-intensive  | May use node  |
| GPU               |                         |               |               | workloads that         | feature       |
|                   |                         |               |               | require GPU compute    | discovery.    |
|                   |                         |               |               | resources on the node. |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Network-intensive | high-speed-network      | ❌            | ✅           | Denotes the presence   |               |
| high-speed        |                         |               |               | of network links (to   |               |
| network (25G)     |                         |               |               | the DC network) with a |               |
|                   |                         |               |               | speed of 25 Gbps or    |               |
|                   |                         |               |               | greater on the node.   |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Network-intensive | very-high-speed-network | ❌            | ✅           | Denotes the presence   |               |
| very-high-speed   |                         |               |               | of network links (to   |               |
| network (100G)    |                         |               |               | the DC network) with a |               |
|                   |                         |               |               | speed of 100 Gbps or   |               |
|                   |                         |               |               | greater on the node.   |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Low latency Edge  | low-latency-edge        | ✅            | ✅           | Labels a host/node as  |               |
| sites             |                         |               |               | located in an Edge     |               |
|                   |                         |               |               | site, for workloads    |               |
|                   |                         |               |               | requiring low latency  |               |
|                   |                         |               |               | (specify value), to    |               |
|                   |                         |               |               | final users or         |               |
|                   |                         |               |               | geographical           |               |
|                   |                         |               |               | distribution.          |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Very low latency  | very-low-latency-edge   | ✅            | ✅           | Labels a host/node as  |               |
| Edge sites        |                         |               |               | located in an Edge     |               |
|                   |                         |               |               | site, for workloads    |               |
|                   |                         |               |               | requiring low latency  |               |
|                   |                         |               |               | (specify value), to    |               |
|                   |                         |               |               | final users or         |               |
|                   |                         |               |               | geographical           |               |
|                   |                         |               |               | distribution.          |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Ultra low latency | ultra-low-latency-edge  | ✅            | ✅           | Labels a host/node as  |               |
| Edge sites        |                         |               |               | located in an Edge     |               |
|                   |                         |               |               | site, for workloads    |               |
|                   |                         |               |               | requiring low latency  |               |
|                   |                         |               |               | (specify value), to    |               |
|                   |                         |               |               | final users or         |               |
|                   |                         |               |               | geographical           |               |
|                   |                         |               |               | distribution.          |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Real-time and     | rt-tsn                  | ❌            | ✅           | Labels a host/node     | For example,  |
| time-sensitive    |                         |               |               | configured for Real-   | nodes to run  |
| networking - RAN  |                         |               |               | -Time predictability   | vDU           |
| cell sites        |                         |               |               | and Time Sensitive     |               |
|                   |                         |               |               | Networking             |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Fixed-function    | compute-ffa             | ❌            | ✅           | Labels a host/node     |               |
| accelerator       |                         |               |               | that includes a        |               |
|                   |                         |               |               | consumable fixed-      |               |
|                   |                         |               |               | function accelerator   |               |
|                   |                         |               |               | (non-programmable,     |               |
|                   |                         |               |               | such as a Crypto- or   |               |
|                   |                         |               |               | vRAN-specific          |               |
|                   |                         |               |               | adapter).              |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| Firmware-         | compute-fpga            | ❌            | ✅           | Labels a host/node     |               |
| programmable      |                         |               |               | that includes a        |               |
| adapter           |                         |               |               | consumable             |               |
|                   |                         |               |               | firmware-programmable  |               |
|                   |                         |               |               | adapter (programmable, |               |
|                   |                         |               |               | such as a network/     |               |
|                   |                         |               |               | storage FPGA with a    |               |
|                   |                         |               |               | programmable part of   |               |
|                   |                         |               |               | the firmware image).   |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| SmartNIC enabled  | network-smartnic        | ❌            | ✅           | Labels a host/node     |               |
|                   |                         |               |               | that includes a        |               |
|                   |                         |               |               | programmable           |               |
|                   |                         |               |               | accelerator for        |               |
|                   |                         |               |               | vSwitch/vRouter,       |               |
|                   |                         |               |               | network function,      |               |
|                   |                         |               |               | and/or hardware        |               |
|                   |                         |               |               | infrastructure.        |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+
| SmartSwitch-      | network-smartswitch     | ❌            | ✅           | Labels a host/node     |               |
| enabled           |                         |               |               | that is connected to a |               |
|                   |                         |               |               | programmable switch    |               |
|                   |                         |               |               | fabric or a TOR        |               |
|                   |                         |               |               | switch.                |               |
+-------------------+-------------------------+---------------+---------------+------------------------+---------------+

**Table 2-1:** Profile extensions

   \*\ **Note:** This is an initial set of proposed profiles and profile extensions. It is expected that more profiles
   or profile extensions, or both, will be added as more requirements are gathered, and as technology evolves and
   matures.
