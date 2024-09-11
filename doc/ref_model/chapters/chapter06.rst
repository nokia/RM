External Interfaces
===================

Introduction to external interfaces
-----------------------------------

In the earlier sections in this document, the various resources and capabilities of the Cloud Infrastructure were
catalogued and the workloads profiled with respect to those capabilities. The intent behind this section and an
“API Layer” is to similarly provide a single place to catalogue, and thereby codify, a common set of open APIs to
access (that is, request, consume, control, and so on) the aforementioned resources, be they directly exposed to
the workloads, or purely internal to the Cloud Infrastructure.

This section and document also aim to ensure that the APIs adopted for the Cloud Infrastructure implementations
are open and not proprietary, in support of compatibility, component substitution, and the ability to realize the
maximum value from existing and future test heads and harnesses.

This section aims to catalogue the APIs.  It does not aim to reprint the APIs, as this would make the maintenance of
this section impractical and its length disproportionate within the Reference Model document. Instead, the APIs
selected for the Cloud Infrastructure implementations and specified in this section will be incorporated by reference
and URLs for the latest authoritative versions of the APIs, provided in the References section of this document.

Although this document does not attempt to reprint the APIs themselves, where appropriate and where the mapping of
the resources and capabilities within the Cloud Infrastructure to objects in the APIs would be otherwise ambiguous,
this section will provide explicit identification and mapping.

In addition to the raw or base-level Cloud Infrastructure functionality to API and object mapping, this section aims
to specify an explicit, normalized set of APIs and mappings to control the logical interconnections and relationships
between these objects, notably, but not limited to, support of Service Function Chaining (SFC) and other networking
and network management functionalities.

This section specifies the abstract interfaces (API, CLI, and so on) supported by the Cloud Infrastructure Reference
Model. The purpose of this section is to define and catalogue a common set of open (not proprietary) APIs, of the
following types:

- Cloud Infrastructure APIs: These APIs are provided to the workloads (that is, exposed), by the infrastructure, in
  order for workloads to access (that is, request, consume, control, and so on) Cloud Infrastructure resources.
- Intra-Cloud Infrastructure APIs: These APIs are provided and consumed directly by the infrastructure. These APIs are
  purely internal to the Cloud Infrastructure and are not exposed to the workloads.
- Enabler Services APIs: These APIs are provided by non-Cloud Infrastructure services and provide capabilities that are
  required for a majority of workloads, such as DHCP, DNS, NTP, DBaaS, and so on.

Cloud Infrastructure APIs
-------------------------

The Cloud Infrastructure APIs consist of sets of APIs that are externally and internally visible. The externally
visible APIs are made available for the orchestration and management of the execution environments that host the
workloads, while the internally visible APIs support actions on the hypervisor and the physical resources. The
ETSI NFV Reference MANO Architecture (:numref:`ETSI NFV architecture mapping`) shows a number of Interface points
where specific APIs, or sets of APIs, are supported. For the scope of the reference model, the relevant interface
points are shown in **Table 6-1**.

.. figure:: ../figures/ch09-etsi-nfv-architecture-mapping.png
   :name: ETSI NFV architecture mapping
   :alt: ETSI NFV architecture mapping

   ETSI NFV architecture mapping


+-----------+----------------+---------------------------------------+-------------------------------------------------+
| Interface | Cloud          | Interface between                     | Description                                     |
| point     | Infrastructure |                                       |                                                 |
|           | exposure       |                                       |                                                 |
+===========+================+=======================================+=================================================+
| Vi-Ha     | Internal NFVI  | Software layer and hardware resources | 1. Discover/collect the resources and their     |
|           |                |                                       | configuration information.                      |
|           |                |                                       | 2. Create an execution environment (for         |
|           |                |                                       | example, VM) for the workloads (VNF).           |
+-----------+----------------+---------------------------------------+-------------------------------------------------+
| Vn-Nf     | External       | NFVI and VM (VNF)                     | Here, VNF represents the execution environment. |
|           |                |                                       | The interface is used to specify the            |
|           |                |                                       | interactions between the VNF and the abstract   |
|           |                |                                       | NFVI accelerators. The interfaces can be used   |
|           |                |                                       | to discover, configure, and manage these        |
|           |                |                                       | accelerators, and for the VNF to register/      |
|           |                |                                       | deregister for receiving accelerator events and |
|           |                |                                       | data.                                           |
+-----------+----------------+---------------------------------------+-------------------------------------------------+
| NF-Vi     | External       | NFVI and VIM                          | 1. Discover/collect physical/virtual resources  |
|           |                |                                       | and their configuration information.            |
|           |                |                                       | 2. Manage (create, resize, suspend, unsuspend,  |
|           |                |                                       | reboot, and so on) physical/virtualised         |
|           |                |                                       | resources.                                      |
|           |                |                                       | 3. Configuration changes of physical/virtual    |
|           |                |                                       | resources.                                      |
|           |                |                                       | 4. Physical/Virtual resource configuration.     |
+-----------+----------------+---------------------------------------+-------------------------------------------------+
| Or-Vi     | External       | VNF orchestrator and VIM              | See below                                       |
+-----------+----------------+---------------------------------------+-------------------------------------------------+
| Vi-Vnfm   | External       | VNF manager and VIM                   | See below                                       |
+-----------+----------------+---------------------------------------+-------------------------------------------------+

**Table 6-1:** NFVI and VIM interfaces with other system components in the ETSI NFV architecture

The Or-Vi and Vi-Vnfm both specify interfaces provided by the VIM and are therefore related. The Or-Vi reference
point is used for exchanges between the NFV orchestrator and the VIM, and supports the interfaces listed below.
Virtualised resources refer to virtualised compute, storage, and network resources:

-  Software image management
-  Virtualised resources information management
-  Virtualised resources capacity management (only VNF orchestrator and VIM (Or-Vi))
-  Virtualised resources management
-  Virtualised resources change management
-  Virtualised resources reservation management
-  Virtualised resources quota management
-  Virtualised resources performance management
-  Virtualised resources fault management
-  Policy management
-  Network forwarding path (NFP) management (only VNF orchestrator and VIM (Or-Vi))

Tenant-level APIs
~~~~~~~~~~~~~~~~~

In the abstraction model of the Cloud Infrastructure (see **Chapter 3**), a conceptual model of a tenant represents
the slice of a cloud zone dedicated to a workload. This slice, the tenant, is composed of virtual resources being
utilized by workloads within that tenant. The tenant has an assigned quota of virtual resources. A set of users can
perform operations according to their assigned roles, and the tenant exists within a cloud zone. The APIs specify
the allowed operations on the tenant, including its component virtual resources. The different APIs can only be
executed by users with the appropriate roles. For example, a tenant may only be allowed to be created and deleted by
the cloud zone administrators, while the virtual compute resources could be allowed to be created and deleted by the
tenant administrators.

The creation of a workload in a tenant also requires APIs for the management (creation, deletion, and operation) of
the tenant, software flavours (see Chapter 5), operating system and workload images (“Images”), identity and
authorization (“Identity”), virtual resources, security, and the workload application (“stack”).

A virtual compute resource is created according to the flavour template, specifying the compute, memory, and local
storage capacity. It is launched using an image with access and security credentials. Once launched, it is referred to
as a virtual compute instance or simply “Instance”. Instances can be launched by specifying the compute, memory, and
local storage capacity parameters, instead of an existing flavour. Reference to flavours covers the situation where the
capacity parameters are specified. IP addresses and storage volumes can be attached to a running Instance.

+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Resource     |Create|List|Attach|Detach|Delete| Notes                                                                |
+==============+======+====+======+======+======+======================================================================+
| Flavour      | +    | +  |      |      | +    |                                                                      |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Image        | +    | +  |      |      | +    | Created and deleted by the appropriate administrators.               |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Key pairs    | +    | +  |      |      | +    |                                                                      |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Privileges   |      |    |      |      |      | Created and managed by the Cloud Service Provider (CSP)              |
|              |      |    |      |      |      | administrators.                                                      |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Role         | +    | +  |      |      | +    | Created and deleted by authorized administrators where roles are     |
|              |      |    |      |      |      | assigned privileges and mapped to the users in scope.                |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Security     | +    | +  |      |      | +    | Created and deleted only by the VDC administrators.                  |
| groups       |      |    |      |      |      |                                                                      |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Stack        | +    | +  |      |      | +    | Created and deleted by VDC users with the appropriate role.          |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Virtual      | +    | +  | +    | +    | +    | Created and deleted by VDC users with the appropriate role.          |
| storage      |      |    |      |      |      |                                                                      |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| User         | +    | +  |      | +    | +    | Created and deleted only by the VDC administrators.                  |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Tenant       | +    | +  |      | +    | +    | Created and deleted only by the Cloud Zone administrators.           |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Virtual      | +    | +  |      | +    | +    | Created and deleted by VDC users with the appropriate role.          |
| compute      |      |    |      |      |      | Additional operations include suspend and unsuspend.                 |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+
| Virtual      | +    | +  | +    | +    | +    | Created and deleted by VDC users with the appropriate role.          |
| network      |      |    |      |      |      |                                                                      |
+--------------+------+----+------+------+------+----------------------------------------------------------------------+

**Table 6-2:** API types for a minimal set of resources

**Table 6-2** specifies a minimal set of operations for a minimal set of resources that are needed to orchestrate
the workloads. The APIs for the listed operations are specified in the Reference Architectures. Each listed
operation can have a number of associated APIs with a different set of parameters. For example, create a virtual
resource using an image or a device.

Hardware acceleration interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Acceleration Interface Specifications**
ETSI GS NFV-IFA 002 :cite:p:`etsigsnfvifa002` defines a technology- and implementation-independent virtual accelerator,
and the accelerator interface requirements and specifications that would allow a workload to leverage a virtual
accelerator. The virtual accelerator is modelled on extensible para-virtualised devices (EDP).
ETSI GS NFV-IFA 002 :cite:p:`etsigsnfvifa002` specifies the architectural model in Chapter 4 and the abstract interfaces
for management, configuration, monitoring, and data exchange in Chapter 7.

ETSI NFV-IFA 019 3.1.1 :cite:p:`etsinfvifa019` has defined a set of technology-independent interfaces for acceleration
resource lifecycle management. These operations allow allocation, release, and querying of acceleration resources, get
and reset statistics, subscribe/unsubscribe (terminate) to fault notifications, notify (only used by NFVI), and get
alarm information.

These acceleration interfaces are summarized here in Table 6.3 for your convenience only.



+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| Request               | Response               | From, | Type   | Parameter     | Description                        |
|                       |                        | To    |        |               |                                    |
+=======================+========================+=======+========+===============+====================================+
| InitAccRequest        | InitAccResponse        | VNF → | Input  | accFilter     | The accelerator subsystems to      |
|                       |                        | NFVI  |        |               | initialize and retrieve their      |
|                       |                        |       |        |               | capabilities.                      |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Filter | accAttributeS | The attribute names of the         |
|                       |                        |       |        | elector       | accelerator capabilities.          |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Output | accCapabiliti | The acceleration subsystem         |
|                       |                        |       |        | es            | capabilities.                      |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| RegisterForAccEventRe | RegisterForAccEventRes | VNF → | Input  | accEvent      | The event in which the VNF is      |
|                       |                        |       |        |               | interested.                        |
| quest                 | ponse                  | NFVI  +--------+---------------+------------------------------------+
|                       |                        |       | Input  | vnfEventHandl | The handler for the NFVI to use    |
|                       |                        |       |        | erId          | when notifying the VNF of the      |
|                       |                        |       |        |               | event.                             |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| AccEventNotificationR | AccEventNotificationRe | NFVI  | Input  | vnfEventHandl | The handler used by the VNF        |
| equest                | sponse                 | → VNF |        | erId          | registering for this event.        |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Input  | accEventMetaD |                                    |
|                       |                        |       |        | ata           |                                    |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| DeRegisterForAccEvent | DeRegisterForAccEventR | VNF → | Input  | accEvent      | The event from which the VNF is    |
| Request               | esponse                | NFVI  |        |               | deregistering.                     |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| ReleaseAccRequest     | ReleaseAccResponse     | VNF → |        |               |                                    |
|                       |                        | NFVI  |        |               |                                    |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        | VNF → | Input  | accConfigurat | The configuration data for the     |
|                       |                        | NFVI  |        | ionData       | accelerator.                       |
| ModifyAccConfiguratio | ModifyAccConfiguration |       +--------+---------------+------------------------------------+
| nRequest              | Response               |       | Input  | accSubSysConf | The configuration data for the     |
|                       |                        |       |        | igurationData | accelerator subsystem.             |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        |       | Input  | accFilter     | The filter for the subsystems from |
|                       |                        |       |        |               | which the configuration data is    |
|                       |                        |       |        |               | requested.                         |
|                       |                        |       +--------+---------------+------------------------------------+
| GetAccConfigsRequest  | GetAccConfigsResponse  | VNF → | Input  | accConfigSele | The attributes of the              |
|                       |                        |       |        | ctor          | configuration types.               |
|                       |                        | NFVI  +--------+---------------+------------------------------------+
|                       |                        |       | Output | accConfigs    | The configuration information      |
|                       |                        |       |        |               | (only for the specified            |
|                       |                        |       |        |               | attributes) for the specified      |
|                       |                        |       |        |               | subsystems.                        |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        |       | Input  | accFilter     | The filter for the subsystems for  |
|                       |                        | VNF → |        |               | which the configuration is to be   |
|                       |                        |       |        |               | reset.                             |
| ResetAccConfigsReque  | ResetAccConfigsRespon  | NFVI  +--------+---------------+------------------------------------+
| st                    | se                     |       | Input  | accConfigSele | The attributes of the              |
|                       |                        |       |        | ctor          | configuration types whose values   |
|                       |                        |       |        |               | will be reset.                     |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        |       | Input  | accData       | The data (metadata) sent to        |
|                       |                        |       |        |               | the accelerator.                   |
|                       |                        |       +--------+---------------+------------------------------------+
| AccDataRequest        | AccDataResponse        | VNF → | Input  | accChannel    | The channel to which the data is   |
|                       |                        |       |        |               | to be sent.                        |
|                       |                        | NFVI  +--------+---------------+------------------------------------+
|                       |                        |       | Output | accData       | The data from the accelerator.     |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| AccSendDataRequest    | AccSendDataResponse    | VNF → | Input  | accData       | The data (metadata) sent to the    |
|                       |                        | NFVI  |        |               | accelerator.                       |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Input  | accChannel    | The channel to which the data is   |
|                       |                        |       |        |               | to be sent.                        |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        |       | Input  | maxNumberOfDa | The maximum number of data items   |
|                       |                        |       |        | taItems       | to be received.                    |
|                       |                        |       +--------+---------------+------------------------------------+
| AccReceiveDataRequest | AccReceiveDataResponse | VNF → | Input  | accChannel    | Channel data is requested from the |
|                       |                        |       |        |               | accelerator.                       |
|                       |                        | NFVI  +--------+---------------+------------------------------------+
|                       |                        |       | Output | accData       | Data is received from the          |
|                       |                        |       |        |               | accelerator.                       |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| RegisterForAccDataAva | RegisterForAccDataAvai | VNF → | Input  | regHandlerId  | Registration identifier.           |
| ilableEventRequest    | lableEventResponse     | NFVI  +--------+---------------+------------------------------------+
|                       |                        |       | Input  | accChannel    | Channel where the event is         |
|                       |                        |       |        |               | requested.                         |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| AccDataAvailableEvent | AccDataAvailableEventN | NFVI  | Input  | regHandlerId  | Reference used by the VNF when     |
| NotificationRequest   | otificationResponse    | → VNF |        |               | registering for the event.         |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| DeRegisterForAccDataA | DeRegisterForAccDataAv | VNF → | Input  | accChannel    | Channel related to the event.      |
| vailableEventRequest  | ailableEventResponse   | NFVI  |        |               |                                    |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        |       | Input  | attachTarget  | The resource to which the          |
|                       |                        |       |        | Info          | accelerator is to be attached      |
|                       |                        |       |        |               | (for example, VM).                 |
|                       |                        |       +--------+---------------+------------------------------------+
| AllocateAccResourceRe | AllocateAccResourceRes | VIM → | Input  | accResourceI  | Accelerator information.           |
| quest                 | ponse                  | NFVI  |        | nfo           |                                    |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Output | accResourceId | ID, if successful.                 |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| ReleaseAccResourceReq | ReleaseAccResourceResp | VIM → | Input  | accResourceId | ID of the resource to be released. |
| uest                  | onse                   | NFVI  |        |               |                                    |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        |       | Input  | hostId        | ID of the specified host.          |
|                       |                        |       +--------+---------------+------------------------------------+
| QueryAccResourceReque | QueryAccResourceRespon | VIM → | Input  | Filter        | Specifies the accelerators to      |
| st                    | se                     | NFVI  |        |               | which the query applies.           |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Output | accQueryResu  | Details of the accelerators        |
|                       |                        |       |        | lt            | matching the input filter located  |
|                       |                        |       |        |               | in the selected host.              |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        |       | Input  | accFilter     | Accelerator subsystems from which  |
|                       |                        |       |        |               | data is requested.                 |
|                       |                        |       +--------+---------------+------------------------------------+
| GetAccStatisticsReque | GetAccStatisticsRespon | VIM → | Input  | accStatSelect | Attributes of AccStatistics whose  |
| st                    | se                     | NFVI  |        | or            | data is returned.                  |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Output | accStatistics | Statistics data of the             |
|                       |                        |       |        |               | accelerators matching the input    |
|                       |                        |       |        |               | filter located in the selected     |
|                       |                        |       |        |               | host.                              |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| ResetAccStatisticsReq | ResetAccStatisticsResp | VIM → | Input  | accFilter     | Accelerator subsystems for which   |
| uest                  | onse                   | NFVI  |        |               | the data is to be reset.           |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Input  | accStatSelect | Attributes of AccStatistics whose  |
|                       |                        |       |        | or            | data will be reset.                |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        |       | Input  | hostId        | ID of the specified host.          |
|                       |                        |       +--------+---------------+------------------------------------+
| SubscribeRequest      | SubscribeResponse      | VIM → | Input  | Filter        | Specifies the accelerators and     |
|                       |                        | NFVI  |        |               | the related alarms. The filter can |
|                       |                        |       |        |               | include accelerator information,   |
|                       |                        |       |        |               | severity of the alarm, and so on.  |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Output | Subscriptio   | Identifier of the successfully     |
|                       |                        |       |        | nId           | created subscription.              |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| UnsubscribeRequest    | UnsubscribeResponse    | VIM → | Input  | hostId        | ID of the specified host.          |
|                       |                        | NFVI  +--------+---------------+------------------------------------+
|                       |                        |       | Input  | Subscription  | Identifier of the subscription to  |
|                       |                        |       |        | Id            | be unsubscribed.                   |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| Notify                |                        | NFVI  |        |               | NFVI notifies an alarm to VIM.     |
|                       |                        | → VIM |        |               |                                    |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        |       | Input  | hostId        | ID of the specified host.          |
|                       |                        |       +--------+---------------+------------------------------------+
| GetAlarmInfoRequest   | GetAlarmInfoResponse   | VIM → | Input  | Filter        | Specifies the accelerators and     |
|                       |                        | NFVI  |        |               | the related alarms. The filter can |
|                       |                        |       |        |               | include accelerator information,   |
|                       |                        |       |        |               | severity of the alarm, and so on.  |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Output | Alarm         | Information about the alarms, if   |
|                       |                        |       |        |               | the filter matches an alarm.       |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
| AccResourcesDiscovery | AccResourcesDiscoveryR | VIM → | Input  | hostId        | ID of the specified host.          |
| Request               | esponse                | NFVI  +--------+---------------+------------------------------------+
|                       |                        |       | Output | discoveredAcc | Information on the acceleration    |
|                       |                        |       |        | ResourceInfo  | resources discovered within the    |
|                       |                        |       |        |               | NFVI.                              |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+
|                       |                        |       | Input  | accResourceId | Identifier of the chosen           |
|                       |                        |       |        |               | accelerator in the NFVI.           |
|                       |                        |       +--------+---------------+------------------------------------+
| OnloadAccImageRequest | OnloadAccImageResponse | VIM → | Input  | accImageInfo  | Information about the acceleration |
|                       |                        | NFVI  |        |               | image.                             |
|                       |                        |       +--------+---------------+------------------------------------+
|                       |                        |       | Input  | accImage      | The binary file of the             |
|                       |                        |       |        |               | acceleration image.                |
+-----------------------+------------------------+-------+--------+---------------+------------------------------------+

**Table 6-3:** Hardware acceleration interfaces in the ETSI NFV architecture

Intra-Cloud Infrastructure interfaces
-------------------------------------

Hypervisor hardware interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table 6-1 lists a number of NFVI and VIM interfaces, including the internal VI-Ha interface. The VI-Ha interface allows
the hypervisor to control the physical infrastructure. The hypervisor acts under VIM control. The VIM issues all
requests and responses using the NF-VI interface. Requests and responses include commands, configuration requests,
policies, updates, alerts, and response to infrastructure results. The hypervisor also provides information about the
health of the physical infrastructure resources to the VM. All these activities, on behalf of the VIM, are performed by
the hypervisor using the VI-Ha interface. While no abstract APIs have yet been defined for this internal VI-Ha
interface, ETSI GS NFV-INF 004 :cite:p:`etsigsnfvinf004` defines a set of requirements and details of the information
that is required by the VIM from the physical infrastructure resources. Hypervisors utilize various programs to get this
data, including BIOS, IPMI, PCI, I/O Adapters/Drivers, and so on.

Enabler services interfaces
---------------------------

In order to function properly, an operational cloud needs a set of standard services. These services comprise NTP for
time synchronization, DHCP for IP address allocation, DNS for obtaining IP addresses for domain names, and LBaaS
(version 2) to distribute incoming requests amongst a pool of designated resources.
