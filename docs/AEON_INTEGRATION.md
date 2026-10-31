# AEON → LibreOne integration

LibreOne incorporates the AEON architecture as its native C systems/AI-compute track.

## Source status

AEON currently has no `LICENSE` file. Therefore LibreOne must not wholesale-copy or redistribute AEON source as if it were open-source. This integration records the complete source inventory and maps AEON capabilities into LibreOne for controlled migration/reimplementation.

Source repository: https://github.com/CMKIXVI/AEON
Source head: 8211dae679561e5f885d7bbddeee48fd951de9b5

## Migration rule

- Preserve LibreOne as the product and repository identity.
- Migrate capabilities, contracts, tests, and architecture from AEON.
- Reimplement or import code only when licensing/ownership permits it.
- Do not silently duplicate AEON source under a new name.
- Every migrated native capability must have a LibreOne-owned API boundary and tests.

## AEON capability tracks

1. Runtime: native runtime and runtime memory.
2. Tensor: tensor objects, layout, views, bindings, materialization and cache.
3. Models: model index, manifest, stream, storage and NVMe queue reads.
4. Compute: transformer compute and cognitive compute.
5. Cognition: cognitive core, cognitive engine, active inference, causal graph, episodic memory and global workspace.
6. Security: identity, cryptographic verification, semantic framing, semantic gate and friction/attestation.
7. System embodiment: CPU capability detection, memory regions, sensors, tool bus and actuator policy.
8. Kernel boundaries: syscall, process, I/O, eBPF, kernel-device and network-policy adapters.
9. Validation: AEON batch tests and production-readiness documentation.

## LibreOne target placement

`libreone/native/` is the target native foundation for capabilities migrated from AEON.

- `native/runtime` → LibreOne runtime foundation
- `native/tensor` → AI tensor/runtime substrate
- `native/model` → model storage/index/streaming
- `native/compute` → native compute
- `native/cognition` → intelligence substrate
- `native/security` → trusted execution and semantic security
- `native/device` → hardware/device abstraction
- `native/kernel` → kernel-facing boundaries

The existing Python `libreone/system` layer remains the orchestration/control-plane layer. Native capabilities must not bypass its lifecycle, policy, authorization, audit and resource contracts.

## Acceptance gate

AEON functionality is not considered production-ready in LibreOne merely because the source exists. Each migrated subsystem requires:

1. LibreOne API contract.
2. Deterministic tests.
3. Strict native compilation.
4. Python/native integration tests where applicable.
5. Security and resource-boundary tests.
6. CI verification.
7. Hardware validation when the subsystem claims hardware behavior.

## Current decision

Pull the **capabilities and contracts** from AEON into LibreOne, but do not wholesale-copy the unlicensed AEON source. Once an explicit license/permission suitable for redistribution exists, source-level migration can be performed under that license.
