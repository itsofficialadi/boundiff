---
name: performance-investigation
description: Diagnose a measured latency, memory, throughput, or resource regression and propose the smallest supported optimization. Use for performance questions; measure before tuning.
---

# Performance investigation

A faster-looking implementation is not necessarily faster. Start with the metric and workload, not the optimization technique. Diagnosis is read-only by default.

1. Define the symptom: p50/p95/p99 latency, throughput, CPU, memory, allocation, query count, or another measurable target. Identify representative inputs and hardware/environment when known.
2. Establish a baseline using existing traces, profiles, metrics, or a reproducible benchmark. If you cannot measure, label the work as hypothesis generation.
3. Narrow the hot path. Check algorithmic work, I/O, database access, serialization, memory pressure, caching, network, and concurrency only where evidence points.
4. Compare candidate remedies by expected benefit, correctness risk, complexity, and blast radius. Avoid architecture changes justified by a microbenchmark alone.
5. On explicit optimization requests, make one bounded change using `$surgical-change`; preserve correctness and measure the same workload again. Otherwise report the recommendation without edits.
6. Record before/after conditions and noise. Do not extrapolate an isolated local benchmark to production SLOs.

## Output

**Metric and workload**, **baseline evidence**, **bottleneck**, **proposed or authorized change**, **post-change evidence if run**, **limits**. Report measurements with units and sample conditions.
