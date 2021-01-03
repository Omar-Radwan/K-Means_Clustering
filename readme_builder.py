import os

iterations = 30
run_path = "./readme-assets"
run_subfiles = os.listdir(run_path)

for file_in_run in os.listdir(run_path):
    label_path = run_path + f"/{file_in_run}"
    if os.path.isdir(label_path):
        label_subfiles = os.listdir(label_path)
        cnt = 0
        centroids, samples, cur_itr = "", "", 0
        for file_in_label in label_subfiles:
            if (file_in_label.endswith('png')):
                if (cur_itr <= 30):
                    centroids += f"![]({label_path}/{file_in_label})"
                else:
                    samples += f"![]({label_path}/{file_in_label})"
                cur_itr += 1
        print(f"Centroids from Cluster {file_in_run}")
        print(" ")
        print(" ")
        print(centroids)
        print(" ")
        print(" ")
        print(f"Samples from Cluster {file_in_run}")
        print(" ")
        print(" ")
        print(samples)
        print(" ")
        print(" ")
