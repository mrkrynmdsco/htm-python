
# Segment

### Description
Segments (dendrite) are where the synapses connects. There are two types of dendrite segments, proximal and
distal.
- A *proximal segment* segment forms synapses with feed-forward inputs. The active synapses on this
type of segment are linearly summed to determine the feed- forward activation of a column.
- A *distal segment* segment forms synapses with cells within the layer. Every cell has many distal
dendrite segments. If the sum of the active synapses on a distal segment exceeds a threshold, then the
associated cell enters the predicted state. Since there are multiple distal dendrite segments per cell, a
cell’s predictive state is the logical OR operation of several constituent threshold detectors.

### Functional Requirements

##### HTM-FR-SEG_01
- [x] A segment object shall inherit the [BaseHTM](./req_basehtm.md) class.



#### References:
* Hierarchical Temporal Memory including HTM Cortical Learning Algorithms,
Version 0.2.1 https://numenta.org/resources/HTM_CorticalLearningAlgorithms.pdf
* Hawkins, J. et al. 2016. Biological and Machine Intelligence.
Release 0.4. Accessed at http://numenta.com/biological-and-machine-intelligence/.
