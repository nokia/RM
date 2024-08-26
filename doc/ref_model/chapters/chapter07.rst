Security
========

Introduction
------------

Security vulnerabilities and attack vectors are everywhere. The telecom industry and its cloud infrastructures are
especially vulnerable to potential attacks due to the ubiquitous nature of the infrastructures and services, combined
with the vital role telecommunications play in the modern world. The attack vectors are many and varied, ranging
from the potential for exposure of sensitive data, both personal and corporate, to weaponized disruption to the
global telecommunications networks. These threats can take the form of physical attacks on the locations where the
infrastructure hardware is housed, to network attacks, such as denial of service and targeted corruption of the
network service applications themselves. Whatever the source, a Cloud Infrastructure needs to be able to withstand
attacks in whatever form they take.

This chapter examines multiple aspects of security, as it relates to cloud infrastructure and security aspects for
workloads. After discussing security attack vectors, this chapter delves into the security requirements. Regarding
security requirements and best practices, specifications and documents are published by standards organisations. A
selection of standards of interest for cloud infrastructure security is listed in a dedicated section. This chapter
culminates with a consolidated set of requirements recommendations. It is suggested that operators carefully evaluate
the recommendations for possible implementation.

Potential attack vectors
------------------------

Previously, attacks designed to place and migrate workloads outside the legal boundaries were not possible using the
traditional infrastructure, due to the closed nature of these systems. However, using cloud infrastructure, violation
of regulatory policies and laws becomes possible by actors diverting or moving an application from an authenticated and
legal location to a potentially illegal location. The consequences of violating regulatory policies may take the
form of a complete banning of service and/or an exaction of a financial penalty by a governmental agency or through SLA
enforcement. Such vectors of attack may be the original intention of the attacker in an effort to harm the service
provider. One possible attack scenario is when an attacker exploits the insecure NF API to dump personal data records
from the database, in an attempt to violate user privacy. Cloud infrastructure operators should ensure that the APIs are
secure and accessible over a secure network (transport layer security or TLS), under strict set of security best practices
and RBAC policies to limit exposure of this vulnerability.

Typical cloud-associated attacker tactics have been identified in the widely accepted
MITRE ATT&CK® Framework :cite:p:`ATT&CK®`. This framework provides a systematic approach to capture adversarial tactics targeting cloud
environments. Examples of such adversarial tactics are listed in the following table.

+------------------+---------------------------------------------------------------------------------------------------+
| Attacker tactics | Examples                                                                                          |
+==================+===================================================================================================+
| Initial access   | Compromising user administration accounts that are not protected by multifactor authentication.   |
+------------------+---------------------------------------------------------------------------------------------------+
| Evasion          | Modifying cloud compute instances in the production environment by modifying virtual instances    |
|                  | for the staging of attacks.                                                                       |
+------------------+---------------------------------------------------------------------------------------------------+
| Discovery        | Discovering which cloud services are operating and then disabling them at a later stage.          |
+------------------+---------------------------------------------------------------------------------------------------+
| Data             | Moving data from the compromised tenant’s production databases to the hacker’s cloud service      |
| exfiltration     | account, or transferring data out of the communication service provider (CSP) to the attacker's   |
|                  | private network.                                                                                  |
+------------------+---------------------------------------------------------------------------------------------------+
| Service impact   | Creating denial-of-service availability issues by modifying the Web Application Firewall (WAF)    |
|                  | rules and compromising APIs and web-based GUIs.                                                   |
+------------------+---------------------------------------------------------------------------------------------------+

**Table 7-1:** Examples of cloud attacker tactics

Security scope
--------------

In-scope and out-of-scope definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The scope of the requirements of the security controls maps to the scope of the Reference Model architecture.

Cloud infrastructure requirements must cover the virtual infrastructure layer and the hardware infrastructure layer,
including virtual resources, hardware resources, the virtual infrastructure manager, and the hardware infrastructure
manager, as described in Chapter 3.

High-level security requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following diagram shows the different security domains that impact the Reference Model:

.. :name: Reference Model Security Domains
.. figure:: ../figures/ch7_security_posture.png
   :alt: "Reference Model Security Domains"

   Reference Model Security Domains

..note::

  "Platform" refers to the cloud infrastructure, with all its hardware and software components.

Platform security requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At a high level, the following areas/requirements cover platform security for a particular deployment:

- Platform certification.
- Secure access controls for administrators.
- A secure API interface for tenants.
- Encryption for all external and control communications.
- Strong separation between tenants, ensuring network, data, memory, and runtime process (CPU running core)
  isolation between tenants.
- Authenticated/secure APIs provided to overlay network administrators.
- Platform change control on hardware.
- Templated approved changes for automation where available.
- Typically well-defined security framework documentation, including approved deployment use cases.
- Infrastructure software update processes.

Workload security requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At a high level, the following areas/requirements cover workload security for a particular deployment:

- Certification up to platform level.
- Requirement of each workload network to undertake it own security self-assessment and accreditation, and not inherit a
  security accreditation from the platform.
- Potentially automated service activation.
- The workload owner owns the workload security certification process.
- The workload owner owns the workload design change process.
- The workload owner owns the workload software update process.

Common security standards
~~~~~~~~~~~~~~~~~~~~~~~~~

The Cloud Infrastructure Reference Model and the supporting architectures are not only required to optimally support
networking functions. They must also be designed, from inception, with common security principles and standards. These
best practices must be applied at all layers of the infrastructure stack and across all points of interconnection
(internal or with outside networks), APIs, and contact points with the NFV network functions overlaying or interacting
with that infrastructure.

A good place to start to understand the security requirements is to use the following widely accepted definitions and
core principles developed by the Open Web Application Security Project (OWASP):

- Confidentiality: only allow access to data which the user is permitted to view.
- Integrity: ensure the data has not been tampered with or altered by unauthorised users.
- Availability: ensure the systems and data are available to authorised users when they need it.

These three principles are complemented for cloud infrastructure security by authenticity. Authenticity refers to the
ability to confirm that the users are valid and have the correct rights to access the systems or data.

Standards organisations with recommendations and best practices, and certifications that need to be taken into
consideration, include the following examples. This is not an exhaustive list, it contains only some of the more
important standards in current use.

- Center for Internet Security - :cite:p:`center-for-internet-security`

- Cloud Security Alliance - :cite:p:`cloud-security-alliance`

- Open Web Application Security Project - :cite:p:`open-web-application-security-project`

- The National Institute of Standards and Technology (NIST), with the following special publications:

  - NIST SP 800-123 Guide to General Server Security :cite:p:`guide-to-general-server-security`

  - NIST SP 800-204A Building Secure Microservices-based Applications Using Service-Mesh Architecture :cite:p:`building-secure-microservices-based-applications-using-service-mesh-architecture`

  - NIST SP 800-204B `Attribute-based Access Control for Microservices-based Applications Using a Service Mesh`__ :cite:p:`attribute-based-access-control-for-microservices-based-applications-using-a-service-mesh`

  - NIST SP 800-207 `Zero Trust Architecture`__ :cite:p:`zero-trust-architecture`

  - NIST SP 800-218 `Secure Software Development Framework (SSDF)`__ :cite:p:`secure-software-development-framework`

- FedRAMP Certification :cite:p:`fedRAMP-certification`

- ETSI Cyber Security Technical Committee (TC CYBER) - :cite:p:`ETSI-cyber-security-technical-committee`

- `ETSI Industry Specification Group Network Functions Virtualisation (ISG NFV)`__ :cite:p:`eTSI-industry-specification-group-network-functions-virtualisation` and its Security Working Group NFV-SEC

- The International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC) - :cite:p:`the-international-organization-for-standardization`. The following ISO standards are of particular interest for NFVI:

  - ISO/IEC 27002:2013 and ISO/IEC 27001: these are the international standards for best-practice information security
    management systems (ISMSs).
  - ISO/IEC 27032: this is the international standard focusing explicitly on cybersecurity.
  - ISO/IEC 27035: this is the international standard for incident management.
  - ISO/IEC 27031: this is the international standard for ICT readiness for business continuity.

In the mobile network field, the GSM Association (`GSMA`__ :cite:p:`gSMA`) and its Fraud and Security working group
of experts have developed a set of documents specifying how to secure the global mobile ecosystem.

- The document “Baseline Security controls”, `FS.31 v2.0`__ :cite:p:`gsmafs31`, published in February 2020, is a practical guide intended for operators and
  stakeholders to check mobile network’s internal security. It lists a set of security controls from business controls
  (including security roles, organizational policies, business continuity management, and so on) to technological controls
  (for user equipment, networks, operations, and so on), covering all areas of mobile network, including Cloud Infrastructure.
  A checklist of questions allows the operator to improve the security of a deployed network.
- The document "Network Equipment Security Assurance Scheme – Development and Lifecycle Security Requirements" :cite:p:`gsmafs16`,
  is part of a set of documents that aim to build a security assurance scheme for network equipment. Focusing on critical controls,
  it defines a set of requirements to be met by the vendors' development and product lifecycle processes.

The GSMA security activities are currently focused on 5G services and the new challenges posed by the virtualisation of network
functions and by open-source software. The following two documents are in the scope of cloud infrastructure security:

- The white paper `“Open Networking & the Security of Open Source Software deployment” `__ :cite:p:`gsmaopensourcesecurity`,
  deals with open-source software security. It highlights the importance of layered security defences and lists
  recommendations and security concepts that are able to secure deployments.
- The “5G Security Guide” :cite:p:`gsmafs40` (non-binding Permanent Reference Document), covers 5G security in a holistic way,
  from user equipment to networks. This document describes the new security features in 5G. It includes a dedicated section on
  the impact of the cloud on 5G security, with recommendations on virtualisation, cloud-native applications, and containerisation
  security.

Cloud infrastructure security
-----------------------------

General platform security
~~~~~~~~~~~~~~~~~~~~~~~~~

The security certification of the platform typically needs to be the same as, or higher than, the workload requirements.

The platform supports the workload, and in effect controls access to the workload to and from the external endpoints,
such as carriage networks used by workloads, by data centre operations staff supporting the workload, or by tenants
accessing workloads. From an access security perspective, the following diagram shows where the different access controls
operate within the platform to provide access controls throughout the platform.

.. :name: Reference Model Access Controls
.. figure:: ../figures/ch7-data-access-model.png
   :alt: "Reference Model access controls"

   Reference Model access controls

High-level functions of access controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **MGMT ACCESS CONTROLS** - These provide platform access to workloads for service management. Typically, all management
  and control-plane traffic is encrypted.
- **DATA ACCESS CONTROLS** - These control the east-west traffic between workloads and control of north-south traffic
  between the network function (NF) and other platform services, such as front-end carriage networks and platform services.
  Inherently strong separation between tenants is mandatory.
- **SERVICES ACCESS CONTROLS** - These protect the platform services from any platform access.
- **BACK-END ACCESS CONTROLS** - These provide data centre operations access to the platform, and subsequently, the
  workloads. Typically, stronger authent,ication, such as Two-Factor Authentication (2FA), is required, as well as the use
  of technologies, such as Role-Based Access Control (RBAC) and encryption. Application Programming Interface (API)
  gateways may be required for automated/script-driven processes.
- **FRONT-END ACCESS CONTROLS** - These protect the platform from malicious carriage network access and provide
  connectivity for specific workloads to specific carriage networks. Carriage networks are those networks that are
  provided as public networks and are operated by carriers, in this case with interfaces that are usually subnetworks or
  virtual networks.
- **TENANT ACCESS CONTROLS** - These provide appropriate tenant access controls to specific platform services and tenant
  workloads. These controls include Role-Based Access Control (RBAC), authentication controls as appropriate for the
  access arrangement, and Application Programming Interface (API) gateways for automated/script-driven processes.

General security requirements for the cloud infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**System hardening**

- Adhering to the principle of least privilege, there is no login to the root on any platform systems when root
  privileges are not required.

..note::

    Platform systems are those systems that are associated with the platform. They include systems that directly
    or indirectly affect the viability of the platform.

- Ensure that all the platform's components, including hypervisors, VMs, and so on, are kept up to date with the
  latest patch.
- To tightly control access to resources and protect them from malicious access and introspection, Linux
  Security Modules, such as SELinux, should be used to enforce access rules.

**Vulnerability management**

- Security defects must be reported.
- The Cloud Infrastructure components must be continuously analysed from deployment to runtime. The cloud infrastructure
  must offer tools to check the code libraries and all other code against the
  `Common Vulnerabilities and Exposures (CVE) databases`__ :cite:p:`common-vulnerabilities-and-exposures` to identify the presence of any
  known vulnerabilities. The CVE is a list of publicly disclosed vulnerabilities and exposures that is maintained by
  `MITRE`__ :cite:p:`mITRE`. Each vulnerability is characterised by an identifier, a description, a date, and
  comments.
- When a vulnerability is discovered on a component (from operating systems to virtualisation layer components), the
  remediation action depends on its severity. The `Common Vulnerability Scoring System (CVSS)`__ :cite:p:`common-vulnerability-scoring-system` allows you to calculate a vulnerability score. It is an open framework widely used in
  vulnerability management tools. The CVSS is owned and managed by the Forum of Incident Response and Security Teams
  (FIRST). The CVSS consists of three metric groups: base, temporal, and environmental. The base metrics produce a score
  ranging from 0 to 10. This score can then be refined using temporal and environmental metrics. The numerical score can
  be translated into a qualitative representation of the severity: low, medium, high, or critical. The severity score
  (or the associated qualitative representation) allows organisations to prioritise the remediation activities, with high
  scores mandating a fast response time. The vulnerable components must then be patched or replaced, or their access must
  be restricted.
- Security patches must be obtained from an authorised source, to ensure their integrity. Patches must be tested and
  validated in a preproduction environment before being deployed into production.

**Platform access**

- Restrict traffic only to traffic that is necessary, and deny all other traffic, including traffic to and from the
  backend.
- Provide protections between the internet and the workloads, including web and volumetrics attack preventions.
- All host-to-host communications within the cloud provider network are to be cryptographically protected in transit.
- Use cryptographically protected protocols for administrative access to the platform.
- Data centre operations staff and systems must use management protocols that limit security risk, such as SNMPv3,
  SSH v2, ICMP, NTP, syslog, and TLS v1.2 or higher.
- Processes for managing platform access control filters must be documented, followed, and monitored.
- Role-Based Access Control (RBAC) must apply to all access to platform systems.
- All access to APIs, including backend APIs, must use the TLS protocol.

**Security hardware assist for data in use**

- Server hardware architectures offer various technologies to assist with protecting data in use. The following table
  categorizes such technologies.

+----------------------+----------------------+-------------------------+----------------------+-----------------------+
| HW technology        | Which security       | Where it must be        | How to operationally | How to assure benign  |
|                      | threat it mitigates  | enabled                 | activate             | workloads are run     |
+======================+======================+=========================+======================+=======================+
| Memory encryption on | Protects data going  | Server HW and BIOS.     | Configure BIOS. On   | Performed by          |
| the level of the     | between the CPU and  |                         | virtualised software | application           |
| whole physical       | the memory DIMMs.    |                         | infrastructure label | scheduling using      |
| server.              |                      |                         | nodes to influence   | node labels.          |
|                      |                      |                         | scheduling.          |                       |
|                      |                      |                         |                      |                       |
+----------------------+----------------------+-------------------------+----------------------+-----------------------+
| Memory encryption on | HW-protected data    | Server HW, BIOS, and    | Configure BIOS and   | Remote attestation    |
| the level of the     | between the VMs.     | hypervisor and guests   | hypervisor. On       | of the freshly spun   |
| VMs.                 |                      | (paravirtualised        | virtualised software | up VM, to provide     |
|                      |                      | generally only in the   | infrastructure label | measurements of the   |
|                      |                      | guest BIOS).            | nodes to influence   | VM and of the         |
|                      |                      | Attestation if          | scheduling.          | platform patch level. |
|                      |                      | assurance of workload   |                      |                       |
|                      |                      | is required.            |                      |                       |
+----------------------+----------------------+-------------------------+----------------------+-----------------------+
| Secure enclaves      | HW-protected         | Server HW and BIOS,     | Configure the BIOS   | Remote attestation of |
| within application.  | specific application | hypervisor if used,     | and the hypervisor,  | freshly spun up       |
|                      | code and data in     | device plugin if        | if used. If          | enclave, to provide   |
|                      | memory, from         | Kubernetes is used, and | Kubernetes is used,  | measurements of the   |
|                      | processes running at | in application.         | then the pod         | enclave and of the    |
|                      | higher privilege     | Attestation if          | descriptor requests  | platform patch level. |
|                      | levels, such as OS   | assurance of workload   | for such resources.  |                       |
|                      | or hypervisor.       | required.               |                      |                       |
+----------------------+----------------------+-------------------------+----------------------+-----------------------+

- Using computing accelerators, such as FPGA or GPU, that are connected via an I/O link, such as PCI Express, breaks
  the confidentiality property, unless HW-assisted encryption of the I/O transfers, runtime encryption of the
  accelerated workload, and attestation of the accelerated workload can be guaranteed.

**Workload security**

- Restrict traffic to and from the workload only to traffic that is necessary, and deny all other traffic.
- Support zoning within a tenant workload using application-level filtering.
- Do not expose tenant-internal IP address details to another tenant.
- All production workloads must be separated from all non-production workloads, including separation between
  non-hosted non-production external networks.

**Confidentiality and integrity**

- All data persisted to primary, replica, or backup storage is to be encrypted.

**Monitoring and security audit**

- All platform security logs are to be time-synchronised.
- Logs are to be regularly scanned for events of interest.
- The cloud services must be regularly tested for vulnerability and penetration.

**Platform provisioning and LCM**

- A platform change management process that is documented, properly communicated to staff and tenants, and rigorously
  followed.
- A process to check change management adherence that is implemented and rigorously followed.
- An approved system or process for last-resort access must exist for the platform.
- Where there are multiple hosting facilities used in the provisioning of a service, network communications between the
  facilities for the purpose of backup, management, and workload communications are cryptographically protected in
  transit between data centre facilities.
- Continuous cloud security compliance is mandatory.
- An incident response plan must exist for the platform.

Platform backend access security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Validate and verify the integrity of the resources management requests coming from a higher orchestration layer to
  the cloud infrastructure manager.

Platform frontend access security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Frontend network security at the application level is the responsibility of the workload. However, the platform
  must ensure the isolation and integrity of tenant connectivity to frontend networks.
- The frontend network may provide Distributed Denial Of Service (DDoS) support.

Infrastructure as a Code security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Infrastructure as a Code (IaaC), alternatively known as Infrastructure as Code (IaC), refers to the software used
for the declarative management of the cloud infrastructure resources. To dynamically address user requirements,
release features incrementally, and deliver more speedily, DevSecOps teams use best practices, including continuous
integration and delivery, and integrate information security controls and scanning tools into these processes, with
with the aim of providing timely and meaningful feedback. This includes identifying vulnerabilities and security
policy violations. With these automated security testing and analysis capabilities, it is of critical value in
detecting vulnerabilities early and maintaining a consistent security policy.

Because of the high complexity of modern Telco cloud infrastructures, even minor IaaC code changes could
disproportionately and sometimes disastrously affect downstream security and privacy. Therefore, the integration of
security testing into the IaaC software development pipeline requires security activities to be automated using
security tools, and integrated with the native DevOps and DevSecOps tools and procedures.

The DevSecOps Automation best practices advocate, among other things, the implementation of a framework for security
automation and programmatic execution, as well as the monitoring of security controls to identify, protect, detect,
respond, and recover from cyber threats. The framework used for IaaC security is based on the joint publication of
the Cloud Security Alliance (CSA) and SAFECode,
"`The Six Pillars of DevSecOps: Automation (2020)`__"
:cite:p:`safecodesixpillarsdevsecops`. This document uses the base definitions and constructs from
`ISO 27000`__ :cite:p:`isoiec270002018`, and the CSA's
`Information Security Management through Reflexive Security`__ :cite:p:`csaeflexivesec`.

The framework identifies the following five distinct stages:

1. Secure design and architecture.
2. Secure coding (developer IDE and code repository).
3. Continuous build, integration, and testing.
4. Continuous delivery and deployment.
5. Continuous monitoring and runtime defence.

Triggers and checkpoints define transitions within stages. When designing DevSecOps security processes, it should be
borne in mind that when a trigger condition is met, one or more security activities is activated. The outcomes of these
security activities need to determine whether or not the requirements of the process checkpoint are satisfied. If the
outcome of the security activities meets the requirements, the next set of security activities is performed as the
process transition to the next checkpoint, or, alternatively, to the next stage, if the checkpoint is the last one in
the current stage. If, however, the outcome of the security activities does not meet the requirements, then the
process should not be allowed to advance to the next checkpoint. In
":ref:`chapters/chapter07:consolidated security requirements`", the IaaC security activities are presented as security
requirements mapped to particular stages and trigger points.

Security of production and non-production environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Telecommunications operators often focus their security efforts on the production environments actively used by their
customers or their employees, or both. This is critical because a breach of these systems can seriously damage the
company and its customers. In addition, production systems often contain the most valuable data, making them attractive
targets for intruders. However, an insecure non-production (development and testing) environment can also create real
problems because they may leave a company open to corporate espionage, sabotage by competitors, and theft of sensitive
data.

Security is about mitigating risk. If operators do not have the same level of security in their non-production
environments compared to production, then an additional level of risk may be introduced. This is especially true if
such non-production environments accept outside connections (for example, for suppliers or partners, which is quite
normal in complex Telco ecosystems). There is a need to monitor the security of these non-production environments. The
gold standard, therefore, is to implement the same security policies in production and non-production infrastructure.
This would reduce risk and typically simplify operations by using the same control tools and processes. However, for
practical reasons, some of the security monitoring rules may differ. As an example, if a company maintains a separate,
isolated environment for infrastructure software development experimentation, the configuration monitoring rules may
be relaxed, in comparison with the production environment, where such experimentation is not allowed. Therefore, in
this document, when dealing with such dilemmas, the focus has been placed on those non-production security requirements
that must be on the same level as in the production environment (typically of **must** type), leaving relaxed
requirements (typically of **should** or **may**) in cases where there is no such necessity.

In the context of contemporary telecommunications technology, the cloud infrastructure typically is considered
Infrastructure as a Code (IaaC). This fact implies that many aspects of code-related security automatically apply to
IaaC. Security aspects of IaaC in the Telco context are discussed in
":ref:`chapters/chapter07:infrastructure as a code security`", which introduces the relevant framework for security
automation and programmatic execution, as well as monitoring of security controls. Organisations need to identify which
of the stages, or activities within these stages, should be performed within the non-production versus production
environments. This mapping will then dictate which security activities defined for particular stages and triggers
(such as vulnerability tests, patch testing, and penetration tests) are mandatory, and which can be regarded as
discretionary.

Workload security and vendor responsibility
-------------------------------------------

Software hardening
~~~~~~~~~~~~~~~~~~

- There must be no hard-coded credentials or clear text passwords in the code and images. The software must support
  configurable or industry-standard password complexity rules.
- The software should be independent of the infrastructure platform (no OS point release dependencies to patch).
- The software must be code-signed. All individual subcomponents are assessed and verified for End-user License
  Agreement (EULA) violations.
- The software should have a process for discovery, classification, communication, and timely resolution of security
  vulnerabilities (that is, bumg bounty, penetration testing/scan findings, and so on).
- The software should support recognised encryption standards. Encryption should be decoupled from the software.
- The software should have support for configurable banners to display authorised use criteria/policies.

Port protection
~~~~~~~~~~~~~~~

- Unused software and unused network ports should be disabled by default.

Software code quality and security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Vendors should use industry-recognized software testing suites.

  - Static and dynamic scanning.
  - Automated static code review with remediation of medium/high/critical security issues. The tool used for static
    code analysis, and analysis of the code being released, must be shared.
  - Dynamic security tests with remediation of medium/high/critical security issues. The tool used for dynamic
    security analysis of code being released must be shared.
  - Penetration tests (pen tests) with remediation of medium/high/critical security issues.
  - The methodology for ensuring that security is included in the Agile/DevOps delivery lifecycle for ongoing
    feature enhancement/maintenance.

Alerting and monitoring
~~~~~~~~~~~~~~~~~~~~~~~

- Security event logging: all security events must be logged, including informational events.
- Privilege escalation must be detected.

Logging
~~~~~~~

-  Logging output should support customizable log retention and log rotation.

Workload security: cloud infrastructure operator responsibility
----------------------------------------------------------------

The operator’s responsibility is not only to make sure that security is included in all the vendor-supplied
infrastructure and NFV components, but also to maintain the security functions from an operational and
management perspective. This includes, but is not limited to, securing the following elements:

- Maintaining standard security operational management methods and processes.
- Monitoring and reporting functions.
- Processes to address regulatory compliance failures.
- Support for appropriate incident response and reporting.
- Methods to support appropriate remote attestation certification of the validity of the security components,
  architectures, and methodologies used. This can include the automated TLS certificate lifecycle management for workloads:

  - Accept signing requests for certificates,
  - Generate and manage private keys and Certificate Signing Requests (CSRs),
  - Manage renewal before expiry.

Remote attestation/OpenCIT
~~~~~~~~~~~~~~~~~~~~~~~~~~

Cloud infrastructure operators must ensure that remote attestation methods are used to remotely verify the trust status
of a given cloud infrastructure platform. The concept is based on boot integrity measurements leveraging the Trusted
Platform Module (TPM) built into the underlying hardware. Remote attestation can be provided as a service. It may be
used by the platform owner or by a customer to verify that the platform has booted in a trusted manner. Practical
implementations of the remote attestation service include the Open Cloud Integrity Tool (OpenCIT). OpenCIT provides
‘Trust’ visibility of the cloud infrastructure. It enables compliance in cloud datacenters by establishing the root
of trust, and builds a chain of trust across hardware, operating system, hypervisor, virtual machines, and containers.
It includes asset tagging for location and boundary control. The platform trust and asset tag attestation information
is used by orchestrators and/or policy compliance management to ensure workloads are launched on trusted and location-
or boundary-compliant platforms. They provide the necessary visibility and auditability of infrastructure in both
public and private cloud environments.

Workload image
~~~~~~~~~~~~~~

Only workload images from trusted sources may be used. Secrets must be stored outside the images.

It is easy to tamper with workload images. It requires only a few seconds to insert some malware into a workload image
file while it is being uploaded to an image database or transferred from an image database to a compute node. To guard
against this danger, workload images must be cryptographically signed and verified during launch time. This can be
achieved by setting up a signing authority and modifying the hypervisor configuration to verify an image’s signature
before it is launched.

To implement image security, the workload operator must test the image and the supplementary components, to verify that
everything conforms to the security policies and best practices. The use of image scanners, such as OpenSCAP or Trivy,
to determine security vulnerabilities is recommended.

CIS hardened images should be used whenever possible. CIS provides, for example, virtual machine hardened images based
on CIS benchmarks for various operating systems. Another best practice is to use minimalist base images whenever
possible.

Images are stored in registries. The images registry must contain vetted images only. The registry must remain a source
of trust for images over time. Images must therefore be continuously scanned to identify vulnerabilities and out-of-date
versions, as described previously. Access to the registry is an important security risk. It must be granted by a
dedicated authorisation process and through secure networks that enforce authentication, integrity, and confidentiality.

Networking security zoning
~~~~~~~~~~~~~~~~~~~~~~~~~~

Network segmentation is important for ensuring that applications can only communicate with those applications with
which they are supposed to communicate. To prevent a workload from impacting other workloads or hosts, it is good
practice to separate workload traffic and management traffic. This prevents attacks by VMs or containers breaking
into the management infrastructure. It is also best to separate the VLAN traffic into appropriate groups and disable
all other VLANs that are not in use. Likewise, workloads of similar functionalities can be grouped into specific zones
and their traffic isolated. Each zone can be protected using access control policies and a dedicated firewall based on
the required security level.

It is recommended to set network security policies following the principle of least privileged, only allowing
approved protocol flows. For example, set 'default deny' for inbound flows and add the approved policies required for
the functioning of the application running on the NFV infrastructure.

Volume encryption
~~~~~~~~~~~~~~~~~

Virtual volume disks associated with workloads may contain sensitive data. Therefore, they need to be protected.
It is best practice is to secure the workload volumes by encrypting them and storing the cryptographic keys in safe
locations. Encryption functions rely on a cloud infrastructure internal key management service. Be aware that the
decision to encrypt the volumes might cause reduced performance. Therefore, the decision to encrypt needs to be
dependent on the requirements of the given infrastructure. The Trusted Platform Module (TPM) module can also be used
to store these keys securely. The hypervisor should also be configured to securely erase the virtual volume disks,
in the event of application crashes, or in case it is intentionally destroyed to protect it from unauthorized access.

For sensitive data encryption, when data sovereignty is required, an external Hardware Security Module (HSM) should
be integrated, in order to protect the cryptographic keys. A HSM is a physical device which manages and stores
secrets. Usage of an HSM strengthens the security of the secrets. For 5G services, GSMA FASG recommends the
implementation of an HSM to secure the storage of the Universal Integrated Circuit Card (UICC) credentials.

Root of trust for measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following sections define the mechanisms to ensure the integrity of the infrastructure pre-boot and post-boot
(running). The following definitions detail a set of terms used in those sections.

- The hardware root of trust helps with the pre-boot and post-boot security issues.
- The Unified Extensible Firmware Interface (UEFI) adheres to standards defined by an industry consortium. Vendors
  (hardware and software) and solution providers collaborate to define common interfaces, protocols, and structures
  for computing platforms.
- The Platform Configuration Register (PCR) is a memory location in the TPM that is used to store TPM Measurements
  (hash values generated by the SHA-1 standard hashing algorithm). The PCRs are cleared only on TPM reset. UEFI
  defines 24 PCRs, of which the first 16, PCR 0 - PCR 15, are used to store measures created during the UEFI boot
  process.
- The Root of Trust for Measurement (RTM) is a computing engine that is capable of making integrity measurements.
- The Core Root of Trust for Measurements (CRTM) is a set of instructions executed when performing an RTM.
- Platform Attestation provides proof of validity of the platform’s integrity measurements. For details, see
  ":ref:`chapters/chapter07:remote attestation/opencit`".

Values stored in a PCR cannot be reset (or forged), as they can only be extended. Whenever a measurement is sent to a
TPM, the hash of the concatenation of the current value of the PCR and the new measurement is stored in the PCR. The PCR
values are used to encrypt data. If the proper environment is not loaded, which will result in different PCR values, the
TPM will be unable to decrypt the data.

Static Root of Trust for Measurement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Static Root of Trust for Measurement (SRTM) begins with measuring and verifying the integrity of the BIOS firmware.
It then measures additional firmware modules, verifies their integrity, and adds each component’s measure to an SRTM
value. The final value represents the expected state of the boot path loads. The SRTM stores the results as one or more
values stored in PCR storage. In the SRTM, the CRTM resets PCRs 0 to 15 only at boot.

Using a Trusted Platform Module (TPM) as a hardware root of trust, measurements of platform components, such as
firmware, bootloader, and OS kernel, can be securely stored and verified. Cloud infrastructure operators should ensure
that the TPM support is enabled in the platform firmware, so that the platform measurements are correctly recorded
during boot time.

A simple process works in the following way:

1. The BIOS CRTM (Bios Boot Block) is executed by the CPU and is used to measure the BIOS firmware.
2. The SHA1 hash of the result of the measurement is sent to the TPM.
3. The TPM stores this new result hash by extending the currently stored value.
4. The hash comparisons can validate settings, as well as the integrity of the modules.

Cloud infrastructure operators should ensure that OS kernel measurements can be recorded by using a TPM-aware
bootloader (for example, tboot, (see :cite:p:`trusted-boot`)
or shim, (see :cite:p:`shim`)), which can extend the root
of trust up to the kernel level.

The validation of the platform measurements can be performed by the TPM’s launch control policy (LCP) or through
the remote attestation server.

Dynamic Root of Trust for Measurement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the Dynamic Root of Trust for Measurement (DRTM), the RTM for the running environment is stored in the PCRs
starting with PCR 17.

If a remote attestation server is used to monitor platform integrity, the operators should ensure that the
attestation is performed periodically or in a timely manner. Additionally, platform monitoring can be extended to
monitor the integrity of the static file system at run-time by using a TPM-aware kernel module, such as Linux
Integrity Measurement Architecture (IMA). For details, see :cite:p:`integrity-measurement-architecture`. Alternatively,
you can use the trust policies functionality of OpenCIT.
See :cite:p:`open-CIT-3.2-product-guide` for details.

The static file system includes a set of important files and folders which do not change between reboots during the
platform's lifecycle. This allows the attestation server to detect any tampering with the static file system during
the platform's runtime.

Zero Trust Architecture
~~~~~~~~~~~~~~~~~~~~~~~

The sections ":ref:`chapters/chapter07:remote attestation/opencit`" and
":ref:`chapters/chapter07:root of trust for measurements`" provide
methods to ensure the integrity of the infrastructure. The Zero Trust concept goes a step further, by enabling
the operator to build secure by design cloud infrastructure, from hardware to applications. The adoption of
Zero Trust principles mitigates the threats and attacks within an enterprise, a network, or an infrastructure,
thereby ensuring a fine grained segmentation between each component of the system.

Zero Trust Architecture (ZTA), as described in `NIST SP 800-207 publication`__ :cite:p:`nistsp800207`, assumes there is no implicit trust granted to assets or
user accounts, whatever their location or ownership. The Zero Trust approach focuses on protecting all types of resources:
data, services, devices, infrastructure components, and virtual and cloud components. Trust is never granted implicitly,
and must be evaluated continuously.

The ZTA principles applied to the cloud infrastructure components are as follows:

- The adoption of least privilege configurations.
- The requirement of authentication and authorization for each entity, service, or session.
- Fine-grained segmentation.
- Separation of the control plane and the data plane.
- Secure internal and external communications.
- The continuous monitoring, testing, and analysing of security.

Zero Trust principles should also be applied to cloud-native applications. With the increasing use of these applications,
which are designed with microservices and deployed using containers as packaging and Kubernetes as an orchestrator, the
security of east-west communications between components must be carefully addressed. The use of secured communication
protocols brings a first level of security. However, considering each component as non-trustworthy will minimize the risk
for applications to be compromised. A good practice is to implement the proxy-based service mesh. This will provide a
framework to build a secured environment for microservices-based applications, offering services such as service
discovery, authentication and authorisation policies enforcement, network resilience, and security monitoring
capabilities. The two documents,
`NIST SP 800-204A`__ :cite:p:`NIST-SP-800-204A` \ (Building Secure
Microservices-based Applications Using Service-Mesh Architecture) and
`NIST SP 800-204B`__ :cite:p:`NIST-SP-800-204B` \ (Attribute-based Access Control for
Microservices-based Applications Using a Service Mesh), describe service mesh, and provide guidance for the deployment
of service mesh components.

Software supply chain security
------------------------------

Software supply chain attacks are increasing worldwide and can cause serious damage. Many enterprises and
organisations are experiencing these threats. Aqua Security's experts estimated that `software supply chain attacks`__ :cite:p:`aqua-security`.
Reuters reported in August 2021 that the `ransomware affecting Kaseya Virtual System Administration product`__ :cite:p:`kaseya-ransomware`
caused downtime for over 1500 companies. In the case of the `backdoor inserted in codecov software`__ :cite:p:`codecov-hackers`,
hundreds of customers were affected. The SolarWinds attack detailed in `Defending against SolarWinds attacks`__ :cite:p:`solarWinds-supply`
is another example of how software suppliers are targeted and, by rebound, their customers affected.
Open-source code weaknesses can also be exploited by attackers. The
`Log4J`__ :cite:p:`apache-Log4j` vulnerability, impacting many
applications, is a recent example in this field. When addressing cyber security, the vulnerabilities of the
software supply chain are often not taken into account. Some governments are already alerting and requesting
actions to face these risks. The British government is hardening the law and standards of cyber security for
the supply chain. The US government requested actions to enhance software supply chain security. The security
of the software supply chain is a challenge also pointed out by the European Network and Information Security
Agency, ENISA, in its report `NFV Security in 5G - Challenges and Best Practices`__ :cite:p:`apache-Log4j`.


Software security
~~~~~~~~~~~~~~~~~

Software supply chain security is crucial and is made complex by the greater attack surface provided by the
many different supply chains in virtualised, containerised, and edge environments.
All software components must be trusted, from commercial software and open-source
code to proprietary software, as well as the integration of these components.
The SAFECode white paper `"Managing Security Risks Inherent in the Use of Third-party Components"`__ :cite:p:`managing-Security` provides
a detailed risk management approach.

To secure the software code, the following methods must be applied:

-  Use best practices coding, such as design pattern, recommended in the `Twelve-Factor App`__ :cite:p:`twelve-factor-app`
   or `OWASP`__ :cite:p:`secure-coding-practices`.
-  Perform threat modelling, as described in the `"Tactical Threat Modeling"`__ :cite:p:`tactical-threat-modeling` document, published by SAFECode.
-  Use trusted, authenticated, and identified software images that are provided by authenticated software
   distribution portals.
-  Require suppliers to provide a Software Bill of Materials to identify all the components parts of their product's
   software releases with their dependencies, and eventually identify the open-source modules.
-  Test the software in a pre-production environment to validate integration.
-  Detect vulnerabilities using security tools scanning and Common Vulnerabilities and Exposures (CVE), and apply
   remediation actions according to their severity ratings.
-  Report and remove vulnerabilities by upgrading components using authenticated software update distribution portals.
-  Actively monitor the open-source software repositories to determine if new versions have been released that address
   identified vulnerabilities discovered in the community.
-  Secure the integration process by securing the software production pipeline.
-  Adopt a DevSecOps approach and rely on testing automation throughout the software build, integration, delivery,
   deployment, and runtime operation to perform automatic security checks, as described in ”Infrastructure
   as a Code Security”.

Open-source software security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open-source code is present in cloud infrastructure software from BIOS and host operating systems to virtualisation
layer components. The most obvious is represented by Linux, KVM, QEMU, OpenStack, and Kubernetes. Workloads
components can also be composed of open-source code. The proportion of open-source code to an application source code
can vary. It can be partial or total, visible or invisible. Open-source code can be upstream code coming directly
from open-source public repositories, or code within a commercial application or network function.

The strength of open-source code is the availability of code source developed by a community which maintains and
improves it. Integration of open-source code with application source code helps to develop and produce applications
faster. This could, however, introduce security risks if a risk management DevSecOps approach is not implemented.
The GSMA white paper  `"Open Networking & the Security of Open Source Software Deployment - Future Networks"`__ :cite:p:`open-networking`
highlights these risks and addresses the challenges coming with open-source code usage. Among the security risks are
poor code quality containing security flaws, an obsolete code with known vulnerabilities, and the lack of knowledge
of the branch activity of the open-source communities. An active branch comes with bugs fixes. This is not the case
with an inactive branch. The GSMA white paper develops means to mitigate these security issues.

Poor code quality is a risk factor. One advantage of open-source code is its transparency. Code can be inspected using
tools with various capabilities, such as open-source software discovery, and static and dynamic code analysis.

Each actor in the whole chain of software production must use a dedicated internal isolated repository separated from
the production environment to store vetted open-source content. This content can include images, as well as the
installer and utilities. These software packages must be signed and the signature must be verified prior to the
installation of the packages or images. Access to the repository must be granted by a dedicated authorization. The
code must be inspected and vulnerabilities identified as described previously. After the software has been validated,
it can be moved to the appropriate production repository.

Software Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure software security, it is crucial to identify the software components and their origins. The
Software Bill of Materials (SBOM), described by the US National Telecommunications and Information Administration
`US NTIA`__ :cite:p:`USNTIA`, is a recommended tool for identifying software
components. The SBOM is an inventory of software components and the relationships between them. The NTIA describes
how to establish an SBOM and provides SBOM standard data formats. In the event of vulnerability being detected in a
component, the SBOM inventory is an effective means of identifying the impacted component and of enabling
remediation.

A transparent software supply chain offers benefits for the remediation of vulnerabilities. It also offers benefits
for licensing management and provides assurance of the source and integrity of the components. To achieve and
benefit from this transparency, a shared model must be supported by industry. This is the goal of the work
performed by the US Department of Commerce and the National Telecommunications and Information Administration (NTIA)
and published, in the report `"The Minimum Elements for a Software Bill of Materials (SBOM)"`__ :cite:p:`the-minimum-elements`, in July 2021. This document gives
guidance and specifies the minimum elements for the SBOM as a starting point.

A piece of software can be modelled as a hierarchical tree with components and subcomponents. Each
component should have its SBOM, including, as a baseline, the information detailed in the following table.


+------------------------------+---------------------------------------------------+
| **Data field**               | Description                                       |
+==============================+===================================================+
| **Supplier name**            | The name of an entity that creates, defines, and  |
|                              | identifies the components.                        |
+------------------------------+---------------------------------------------------+
| **Component name**           | The designation assigned to a unit of software    |
|                              | defined by the original supplier.                 |
+------------------------------+---------------------------------------------------+
| **Component version**        | The identifier used by the supplier to specify a  |
|                              | change in the software from a previously          |
|                              | identified version.                               |
+------------------------------+---------------------------------------------------+
| **Other unique identifiers** | Other identifiers that are used to identify a     |
|                              | component, or to serve as a look-up key for       |
|                              | relevant databases.                               |
+------------------------------+---------------------------------------------------+
| **Dependency relationship**  | Characterization of the relationship that an      |
|                              | upstream component X is included in software Y.   |
+------------------------------+---------------------------------------------------+
| **Author of SBOM data**      | The name of the entity that creates the SBOM data |
|                              | for this component.                               |
+------------------------------+---------------------------------------------------+
| **Timestamp**                | The record of the date and time of the SBOM data  |
|                              | assembly.                                         |
+------------------------------+---------------------------------------------------+

**Table 7-2**: SBOM components of the data fields. (Source:
`NTIA`__ :citr:p:`ntia`)

For more details about each data field, see the NTIA SBOM document. Examples of commonly used identifiers are
provided.

To use SBOMs efficiently and encourage their widespread adoption, information must be generated and shared in a
standard format. This format must be machine-readable, to allow automation. Proprietary formats should not be used.
Multiple data formats exist covering baseline SBOM information. The three key formats, Software Package Data
eXchange (SPDX), CycloneDX, and Software Identification Tags (SWID tags), are interoperable for the core data
fields and use common data syntax representations.

- `SPDX`__ :cite:p:`spdx` is an open-source machine-readable format developed under the umbrella of the Linux
  Foundation. `SPDX specification 2.2`__ :cite:p:`spdx-specification-2.2` has been published as the standard
  ISO/IEC 5962:2021. It provides a language for communicating the data, licenses, copyrights, and security
  information associated with software components. With SPDX specification 2.2, multiple file formats are available:
  YAML, JSON, RDF/XML, tag\:value flat text, and xls spreadsheets.

- `CycloneDX`__ :cite:p:`cycloneDX` was designed in 2017 for use with the Open Web Application Security Project
  (OWASP) Dependency-Track tool, an open-source component analysis platform that identifies risk in the software
  supply chain. CycloneDX supports a wide range of software components, including applications, containers,
  libraries, files, firmware, frameworks, and operating systems. The CycloneDX project provides standards in XML,
  JSON, and Protocol Buffers, as well as a large collection of official and community supported tools that create or
  interoperate with the standard.

- `SWID Tags`__ :cite:p:`swid-tags` is an international XML-based standard used by commercial
  software publishers. It has been published as the standard ISO/IEC 19770-2. The specification defines four types
  of SWID tags: primary, patch, corpus, and supplemental, to describe a software component.

The SBOM should be integrated into the operations of the secure development lifecycle, especially for vulnerabilities
management. It should also evolve in time. When a software component is updated, a new SBOM must be created. The
elements described in this section are part of an ongoing effort. Improvements, such as SBOM integrity and
authenticity, will be added in the future.

Vulnerability identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability management must be continuous: from development to runtime, not only on the development process, but
during the entire life of the application, workload, or service. When a public vulnerability on a component is
released, an update of the component must be triggered. When an SBOM recording the code composition is provided,
the affected components are easier to identify. It is essential to remediate the affected components as soon as
possible, because the vulnerability can be exploited by attackers who can exploit code weaknesses.

The CVE and the CVSS must be used to identify vulnerabilities and their severity rating. The CVE identifies,
defines, and catalogues publicly disclosed cybersecurity vulnerabilities. The CVSS is an open framework to
calculate the severity rating of the vulnerabilities.

Image scanning tools, including open-source tools such as Clair or Trivy, are useful for auditing images for
security vulnerabilities. The results of a vulnerabilities scan audit must be analysed carefully when it is applied
to a vendor offering packaged solutions. As patches are not detected by scanning tools, some components can be
detected as obsolete.

.. _testing--certification:

Testing and certification
-------------------------

Testing demarcation points
~~~~~~~~~~~~~~~~~~~~~~~~~~

It is not enough simply to secure all the potential points of entry and hope for the best. Any cloud infrastructure
architecture must be able, as much as possible, to be tested and confirmed to be protected from attack. The ability
to continuously test the infrastructure for vulnerabilities is critical for maintaining the highest possible level
of security. Testing needs to be done both from the inside and the outside of the systems and networks. Below is a
sample of some of the available testing methodologies and frameworks.

- OWASP testing guide
- Penetration Testing Execution Standard, PTES
- Technical Guide to Information Security Testing and Assessment, `NIST 800-115`__ :cite:p:`NIST-800-115`
- Vulnerability Assessment Framework for Cloud Computing (VULCAN), IEEE 2013
- Penetration Testing Framework, VulnerabilityAssessment.co.uk
- Information Systems Security Assessment Framework (ISSAF)
- Open Source Security Testing Methodology Manual (OSSTMM)
- FedRAMP Penetration Test Guidance (US Only)
- CREST Penetration Testing Guide

Ensuring that the security standards and best practices are incorporated into the cloud infrastructure and
architectures must be a shared responsibility. The telecommunications operators interested in building and
maintaining the infrastructures in support of their services, the application vendors developing the network
services to be used by the operators, and the cloud infrastructure vendors creating the infrastructures for
their telecommunications customers must all be responsible for performing this task. Each party needs to
incorporate security and testing components, and maintain operational processes and procedures to address
any security threats or incidents in an appropriate manner. Each of the stakeholders needs to contribute
to the creation of effective security for the cloud infrastructure.

Certification requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~

Security certification should encompass the following elements:

- Security test cases executed and test case results.
- Industry standard compliance achieved (NIST, ISO, PCI, FedRAMP Moderate, and so on).
- Output and analysis from automated static code reviews, dynamic tests, and penetration tests with
  remediation of medium, high, and critical security issues. Tools used for the security testing of software
  that is being released must be shared.
- Details of unremediated low-severity security issues must be shared.
- Threat models performed during the design phase. This includes remediation summaries to mitigate threats
  identified.
- Details of unremediated low-severity security issues.
- Any additional security and privacy requirements implemented in the software deliverable beyond the
  default rules used by security analysis tools.
- Execution of resiliency tests, such as hardware failures or power failure tests.


Cloud infrastructure regulatory compliance
------------------------------------------
Evolving cloud adoption in the telecom industry, now encroaching on its inner sanctum of network services,
brings many benefits for the network operators and their partners, and ultimately to the consumers of
the telecommunication services. However, it also brings major compliance challenges. The telecommunication
industry players can mitigate these challenges by arming themselves with information about which laws they
need to comply with, why they need to comply with them, and how they can do this.

The costs of non-compliance can be heavy. Organisations may not only have to contend with hefty fines and
possible lawsuits, but they may also end up damaging their reputation and, consequently, losing customers,
which would, in turn, adversely affect revenues and profitability.

Compliance means that an operator’s systems, processes, and workflows align with the requirements mandated by the
regulatory regimes imposed by the relevant  governmental and industry regulatory bodies. The need for compliance
extends to the cloud. Therefore, operators must ensure that any data that is stored in their cloud infrastructure,
as well as data that is transferred to and from it, complies with all the relevant data protection laws, including
data residency and privacy laws.

To comply with the laws that apply to an operator’s business, the correct security controls need to be applied. The
applicable laws have specific rules and constraints about how companies can collect, store, and process data in
the cloud. To satisfy these constraints and ensure compliance, the telecom operators should work with their cloud
providers and other partners to implement tight controls. To speed up this process, the operators may start from
augmenting their existing  cybersecurity and information security frameworks to guide their security programs to
implement controls to secure their cloud infrastructure and to achieve regulatory compliance. This process can also
be assisted by support from the cloud providers and from third parties, who can offer their well-proven compliance
offerings, resources, audit reports, dashboards, and ecertain security controls as a service.

After implementing these controls, companies need to train their employees and partners to use the controls properly,
to protect data and maintain the required compliance posture. This is a critical requirement to maintain compliance
by enforcing relevant security guidelines in all aspects of everyday operations, as well as for ensuring a process
of regular assessment of the compliance posture.

Due to the localised nature of the regulatory regimes, this document may not provide any specific compliance
requirements.  However, some examples provided below may help in an operator’ compliance considerations.

Commonly used (in many jurisdictions) compliance audit reports are based on the SOC 2 report from the System and
Organization Controls (SOC) suite of services, standardised by the American Institute of Certified Public
Accountants (AICPA) and meant for service organizations, such as cloud providers. See
`AICPA SOC`__ :cite:p:`AICPA` for
details. A SOC 2 report shows whether the cloud provider has implemented the security controls required to comply
with the AICPA’s five “trust services criteria”: security, availability, confidentiality, processing integrity,
and privacy. Operators should request a SOC 2 report from their cloud  providers (public or internal to their
organisations). SOC 2 comprises two types: type 1 and type 2. A type 1 report shows the status and suitability
of the provider’s controls at a particular moment. A type 2 report shows the operational effectiveness of
these controls over a certain period. In cases where a cloud provider is not willing to share an SOC 2 report
because it may contain sensitive information, operators can ask for an SOC 3 report. This is intended as a
general-use report, but can still help to assess the provider’s compliance posture.

Some cloud providers also provide attestations (or, in the case of the private cloud, telecoms should seek
such attestations) to show which of their cloud services have achieved compliance with different frameworks,
such as SOC, but also commonly used frameworks, such as OWASP, ISAE, NIST, ETSI, and the ISO 27000 series,
as well as more geographically localised standard frameworks such as NIST (as used in the U.S.A.), ENISA,
GDPR, and ISM.

The use of the ISO 2700s, OWASP, ISAE, NIST, and ETSI security frameworks for the cloud infrastructure is
referenced in the Common Security Standards and Compliance with Standards sections.

Examples of regulatory frameworks are presented below. It is intended to expand this list of examples in
future releases to cover more jurisdictions and to accommodate changes in the rapidly evolving security and
regulatory landscape.


United States of America (U.S.A.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the United States, the Federal Communications Commission `(FCC)`__ :cite:p:`fcc` regulates
interstate and international communications by radio, television, wire, satellite, and cable in all 50 states,
the District of Columbia, and all U.S. overseas territories. The FCC is an independent U.S. government agency
overseen by Congress. The Commission is the federal agency responsible for implementing and enforcing
America’s communications laws and regulations.

National Institute of Standards and Technology
`(NIST) Cybersecurity Framework`__ :cite:p:`nist-cyberframework`,
compliance is mandatory for the supply chain for all U.S. federal government agencies. Because this framework
references globally accepted standards, guidelines, and practice, telecom organisations in the U.S.A. and
worldwide can use it to efficiently operate in a global environment and manage new and evolving cybersecurity
risks in the cloud adoption area.


European Union (EU)
~~~~~~~~~~~~~~~~~~~

The overall telecommunications regulatory framework in the European Union (EU) is provided in
`The European Electronic Communications Code`__ :cite:p:`the-european-electronic`.

The European Union Agency for Cybersecurity `(ENISA)`__ :cite:p:`ENISA` contributes to EU cyber
policy, enhances the trustworthiness of Information and Communications Technology (ICT) products, services,
and processes with cybersecurity certification schemes, cooperates with Member States and EU bodies, and helps
Europe prepare for the cyber challenges of tomorrow. In particular, ENISA performs risk assessments of cloud
computing and works on the European Cybersecurity Certification Scheme
`(EUCS)`__ :cite:p:`EUCS` for Cloud Services, which
looks into the certification of the cybersecurity of cloud services.

The General Data Protection Regulation `(GDPR)`__ :cite:p:`GDPR` is a set of EU regulations that govern
how data should be protected for EU citizens. It affects organisations that have EU-based customers, even if
these organisations are not themselves based in the EU.


United Kingdom (UK)
~~~~~~~~~~~~~~~~~~~

The Office of Communications `(Ofcom)`__ :cite:p:`Ofcom` is the regulator and competition authority
for the UK communications industries. It regulates the television and radio sectors, fixed-line telecoms,
mobiles, postal services, and the airwaves over which wireless devices operate.

The Security of Networks and Information Systems
`NIS Regulations in UK`__ :cite:p:`NIS`,
provides legal measures to boost the level of security (both cyber and physical resilience) of network and
information systems for the provision of essential services and digital services.

The UK’s National Cyber Security Centre `(NCSC)`__ :cite:p:`NCSC` acts as a bridge between industry
and government. It provides a unified source of advice, guidance, and support on cyber security, including the
management of cyber security incidents. From this perspective, it is critical for cloud-related security in the
UK telecommunications industry. The NCSC is not a regulator. Within the general UK cyber security regulatory
environment, including both NIS and GDPR, the NCSC’s aim is to operate as a trusted, expert, and impartial
advisor to all interested parties. The NCSC supports Security of Networks & Information Systems (NIS)
Regulations.

Data protection in UK is controlled by
`Data Protection Act 2018`__ :cite:p:`data-protection`, which is UK’s
implementation of the EU's General Data Protection Regulation (GDPR).

Australia
~~~~~~~~~

In Australia, the telecommunication sector is regulated by the
`Australian Competition & Consumer Commission (ACCC)`__ :cite:p:`accc`.
The ACCC is responsible for the economic regulation of the communications sector. This includes telecommunications, the
National Broadband Network (NBN), and the broadcasting and content sectors.

From the point of view of cloud services security, the
`Information Security Manual (ISM)`__ :cite:p:`ism`,
produced by the Australian Cyber Security Centre (ACSC), is of particular importance. The purpose of the ISM is to outline
a cyber security framework that organisations can apply, using their risk management framework, to protect their information
and systems from cyber threats. The ISM is intended for Chief Information Security Officers, Chief Information Officers,
cyber security professionals, and information technology managers. While in general the ISM provides guidelines rather than
mandates, several security controls are, by law, mandatory for cloud-based services used by the Australian telecommunications
operators, in situations involving strategically important data and/or services.

Australia regulates data privacy and protection through a mix of federal, state, and territory laws. The federal
`Privacy Act 1988`__ :cite:p:`privacy-act-1988` (currently under review by the Australian
Government) and the Australian Privacy Principles (APPs), contained in the Privacy Act, regulate the handling of
personal information by relevant entities and under the Privacy Act. The Privacy Commissioner has the authority to conduct
investigations, including its own motion investigations, to enforce the Privacy Act and to seek civil penalties for serious
and egregious breaches, or for repeated breaches of the APPs where an entity has failed to implement remedial efforts.



Consolidated security requirements
----------------------------------

System hardening
~~~~~~~~~~~~~~~~

+-----------------+--------------------------------------------------+-------------------------------------------------+
| Ref             | Requirement                                      | Definition/Note                                 |
+=================+==================================================+=================================================+
| req.sec.gen.001 | The platform **must** maintain the specified     |                                                 |
|                 | configuration.                                   |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.002 | The systems part of the cloud infrastructure     | Hardening: CIS Password Policy Guide            |
|                 | **must** support password hardening, as defined  |                                                 |
|                 | in CIS Password Policy Guide `https://www.cisecu |                                                 |
|                 | rity.org/insights/white-papers/cis-password-poli |                                                 |
|                 | cy-guide <https://www.cisecurity.org/insights/wh |                                                 |
|                 | ite-papers/cis-password-policy-guide>`__.        |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.003 | The servers part of the cloud infrastructure     |                                                 |
|                 | **must** support a root of trust and secure      |                                                 |
|                 | boot.                                            |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.004 | The operating systems of all the parts of the    | NIST SP 800-123                                 |
|                 | cloud infrastructure dealing with servers        |                                                 |
|                 | **must** be hardened by removing or disabling    |                                                 |
|                 | unnecessary services, applications, and network  |                                                 |
|                 | protocols, configuring operating system user     |                                                 |
|                 | authentication, configuring resource controls,   |                                                 |
|                 | installing and configuring additional security   |                                                 |
|                 | controls where needed, and testing the security  |                                                 |
|                 | of the operating system.                         |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.005 | The platform **must** support operating system-  |                                                 |
|                 | level access control.                            |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.006 | The platform **must** support secure logging.    |                                                 |
|                 | Logging with the root account must be prohibited |                                                 |
|                 | when the root privileges are not required.       |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.007 | All parts of the cloud infrastructure dealing    |                                                 |
|                 | with servers **must** be time-synchronized with  |                                                 |
|                 | the authenticated time service.                  |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.008 | All parts of the cloud infrastructure dealing    |                                                 |
|                 | with servers **must** be regularly updated to    |                                                 |
|                 | address security vulnerabilities.                |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.009 | The platform **must** support software integrity |                                                 |
|                 | protection and verification, and **must** scan   |                                                 |
|                 | the source code and manifests.                   |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.010 | The cloud infrastructure **must** support        |                                                 |
|                 | encrypted storage, for example, block, object    |                                                 |
|                 | and file storage, with access to encryption keys |                                                 |
|                 | restricted on a need-to-know basis. Controlled   |                                                 |
|                 | access based on a need to know `https://www.cis  |                                                 |
|                 | ecurity.org/controls/cis-controls-list           |                                                 |
|                 | <https://www.cisecurity.org/controls/            |                                                 |
|                 | cis-controls-list>`__.                           |                                                 |          
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.011 | The cloud infrastructure **should** support      |                                                 |
|                 | read- and write-only storage partitions (write-  |                                                 |
|                 | only permission to one or more authorized        |                                                 |
|                 | actors).                                         |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.012 | The operator **must** ensure that only           |                                                 |
|                 | authorized actors have physical access to the    |                                                 |
|                 | underlying infrastructure.                       |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.013 | The platform **must** ensure that only           |                                                 |
|                 | authorized actors have logical access to the     |                                                 |
|                 | underlying infrastructure.                       |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.014 | All parts of the cloud infrastructure dealing    |                                                 |
|                 | with servers **should** support measured boot    |                                                 |
|                 | and an attestation server that monitors the      |                                                 |
|                 | measurements of the servers.                     |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.gen.015 | Any change to the platform **must** be logged as |                                                 |
|                 | a security event. The logged event must include  |                                                 |
|                 | the identity of the entity making the change,    |                                                 |
|                 | the change itself, and the date and time of the  |                                                 |
|                 | change.                                          |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+

**Table 7-3:** System hardening requirements

Platform and access
~~~~~~~~~~~~~~~~~~~

+-----------------+--------------------------------------------------+-------------------------------------------------+
| Ref             | Requirement                                      | Definition/Note                                 |
+=================+==================================================+=================================================+
| req.sec.sys.001 | The platform **must** support authenticated and  |                                                 |
|                 | secure access to APIs, GUIs, and command line    |                                                 |
|                 | interfaces (CLIs).                               |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.002 | The platform **must** support traffic filtering  |                                                 |
|                 | for workloads (for example, firewalls).          |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.003 | The platform **must** support secure and         |                                                 |
|                 | encrypted communications, and the                |                                                 |
|                 | confidentiality and integrity of network         |                                                 |
|                 | traffic.                                         |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.004 | The cloud infrastructure **must** support        | A secure channel enables the transferring of    |
|                 | authentication, integrity, and confidentiality   | data that is resistant to overhearing and       |
|                 | on all network channels.                         | tampering.                                      |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.005 | The cloud infrastructure **must** segregate the  |                                                 |
|                 | underlay and overlay networks.                   |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.006 | The cloud infrastructure must be able to utilize |                                                 |
|                 | the cloud infrastructure manager identity        |                                                 |
|                 | lifecycle management capabilities.               |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.007 | The platform **must** implement controls         |                                                 |
|                 | enforcing the separation of duties and           |                                                 |
|                 | privileges, least privilege use and least common |                                                 |
|                 | mechanism (role-based access control).           |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.008 | The platform **must** be able to assign the      | Communication between different trust domains   |
|                 | entities that comprise the tenant networks to    | is not allowed, by default.                     |
|                 | different trust domains.                         |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.009 | The platform **must** support the creation of    | These may be uni-directional relationships      |
|                 | trust relationships between trust domains.       | where the trusting domain trusts another domain |
|                 |                                                  | (the “trusted domain”) to authenticate users    |
|                 |                                                  | for them, or to allow access to its resources   |
|                 |                                                  | from the trusted domain. In a bidirectional     |
|                 |                                                  | relationship, both domains are “trusting” and   |
|                 |                                                  | “trusted”.                                      |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.010 | For two or more domains without existing trust   |                                                 |
|                 | relationships, the platform **must not** allow   |                                                 |
|                 | the effect of an attack on one domain to impact  |                                                 |
|                 | the other domains, either directly or            |                                                 |
|                 | indirectly.                                      |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.011 | The platform **must not** reuse the same         |                                                 |
|                 | authentication credentials (for example, a key-  |                                                 |
|                 | pair) on different platform components (for      |                                                 |
|                 | example, on different hosts, or different        |                                                 |
|                 | services).                                       |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.012 | The platform **must** protect all secrets by     | For example, in OpenStack Barbican.             |
|                 | using strong encryption techniques and storing   |                                                 |
|                 | the protected secrets externally from the        |                                                 |
|                 | component.                                       |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.013 | The platform **must** provide secrets            |                                                 |
|                 | dynamically as and when needed.                  |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.014 | The platform **should** use Linux Security       |                                                 |
|                 | Modules, such as SELinux, to control access to   |                                                 |
|                 | resources.                                       |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.015 | The platform **must not** contain back-door      |                                                 |
|                 | entries (such as unpublished access points,      |                                                 |
|                 | APIs, and so on).                                |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.016 | Login access to the platform's components        | Hardened jump servers isolated from             |
|                 | **must** be through encrypted protocols, such as | external networks are recommended.              |
|                 | SSH v2 or TLS v1.2, or higher.                   |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.017 | The platform **must** provide the capability of  |                                                 |
|                 | using digital certificates that comply with      |                                                 |
|                 | X.509 standards issued by a trusted              |                                                 |
|                 | certification authority.                         |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.018 | The platform **must** provide the ability to     |                                                 |
|                 | allow certificate renewal and revocation.        |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.019 | The platform **must** provide the ability to     |                                                 |
|                 | test the validity of a digital certificate       |                                                 |
|                 | (CA signature, validity period, non-revocation,  |                                                 |
|                 | identity).                                       |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+
| req.sec.sys.020 | The cloud infrastructure architecture **should** | Zero Trust Architecture (ZTA) described in NIST |
|                 | rely on Zero Trust principles to build a secure  | SP 800-207                                      |
|                 | by design environment.                           |                                                 |
+-----------------+--------------------------------------------------+-------------------------------------------------+

**Table 7-4:** Platform and access requirements

Confidentiality and integrity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------+----------------------------------------------------------------------------+------------------------+
| Ref            | Requirement                                                                | Definition/Note        |
+================+============================================================================+========================+
| req.sec.ci.001 | The platform **must** support the confidentiality and integrity of data    |                        |
|                | at rest and in transit.                                                    |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.ci.002 | The platform **should** support self-encrypting storage devices.           |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.ci.003 | The platform **must** support the confidentiality and integrity of data-   |                        |
|                | related metadata.                                                          |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.ci.004 | The platform **must** support the confidentiality of processes and         |                        |
|                | restrict information sharing to the process owner only (for example, the   |                        |
|                | tenant).                                                                   |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.ci.005 | The platform **must** support the confidentiality and integrity of         |                        |
|                | process-related metadata and restrict information sharing to the process   |                        |
|                | owner only (for example, the tenant).                                      |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.ci.006 | The platform **must** support the confidentiality and integrity of         |                        |
|                | workload resource utilization (RAM, CPU, storage, network I/O, cache,      |                        |
|                | hardware offload), and restrict information sharing to the workload owner  |                        |
|                | only (for example, the, tenant).                                           |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.ci.007 | The platform **must not** allow memory inspection by any other actor than  | Admin access must be   |
|                | the authorized actors for the entity to which memory is assigned (such as  | carefully regulated.   |
|                | the tenants owning the workload), for lawful inspection, and by secure     |                        |
|                | monitoring services.                                                       |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.ci.008 | The cloud infrastructure **must** support the segregation of the tenant    |                        |         
|                | networks.                                                                  |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.ci.009 | For sensitive data encryption, the key management service **should**       |                        |
|                | leverage a hardware security module to manage and protect cryptographic    |                        |
|                | keys.                                                                      |                        |
+----------------+----------------------------------------------------------------------------+------------------------+

**Table 7-5:** Confidentiality and integrity requirements

Workload security
~~~~~~~~~~~~~~~~~

+----------------+----------------------------------------------------------------------------+------------------------+
| Ref            | Requirement                                                                | Definition/Note        |
+================+============================================================================+========================+
| req.sec.wl.001 | The platform **must** support a workload placement policy.                 |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.wl.002 | The cloud infrastructure **must** provide methods to ensure the            |                        |
|                | platform’s trust status and integrity (for example, remote attestation,    |                        |
|                | trusted platform module).                                                  |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.wl.003 | The platform **must** support the secure provisioning of workloads.        |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.wl.004 | The platform **must** support location assertion (for mandated in-country  |                        |
|                | or location requirements).                                                 |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.wl.005 | The platform **must** support the separation of production and             |                        |
|                | non-production workloads.                                                  |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.wl.006 | The platform **must** support the separation of workloads based on their   |                        |
|                | categorisation (for example, payment card information, healthcare, and so  |                        |
|                | on).                                                                       |                        |
+----------------+----------------------------------------------------------------------------+------------------------+
| req.sec.wl.007 | The operator **should** implement processes and tools to verify NF         |                        |
|                | authenticity and integrity.                                                |                        |
+----------------+----------------------------------------------------------------------------+------------------------+

**Table 7-6:** Workload security requirements

Image security
~~~~~~~~~~~~~~

+-----------------+----------------------------------------------------------------------------------+-----------------+
| Ref             | Requirement                                                                      | Definition/Note |
+=================+==================================================================================+=================+
| req.sec.img.001 | Images must be scanned, in order to be kept free from known vulnerabilities.     |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.img.002 | Images must be scanned, in order to be kept free from known vulnerabilities.     |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.img.003 | Images must not be configured to run with privileges higher than those of the    |                 |
|                 | actor who is authorized to run them.                                             |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.img.004 | Images **must** only be accessible to authorized actors.                         |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.img.005 | Image registries **must** only be accessible to authorized actors.               |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.img.006 | Image registries **must** only be accessible over secure networks that enforce   |                 |
|                 | authentication, integrity, and confidentiality.                                  |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.img.007 | Image registries **must** be clear of vulnerable and out of date versions.       |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.img.008 | Images **must not** include any secrets. Secrets include passwords, cloud        |                 |
|                 | provider credentials, SSH keys, TLS certificate keys, and so on.                 |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.img.009 | CIS hardened images **should** be used whenever possible.                        |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.img.010 | Minimalist base images **should** be used whenever possible.                     |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+

**Table 7-7:** Image security requirements

Security LCM
~~~~~~~~~~~~

+-----------------+---------------------------------------------------------------------------+------------------------+
| Ref             | Requirement                                                               | Definition/Note        |
+=================+===========================================================================+========================+
| req.sec.lcm.001 | The platform **must** support secure provisioning, availability, and      | Secure clean-up:       |
|                 | deprovisioning (secure clean-up) of workload resources where secure       | tear-down, defending   |
|                 | clean-up includes tear-down, and defence against virus attacks or other   | against virus attacks  |
|                 | attacks.                                                                  | or other attacks, or   |
|                 |                                                                           | observing of           |
|                 |                                                                           | cryptographic or user  |
|                 |                                                                           | service data.          |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.002 | Cloud operations staff and systems **must** use management protocols      |                        |
|                 | limiting security risk, such as SNMPv3, SSH v2, ICMP, NTP, syslog, and    |                        |
|                 | TLS v1.2 or higher.                                                       |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.003 | The cloud operator **must** implement and strictly follow change          |                        |
|                 | management processes for the cloud infrastructure, cloud infrastructure   |                        |
|                 | manager, and other components of the cloud, and platform change control   |                        |
|                 | on hardware.                                                              |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.004 | The cloud operator **should** support automated templated approved        | Templated approved     |
|                 | changes.                                                                  | changes for automation |
|                 |                                                                           | where available.       |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.005 | The platform **must** provide logs. These logs must be regularly          |                        |
|                 | monitored for anomalous behaviour.                                        |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.006 | The platform **must** verify the integrity of all resource management     |                        |
|                 | requests.                                                                 |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.007 | The platform **must** be able to update newly instantiated, suspended,    |                        |
|                 | hibernated, migrated, and restarted images with the current time          |                        |
|                 | information.                                                              |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.008 | The platform **must** be able to update newly instantiated, suspended,    |                        |
|                 | hibernated, migrated, and restarted images with the relevant DNS          |                        |
|                 | information.                                                              |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.009 | The platform **must** be able to update the tags of newly instantiated,   |                        |
|                 | suspended, hibernated, migrated, and restarted images with the relevant   |                        |
|                 | geolocation (geographical) information.                                   |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.010 | The platform **must** log all changes to geolocation along with the       |                        |
|                 | mechanisms and sources of the location information (that is, GPS, IP      |                        |
|                 | block, and timing).                                                       |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.011 | The platform **must** implement security lifecycle management processes,  |                        |
|                 | including the proactive update and patching of all deployed cloud         |                        |
|                 | infrastructure software.                                                  |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.lcm.012 | The platform **must** log any access privilege escalation.                |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+

**Table 7-8:** Security LCM requirements

Monitoring and security audit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform is assumed to provide configurable alerting and notification capabilities. The operator is assumed to have
systems, policies, and procedures in place to act on alerts and notifications in a timely fashion. In the following,
the monitoring and logging capabilities can trigger alerts and notifications for appropriate action. In general, it is
recommended to have the same security monitoring and auditing capabilities in both production and non-production
environments. However, we distinguish between the requirements for the production platform (Prod-Platform) and the
non-production platform (NonProd-Platform), as some of the requirements may, in practice, need to differ. See
:ref:`chapters/chapter07:security of production and non-production environments` for a general discussion of this
topic. In the table below, when a requirement mentions only Prod-Platform, it is assumed that this requirement is
optional for the NonProd-Platform. If a requirement does not mention either platform, it is assumed that it is valid
for both the Prod-Platform and the NonProd-Platform.

+-----------------+----------------------------------------------------------------------------------+-----------------+
| Ref             | Requirement                                                                      | Definition/Note |
+=================+==================================================================================+=================+
| req.sec.mon.001 | The Prod-Platform and NonProd-Platform **must** provide logs. The logs **must**  |                 |
|                 | contain the following fields: event type, date/time, protocol, the service or    |                 |
|                 | program used for access, success/failure, the login ID or process ID, the IP     |                 |
|                 | address, and the ports (source and destination) involved.                        |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.002 | The logs **must** be regularly monitored for events of interest.                 |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.003 | The logs **must** be time-synchronised for the Prod-Platform, as well as for     |                 |
|                 | the NonProd-Platform.                                                            |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.004 | The Prod-Platform and the NonProd-Platform **must** log all changes to the time  |                 |
|                 | server source, time, and date and time zones.                                    |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.005 | The Prod-Platform and the NonProd-Platform **must** secure and protect all the   |                 |
|                 | logs containing sensitive information, both in transit and at rest.              |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.006 | The Prod-Platform and the NonProd-Platform **must** monitor and audit the        |                 |
|                 | various behaviours of connection and login attempts to detect access attacks     |                 |
|                 | and potential access attempts, and take corrective action accordingly.           |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.007 | The Prod-Platform and the NonProd-Platform **must** Monitor and Audit operations |                 |
|                 | by authorized account access after login, to detect malicious operational        |                 |
|                 | activity and take corrective action.                                             |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.008 | The Prod-Platform **must** monitor and audit security parameter configurations   |                 |
|                 | for compliance with defined security policies.                                   |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.009 | The Prod-Platform and the NonProd-Platform **must** monitor and audit            |                 |
|                 | externally exposed interfaces for illegal access (attacks) and take corrective   |                 |
|                 | security hardening measures.                                                     |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.010 | The Prod-Platform **must** monitor and audit the service for various attacks     |                 |
|                 | (malformed messages, signalling flooding and replaying, and so on), and take     |                 |
|                 | corrective action.                                                               |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.011 | The Prod-Platform **must** monitor and audit running processes to detect         |                 |
|                 | unexpected or unauthorized processes, and take corrective action.                |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.012 | The Prod-Platform and the NonProd-Platform **must** monitor and audit logs from  |                 |
|                 | the infrastructure elements and workloads to detect anomalies in the system      |                 |
|                 | components and take corrective action.                                           |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.013 | The Prod-Platform and the NonProd-Platform **must** monitor and audit traffic    |                 |
|                 | patterns and volumes to prevent malware download attempts.                       |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.014 | The monitoring system **must not** affect the security (integrity and            |                 |
|                 | confidentiality) of the infrastructure, workloads, or the user data (through     |                 |
|                 | back-door entries).                                                              |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.015 | The monitoring systems **should not** impact IaaS, PaaS, and SaaS SLAs,          |                 |
|                 | including availability SLAs.                                                     |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.016 | The Prod-Platform and the NonProd-Platform **must** ensure that the monitoring   |                 |
|                 | systems are never starved of resources and **must** activate alarms when         |                 |
|                 | resource utilisation exceeds a configurable threshold.                           |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.017 | The Prod-Platform and the NonProd-Platform monitoring components **should**      |                 |
|                 | follow security best practices for auditing, including secure logging and        |                 |
|                 | tracing.                                                                         |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.018 | The Prod-Platform and the NonProd-Platform **must** audit systems for any        |                 |
|                 | missing security patches and take appropriate action.                            |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.019 | The Prod-Platform, starting from initialization, **must** collect and analyse    |                 |
|                 | logs to identify security events and store these events in an external system.   |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.020 | The components of the Prod-Platform and the NonProd-Platform **must not**        |                 |
|                 | include any authentication credentials, such as passwords, in any logs, even if  |                 |
|                 | they are encrypted.                                                              |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.021 | The logging system of the Prod-Platform and the NonProd-Platform **must**        |                 |
|                 | support the storage of the security audit logs for a configurable period.        |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+
| req.sec.mon.022 | The Prod-Platform **must** store the security events locally, if the external    |                 |
|                 | logging system is unavailable. It must periodically attempt to send them to      |                 |
|                 | the external logging system until it is successful.                              |                 |
+-----------------+----------------------------------------------------------------------------------+-----------------+

**Table 7-9:** Monitoring and security audit requirements

Open-source software
~~~~~~~~~~~~~~~~~~~~

+-----------------+---------------------------------------------------------------------------+------------------------+
| Ref             | Requirement                                                               | Definition/Note        |
+=================+===========================================================================+========================+
| req.sec.oss.001 | Open-source code **must** be inspected by tools with various capabilities |                        |
|                 | for static and dynamic code analysis.                                     |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.oss.002 | The Common Vulnerabilities and Exposures (CVE) **must** be used to        | `https://cve.mitre.org |
|                 | identify vulnerabilities and assess their severity rating for the         | / <https://cve.mitre.o |
|                 | open-source code part of the cloud infrastructure and workloads software. | rg/>`__                |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.oss.003 | Critical- and high-severity-rated vulnerabilities **must** be fixed in a  | `https://www.first.org |
|                 | timely manner. See the Common Vulnerability Scoring System (CVSS) to find | /cvss/ <https://www.fi |
|                 | out a vulnerability score and its associated rate (low, medium, high, or  | rst.org/cvss/>`__      |
|                 | critical).                                                                |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.oss.004 | A dedicated internal isolated repository separated from the production    |                        |
|                 | environment **must** be used to store vetted open-source content.         |                        |
+-----------------+---------------------------------------------------------------------------+------------------------+
| req.sec.oss.005 | A Software Bill of Materials (SBOM) **should** be provided or built, and  | Inventory of software  |
|                 | maintained to identify the software components and their origins.         | components, `https://  |
|                 |                                                                           | ntia.gov/SBOM <http    |
|                 |                                                                           | s://ntia.gov/SBO       |
|                 |                                                                           | M>`__                  |
+-----------------+---------------------------------------------------------------------------+------------------------+

**Table 7-10:** Open-source software requirements

IaaC - Secure design and architecture stage requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+---------------------------------------------+-----------------------------------------------------+
| Ref              | Requirement                                 | Definition/Note                                     |
+==================+=============================================+=====================================================+
| req.sec.arch.001 | Threat modelling methodologies and tools    | These are methodologies for identifying and         |
|                  | **should** be used during the               | understanding threats impacting a resource or a set |
|                  | Secure Design and Architecture stage,       | of resources. It may be done manually or by using   |
|                  | triggered by the Software Feature Design    | tools such as the open-source OWASP Threat Dragon.  |
|                  | trigger.                                    |                                                     |
+------------------+---------------------------------------------+-----------------------------------------------------+
| req.sec.arch.002 | A Security Control Baseline Assessment      | Security Control Baseline Assessments are typically |
|                  | **should** be performed during the Secure   | done manually by internal or independent assessors. |
|                  | Design and Architecture stage, triggered by |                                                     |
|                  | the Software Feature Design trigger.        |                                                     |
+------------------+---------------------------------------------+-----------------------------------------------------+

**Table 7-11:** IaaC - Secure design and architecture stage requirements

IaaC - Secure code stage requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+---------------------------------------------+-----------------------------------------------------+
| Ref              | Requirement                                 | Definition/Note                                     |
+==================+=============================================+=====================================================+
| req.sec.code.001 | Static Application Security Testing (SAST)  | SAST is a type of security testing that analyses    |
|                  | **must** be applied during the secure       | application source code for software                |
|                  | coding stage, triggered by the Pull, Clone  | vulnerabilities and gaps against best practices.    |
|                  | or Comment trigger.                         | An example of this is the open-source OWASP range   |
|                  |                                             | of tools.                                           |
+------------------+---------------------------------------------+-----------------------------------------------------+
| req.sec.code.002 | Software Composition Analysis (SCA)         | SCA is a type of security testing that analyses     |
|                  | **should** be applied during the secure     | application source code or compiled code for        |
|                  | coding stage, triggered by the Pull, Clone, | software components with known vulnerabilities.     |
|                  | or Comment trigger.                         | An example of this is the open-source OWASP range   |
|                  |                                             | of tools.                                           |
+------------------+---------------------------------------------+-----------------------------------------------------+
| req.sec.code.003 | A source code review **should** be          | This is typically done manually.                    |
|                  | performed continuously during Secure Coding |                                                     |
|                  | stage.                                      |                                                     |
+------------------+---------------------------------------------+-----------------------------------------------------+
| req.sec.code.004 | Integrated SAST via IDE plugins **should**  | On the local machine: through the IDE or integrated |
|                  | be used during the secure coding stage,     | test suites and triggered on completion of the      |
|                  | triggered by the Developer Code trigger.    | coding development.                                 |
+------------------+---------------------------------------------+-----------------------------------------------------+
| req.sec.code.005 | Static Application Security Testing of      | Continuous delivery predeployment: scanning prior   |
|                  | the source code repo **should** be          | to deployment.                                      |
|                  | performed during the secure coding stage,   |                                                     |
|                  | triggered by the Developer Code trigger.    |                                                     |
+------------------+---------------------------------------------+-----------------------------------------------------+

**Table 7-12:** IaaC - Secure code stage requirements

IaaC - Continuous build, integration, and testing stage requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+----------------------------------------------+-----------------------------------------------------+
| Ref             | Requirement                                  | Definition/Note                                     |
+=================+==============================================+=====================================================+
| req.sec.bld.001 | Static Application Security Testing (SAST)   | Example: the open-source OWASP range of tools.      |
|                 | **should** be applied during the continuous  |                                                     |
|                 | build, integration, and testing stage,       |                                                     |
|                 | triggered by the Build and Integrate         |                                                     |
|                 | trigger.                                     |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.bld.002 | Software Composition Analysis (SCA)          | Example: the open-source OWASP range of tools.      |
|                 | **should** be applied during the continuous  |                                                     |
|                 | build, integration, and testing stage,       |                                                     |
|                 | triggered by the Build and Integrate         |                                                     |
|                 | trigger.                                     |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.bld.003 | An image scan **must** be applied during the | Example: pushing a container image to a container   |
|                 | continuous build, integration, and testing   | registry may trigger a vulnerability scan before    |
|                 | stage, triggered by the Package trigger.     | the image becomes available in the registry.        |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.bld.004 | Dynamic Application Security Testing (DAST)  | DAST is a type of security testing that analyses a  |
|                 | **should** be applied during the continuous  | running application by exercising the application   |
|                 | build, integration, and testing stage,       | functionality and detecting vulnerabilities based   |
|                 | triggered by the Stage and Test trigger.     | on the behaviour and response of the application.   |
|                 |                                              | Example: OWASP Zed Attack Proxy (ZAP).              |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.bld.005 | Fuzzing **should** be applied during the     | Fuzzing, or fuzz testing, is an automated software  |
|                 | continuous build, integration, and testing   | testing technique that involves providing invalid,  |
|                 | stage, triggered by the Stage and Test       | unexpected, or random data as input to a computer   |
|                 | trigger.                                     | program. Example: GitLab Open Sources Protocol      |
|                 |                                              | Fuzzer Community Edition.                           |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.bld.006 | Interactive Application Security Testing     | A software component deployed with an application   |
|                 | (IAST) **should** be applied during the      | that assesses the behaviour of the application and  |
|                 | continuous build, integration, and testing   | detects the presence of vulnerabilities on          |
|                 | stage, triggered by the Stage and Test       | applications that are being exercised in realistic  |
|                 | trigger.                                     | testing scenarios. Example: Contrast Community      |
|                 |                                              | Edition.                                            |
+-----------------+----------------------------------------------+-----------------------------------------------------+

**Table 7-13:** IaaC - Continuous build, integration, and testing stage requirements

IaaC - Continuous delivery and deployment stage requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+----------------------------------------------+-----------------------------------------------------+
| Ref             | Requirement                                  | Definition/Note                                     |
+=================+==============================================+=====================================================+
| req.sec.del.001 | An image scan **must** be applied during the | Example: GitLab uses the open-source Clair engine   |
|                 | continuous delivery and deployment stage,    | for container image scanning.                       |
|                 | triggered by the Publish to Artifact and     |                                                     |
|                 | Image Repository trigger.                    |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.del.002 | Code signing **must** be applied during the  | Code signing provides authentication to assure that |
|                 | continuous delivery and deployment stage,    | downloaded files are from the publisher named on    |
|                 | triggered by the Publish to Artifact and     | the certificate.                                    |
|                 | Image Repository trigger.                    |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.del.003 | An artifact and image repository scan        | Example: GitLab uses the open-source Clair engine   |
|                 | **should** be continuously applied during    | for container scanning.                             |
|                 | the continuous delivery and deployment       |                                                     |
|                 | stage.                                       |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.del.004 | A component vulnerability scan **must** be   | The vulnerability scanning system is deployed on    |
|                 | applied during the continuous delivery and   | the cloud platform to detect the security           |
|                 | deployment stage, triggered by the           | vulnerabilities of specified components through     |
|                 | Instantiate Infrastructure trigger.          | scanning and to provide timely security protection. |
|                 |                                              | Example: OWASP Zed Attack Proxy (ZAP).              |
+-----------------+----------------------------------------------+-----------------------------------------------------+

**Table 7-14:** IaaC - Continuous delivery and deployment stage requirements

IaaC - Runtime defence and monitoring requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+----------------------------------------------+-----------------------------------------------------+
| Ref             | Requirement                                  | Definition/Note                                     |
+=================+==============================================+=====================================================+
| req.sec.run.001 | Component vulnerability monitoring **must**  | Security technology that monitors components such   |
|                 | be continuously applied during the runtime   | as virtual servers and assesses data, applications, |
|                 | defence and monitoring stage, and            | and infrastructure for security risks.              |
|                 | remediation actions **must** be applied for  |                                                     |
|                 | high-severity-rated vulnerabilities.         |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.run.002 | Runtime Application Self-Protection (RASP)   | Security technology deployed within the target      |
|                 | **should** be continuously applied during    | application in production for detecting, alerting,  |
|                 | the runtime defence and monitoring stage.    | and blocking attacks.                               |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.run.003 | Application testing and fuzzing **should**   | Fuzzing, or fuzz, testing is an automated software  |
|                 | be continuously applied during the runtime   | testing technique that involves providing invalid,  |
|                 | defence and monitoring stage.                | unexpected, or random data as input to a computer   |
|                 |                                              | program. Example: GitLab Open Sources Protocol      |
|                 |                                              | Fuzzer Community Edition.                           |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.run.004 | Penetration testing **should** be            | This is typically done manually.                    |
|                 | continuously applied during the runtime      |                                                     |
|                 | defence and monitoring stage.                |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+

**Table 7-15:** IaaC - Runtime defence and monitoring requirements

Compliance with standards
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+----------------------------------------------+-----------------------------------------------------+
| Ref             | Requirement                                  | Definition/Note                                     |
+=================+==============================================+=====================================================+
| req.sec.std.001 | The cloud operator **should** comply with the| Center for Internet Security - `https://www.cisecur |
|                 | Center for Internet Security CIS Controls.   | ity.org/ <https://www.cisecurity.org/>`__           |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.002 | The cloud operator, platform, and workloads  | Cloud Security Alliance - `https://cloudsecurityall |
|                 | **should** follow the guidance in the CSA    | iance.org/ <https://cloudsecurityalliance.org/>`__  |
|                 | Security Guidance for Critical Areas of      |                                                     |
|                 | Focus in Cloud Computing (latest version).   |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.003 | The platform and workloads **should** follow | Open Web Application Security Project `https://www. |
|                 | the guidance in the OWASP Cheat Sheet Series | owasp.org <https://owasp.org/>`__                   |
|                 | (OCSS) `https://github.com/OWASP/CheatSheetS |                                                     |
|                 | eries <https://github.com/OWASP/CheatSheetSe |                                                     |
|                 | ries>`__.                                    |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.004 | The cloud operator, platform, and workloads  |                                                     |
|                 | **should** ensure that their code is not     |                                                     |
|                 | vulnerable to the OWASP Top Ten Security     |                                                     |
|                 | Risks `https://owasp.org/www-project-top-ten |                                                     |
|                 | / <https://owasp.org/www-project-top-ten     |                                                     |
|                 | />`__.                                       |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.005 | The cloud operator, platform, and workloads  |                                                     |
|                 | **should** strive to improve their maturity  |                                                     |
|                 | on the OWASP Software Maturity Model (SAMM)  |                                                     |
|                 | `https://owaspsamm.org/blog/2019/12/20/versi |                                                     |
|                 | on2-community-release/ <https://owaspsamm.or |                                                     |
|                 | g/blog/2019/12/20/version2-community-release |                                                     |
|                 | />`__.                                       |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.006 | The cloud operator, platform, and workloads  |                                                     |
|                 | **should** utilize the OWASP Web Security    |                                                     |
|                 | Testing Guide `https://github.com/OWASP/wstg |                                                     |
|                 | /tree/master/document <https://github.com/OW |                                                     |
|                 | ASP/wstg/tree/master/document>`__.           |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.007 | The cloud operator and platform **should**   | ISO/IEC 27002:2013 - ISO/IEC 27001 is the           |
|                 | satisfy the requirements for Information     | international standard for best-practice            |
|                 | Management Systems, specified in ISO/IEC     | information security management systems (ISMSs).    |
|                 | 27001 `https://www.iso.org/obp/ui/#iso:std:i |                                                     |
|                 | so-iec:27001:ed-2:v1:en <https://www.iso.org |                                                     |
|                 | /obp/ui/#iso:std:iso-iec:27001:ed-2:v1:e     |                                                     |
|                 | n>`__ .                                      |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.008 | The cloud operator and platform **should**   |                                                     |
|                 | implement the code of practice for Security  |                                                     |
|                 | Controls specified ISO/IEC 27002:2013 (or    |                                                     |
|                 | latest) `https://www.iso.org/obp/ui/#iso:std |                                                     |
|                 | :iso-iec:27002:ed-2:v1:en <https://www.iso.o |                                                     |
|                 | rg/obp/ui/#iso:std:iso-iec:27002:ed-2:v1:e   |                                                     |
|                 | n>`__ .                                      |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.009 | The cloud operator and platform **should**   | ISO/IEC 27032 - ISO/IEC 27032is the international   |
|                 | implement the ISO/IEC 27032:2012 (or latest) | Standard focusing explicitly on cybersecurity.      |
|                 | Guidelines for Cybersecurity techniques `htt |                                                     |
|                 | ps://www.iso.org/obp/ui/#iso:std:iso-iec:270 |                                                     |
|                 | 32:ed-1:v1:en <https://www.iso.org/obp/ui/#i |                                                     |
|                 | so:std:iso-iec:27032:ed-1:v1:en>`__ .        |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.010 | The cloud operator **should** conform to the | ISO/IEC 27035 - ISO/IEC 27035 is the international  |
|                 | ISO/IEC 27035 standard for incidence         | standard for incident management.                   |
|                 | management.                                  |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.011 | The cloud operator **should** conform to the |                                                     |
|                 | ISO/IEC 27031 standard for business          |                                                     |
|                 | continuity ISO/IEC 27031. ISO/IEC 27031 is   |                                                     |
|                 | the international standard for ICT readiness |                                                     |
|                 | for business continuity.                     |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+
| req.sec.std.012 | The public cloud operator **must**, and the  | International Standard on Awareness Engagements     |
|                 | private cloud operator **may**, be certified | (ISAE) 3402. US Equivalent: SSAE16.                 |
|                 | to be compliant with the International       |                                                     |
|                 | Standard on Awareness Engagements (ISAE)     |                                                     |
|                 | 3402 (in the US: SSAE 16).                   |                                                     |
+-----------------+----------------------------------------------+-----------------------------------------------------+

**Table 7-16:** Compliance with standards requirements

Additional security references
------------------------------

In addition to the security standards used throughout this specification,
the following lists gather together additional standards of interest for cloud infrastructure security.

**ETSI Documents**

- Network Functions Virtualisation (NFV); NFV Security; Problem Statement, ETSI GS NFV-SEC 001 V1.1.1 (2014-10)

- Network Functions Virtualisation (NFV); NFV Security; Security and Trust Guidance, ETSI GS NFV-SEC 003 V1.1.1
  (2014-12)

- Network Functions Virtualisation (NFV) Release 3; Security; Security Management and Monitoring specification,
  ETSI GS NFV-SEC 013 V3.1.1 (2017-02)

- Network Functions Virtualisation (NFV) Release 3; NFV Security; Security Specification for MANO Components and
  Reference points, ETSI GS NFV-SEC 014 V3.1.1 (2018-04)

- Network Functions Virtualisation (NFV) Release 2; Security; VNF Package Security Specification,
  ETSI GS NFV-SEC 021 V2.6.1 (2019-06)

**NIST Documents**

- `NIST SP 800-53 Security and Privacy Controls for Federal Information Systems and Organizations`__ :cite:p:`NIST-SP-800-53`

- `NIST SP 800-53A Assessing Security and Privacy Controls in Federal Information Systems and Organizations: Building
  Effective Assessment Plans`__ :cite:p:`NIST-SP-800-53A`

- `NIST SP 800-63B Digital Identity Guidelines`__ :cite:p:`NIST-SP-800-63B`

- `NIST SP 800-115 Technical Guide to Information Security Testing and Assessment`__ :cite:p:`NIST-SP-800-115`

- `NIST SP 800-125 Guide to Security for Full Virtualization Technologies`__ :cite:p:`NIST-SP-800-125`

- `NIST SP 800-125a Security Recommendations for Server-based Hypervisor Platforms`__ :cite:p:`NIST-SP-800-125a`

- `NIST SP 800-125b Secure Virtual Network Configuration for Virtual Machine (VM) Protection`__ :cite:p:`NIST-SP-800-125b`

- `NIST SP 800-137 Information Security Continuous Monitoring for Federal Information
  Systems and Organizations`__ :cite:p:`NIST-SP-800-137`

- `NIST SP 800-145 The NIST Definition of Cloud Computing`__ :cite:p:`NIST-SP-800-145`

- `NIST SP 800-190 Application Container Security Guide`__ :cite:p:`NIST-SP-800-190`


