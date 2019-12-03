
# Dendrite

### Description
Dendrite segments are where the synapses connects. There are two types of dendrite segments, proximal and
distal.
- A *proximal dendrite* segment forms synapses with feed-forward inputs. The active synapses on this
type of segment are linearly summed to determine the feed- forward activation of a column.
- A *distal dendrite* segment forms synapses with cells within the layer. Every cell has many distal
dendrite segments. If the sum of the active synapses on a distal segment exceeds a threshold, then the
associated cell enters the predicted state. Since there are multiple distal dendrite segments per cell, a
cell’s predictive state is the logical OR operation of several constituent threshold detectors.

### Functional Requirements

##### HTM-FR-DEN_01
- [x] A dendrite object shall inherit the [HTM Object](./req_htmobject.md) class.

##### HTM-FR-DEN_02
- [ ] A dendrite object shall have a list of synapses that are connected to it.

##### HTM-FR-DEN_03
- [ ] A dendrite object shall have a configurable scalar property that represents the *maximum number of synapses* allowed to connect.

    > `16` -- *default*

##### HTM-FR-DEN_04
- [ ] A dendrite object shall be able to change its state to `ON` whenever there is enough number of active synapses reach or exceeds its **activation threshold**

##### HTM-FR-DEN_05
- [ ] A dendrite object shall be able to remember the **potential synapses** that caused it to become `ON`.

##### HTM-FR-DEN_06
- [ ] A dendrite object shall be able to initiate an increment or decrement of each potential synapse's permanence.

##### HTM-FR-DEN_07
- [ ] A dendrite object shall be able to initiate the update of its synapses.



#### References:
* Hierarchical Temporal Memory including HTM Cortical Learning Algorithms, version [0.2.1](https://numenta.org/resources/HTM_CorticalLearningAlgorithms.pdf)
* Biological and Machine Intelligence, Hawkins, J. et al. 2016, release [0.4](https://numenta.com/resources/biological-and-machine-intelligence/)
