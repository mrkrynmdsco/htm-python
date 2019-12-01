
# Synapse
A typical neuron might have several thousand synapses. The large majority
(perhaps 90%) of these will be on distal dendrites, and the rest will be on proximal
dendrites.

For many years it was assumed that learning involved strengthening and weakening
the effect or *weight* of synapses. Although this effect has been observed, each
synapse is somewhat stochastic. When activated, it will not reliably release a
neurotransmitter. Therefore the algorithms used by the brain cannot depend on
precision or fidelity of individual synapse weights.

Further, we now know that entire synapses form and un-form rapidly. This
flexibility represents a powerful form of learning and better explains the rapid
acquisition of knowledge. A synapse can only form if an axon and a dendrite are
within a certain distance, leading to the concept of *potential synapses*. With these
assumptions, learning occurs largely by forming **valid** synapses from potential
synapses.



## Functional Requirements
- [ ] 1. A synapse object state shall be binary.
    > `INACTIVE` -- (*default*) this value indicates that the object is **not** active
    > `ACTIVE` -- this value indicates that the object is active
- [ ] 2. A synapse object shall have a scalar property that describe its **permanence** value.
    > `0.0` -- (*minimum*) represents a potential synapse which is not valid and has not progressed at all
    > `1.0` -- (*maximum*) represents a potential synapse that is fully connected
- [ ] 3. The synapse object's **permanence** value shall be adjustable within its range dynamically.
- [ ] 4. A synapse object shall have a scalar threshold property that shall be used as a measure of permanence status.
    > `if (permanence >= threshold) then ACTIVE`
    > `if (permanence < threshold) then INACTIVE`




### References:
* Hierarchical Temporal Memory including HTM Cortical Learning Algorithms, version [0.2.1](https://numenta.org/resources/HTM_CorticalLearningAlgorithms.pdf)
