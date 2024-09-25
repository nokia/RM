Feature Set and Requirements from Infrastructure
================================================

A profile :ref:`chapters/chapter02:profiles, profile extensions & flavours` specifies the configuration of a
Cloud Infrastructure node (host or server). :ref:`chapters/chapter02:profile extensions (specialisations)`
may specify additional configurations. Workloads use profiles to describe the configuration of nodes on which they
can be hosted to execute on. Workload flavours provide a mechanism to specify the VM or Pod sizing information to host
the workload. Depending on the requirements of the workloads, a VM or a Pod is deployed according to the specified
flavour information on a node configured according to the specified profile. Not only do the nodes (the hardware) have
to be configured but some of the capabilities also need to be configured in the software layers (such as Operating
System and Virtualisation Software). Therefore, a profile can be defined in terms of the configuration required in the
software layers, the Cloud Infrastructure software profile, and the hardware, the Cloud Infrastructure Hardware
Profile.

Cloud Infrastructure software profile description
-------------------------------------------------

The Cloud Infrastructure software layer is composed of the following two layers:

-  The virtualisation infrastructure layer. This layer is based on hypervisor virtualisation technology or container-based
   virtualisation technology. Container virtualisation can be nested in hypervisor-based virtualisation.
-  The host operating system (OS) layer.

.. figure:: ../figures/ch05-cloud-infrastructure-sw-profile-layers.png
   :name: Cloud Infrastructure software layers
   :alt: Cloud Infrastructure software layers

   Cloud Infrastructure software layers

+--------------+----------------+---------+-------------------------------------------------------------+--------------+
| Ref          | Cloud          | Type    | Definition/notes                                            | Capabilities |
|              | Infrastructure |         |                                                             | reference    |
|              | software       |         |                                                             | (1)          |
+==============+================+=========+=============================================================+==============+
| infra.sw.001 | Host operating | <value> | Values, such as Ubuntu20.04, Windows 10 Release #, and so   | e.cap.021    |
|              | system         |         | on.                                                         |              |
+--------------+----------------+---------+-------------------------------------------------------------+--------------+
| infra.sw.002 | Virtualisation | <value> | Values, such as KVM, Hyper-V, Kubernetes, and so on.        | e.cap.022    |
|              | infrastructure |         |                                                             |              |
|              | layer          |         |                                                             |              |
+--------------+----------------+---------+-------------------------------------------------------------+--------------+

..

   (1) Reference to the capabilities defined in
   :ref:`chapters/chapter04:infrastructure capabilities, measurements and catalogue`.

For a host (a compute node or a physical server), the virtualisation layer is an abstraction layer between the hardware
components (compute, storage, and network resources) and the virtual resources allocated to a VM or a Pod.
:numref:`Cloud Infrastructure Virtual resources` represents the virtual resources (virtual compute, virtual network, and
virtual storage) allocated to a VM or a Pod and managed by the Cloud Infrastructure manager.

.. figure:: ../figures/ch05_b_ref_profile.png
   :name: Cloud Infrastructure Virtual resources
   :alt: Cloud Infrastructure Virtual resources

   Cloud Infrastructure virtual resources

A Cloud Infrastructure software profile is a set of features, capabilities, and metrics offered by a Cloud
Infrastructure software layer and configured in the software layers (the Operating System (OS) and the virtualisation
software (such as the hypervisor)). :numref:`Cloud Infrastructure Software Profiles` depicts a high-level view of the
basic and high-performance Cloud Infrastructure profiles.

.. figure:: ../figures/RM-ch05-sw-profile.png
   :name: Cloud Infrastructure software profiles
   :alt: Cloud Infrastructure software profiles

   Cloud Infrastructure software profiles

The following sections detail the Cloud Infrastructure software profile capabilities according to the type of virtual
resource.

Virtual compute profiles
~~~~~~~~~~~~~~~~~~~~~~~~

**Table 5-1** and **Table 5-2** depict the features related to virtual compute.

+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| Reference         | Feature              | Type            | Description                              | Capabilities |
|                   |                      |                 |                                          | reference    |
+===================+======================+=================+==========================================+==============+
| infra.com.cfg.001 | CPU allocation ratio | <value>         | The number of virtual cores per physical | i.cap.016    |
|                   |                      |                 | core.                                    |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.cfg.002 | NUMA alignment       | Yes/No          | Support of NUMA at the host OS and the   | e.cap.007    |
|                   |                      |                 | virtualisation layers, in addition to    |              |
|                   |                      |                 | the hardware.                            |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.cfg.003 | CPU pinning          | Yes/No          | This feature binds a vCPU to a physical  | e.cap.006    |
|                   |                      |                 | core or an SMT thread. It is configured  |              |
|                   |                      |                 | in the OS and virtualisation layers.     |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.cfg.004 | Huge pages           | Yes/No          | The ability to manage huge pages of      | i.cap.018    |
|                   |                      |                 | memory. It is configured in the OS and   |              |
|                   |                      |                 | virtualisation layers.                   |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.cfg.005 | Simultaneous         | Yes/No/Optional | SMT allows multiple execution threads to | e.cap.018    |
|                   | multithreading (SMT) |                 | be executed on a single physical CPU     |              |
|                   |                      |                 | core. It is configured in the OS, in     |              |
|                   |                      |                 | addition to the hardware.                |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+

**Table 5-1:** Virtual compute features.

+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| Reference         | Feature              | Type            | Description                              | Capabilities |
|                   |                      |                 |                                          | reference    |
+===================+======================+=================+==========================================+==============+
| infra.com.acc.cfg | IPSec acceleration   | Yes/No/Optional | IPSec acceleration                       | e.cap.008    |
| .001              |                      |                 |                                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.acc.cfg | Transcoding          | Yes/No/Optional | Transcoding acceleration                 | e.cap.010    |
| .002              | acceleration         |                 |                                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.acc.cfg | Programmable         | Yes/No/Optional | Programmable acceleration                | e.cap.011    |
| .003              | acceleration         |                 |                                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.acc.cfg | GPU                  | Yes/No/Optional | Hardware coprocessor                     | e.cap.014    |
| .004              |                      |                 |                                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.com.acc.cfg | FPGA/other           | Yes/No/Optional | This is non-specific hardware. These     | e.cap.016    |
| .005              | acceleration H/W     |                 | capabilities generally require           |              |
|                   |                      |                 | hardware-dependent drivers to be         |              |
|                   |                      |                 | injected into the workloads.             |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+

**Table 5-2:** Virtual compute acceleration features.

Virtual storage profiles
~~~~~~~~~~~~~~~~~~~~~~~~

**Table 5-3** and **Table 5-4** depict the features related to virtual storage.

================= ======================== ====== =======================================================
Reference         Feature                  Type   Description
================= ======================== ====== =======================================================
infra.stg.cfg.001 Catalogue storage types  Yes/No The support of storage types described in the catalogue
infra.stg.cfg.002 Storage block            Yes/No
infra.stg.cfg.003 Storage with replication Yes/No
infra.stg.cfg.004 Storage with encryption  Yes/No
================= ======================== ====== =======================================================

**Table 5-3:** Virtual storage features.

===================== ========================= ====== ===========
Reference             Feature                   Type   Description
===================== ========================= ====== ===========
infra.stg.acc.cfg.001 Storage IOPS oriented     Yes/No
infra.stg.acc.cfg.002 Storage capacity oriented Yes/No
===================== ========================= ====== ===========

**Table 5-4:** Virtual storage acceleration features.

Virtual networking profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Table 5-5** and **Table 5-6** depict the features related to virtual networking.

+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| Reference         | Feature              | Type            | Description                              | Capabilities |
|                   |                      |                 |                                          | Reference    |
+===================+======================+=================+==========================================+==============+
| infra.net.cfg.001 | Connection point     |IO virtualisation|  For example, virtio1.1.                 |              |
|                   | interface IO         |                 |                                          |              |
|                   | virtualisation       |                 |                                          |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.net.cfg.002 | Overlay protocol     | Protocols       | The overlay network encapsulation        |              |
|                   |                      |                 | protocol needs to enable ECMP in the     |              |
|                   |                      |                 | underlay to take advantage of the        |              |
|                   |                      |                 | scale-out features of the network        |              |
|                   |                      |                 | fabric.                                  |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.net.cfg.003 | NAT                  | Yes/No          | Support of network address translation.  |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.net.cfg.004 | Security groups      | Yes/No          | The set of rules managing incoming and   |              |
|                   |                      |                 | outgoing network traffic.                |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.net.cfg.005 | Service function     | Yes/No          | Support of service function chaining     |              |
|                   | chaining             |                 | (SFC).                                   |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+
| infra.net.cfg.006 | Traffic patterns     | Yes/No          | Traffic patterns should be optimal, in   |              |
|                   | symmetry             |                 | terms of packet flow. North-south        |              |
|                   |                      |                 | traffic must not be concentrated in      |              |
|                   |                      |                 | specific elements in the architecture,   |              |
|                   |                      |                 | making those critical choke-points,      |              |
|                   |                      |                 | unless strictly necessary (for example,  |              |
|                   |                      |                 | when NAT 1:many is required).            |              |
+-------------------+----------------------+-----------------+------------------------------------------+--------------+

**Table 5-5:** Virtual networking features.

===================== ============================= ========================== ================== ======================
Reference             Feature                       Type                       Description        Capabilities reference
===================== ============================= ========================== ================== ======================
infra.net.acc.cfg.001 vSwitch optimisation          Yes/No and SW optimisation For example, DPDK. ``e.cap.019``
infra.net.acc.cfg.002 SmartNIC (for HW offload)     Yes/No                     HW offload         ``e.cap.015``
infra.net.acc.cfg.003 Crypto acceleration           Yes/No                                        ``e.cap.009``
infra.net.acc.cfg.004 Crypto acceleration interface Yes/No
===================== ============================= ========================== ================== ======================

**Table 5-6:** Virtual networking acceleration features.

Security
~~~~~~~~

For details, see section 7 Security.

Platform services
~~~~~~~~~~~~~~~~~

This section details the services that may be made available to the workloads by the Cloud Infrastructure.

================= ============== ====== ====================================================
Reference         Feature        Type   Description
================= ============== ====== ====================================================
infra.svc.stg.001 Object storage Yes/No Object storage service (for example, S3-compatible).
================= ============== ====== ====================================================

**Table 5-7:** Cloud Infrastructure platform services.

+--------------------------------------+-------------------------------------------------------------------------------+
| Platform service category            | Platform service examples                                                     |
+======================================+===============================================================================+
| Data stores/databases                | Ceph, etcd, MongoDB, Redis                                                    |
+--------------------------------------+-------------------------------------------------------------------------------+
| Streaming and messaging              | Apache Kafka, Rabbit MQ                                                       |
+--------------------------------------+-------------------------------------------------------------------------------+
| Load balancer and service proxy      | Envoy, Istio, NGINX                                                           |
+--------------------------------------+-------------------------------------------------------------------------------+
| Service mesh                         | Envoy, Istio                                                                  |
+--------------------------------------+-------------------------------------------------------------------------------+
| Security and compliance              | Calico, cert-manager                                                          |
+--------------------------------------+-------------------------------------------------------------------------------+
| Monitoring                           | Prometheus, Grafana (for visualisation), Kiali (for service mesh)             |
+--------------------------------------+-------------------------------------------------------------------------------+
| Logging                              | Fluentd, ElasticSearch (Elastic.io, Open Distro), ELK Stack (Elasticsearch,   |
|                                      | Logstash, and Kibana)                                                         |
+--------------------------------------+-------------------------------------------------------------------------------+
| Application definition and image     | Helm                                                                          |
| build                                |                                                                               |
+--------------------------------------+-------------------------------------------------------------------------------+
| CI/CD                                | Argo, GitLab, Jenkins                                                         |
+--------------------------------------+-------------------------------------------------------------------------------+
| Ingress/egress controllers           | Envoy, Istio, NGINX                                                           |
+--------------------------------------+-------------------------------------------------------------------------------+
| Network related services             | CoreDNS, Istio                                                                |
+--------------------------------------+-------------------------------------------------------------------------------+
| Coordination and service discovery   | CoreDNS, etcd, Zookeeper                                                      |
+--------------------------------------+-------------------------------------------------------------------------------+
| Automation and configuration         | Ansible                                                                       |
+--------------------------------------+-------------------------------------------------------------------------------+
| Key management                       | Vault                                                                         |
+--------------------------------------+-------------------------------------------------------------------------------+
| Tracing                              | Jaeger                                                                        |
+--------------------------------------+-------------------------------------------------------------------------------+

**Table 5-7a:** Service examples.


Platform services - load balancer requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below specifies a set of requirements for the load balancer platform service.

+------------+--------------------------------------------------------+---------------------------------------------+
| Reference  | Requirement                                            | Notes                                       |
+============+========================================================+=============================================+
| pas.lb.001 | The load balancer must support workload resource       |                                             |
|            | scaling.                                               |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.002 | The load balancer must support resource resiliency.    |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.003 | The load balancer must support scaling and resiliency  | Local environment: within a subnet, tenant  |
|            | in the local environment.                              | network, Availability Zone of a cloud, ...  |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.004 | The load balancer must support OSI Level 3/4           | Specifically, OSI Level 3 load balancing    |
|            | load balancing.                                        | decisions on the source and destination IP  |
|            |                                                        | addresses, and OSI Level 4 TCP port numbers.|
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.005 | The load balancer must, at a minimum, support          |                                             |
|            | round-robin load balancing.                            |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.006 | The load balancer must create event logs with the      |                                             |
|            | appropriate severity levels (catastrophic,             |                                             |
|            | critical, and so on).                                  |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.007 | The load balancer must support monitoring of           |                                             |
|            | endpoints.                                             |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.008 | The load balancer must support Direct Server           | Other modes can also be supported, but DSR  |
|            | Return (DSR).                                          | should always be supported.                 |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.009 | The load balancer must support stateful TCP load       |                                             |
|            | balancing.                                             |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.010 | The load balancer must support UDP load-balancing.     |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.011 | The load balancer must support load balancing and      |                                             |
|            | the correct handling of fragmented packets.            |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.012 | The load balancer may support stateful SCTP load       |                                             |
|            | balancing.                                             |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.013 | The load balancer may support stateful M-TCP load      |                                             |
|            | balancing.                                             |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.014 | The load balancer may support Level 7 load             | Application characteristics-based OSI       |
|            | balancing.                                             | Level 7 should support HTTP and HTTPS.      |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.015 | The L7 load balancer may support HTTP2.                |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.016 | The L7 load balancer may support HTTP3.                |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+
| pas.lb.017 | The L7 load balancer may support QUIC.                 |                                             |
+------------+--------------------------------------------------------+---------------------------------------------+

**Table 5-7b:** Platform services - load balancer requirements.

Platform services - log management service (LMS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below specifies a set of requirements for the log management service (LMS).

+-------------+-----------------------------------------------------------------------+---------------------------------------+
| Reference   | Requirement                                                           | Notes                                 |
+=============+=======================================================================+=======================================+
| pas.lms.001 | The LMS must support log management from multiple distributed         |                                       |
|             | sources.                                                              |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.002 | The LMS must manage log rotation at configurable periods.             |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.003 | The LMS must manage log rotation at configurable log file status      |                                       |
|             | (%full).                                                              |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.004 | The LMS must manage archival and retention of logs for configurable   |                                       |
|             | periods by different log types.                                       |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.005 | The LMS must ensure log file integrity (no changes, particularly      | This is covered by req.sec.mon.005:   |
|             | changes that may affect the completeness, consistency, and accuracy,  | "The Prod-Platform and NonProd-       |
|             | including event times, of the log file content).                      | Platformmust secure  and protect all  |
|             |                                                                       | logs (containing  sensitive           |
|             |                                                                       | information) both in-transit  and at  |
|             |                                                                       | rest."                                |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.006 | The LMS must monitor log rotation and log archival processes.         |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.007 | The LMS must monitor the logging status of all the log sources.       |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.008 | The LMS must ensure that the clock of each logging host is            |                                       |
|             | synchronized to a common time source.                                 |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.009 | The LMS must support the reconfiguring of logging as needed, based on |                                       |
|             | policy changes, technology changes, and other factors.                |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.010 | The LMS must support the documenting and reporting of anomalies in    |                                       |
|             | log settings, configurations, and processes.                          |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.011 | The LMS must support the correlating of entries from multiple logs    |                                       |
|             | that relate to the same event.                                        |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.012 | The LMS must support the correlating of multiple log entries from a   |                                       |
|             | single source or multiple sources, based on logged values (for        |                                       |
|             | example, event types, timestamps, and IP addresses).                  |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+
| pas.lms.013 | The LMS should support rule-based correlation.                        |                                       |
+-------------+-----------------------------------------------------------------------+---------------------------------------+

**Table 5-7c:** Platform services - log management service (LMS) requirements


Platform services - monitoring service requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below specifies a set of requirements for the monitoring service (aka monitoring system).

+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| Reference   | Requirement                                                           | Notes                                                 |
+=============+=======================================================================+=======================================================+
| pas.mon.001 | The monitoring service must be able to collect data generated by or   | Ability to monitor applications, services,            |  
|             | collected from any resource (physical and virtual infrastructure,     | operating systems, network protocols, system metrics, |
|             | application, network, and so on).                                     | and infrastructure components.                        |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.002 | The monitoring service must be able to aggregate the collected data.  |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.003 | The monitoring service must be able to correlate data from different  |                                                       |
|             | systems.                                                              |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.004 | The monitoring service must be able to perform active or passive      |                                                       |
|             | monitoring, or both.                                                  |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.005 | The monitoring service must support the configuration of thresholds,  |                                                       |
|             | outside which the resource cannot function normally, for alert        |                                                       |
|             | generation.                                                           |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.006 | The monitoring service must support the configuration of alert        |                                                       |
|             | notification media (such as email, SMS, phone, and so on).            |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.007 | The monitoring service must support configurable realerting after     |                                                       |
|             | a configurable period, if the metric remains outside the              |                                                       |
|             | threshold.                                                            |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.008 | The monitoring service must support configurable alert escalations.   |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.009 | The monitoring service must support alert acknowledgments by          |                                                       |
|             | disabling the future alerting of the same resource/reason.            |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.010 | The monitoring service must support the selective enabling and        |                                                       |
|             | disabling of alerts by resource, category of resources, and lengths   |                                                       | 
|             | of time.                                                              |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.011 | The monitoring service must publish its APIs for programmatic         |                                                       |
|             | invocation of all monitoring service functions.                       |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.012 | The monitoring service must itself be monitored through a logging     |                                                       |
|             | service.                                                              |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.013 | The monitoring service should be implemented for high availability    |                                                       |
|             | to ensure the non-stop monitoring of critical infrastructure          |                                                       |
|             | components.                                                           |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.014 | The monitoring service should run separately from production          |                                                       |
|             | services.                                                             |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.015 | A failure of the monitoring of the system should not cause a failure  |                                                       |
|             | in the monitoring service.                                            |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.016 | An inoperative monitoring service should not generate alerts about    |                                                       |
|             | the monitored system.                                                 |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+
| pas.mon.017 | The monitoring service should provide a consolidated view of the      |  View: dashboard or report                            |
|             | entire monitored infrastructure.                                      |                                                       |
+-------------+-----------------------------------------------------------------------+-------------------------------------------------------+

**Table 5-7d:** Platform services - monitoring service requirements



Features and requirements of the Cloud Infrastructure software profiles
-----------------------------------------------------------------------


This section details the Cloud Infrastructure software profiles and the associated configurations for the two types of Cloud 
Infrastructure profiles: Basic and High Performance.

.. _virtual-compute-1:

Virtual compute
~~~~~~~~~~~~~~~


**Table 5-8** depicts the features and configurations related to virtual compute for the two Cloud Infrastructure
profiles.

================= ================================= =============== ===================== ================
Reference         Feature                           Type            Basic                 High performance
================= ================================= =============== ===================== ================
infra.com.cfg.001 CPU allocation ratio              <value>         N:1                   1:1
infra.com.cfg.002 NUMA alignment                    Yes/No          N                     Y
infra.com.cfg.003 CPU pinning                       Yes/No          N                     Y
infra.com.cfg.004 Huge pages                        Yes/No          N                     Y
infra.com.cfg.005 Simultaneous multithreading (SMT) Yes/No/Optional Y if SMT is supported Optional
================= ================================= =============== ===================== ================

**Table 5-8:** Virtual compute features and configuration for the two types of Cloud Infrastructure profiles


**Table 5-9** lists the features related to compute acceleration for the high-performance profile. The table also 
lists the applicable :ref:`chapters/chapter04:profile extensions` and extra specifications that may need to be 
specified.


===================== =========================== ============================= ===================
Reference             Feature                     Profile-Extensions            Profile extra specs
===================== =========================== ============================= ===================
infra.com.acc.cfg.001 IPSec acceleration          Compute-intensive GPU
infra.com.acc.cfg.002 Transcoding acceleration    Compute-intensive GPU         Video transcoding
infra.com.acc.cfg.003 Programmable acceleration   Firmware-programmable adapter accelerator
infra.com.acc.cfg.004 GPU                         Compute-intensive GPU
infra.com.acc.cfg.005 FPGA/other acceleration H/W Firmware-programmable adapter
===================== =========================== ============================= ===================

**Table 5-9:** Virtual compute acceleration features

.. _virtual-storage-1:

Virtual storage
~~~~~~~~~~~~~~~


**Table 5-10** and **Table 5-11** depict the features and configurations related to virtual storage for the two
Cloud Infrastructure profiles.

================= ======================== ====== ===== ================
Reference         Feature                  Type   Basic High performance
================= ======================== ====== ===== ================
infra.stg.cfg.001 Catalogue storage types  Yes/No Y     Y
infra.stg.cfg.002 Storage block            Yes/No Y     Y
infra.stg.cfg.003 Storage with replication Yes/No N     Y
infra.stg.cfg.004 Storage with encryption  Yes/No Y     Y
================= ======================== ====== ===== ================

**Table 5-10:** Virtual storage features and configuration for the two profiles

**Table 5-11** depicts the features related to virtual storage acceleration.

===================== ========================= ====== ===== ================
Reference             Feature                   Type   Basic High performance
===================== ========================= ====== ===== ================
infra.stg.acc.cfg.001 Storage IOPS oriented     Yes/No N     Y
infra.stg.acc.cfg.002 Storage capacity oriented Yes/No N     N
===================== ========================= ====== ===== ================

**Table 5-11:** Virtual storage acceleration features.

.. _virtual-networking-1:

Virtual networking
~~~~~~~~~~~~~~~~~~


**Table 5-12** and **Table 5-13** depict the features and configurations related to virtual networking for the two types
of Cloud Infrastructure profiles.

+-------------------+----------------------+------------------------+-------------------------+------------------------+
| Reference         | Feature              | Type                   | Basic                   | High performance       |
+===================+======================+========================+=========================+========================+
| infra.net.cfg.001 | Connection point     | IO virtualisation      | virtio1.1               | virtio1.1\*            |
|                   | interface            |                        |                         |                        |
+-------------------+----------------------+------------------------+-------------------------+------------------------+
| infra.net.cfg.002 | Overlay protocol     | Protocols              | VXLAN, MPLSoUDP,        | VXLAN, MPLSoUDP,       |
|                   |                      |                        | GENEVE, other           | GENEVE, other          |
+-------------------+----------------------+------------------------+-------------------------+------------------------+
| infra.net.cfg.003 | NAT                  | Yes/No                 | Y                       | Y                      |
+-------------------+----------------------+------------------------+-------------------------+------------------------+
| infra.net.cfg.004 | Security group       | Yes/No                 | Y                       | Y                      |
+-------------------+----------------------+------------------------+-------------------------+------------------------+
| infra.net.cfg.005 | Service function     | Yes/No                 | N                       | Y                      |
|                   | chaining             |                        |                         |                        |
+-------------------+----------------------+------------------------+-------------------------+------------------------+
| infra.net.cfg.006 | Traffic patterns     | Yes/No                 | Y                       | Y                      |
|                   | symmetry             |                        |                         |                        |
+-------------------+----------------------+------------------------+-------------------------+------------------------+

**Table 5-12:** Virtual networking features and configuration for the two types of SW profiles

   **Note:** \* might have other interfaces (such as SR-IOV VFs to be directly passed to a VM or a Pod) or NIC-specific
   drivers on guest machines transiently allowed until mature enough solutions are available with a similar efficiency
   level (for example, regarding CPU and energy consumption).

===================== ============================= ========================== ===== ================
Reference             Feature                       Type                       Basic High performance
===================== ============================= ========================== ===== ================
infra.net.acc.cfg.001 vSwitch optimisation (DPDK)   Yes/No and SW optimisation N     Y
infra.net.acc.cfg.002 SmartNIC (for HW Offload)     Yes/No/Optional            N     Optional
infra.net.acc.cfg.003 Crypto acceleration           Yes/No/Optional            N     Optional
infra.net.acc.cfg.004 Crypto acceleration interface Yes/No/Optional            N     Optional
===================== ============================= ========================== ===== ================

**Table 5-13:** Virtual networking acceleration features

Cloud Infrastructure hardware profile description
-------------------------------------------------


The support of various workload types, each with different, and sometimes conflicting, compute, storage, and
network characteristics, including accelerations and optimizations, drives the need to aggregate these characteristics
as a hardware (host) profile and capabilities. A host profile is a “personality” assigned to a compute host (also
known as physical server, compute host, host, node, or pServer). The host profiles and related capabilities consist of
the intrinsic compute host capabilities, such as the number of CPU sockets, the number of cores per CPU, RAM, local
disks and their capacity, and so on, as well as capabilities enabled in the hardware/BIOS, specialized hardware, such
as accelerators, the underlay networking, and storage.

This chapter defines a simplified host, profile, and related capabilities model associated with each of the different 
Cloud Infrastructure hardware profile and related capabilities. The two :ref:`chapters/chapter02:profiles, profile 
extensions & flavours` (also known as host profiles, node profiles, and hardware profiles), and some of their
associated capabilities, are shown in :numref:`Cloud Infrastructure Hardware Profiles and host-associated capabilities`.


.. figure:: ../figures/RM-ch05-hw-profile.png
   :name: Cloud Infrastructure hardware profiles and host-associated capabilities
   :alt: Cloud Infrastructure hardware profiles and host-associated capabilities

   Cloud Infrastructure hardware profiles and host-associated capabilities

The profiles can be considered to be the set of Enhanced Performance Awareness (EPA)-related configurations on Cloud
Infrastructure resources.

   **Note:** In this chapter we will not list all of the EPA-related configuration parameters.


A given host can only be assigned a single host profile. A host profile can be assigned to multiple hosts. In addition
to the host profile, :ref:`chapters/chapter04:profiles and workload flavours`, and additional capability
specifications for the configuration of the host can be specified. Different cloud service providers (CSPs) may use
different naming standards for their host profiles. For the profiles to be configured, the architecture of the
underlying resource needs to be known.

============ ============================= ======= =================================== ======================
Ref          Cloud Infrastructure resource Type    Definition/Notes                    Capabilities reference
============ ============================= ======= =================================== ======================
infra.hw.001 CPU architecture              <value> Values such as x64, ARM, and so on. ``e.cap.020``
============ ============================= ======= =================================== ======================


The host profile properties are specified in the following subsections. The following diagram
(:numref:`Generic model of a compute host for use in Host Profile configurations`) represents a high-level
abstraction of a physical server (host).


.. figure:: ../figures/ch06_ref_hw_profile.PNG
   :name: Generic model of a compute host for use in host profile configurations
   :alt: Generic model of a compute host for use in host profile configurations

   Generic model of a compute host for use in host profile configurations

.. _cloud-infrastructure-hardware-profiles-features-and-requirements:

Features and requirements of the Cloud Infrastructure hardware profiles 
-----------------------------------------------------------------------


The configurations specified in this section are used to specify the hardware profile configurations for each of
the Cloud Infrastructure hardware profiles depicted in **Figure 5-4**.


Compute resources
~~~~~~~~~~~~~~~~~

+----------------------+---------------------------------+---------------------------------+-------------+-------------+
| Reference            | Feature                         | Description                     | Basic       | High        |
|                      |                                 |                                 |             | performance |
+======================+=================================+=================================+=============+=============+
| infra.hw.cpu.cfg.001 | Minimum number of CPU sockets   | This feature specifies the      | 2           | 2           |
|                      |                                 | minimum number of populated CPU |             |             |
|                      |                                 | sockets within each host (*).   |             |             |
+----------------------+---------------------------------+---------------------------------+-------------+-------------+
| infra.hw.cpu.cfg.002 | Minimum number of cores per CPU | This feature specifies the      | 20          | 20          |
|                      |                                 | number of cores needed per CPU  |             |             |
|                      |                                 | (*).                            |             |             |
+----------------------+---------------------------------+---------------------------------+-------------+-------------+
| infra.hw.cpu.cfg.003 | NUMA alignment                  | NUMA alignment is enabled and   | N           | Y           |
|                      |                                 | BIOS is configured to enable    |             |             |
|                      |                                 | NUMA.                           |             |             |
+----------------------+---------------------------------+---------------------------------+-------------+-------------+
| infra.hw.cpu.cfg.004 | Simultaneous Multithreading     | SMT is enabled, allowing each   | Y if SMT is | Y if SMT is |
|                      | (SMT)                           | core to work multiple streams   | supported   | supported   |
|                      |                                 | of data simultaneously.         |             |             |
+----------------------+---------------------------------+---------------------------------+-------------+-------------+

**Table 5-14:** Minimum sizing and capability configurations for general purpose servers

..

   (*) These specifications are for general purpose servers normally located in large data centres.
   Servers for specialised use with the data centres or other locations, such as at edge sites, are likely to have
   different specifications.



Compute acceleration hardware specifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================== =========================== =============== ===== ================ ======================
Reference            Feature                     Description     Basic High performance Capabilities reference
==================== =========================== =============== ===== ================ ======================
infra.hw.cac.cfg.001 GPU                         GPU             N     Optional         ``e.cap.014``
infra.hw.cac.cfg.002 FPGA/other acceleration HW  HW accelerators N     Optional         ``e.cap.016``
==================== =========================== =============== ===== ================ ======================

**Table 5-15:** Compute acceleration configuration specifications

Storage configurations
~~~~~~~~~~~~~~~~~~~~~~

========================== ================= ================= =========== ================
Reference                  Feature           Description       Basic       High performance
========================== ================= ================= =========== ================
infra.hw.stg.hdd.cfg.001\* Local storage HDD Hard disk drive
infra.hw.stg.ssd.cfg.002\* Local storage SSD Solid state drive Recommended Recommended
========================== ================= ================= =========== ================

**Table 5-16:** Storage configuration specification

   **Note:** \*These are specified local storage configurations including # and capacity of storage drives.

Network resources
~~~~~~~~~~~~~~~~~

NIC configurations
^^^^^^^^^^^^^^^^^^

==================== ========== ================================================ ===== ================
Reference            Feature    Description                                      Basic High performance
==================== ========== ================================================ ===== ================
infra.hw.nic.cfg.001 NIC ports  Total number of NIC ports available in the host. 4     4
infra.hw.nic.cfg.002 Port speed Port speed, in Gbps (minimum values).            10    25
==================== ========== ================================================ ===== ================

**Table 5-17:** Minimum NIC configuration specification

PCIe configurations
^^^^^^^^^^^^^^^^^^^

==================== ========== =========================================== ===== ================
Reference            Feature    Description                                 Basic High performance
==================== ========== =========================================== ===== ================
infra.hw.pci.cfg.001 PCIe slots Number of PCIe slots available in the host. 8     8
infra.hw.pci.cfg.002 PCIe speed                                             Gen 3 Gen 3
infra.hw.pci.cfg.003 PCIe lanes                                             8     8
==================== ========== =========================================== ===== ================

**Table 5-18:** PCIe configuration specifications

Network acceleration configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------+----------------+----------------------+----------+-------------+---------------+
| Reference            | Feature        | Description          | Basic    | High        | Capabilities  |
|                      |                |                      |          | performance | Reference     |
+======================+================+======================+==========+=============+===============+
| infra.hw.nac.cfg.001 | Crypto         | IPSec, Crypto.       | N        | Optional    | ``e.cap.009`` |
|                      | acceleration   |                      |          |             |               |
+----------------------+----------------+----------------------+----------+-------------+---------------+
| infra.hw.nac.cfg.002 | SmartNIC       | Offloads network     | N        | Optional    | ``e.cap.015`` |
|                      |                | functionality.       |          |             |               |
+----------------------+----------------+----------------------+----------+-------------+---------------+
| infra.hw.nac.cfg.003 | Compression    |                      | Optional | Optional    |               |
+----------------------+----------------+----------------------+----------+-------------+---------------+
| infra.hw.nac.cfg.004 | SR-IOV over    | SR-IOV               | N        | Optional    | ``e.cap.013`` |
|                      | PCI-PT         |                      |          |             |               |
+----------------------+----------------+----------------------+----------+-------------+---------------+
| infra.hw.nac.cfg.005 | Time Sensitive | Timing accuracy with | N        | Optional    | ``e.cap.027`` |
|                      | Networking     | PTP Hardware Clock   |          |             |               |
|                      |                | and synchronization  |          |             |               |
|                      |                | with SyncE.          |          |             |               |
+----------------------+----------------+----------------------+----------+-------------+---------------+

**Table 5-19:** Network acceleration configuration specification
