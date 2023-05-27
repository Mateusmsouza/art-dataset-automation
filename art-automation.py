import os


SEEDS = [
    42,
    84,
    168,
    336
]

PROMPTS_FILES = [
    "prompts/file0.csv",
    "prompts/file1.csv",
    "prompts/file2.csv",
    "prompts/file3.csv",
    "prompts/file4.csv",
    "prompts/file5.csv",
    "prompts/file6.csv",
    "prompts/file7.csv",
    "prompts/file8.csv",
    "prompts/file9.csv",
]

def generate_images(seed: int):
    for prompts in PROMPTS_FILES:
        os.system(
            f"python3 scripts/txt2img.py --seed {seed} --from-file {prompts} " \
                "--ckpt v2-1_512-ema-pruned.ckpt --H 512 --W 512 " \
                "--config configs/stable-diffusion/v2-inference.yaml " \
                f"--n_samples 1 --n_iter 1 --outdir art-dataset/seed_{seed} --device cuda"
        )
 
if __name__ == "__main__":
    for seed in SEEDS:
        print(f"generating images for seed {seed}")
        generate_images(
            seed=seed
        )