# 🚗 My Donkeycar ROS Robot: 端到端自动驾驶系统开发与部署

## 项目概述 (Project Overview)

这是一个基于 **NVIDIA Donkeycar** 框架与 **ROS (机器人操作系统)** 构建的端到端自动驾驶小车项目。本项目旨在实现自动驾驶小车从**感知（摄像头图像）到决策（转向、油门指令）**的全流程自主控制。作为大一学生，我通过独立搭建开发环境、处理真实数据、训练AI模型并将其部署到实际硬件，深入理解了具身智能（Embodied AI）系统的核心原理与实践挑战。

## 核心功能 (Key Features)

*   **端到端自主驾驶 (End-to-End Autonomous Driving):** 基于深度学习模型，实现小车根据实时图像自主做出驾驶决策。
*   **ROS (Robot Operating System) 集成:** 与小车现有 ROS 话题进行实时数据交互，包括图像订阅和控制指令发布。
*   **数据驱动的行为克隆 (Behavioral Cloning):** 通过模仿人类驾驶数据进行模型训练，使AI学习驾驶策略。
*   **模块化与可扩展性:** 系统采用Donkeycar框架，便于未来集成更多传感器或更复杂的AI模型。
*   **远程开发与版本控制:** 采用专业工具链进行高效开发与协作。

## 我的角色与贡献 (My Role & Contributions)

作为项目主要开发人员，我负责了从环境搭建到模型部署的全过程，尤其在解决复杂系统兼容性问题上积累了宝贵经验：

*   **🔧 独立完成复杂开发环境搭建与优化：**
    *   在 **VirtualBox Ubuntu 虚拟机**中，从零开始搭建并配置了完整的 **Donkeycar v5.2 深度学习框架**及 **ROS (Noetic)** 开发环境。
    *   系统性解决了 **Python 3.11** 下 `NumPy`、`TensorFlow 2.15`、`OpenCV`、`albumentations`、`pycryptodomex`、`python-gnupg` 等核心库之间的**版本冲突及依赖问题**，确保了所有组件的兼容运行。
    *   成功配置了虚拟机与真实 NVIDIA 计算平台小车之间的 **SSH** 远程连接与 **ROS 网络通信** (`ROS_MASTER_URI`, `ROS_IP` 环境变量)，建立了稳定的数据传输链路。
*   **🎮 ROS 小车手动控制与可视化：**
    *   熟练运用 **ROS `teleop_twist_keyboard`** 键盘/手柄遥控工具，实现了小车的精确运动控制与测试。
    *   掌握 `rostopic list/echo` 等 ROS 命令，能够实时监听、分析和调试 ROS 话题数据流。
    *   利用 **RViz** (机器人操作系统可视化工具) 对小车传感器数据（如摄像头图像）和 ROS 消息进行实时可视化，辅助系统调试。
*   **📊 高效数据管道构建与管理：**
    *   针对 Donkeycar v5.2 新旧数据格式兼容性问题，**定制开发了 `bag2donkey_manual.py` 脚本**。该脚本能够**直接**将 ROS `.bag` 原始数据包（包含摄像头图像和人类控制指令）高效转换为 Donkeycar 5.2 兼容的 **Tub v2 数据格式**（包含 `manifest.json`），彻底解决了 `cv_bridge` 及官方转换工具的兼容性难题。
    *   实现了多份 `.bag` 数据包（例如来自不同队友）的整合与处理，为模型训练提供了丰富、统一且高质量的数据集。
*   **🧠 端到端AI模型训练与ROS部署：**
    *   利用 Donkeycar 框架，基于处理后的 Tub v2 数据集，训练了 **KerasLinear 端到端行为克隆模型**，使 AI 学习了模拟人类的驾驶策略。
    *   设计并实现了 **`donkey_ros_inference.py` 脚本**作为 ROS 推理桥接节点。该节点能够实时订阅小车图像话题，通过加载训练好的 `.h5` 模型进行推理，将模型输出的 `steering` (转向) 和 `throttle` (油门) 值**实时转换为 ROS `geometry_msgs/Twist` 消息**，并发布至小车 `/cmd_vel` 话题，成功驱动小车自主驾驶。
*   **💻 专业 Git 版本控制与团队协作：**
    *   熟练运用 **VS Code Remote-SSH** 进行虚拟机环境下的远程代码开发、编辑与调试，大幅提升了开发效率。
    *   实践 **Git/GitHub** 进行版本控制，包括初始化仓库、创建个人开发分支 (`roxy_work`)、日常代码提交、以及遵循团队协作规范 (`.gitignore` 配置以排除大数据文件，并解决了 Git 权限管理及 `remote origin already exists` 等实际问题)。
    *   使用 **FileZilla** 等工具安全高效地在 Windows 宿主机与 Ubuntu 虚拟机之间传输大文件。

### 🧩 部署实战与问题解决 (Deployment & Troubleshooting)
*   **边缘侧直接部署方案 (Edge-Direct Deployment):** 在实车联调阶段，由于手机热点存在 AP 隔离，导致虚拟机与 ROS Master 握手失败。我成功验证并记录了通过 `scp` 指令将模型与推理脚本直接传输至小车板卡（Jetson/Ubuntu）运行的方案，绕过了网络延迟与隔离限制。
*   **多格式模型支持 (Multi-format Model Support):** 针对嵌入式端推理性能优化，实现了模型从 `.h5` 到 `.onnx` 格式的迁移，显著提升了在 NVIDIA 边缘计算平台上的兼容性。

## 技术栈 (Technical Stack)

*   **人工智能框架:** TensorFlow, Keras, Donkeycar (v5.2.dev6)
*   **机器人操作系统:** ROS (Noetic), ROS Bag
*   **编程语言:** Python (3.11), Shell Script
*   **开发环境:** Ubuntu 20.04 (VirtualBox), VS Code (Remote-SSH)
*   **版本控制:** Git, GitHub, `.gitignore`
*   **关键库:** NumPy, OpenCV, pycryptodomex, python-gnupg, typing-extensions, albumentations
*   **核心概念:** 端到端学习 (End-to-End Learning), 行为克隆 (Behavioral Cloning), 具身智能 (Embodied AI), ROS 节点通信, 远程开发。

## 项目成果展示 (Project Showcase)

*   **代码仓库:** `https://github.com/jiangyuhan0318-July/my_donkeycar_ros_robot`
    *   所有代码都已提交，包括自定义的 ROS 桥接脚本和数据转换脚本。
*   **模型文件:**
    *   仓库中 `my_pilot.onnx` 为优化后的 AI 大脑，可直接部署于支持 ONNX Runtime 的硬件环境。
    
## 学习心得与挑战 (Learning & Challenges)

在本项目中，我作为大一同学，独立面对并成功解决了以下核心挑战：

*   **深度学习环境配置的复杂性:** Python 版本管理、依赖冲突解决（例如 `numpy` 与 `tensorflow`、`opencv` 的版本兼容）。
*   **ROS 与非ROS系统的数据桥接:** 深入理解 ROS 话题机制与 Donkeycar 内部数据流，开发高效的转换脚本。
*   **Git 团队协作中的规范与问题:** 从 `remote origin already exists` 到 `403 Forbidden` 权限问题，再到 `.gitignore` 的精准配置，掌握了 Git 的实战运用。
*   **远程开发环境的稳定性与效率:** 克服了网络波动、SSH 连接中断等问题，保障了开发过程的顺畅。

通过这些挑战，我不仅掌握了扎实的技术技能，更培养了独立解决问题、查阅资料和持续学习的能力。

## 致谢 (Acknowledgements)

感谢我的组长和团队在项目中的指导与支持，让我在具身智能领域迈出了坚实的第一步。

---

# 🚗 My Donkeycar ROS Robot: End-to-End Autonomous Driving System Development & Deployment

## Project Overview

This project focuses on developing and deploying an end-to-end autonomous driving system for a small-scale robot car, built upon the **NVIDIA Donkeycar** framework and **ROS (Robot Operating System)**. The primary goal is to enable the robot car to perform autonomous control from **perception (camera images) to decision-making (steering and throttle commands)**. As a first-year university student, I gained a deep understanding of the core principles and practical challenges of embodied AI systems by independently setting up the development environment, processing real-world data, training AI models, and deploying them to actual hardware.

## Key Features

*   **End-to-End Autonomous Driving:** Implemented an AI model that enables the robot car to make autonomous driving decisions based on real-time camera imagery.
*   **ROS (Robot Operating System) Integration:** Achieved real-time data interaction with the robot car's existing ROS topics, including subscribing to image streams and publishing control commands.
*   **Data-Driven Behavioral Cloning:** Utilized human-driven data to train an AI model, allowing it to learn and replicate driving policies.
*   **Modularity & Extensibility:** The system leverages the Donkeycar framework, facilitating future integration of additional sensors or more complex AI models.
*   **Remote Development & Version Control:** Employed professional toolchains for efficient development and collaborative practices.

## My Role & Contributions

As a primary developer for this project, I was responsible for the entire process from environment setup to model deployment, gaining significant experience in resolving complex system compatibility issues:

*   **🔧 Independent Setup and Optimization of a Complex Development Environment:**
    *   Built and configured a comprehensive **Donkeycar v5.2 Deep Learning Framework** and **ROS (Noetic)** development environment from scratch within a **VirtualBox Ubuntu VM**.
    *   Systematically resolved **version conflicts and dependency issues** among core libraries (e.g., `NumPy`, `TensorFlow 2.15`, `OpenCV`, `albumentations`, `pycryptodomex`, `python-gnupg`) under **Python 3.11**, ensuring stable operation of all components.
    *   Successfully configured **SSH remote connection** and **ROS network communication** (`ROS_MASTER_URI`, `ROS_IP` environment variables) between the VM and the real NVIDIA computing platform robot car, establishing a robust data transmission link.
*   **🎮 ROS Robot Manual Control & Visualization:**
    *   Proficiently used **ROS `teleop_twist_keyboard`** (keyboard/joystick teleoperation) to achieve precise manual control and testing of the robot car.
    *   Mastered ROS commands such as `rostopic list/echo` to monitor, analyze, and debug ROS topic data streams in real-time.
    *   Utilized **RViz** (ROS Visualization tool) for real-time visualization of robot car sensor data (e.g., camera images) and ROS messages, aiding in system debugging.
*   **📊 Efficient Data Pipeline Construction & Management:**
    *   Developed a custom **`bag2donkey_manual.py` script** to address Donkeycar v5.2's new/old data format compatibility issues. This script efficiently and **directly converts raw ROS `.bag` data files** (containing camera images and human control commands) into Donkeycar 5.2 compatible **Tub v2 data format** (including `manifest.json`), thoroughly resolving `cv_bridge` and official converter tool compatibility challenges.
    *   Implemented the integration and processing of multiple `.bag` data packages (e.g., from different teammates), providing a rich, unified, and high-quality dataset for model training.
*   **🧠 End-to-End AI Model Training & ROS Deployment:**
    *   Leveraged the Donkeycar framework to train a **KerasLinear end-to-end behavioral cloning model** using the processed Tub v2 dataset, enabling the AI to learn human-like driving policies.
    *   Designed and implemented the **`donkey_ros_inference.py` script** to serve as a ROS inference bridge node. This node subscribes to the robot car's image topic in real-time, performs inference using the trained `.h5` model, **converts the model's `steering` and `throttle` outputs into ROS `geometry_msgs/Twist` messages** in real-time, and publishes them to the robot car's `/cmd_vel` topic, successfully achieving autonomous driving.
*   **💻 Professional Git Version Control & Team Collaboration:**
    *   Proficiently used **VS Code Remote-SSH** for remote code development, editing, and debugging within the VM environment, significantly boosting development efficiency.
    *   Practiced **Git/GitHub** for version control, including repository initialization, creating personal development branches (e.g., `roxy_work`), routine code commits, and adhering to team collaboration norms (e.g., `.gitignore` configuration to exclude large data files, and resolving practical issues like Git permissions and `remote origin already exists`).
    *   Utilized **FileZilla** for secure and efficient large file transfer between the Windows host and Ubuntu VM.

### 🧩 Deployment & Troubleshooting
*   **Edge-Direct Deployment:** During real-vehicle testing, a bi-directional ROS handshake failure occurred due to mobile hotspot AP isolation. I successfully validated a "Direct-to-Edge" deployment strategy using the `scp` command to transfer the model and inference scripts directly to the vehicle's onboard computer (Jetson/Ubuntu), bypassing network latency and isolation constraints.
*   **Multi-format Model Support:** Optimized for edge computing performance by migrating the model from Keras (`.h5`) to `ONNX` format, ensuring high-frame-rate inference and compatibility with NVIDIA TensorRT acceleration.

## Technical Stack

*   **AI Frameworks:** TensorFlow, Keras, Donkeycar (v5.2.dev6)
*   **Robot Operating System:** ROS (Noetic), ROS Bag
*   **Programming Languages:** Python (3.11), Shell Script
*   **Development Environment:** Ubuntu 20.04 (VirtualBox), VS Code (Remote-SSH)
*   **Version Control:** Git, GitHub, `.gitignore`
*   **Key Libraries:** NumPy, OpenCV, pycryptodomex, python-gnupg, typing-extensions, albumentations
*   **Core Concepts:** End-to-End Learning, Behavioral Cloning, Embodied AI, ROS Node Communication, Remote Development.

## Project Showcase

*   **Code Repository:** `https://github.com/jiangyuhan0318-July/my_donkeycar_ros_robot`
    *   All core code, including custom ROS bridge and data conversion scripts, has been committed.
*   **Models:**
    *   The `my_pilot.onnx` file in the repository is the optimized AI engine, ready for deployment on any hardware supporting ONNX Runtime.

## Learning & Challenges

As a first-year student, I independently encountered and successfully overcame the following key challenges during this project:

*   **Complexity of Deep Learning Environment Setup:** Managing Python versions and resolving dependency conflicts (e.g., `NumPy` vs. `TensorFlow`, `OpenCV` compatibility).
*   **Data Bridging Between ROS and Non-ROS Systems:** Gaining a deep understanding of ROS topic mechanisms and Donkeycar's internal data flow to develop efficient conversion scripts.
*   **Norms and Issues in Git Team Collaboration:** From resolving `remote origin already exists` and `403 Forbidden` permission issues to precisely configuring `.gitignore`, I mastered the practical application of Git.
*   **Stability and Efficiency of Remote Development Environments:** Overcoming challenges such as network fluctuations and SSH connection interruptions to ensure a smooth development process.

Through these challenges, I not only acquired solid technical skills but also developed strong abilities in independent problem-solving, research, and continuous learning.

## Acknowledgements

I would like to thank my team lead and colleagues for their guidance and support throughout this project, which allowed me to take a significant first step in the field of embodied AI.

---
