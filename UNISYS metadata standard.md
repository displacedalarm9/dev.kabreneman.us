X‑00002_ — UNISYS Metadata Standard

(Constitutional Artifact — X‑Class)

Identity

Class: X‑Class (Cross‑System Constitutional Artifact)

ID: X‑00002_

Scope: Metadata rules governing all UNISYS subsystems

State: Active constitutional standard

Dependencies:

X‑00001_ Identity Constitution

G‑00001_ Governance Overview

AUTOENV (environment substrate)

DOCSYS (document subsystem)

SyncKit (transport layer)

AE‑RPG (AUTOENV pawn daemon)

1. Purpose of the Metadata Standard

This Standard defines the required metadata fields, their semantics, inheritance rules, and immutability constraints for all UNISYS artifacts.

Metadata is the connective tissue between:

DOCSYS

SyncKit

AUTOENV

AE‑RPG

PMFs

Pages

Reports

Validations

Reviews

Without a unified metadata standard, identity cannot be preserved, SyncKit cannot sync safely, and AE‑RPG cannot generate deterministic outputs.

2. Required Metadata Fields

Every governed artifact must contain the following fields:

Field

Description

Rules

TSN

Trace Serial Number (event identity)

Immutable; assigned first; shared across event lineage

AUID

Artifact Unique Identifier

Immutable; assigned after TSN; unique across system

UDIS

Unified Document/Devuce Instance Serial

Immutable; assigned only when instantiated/exported

Class

Artifact class (e.g., X, G, P, Q, W, F, R, A, V)

Immutable after assignment

Lifecycle

Fragment → Draft → Final → Published → Archived

Must be preserved by SyncKit

Title

Human‑readable artifact name

Editable; must not affect identity

CreatedBy

Originating operator or subsystem

Immutable

CreatedOn

Timestamp of creation

Immutable

Supersedes

AUID of prior artifact (if any)

Optional; immutable once set

SupersededBy

AUID of successor artifact

Optional; immutable once set

PMFPath

Path to Provenance Metadata File

Required for DOCSYS artifacts

3. Optional Metadata Fields

Optional fields may be included depending on class:

Tags

Subsystem (e.g., DOCSYS, AUTOENV, AE‑RPG)

TriggerEvent

ValidationStatus

ReviewStatus

ReportType

TemplateID

DataSource

Optional fields must never override required fields.

4. Metadata Inheritance Rules

4.1 TSN Inheritance

All derivative artifacts inherit the TSN of the originating event.

TSN must never be regenerated.

4.2 AUID Assignment

Every new artifact receives a new AUID.

Supersession does not reuse AUIDs.

4.3 UDIS Assignment

Only assigned when an artifact is instantiated/exported.

AE‑RPG must request a UDIS when generating a Report.

4.4 Lifecycle Inheritance

Lifecycle state is preserved across sync.

SyncKit must not alter lifecycle.

5. Metadata Immutability

The following fields are constitutionally immutable:

TSN

AUID

UDIS

CreatedBy

CreatedOn

Class

Any attempt to modify these must:

be rejected

logged

surfaced to Governance

AUTOENV daemons (including AE‑RPG) must treat immutable fields as read‑only.

6. Metadata Validation Requirements

All subsystems must validate metadata before accepting an artifact.

DOCSYS must validate:

identity completeness

lifecycle correctness

PMF presence

supersession chain integrity

SyncKit must validate:

identity preservation

lifecycle preservation

no silent overwrites

no collisions

no missing PMFs

AE‑RPG must validate:

input dataset structure

presence of required metadata

template compatibility

identity fields before generating output

7. Metadata and SyncKit

SyncKit must:

preserve all metadata fields

never generate identity fields

never modify identity fields

never modify lifecycle

detect collisions

surface conflicts

write PMFs atomically

sync Pages and PMFs together

SyncKit is the transport layer, not the identity authority.

8. Metadata and AE‑RPG

AE‑RPG must:

read metadata from DOCSYS artifacts

validate metadata before processing

generate R‑Class outputs with:

inherited TSN

new AUID

new UDIS

apply dynamic header/footer at instantiation

write PMFs for generated Reports

hand off to SyncKit for sync

AE‑RPG is a pawn daemon, not a metadata authority.

9. Metadata and PMFs

PMFs must contain:

TSN

AUID

UDIS (if applicable)

lifecycle

supersession chain

creation metadata

related artifacts

provenance notes

PMFs are the source of truth for artifact lineage.

10. Constitutional Authority

Only X‑Class artifacts may:

define metadata rules

modify metadata rules

supersede metadata rules

Governance (G‑Class) may interpret but not alter metadata rules.

AUTOENV daemons must comply with metadata rules.

DOCSYS must enforce metadata rules.

SyncKit must preserve metadata rules.

End of X‑00002_ — UNISYS Metadata Standard