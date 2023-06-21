docker_run_tf:
	docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu
docker_run_tf_nvidia:
	docker run --gpus all -it --rm nvcr.io/nvidia/tensorflow:21.11-tf2-py3
docker_run_torch_nvidia:
	docker run --gpus all -it --rm nvcr.io/nvidia/pytorch:23.05-py3