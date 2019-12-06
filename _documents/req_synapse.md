
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
assumptions, learning occurs largely by forming *valid* synapses from potential
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
- [x] A synapse object shall be an instance of [BaseHTM](./req_basehtm.md) class.





#### References:
* Hierarchical Temporal Memory including HTM Cortical Learning Algorithms,  
Version 0.2.1 https://numenta.org/resources/HTM_CorticalLearningAlgorithms.pdf
* Hawkins, J. et al. 2016. Biological and Machine Intelligence.  
Release 0.4. Accessed at http://numenta.com/biological-and-machine-intelligence/.
