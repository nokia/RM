Appendix A: Guidelines For Application Vendors
==============================================

Goals
-----

This Appendix has the following two goals:

1. To provide guidance to the VNF, or more generally to the application vendors, on how to consume the CNTT
   Reference Model and Architectures.
2. To provide usable definitions of maturity levels for the VNF software architecture between physical-to-virtual
   migration and cloud native.

The goal is not to be prescriptive on how to design new applications or redesign existing applications, but rather
to stay within the scope of focusing on the interface and interaction between the applications and the platform.

Introduction and terminology
----------------------------

Taking advantage of the RM and RA environments with common capabilities, applications can be developed and deployed
more rapidly, providing more service agility and easier operations. The extent to which this can be achieved
depends on the levels of decoupling between the applications and the infrastructure, or the platform underneath the
applications:

**1. Infrastructure**:

a. Application functionality or application control requires infrastructure components beyond RM profiles or
   infrastructure configuration changes beyond RA-exposed APIs. Generally, such an application is tightly coupled
   with the infrastructure. This results in an appliance deployment model.
b. Application control using RA APIs finds nodes (already configured in support of the profiles) with the required
   infrastructure components. In these nodes, using RA APIs configures the infrastructure components that make the
   application work. An example of this is an application that needs certain acceleration adapters available in the
   RM profile to achieve the latency requirements and is exposed through RA APIs.
c. Application control using RA APIs finds nodes (already configured in support of the profiles) with optional
   infrastructure components. In these nodes, using RA APIs configures the infrastructure components in a way that
   improves the application's performance. An example of this is an application that has a better TCO with certain
   acceleration adapters, but can also work without them.
d. Application control using RA APIs finds general profile node without any specific infrastructure components.

**2. Platform services**

a. Application functionality or application control can work only with its own components, instead of using
   RA-defined platform services.
b. With a custom integration effort, an application can be made to use RA-defined platform services.
c. An application is designed and can be configured for running with RA-defined platform services.

**3. Application resilience**

a. The application is designed and tested to run only on a carrier-grade platform with predictable infrastructure
   availability and performance.
b. The application is designed and tested for full failures of infrastructure hardware and software components.
   It is not designed and tested for infrastructure impairment, as the application still needs predictable
   infrastructure performance (such as CPU cycles and network latencies).
c. The application is designed to run on shared cloud platforms and is tested for resilience to infrastructure
   impairments. This is relevant for sizing infrastructure and application operations (which are often other telecom operators'
   organizational units or external third parties).

**4. Other application functionalities** (decomposition and manageability for scaling, availability, and upgrades):

a. The application consists of monolithic components, including algorithms that have different scaling (for example,
   depending on the type of traffic) or availability requirements, or both.
b. The application consists of smaller, tightly coupled components.
c. The application is decomposed, with loosely coupled or decoupled components.
d. Availability, such as N+K or 1+1, is defined during the application design and is not configurable at the time
   of deployment.
e. Mutable or immutable instances of application components.

VNF design guidelines
---------------------

A number of software design guidelines, or industry best practices, have been developed over the years. These
include microservices, cohesion, and coupling. In addition to the industry best practices, additional guidelines and
requirements are specified by ONAP in the VNF or PNF Requirements Documentation. :cite:p:`onap-vnfrqts-requirements`.
This section does not supplant these guidelines and practices. The content here only draws attention to some other
design considerations that VNF developers need to incorporate into their practices.

**Note:** Some of these guidelines may be incorporated by operators into their contracts with the VNF vendors.


These guidelines are written in an informal style. Any resemblance to requirements is incidental. The VNF developer
**should** ensure that their software and the resultant VNF images conform to the following rules:

1. They do not contain malicious code, such as malware, logic bombs, and so on.
2. They do not contain code, such as daemons, that exposes them to risk.
3. They do not contain clear-text secrets.
4. They are only created with content and files from trusted sources.
5. They are only packaged with files that have been found to be free of malware and vulnerabilities.

Additionally, in the design and implementation of their software, the VNF developer **should** follow the guidance
in the following literature:

1. CSA Security Guidance for Critical Areas of Focus in Cloud Computing (latest version) :cite:p:`owasp-Cheat-sheet-series`.
2. OWASP Cheat Sheet Series (OCSS) :cite:p:`owasp-Cheat-sheet-series` from the Open Web Application
   Security Project :cite:p:`owasp-Web-application-security-project`.
3. :ref:`chapters/chapter07:workload security and vendor responsibility` section of the Reference Model.

The VNF Developer **should** ensure that their code is not vulnerable to the OWASP Top Ten Security Risks
:cite:p:`owasp-top-ten`, created by the Open Web Application Security Project :cite:p:`owasp`.

Miscellaneous
-------------

.. _vnf-network-monitoring-capabilities---usecase:

VNF ntwork monitoring capabilities: use case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Network monitoring capabilities exposed by the NFVI platform are used for the passive observation of VNF-specific
traffic traversing the NFVI in the following cases:

- Performance issues or packet drops, or both, are reported in the VNF.
- Determining performance bottlenecks at VNF level.
- Performing anomaly detection and network forensics.

**Note:** It is the responsibility of the NFVI platform to provide the capability to create a virtual interface
that has mirrored traffic from the monitored VNF. This port can be attached to the monitoring VNF, so that all
traffic from the monitored VNF is available for troubleshooting/debugging purposes.
