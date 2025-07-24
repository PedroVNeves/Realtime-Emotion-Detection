import kagglehub

# Download latest version
path = kagglehub.dataset_download("davilsena/ckdataset")

print("Path to dataset files:", path)