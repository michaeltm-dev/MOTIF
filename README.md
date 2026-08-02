# MOTIF Reproducibility Audit (Critical Report)

This repository README was rewritten as a reproducibility audit based on the local run artifacts in [run_cfg](run_cfg) and [results](results).

The short version: local reruns do not match the magnitude or behavior claimed by the paper figures/tables for the tested settings, and the optimization pipeline appears dominated by Phase 1 with minimal useful contribution from Phase 2.

## Scope

This report summarizes only what is observable in this workspace:

- Run logs in [run_cfg/tsp_gls](run_cfg/tsp_gls), [run_cfg/tsp_aco](run_cfg/tsp_aco), [run_cfg/cvrp_aco](run_cfg/cvrp_aco), [run_cfg/tsp_aco_5.4_mini](run_cfg/tsp_aco_5.4_mini)
- JSON logs in [results](results)
- Current baseline implementations in [problems/tsp_aco](problems/tsp_aco) and [problems/cvrp_aco](problems/cvrp_aco)
- Current execution flow in [src/controller.py](src/controller.py) and [src/final_round.py](src/final_round.py)

## Main Findings

1. Experimental setting mismatch versus paper narrative.
- Local artifacts show 5 logged reruns for multiple tracks (for example [run_cfg/tsp_gls](run_cfg/tsp_gls), [run_cfg/tsp_aco](run_cfg/tsp_aco), [run_cfg/cvrp_aco](run_cfg/cvrp_aco)), while the referenced table/figure text is presented as 3-run summaries.
- Optimization is evaluated in train mode (see subprocess call with train argument in [src/controller.py](src/controller.py) and [src/final_round.py](src/final_round.py)).
- TSP train dataset generators currently hardcode 5 training instances in [problems/tsp_aco/generator.py](problems/tsp_aco/generator.py) and [problems/tsp_gls/generator.py](problems/tsp_gls/generator.py).

2. TSP-GLS table behavior is near-zero in local reruns.
- Across [run_cfg/tsp_gls/run_1.stdout](run_cfg/tsp_gls/run_1.stdout), [run_cfg/tsp_gls/run_2.stdout](run_cfg/tsp_gls/run_2.stdout), [run_cfg/tsp_gls/run_3.stdout](run_cfg/tsp_gls/run_3.stdout), [run_cfg/tsp_gls/run_4.stdout](run_cfg/tsp_gls/run_4.stdout), [run_cfg/tsp_gls/run_5.stdout](run_cfg/tsp_gls/run_5.stdout), Round 1 gains are ~0.00% to 0.04%, and Final Round is usually 0.00% (one run shows 0.06%).
- This is inconsistent with any narrative that implies broad meaningful GLS gains across sizes.

3. Figure-style improvement magnitudes are not reproduced for ACO-TSP and ACO-CVRP.
- TSP ACO with gpt-4o-mini config: Round 1 is around 11.49% to 11.95% in [run_cfg/tsp_aco](run_cfg/tsp_aco), often below a 12% threshold.
- TSP ACO with gpt-5.4-mini config: Round 1 is around 12.11% to 12.45% in [run_cfg/tsp_aco_5.4_mini](run_cfg/tsp_aco_5.4_mini), but Final Round remains 0.00%.
- CVRP ACO: Round 1 is around 1.50% to 6.65% in [run_cfg/cvrp_aco](run_cfg/cvrp_aco), far from high-improvement curves such as 50% to 30% decline patterns shown in the provided figure.

4. Phase 2 contribution is typically negligible.
- Final Round improvements are overwhelmingly 0.00%, with rare tiny values (for example 0.01%, 0.11%, 0.21%) in [run_cfg/tsp_aco](run_cfg/tsp_aco) and [run_cfg/cvrp_aco](run_cfg/cvrp_aco).
- This aligns with the claim that the two-phase narrative is weak in practice: most measurable gain comes from Phase 1.

5. ACO baselines are extremely naive and likely bottleneck meaningful differentiation.
- TSP ACO baseline code in [problems/tsp_aco/F1.py](problems/tsp_aco/F1.py), [problems/tsp_aco/F2.py](problems/tsp_aco/F2.py), [problems/tsp_aco/F3.py](problems/tsp_aco/F3.py) uses simple inverse-distance heuristic, fixed alpha/beta, and basic evaporation/deposit.
- CVRP ACO baseline code in [problems/cvrp_aco/F1.py](problems/cvrp_aco/F1.py), [problems/cvrp_aco/F2.py](problems/cvrp_aco/F2.py), [problems/cvrp_aco/F3.py](problems/cvrp_aco/F3.py) is similarly simplistic.
- If the baseline is this weak and coarse, large claims such as expert-level strategic superiority require stronger controls and significantly better ablations.

6. Model upgrade signal is weak relative to claimed framework effect.
- Config switch from gpt-4o-mini to gpt-5.4-mini is visible in [run_cfg/tsp_aco/config.yaml](run_cfg/tsp_aco/config.yaml) and [run_cfg/tsp_aco_5.4_mini/config.yaml](run_cfg/tsp_aco_5.4_mini/config.yaml).
- Local outcomes remain very similar in structure (Round 1 around low-teens, Phase 2 near zero), suggesting limited practical sensitivity in this setup.

## Extracted Run Summaries

### TSP GLS (5 reruns)

- [run_cfg/tsp_gls/run_1.stdout](run_cfg/tsp_gls/run_1.stdout): Round 1 0.00%, Final Round 0.00%
- [run_cfg/tsp_gls/run_2.stdout](run_cfg/tsp_gls/run_2.stdout): Round 1 0.04%, Final Round 0.00%
- [run_cfg/tsp_gls/run_3.stdout](run_cfg/tsp_gls/run_3.stdout): Round 1 0.04%, Final Round 0.00%
- [run_cfg/tsp_gls/run_4.stdout](run_cfg/tsp_gls/run_4.stdout): Round 1 0.01%, Final Round 0.06%
- [run_cfg/tsp_gls/run_5.stdout](run_cfg/tsp_gls/run_5.stdout): Round 1 0.00%, Final Round 0.00%

### TSP ACO with gpt-4o-mini (5 reruns)

- [run_cfg/tsp_aco/run_1.stdout](run_cfg/tsp_aco/run_1.stdout): Round 1 11.52%, Final Round 0.00%
- [run_cfg/tsp_aco/run_2.stdout](run_cfg/tsp_aco/run_2.stdout): Round 1 11.95%, Final Round 0.01%
- [run_cfg/tsp_aco/run_3.stdout](run_cfg/tsp_aco/run_3.stdout): Round 1 11.52%, Final Round 0.21%
- [run_cfg/tsp_aco/run_4.stdout](run_cfg/tsp_aco/run_4.stdout): Round 1 11.84%, Final Round 0.00%
- [run_cfg/tsp_aco/run_5.stdout](run_cfg/tsp_aco/run_5.stdout): Round 1 11.49%, Final Round 0.00%

### TSP ACO with gpt-5.4-mini (3 reruns)

- [run_cfg/tsp_aco_5.4_mini/run_1.stdout](run_cfg/tsp_aco_5.4_mini/run_1.stdout): Round 1 12.16%, Final Round 0.00%
- [run_cfg/tsp_aco_5.4_mini/run_2.stdout](run_cfg/tsp_aco_5.4_mini/run_2.stdout): Round 1 12.11%, Final Round 0.00%
- [run_cfg/tsp_aco_5.4_mini/run_3.stdout](run_cfg/tsp_aco_5.4_mini/run_3.stdout): Round 1 12.45%, Final Round 0.00%

### CVRP ACO (5 reruns)

- [run_cfg/cvrp_aco/run_1.stdout](run_cfg/cvrp_aco/run_1.stdout): Round 1 3.72%, Final Round 0.00%
- [run_cfg/cvrp_aco/run_2.stdout](run_cfg/cvrp_aco/run_2.stdout): Round 1 1.50%, Final Round 0.00%
- [run_cfg/cvrp_aco/run_3.stdout](run_cfg/cvrp_aco/run_3.stdout): Round 1 3.14%, Final Round 0.00%
- [run_cfg/cvrp_aco/run_4.stdout](run_cfg/cvrp_aco/run_4.stdout): Round 1 6.65%, Final Round 0.00%
- [run_cfg/cvrp_aco/run_5.stdout](run_cfg/cvrp_aco/run_5.stdout): Round 1 2.62%, Final Round 0.11%

## Bottom Line

Based on the current code and run artifacts in this repository:

- Claimed figure/table magnitudes are not reproduced by these reruns.
- Phase 2 contribution is mostly negligible.
- Baseline ACO formulation is too naive to support strong high-level claims without stricter controls.
- Model upgrades do not produce a corresponding qualitative shift in outcome patterns here.

Anyone using this project should treat paper-level performance claims as unverified unless they can be reproduced under explicitly matched settings, datasets, seeds, and evaluation protocol.

## Reproduction Pointers

- Configurations used for these reruns: [run_cfg](run_cfg)
- Runtime entry point: [main.py](main.py)
- Evaluation scripts: [problems/tsp_aco/eval.py](problems/tsp_aco/eval.py), [problems/cvrp_aco/eval.py](problems/cvrp_aco/eval.py), [problems/tsp_gls/eval.py](problems/tsp_gls/eval.py)
- Logged structured results: [results](results)
