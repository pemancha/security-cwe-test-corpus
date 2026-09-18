# Benchmark methodology

## Unit of evaluation

One scenario pair contains the same security behavior in vulnerable and remediated form. The vulnerable file has one expected CWE finding and exact sink line. The fixed file is a negative control.

## Metrics

- **True positive:** the scanner reports the expected CWE against the vulnerable path.
- **False negative:** the expected vulnerable path/CWE pair is absent.
- **False positive:** the scanner reports the expected CWE against the paired fixed path.
- **Precision:** `TP / (TP + FP)`.
- **Recall:** `TP / (TP + FN)`.
- **F1:** harmonic mean of precision and recall.

File-level scanners can be scored on path and CWE. Line-capable scanners should additionally compare the reported region with the expected sink line.

## Test integrity

The repository validator confirms counts, schema consistency, unique scenario identifiers, file existence, path containment, one vulnerable marker, no marker in fixed controls, and synchronized aggregate ground truth.

## Limitations

Small deterministic fixtures measure pattern recognition and workflow correctness. They do not reproduce the architectural complexity, framework behavior, build systems, or data flow of production applications. Results must not be presented as a complete product efficacy assessment.
