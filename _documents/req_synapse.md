
# Synapse

### Description
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

Synapses on an HTM cell have a binary weight. There is nothing in the HTM model
that precludes scalar synapse weights, but due to the use of sparse distributed
patterns we have not yet had a need to use scalar weights.

However, synapses on an HTM cell have a scalar value called *permanence* which is
adjusted during learning. A `0.0` permanence value represents a potential synapse
which is not valid and has not progressed at all towards becoming a valid synapse.
A permanence value above a threshold (typically `0.2`) represents a synapse that has
just connected but could easily be un-connected. A high permanence value, for
example `0.9`, represents a synapse that is connected and cannot easily be unconnected.

The number of valid synapses on the proximal and distal dendrite segments of an
HTM cell is not fixed. It changes as the cell is exposed to patterns. For example, the
number of valid synapses on the distal dendrites is dependent on the temporal
structure of the data. If there are no persistent temporal patterns in the input to the
region, then all the synapses on distal segments would have low permanence values
and very few synapses would be valid. If there is a lot of temporal structure in the
input stream, then we will find many valid synapses with high permanence.

### Functional Requirements

##### HTM-FR-SYN_01
- [x] A synapse object shall be an instance of [HTM Object](./req_htmobject.md) class.

##### HTM-FR-SYN_02
- [x] A synapse object shall have only two (2) states.

    > `INACTIVE` -- (*default*) this value indicates that the object is *not active*

    > `ACTIVE` -- this value indicates that the object is *active*

##### HTM-FR-SYN_03
- [x] A synapse object shall have a scalar property that describe its **permanence** value.

    > `0.0` -- (*minimum*, *default*) represents a potential synapse which is not valid and has not progressed at all

    > `1.0` -- (*maximum*) represents a potential synapse that is fully connected  

##### HTM-FR-SYN_04
- [x] The synapse object's **permanence** value shall be able to be *incremented* within its range.
- [x] The synapse object's **permanence** value shall be able to be *decremented* within its range.

##### HTM-FR-SYN_05
- [x] A synapse object shall have a configurable scalar property that represents its **connection threshold** that shall be used as a measure of permanence status.

    > `0.3 <= connection_threshold >= 0.75`  
    > `0.6` -- *default*

##### HTM-FR-SYN_06
- [ ] A synapse object shall be able to change its **state** depending on the value of its **permanence** and the **connection threshold**.

    > `if (permanence >= connection_threshold) then state = ACTIVE`  

    > `if (permanence < connection_threshold) then state = INACTIVE`  

##### HTM-FR-SYN_07
- [x] A synapse object shall have a configurable scalar property that represents its **learning rate** that serves as a parameter of how fast the object will reach the **connecton threshold** of **permanence** and become `ACTIVE`.

    > `0.0 <= learning_rate >= 1.0`  
    > `0.03` -- *default*

##### HTM-FR-SYN_08
- [x] A synapse object shall be able to store the index of the cell (**connection index**) where it is connected or trying to connect to.  

    > `None` -- *default*

##### HTM-FR-SYN_09
- [ ] A synapse object shall be able to *update* all its adjustable parameters (e.g. *state*, *permanence*, *connection index*) during runtime.




#### References:
* Hierarchical Temporal Memory including HTM Cortical Learning Algorithms, version [0.2.1](https://numenta.org/resources/HTM_CorticalLearningAlgorithms.pdf)
