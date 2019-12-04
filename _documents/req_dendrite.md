
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



#### References:
* Hierarchical Temporal Memory including HTM Cortical Learning Algorithms, version [0.2.1](https://numenta.org/resources/HTM_CorticalLearningAlgorithms.pdf)
* Biological and Machine Intelligence, Hawkins, J. et al. 2016, release [0.4](https://numenta.com/resources/biological-and-machine-intelligence/)
