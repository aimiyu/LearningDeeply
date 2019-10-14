## Title

2019,Recsys, Google. Recommending what video to watch next: a multitask ranking system. [paper](https://dl.acm.org/citation.cfm?id=3346997)


## problem

- multiple competing ranking objectives
- implicit selection biases in user feedback


## Solution

1, extends the Wide & Deepmodel architecture by adopting Multi-gate Mixture-of-Experts (MMoE) [30] for multitask learning [9]

To learn and estimate multiple types of user behaviors, we use MMoE to automatically learn parameters to share across potentially conficting objectives.

The Mixture-of- Experts [21] architecture modularizes input layer into experts, each of which focuses on diferent aspects of input.
This improves the representation learned from complicated feature space generated from multiple modalities.
Then by utilizing multiple gating net- works, each of the objectives can choose experts to share or not share with others.

2, introduces a shallow tower to model and remove selection bias.

To model and reduce the selection bias (e.g., position bias) from biased training data, we propose to add a shallow tower to the main model.
 The shallow tower takes input related to the selection bias, e.g., ranking order decided by the current system, and outputs a scalar serving as a bias term to the fnal prediction of the main model.
 This model architecture factorizes the label in training data into two parts: the unbiased user utility learned from the main model, and the estimated propensity score learned from the shallow tower.


## details

multiple objectives into two categories:
 - 1) engagement objectives, such as user clicks, and degree of engagement with recommended videos;
 - 2) satisfaction objec- tives, such as user liking a video on YouTube, and leaving a rating on the recommendation.

## Refs
- [30] Jiaqi Ma, Zhe Zhao, Xinyang Yi, Jilin Chen, Lichan Hong, and Ed H Chi. 2018. Modeling task relationships in multi-task learning with multi-gate mixture-of- experts. In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. ACM, 1930–1939.
- [9] Heng-TzeCheng,LeventKoc,JeremiahHarmsen,TalShaked,TusharChandra,
Hrishi Aradhye, Glen Anderson, Greg Corrado, Wei Chai, Mustafa Ispir, et al. 2016. Wide & deep learning for recommender systems. In Proceedings of the 1st workshop on deep learning for recommender systems. ACM, 7–10.
