# MPOSE2021
#### A Dataset for Short-time Pose-based Human Action Recognition

This repository contains the MPOSE2021 Dataset for short-time pose-based Human Action Recognition (HAR). 

MPOSE2021 is developed as an evolution of the MPOSE Dataset [1-3]. It is made by human pose data detected by 
[OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) [4], [Posenet](https://github.com/google-coral/project-posenet) [11], and [Movenet](https://github.com/google-coral/pycoral/blob/master/examples/movenet_pose_estimation.py) on popular datasets for HAR, i.e. Weizmann [5], i3DPost [6], IXMAS [7], KTH [8], UTKinetic-Action3D (RGB only) [9] and UTD-MHAD (RGB only) [10], alongside original video datasets, i.e. ISLD and ISLD-Additional-Sequences [1].
Since these datasets have heterogenous action labels, each dataset labels are remapped to a common and homogeneous list of 20 actions.

This repository allows users to generate pose data for MPOSE2021 in a python-friendly format. 
Generated sequences have a number of frames between 20 and 30. 
Sequences are obtained by cutting the so-called Precursor videos (from the above-mentioned datasets), with non-overlapping sliding windows.
Frames where OpenPose/PoseNet/MoveNet cannot detect any subject are automatically discarded. Resulting samples contain one subject at a time, performing a fraction of a single action. Overall, MPOSE2021 contains 15429 samples, divided into 20 actions, performed by 100 subjects. 

Below, the steps to install the ```mpose``` library and obtain sequences are explained. Source code can be found in the [MPOSE2021 repository](https://github.com/PIC4SeRCentre/MPOSE2021_Dataset).

### Installation

Install MPOSE2021 as python package from [PyPi](https://pypi.org/project/mpose)
```
pip install mpose
```

### Getting Started

```python
# import package
import mpose

# initialize and download data
dataset = mpose.MPOSE(pose_extractor='openpose', 
                      split=1, # 1, 2, 3
                      preprocess=None, # scale_and_center, scale_to_unit
                      config_file=None, # specify custom configuration (debug)
                      velocities=False, # if True, computes additional veocity channels
                      remove_zip=False, # if True, removes zip files after extraction
                      overwrite=False, # if True, overwrites old zip files
                      verbose=True)

# print data info 
dataset.get_info()

# get data samples (as numpy arrays)
X_train, y_train, X_test, y_test = dataset.get_data()
```

Check out our [Colab Notebook Tutorial](https://colab.research.google.com/drive/1_v3DYwgZPMCiELtgiwMRYxQzcYGdSWFH?usp=sharing) for quick hands-on examples.

### Class methods

* `transform(fn=None, target='X')`: apply custom transformation function to the data.
  * `fn`: the function (fn(X) or fn(y))
  * `target`: the data target (X or y)
    
* `reduce_keypoints()`: reduce the number of keypoints grouping head and feet landmarks [1]
    
* `scale_and_center()`: center poses and resize to a common scale [1]

* `scale_to_unit()`: rescale all pose data between 0 and 1

* `add_velocities(overwrite=False)`: compute keypoint velocities and add them as new channels
  * `overwrite`: if True, recomputes velocities even if already present

* `remove_velocities()`: remove velocity channels (if present)

* `remove_confidence()`: remove confidence channel (if present)

* `flatten_features()`: flatten (keypoints,channels) dimensions

* `reduce_labels()`: map labels to a smaller set of actions (e.g. to realize small demos)

* `reset_data()`: restore original data

* `get_dataset(seq_id=False)`: get data samples (as numpy arrays)
  * `seq_id`: if True, returns also the lists of sample IDs correspondent to X_train and X_test
    
* `get_info()`: print a summary of dataset statistics
        
* `get_labels()`: get the list of action labels

### References

MPOSE2021 was presented in a [paper published by the Pattern Recognition Journal (Elsevier)](https://authors.elsevier.com/a/1eH6s77nKcvmg), and is intended for scientific research purposes.
If you want to use MPOSE2021 for your research work, please also cite [1-11].

```
@article{mazzia2021action,
  title={Action Transformer: A Self-Attention Model for Short-Time Pose-Based Human Action Recognition},
  author={Mazzia, Vittorio and Angarano, Simone and Salvetti, Francesco and Angelini, Federico and Chiaberge, Marcello},
  journal={Pattern Recognition},
  pages={108487},
  year={2021},
  publisher={Elsevier}
}
```

[1] Angelini, F., Fu, Z., Long, Y., Shao, L., & Naqvi, S. M. (2019). 2D Pose-Based Real-Time Human Action Recognition With Occlusion-Handling. IEEE Transactions on Multimedia, 22(6), 1433-1446.

[2] Angelini, F., Yan, J., & Naqvi, S. M. (2019, May). Privacy-preserving Online Human Behaviour Anomaly Detection Based on Body Movements and Objects Positions. In ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 8444-8448). IEEE.

[3] Angelini, F., & Naqvi, S. M. (2019, July). Joint RGB-Pose Based Human Action Recognition for Anomaly Detection Applications. In 2019 22th International Conference on Information Fusion (FUSION) (pp. 1-7). IEEE.

[4] Cao, Z., Hidalgo, G., Simon, T., Wei, S. E., & Sheikh, Y. (2019). OpenPose: Realtime Multi-Person 2D Pose Estimation Using Part Affinity Fields. IEEE transactions on pattern analysis and machine intelligence, 43(1), 172-186.

[5] Gorelick, L., Blank, M., Shechtman, E., Irani, M., & Basri, R. (2007). Actions as Space-Time Shapes. IEEE transactions on pattern analysis and machine intelligence, 29(12), 2247-2253.

[6] Starck, J., & Hilton, A. (2007). Surface Capture for Performance-Based Animation. IEEE computer graphics and applications, 27(3), 21-31.

[7] Weinland, D., Özuysal, M., & Fua, P. (2010, September). Making Action Recognition Robust to Occlusions and Viewpoint Changes. In European Conference on Computer Vision (pp. 635-648). Springer, Berlin, Heidelberg.

[8] Schuldt, C., Laptev, I., & Caputo, B. (2004, August). Recognizing Human Actions: a Local SVM Approach. In Proceedings of the 17th International Conference on Pattern Recognition, 2004. ICPR 2004. (Vol. 3, pp. 32-36). IEEE.

[9] Xia, L., Chen, C. C., & Aggarwal, J. K. (2012, June). View Invariant Human Action Recognition using Histograms of 3D Joints. In 2012 IEEE computer society conference on computer vision and pattern recognition workshops (pp. 20-27). IEEE.

[10] Chen, C., Jafari, R., & Kehtarnavaz, N. (2015, September). UTD-MHAD: A Multimodal Dataset for Human Action Recognition utilizing a Depth Camera and a Wearable Inertial Sensor. In 2015 IEEE International conference on image processing (ICIP) (pp. 168-172). IEEE.

[11] Papandreou, G., Zhu, T., Chen, L. C., Gidaris, S., Tompson, J., & Murphy, K. (2018). Personlab: Person Pose Estimation and Instance Segmentation with a Bottom-Up, Part-Based, Geometric Embedding Model. In Proceedings of the European Conference on Computer Vision (ECCV) (pp. 269-286).