Introduction
============

Overview
--------

The Reference Model (RM) specifies a virtualisation technology-agnostic (VM-based and container-based) cloud
infrastructure abstraction. It acts as a catalogue of the exposed infrastructure capabilities, resources, and
interfaces required by the workloads. This document has been developed by the Linux Foundation Networking project
:doc:`cntt:common/chapter00`.

**Problem statement:** Based on community consultations, including Telco operators, technology suppliers, and software
developers, it is understood that there are significant technical, operational, and business challenges to the
development and deployment of Virtual Network Functions (VNF) and Cloud-Native Network Functions (CNF), due to the
lack of a common cloud infrastructure platform. These include, but are not limited to, the following:

- Higher development costs, due to the need to develop virtualised/containerised network applications on multiple custom
  platforms for each operator.
- Increased complexities, due to the need to maintain multiple versions of applications to support each custom
  environment.
- Lack of testing and validation commonalities, leading to inefficiencies and increased time to market. While the
  operators will still perform internal testing, the application developers utilising an industry standard verification
  program on a common cloud infrastructure would lead to efficiencies and faster time to market.
- Slower adoption of cloud-native applications and architectures. A common Telco cloud may provide an easier path to
  methodologies that will drive faster cloud-native development.
- Increased operational overheads, due to the need for operators to integrate diverse and sometimes conflicting cloud
  platform requirements.

One of the main challenges holding back the more rapid and widespread adoption of virtualised/containerised network
applications is when, while building or designing their virtualised services, specific infrastructure assumptions and
requirements are implied, often with custom design parameters. This forces the operators to build complex integrations
of various vendor-/function-specific silos which are incompatible with each other and might possibly have differing and
conflicting operating models. This also makes the onboarding and conformance processes of the VNFs/CNFs (coming from
different vendors) hard to automate and standardise. There is a clear need for a common model across the industry to
facilitate more rapid adoption.

This document starts from the abstract and, as it progresses, becomes more detailed. It follows the traditional design
process where you start from the core principles, progress to abstract concepts and models, and then finish with
operational considerations, such as security and lifecycle management.

- **Chapter 01 - Introduction**: This provides an overall scope of the Reference Model document, including the goals
  and objectives of the project.

  - **Audience**: This chapter is aimed at a general technical audience with an interest in this topic.

- **Chapter 02 - Workload Requirements and Analysis**: This chapter covers the high-level requirements and core
  principles needed to understand how the model was developed. It addresses the thinking behind the decisions that
  were made.

  - **Audience**: This chapter is aimed at architects and others with an interest in how the decisions were made.

- **Chapter 03 - Modelling**: This chapter covers the high-level cloud infrastructure model itself.

  - **Audience**: This chapter is aimed at architects and others who want to gain a quick high-level understanding
    of the model.

- **Chapter 04 - Infrastructure Capabilities, Metrics, and Catalogue**: This chapter provides details about the
  capabilities needed to support the various types of workloads and how the capabilities are applied to the model.
  Details regarding T-shirt sizes and other considerations are found in this section.

  - **Audience**: This chapter is aimed at architects, developers, and others who need to deploy infrastructure or
    develop applications.

- **Chapter 05 - Feature set and Requirements from Infrastructure**: This chapter goes into more detail on what
  needs to be part of the cloud infrastructure. It describes the software and hardware capabilities, and the
  configurations recommended for the different types of cloud infrastructure profiles.

  - **Audience**: This chapter is aimed at architects, developers, and others who need to deploy infrastructure or
    develop applications.

- **Chapter 06 - External Interfaces**: This chapter covers APIs and other interfaces needed to communicate with
  the workloads and other external components.

  - **Audience**: This chapter is aimed at architects, developers, and others who need to develop APIs or
    applications that use the APIs.

- **Chapter 07 - Security**: This chapter identifies the security requirements that need to be taken into consideration
  when designing and implementing a cloud infrastructure environment. It does not cover details related to
  company-specific requirements to meet regulatory requirements.

  - **Audience**: This chapter is aimed at security professional, architects, developers, and others who need to
    understand the role of security in the cloud infrastructure environment.

- **Chapter 08 - Hybrid Multicloud: Data Centre to Edge**: A generic Telco cloud is a hybrid multicloud, or a federated
  cloud, that is deployed in large data centres, central offices or colocation facilities, and the edge. This chapter
  discusses the characteristics of Telco edge and hybrid multicloud.

  - **Audience**: This chapter is aimed at a general technical audience with an interest in this topic.

- **Chapter 09 - Lifecycle Management**: This chapter focuses on the operational aspects of the cloud infrastructure.
  Discussions include deployment considerations, ongoing management, upgrades, and other lifecycle concerns and
  requirements. It does not cover details related to company-specific operational requirements, nor does it go into how
  the cloud infrastructure interfaces with the existing BSS/OSS systems.

  - **Audience**: This chapter is aimed at lifecycle managers, operational support teams, and others who need to
    support the infrastructure or the applications.

- **Chapter 10 - Challenges and Gaps**: This chapter discusses the opportunities for future developments, as the
  technology changes over time.

  - **Audience**: This chapter is aimed at a general technical audience with an interest in this topic.

Scope
-----

This **Reference Model** document focuses on identifying the abstractions and associated concepts that are needed to
represent the cloud infrastructure. See :numref:`scope-of-reference-model` for the scope of the Reference Model.

.. figure:: ../figures/ch01_scope.png
   :alt: Scope of the Reference Model
   :name: scope-of-reference-model

   Scope of the Reference Model

This document specifies the following:

- **Cloud infrastructure abstraction**: In context with how it interacts with the other components required to build
  a complete cloud system that supports workloads deployed in virtual machines (VMs) or containers. Network function
  workloads that are deployed on virtual machines and containers are referred to as virtual network functions (VNFs)
  and containerised network functions (CNFs), respectively.

  **Note:** CNFs are now more commonly referred to as cloud-native network functions.
  
  - **Cloud infrastructure capabilities and metrics**: This is a set of cloud infrastructure capabilities and metrics
    required to perform Telco scale network functions, and satisfy their performance criteria.
  - **Infrastructure profiles catalogue**: This is a catalogue of standard infrastructure software and hardware
    configurations, referred to as profiles. These profiles abstract the infrastructure for the workloads. Only a few
    profiles, with well-defined characteristics, can meet the operational and performance requirements of all the
    workloads.

- **Cloud infrastructure software and hardware profiles**:

  - **Cloud infrastructure software profiles**: These software profiles are components of the corresponding
    infrastructure profiles within the infrastructure profiles catalogue. They specify the host infrastructure
    software configurations.
  - **Cloud infrastructure hardware profiles**: These hardware profiles are components of the corresponding
    infrastructure profiles within the infrastructure profiles catalogue. They specify the host infrastructure
    hardware configurations.

- **Conformance and verification**:

  - **Conformance programs**: These define the requirements for verification and validation programs for the cloud
    infrastructure and workloads.
  - **Test framework**: This document provides the input for the test suites to allow the conformance of the cloud
    infrastructure and the workloads.

Principles
----------

The Reference Model specifications conform to the overall principles defined in
:ref:`common/chapter00:anuket general principles`.

Definitions/terminology/abbreviations
-------------------------------------

To help guide the reader, the Anuket Glossary :cite:p:`anuket-glossary` provides an introduction to the main terms used
within this document and throughout the project as a whole. These definitions are, with a few exceptions, based on the
ETSI GR NFV 003 :cite:p:`etsigrnfv003` definitions. In a few cases, they have been modified to avoid deployment
technology dependencies, only when it is necessary to avoid confusion.

For a full list of abbreviations used in this document, see the Anuket Abbreviations :cite:p:`anuket-abbreviatons`.

Conventions
-----------

The key words "must", "must not", "required", "shall", "shall not", "should", "should not", "recommended", "may", and
"optional", in this document, are to be interpreted according to the descriptions in RFC2119 :cite:p:`rfc2119`.

References
----------

.. bibliography::
   :cited:
