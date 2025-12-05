import os
import sys
import time
from openai import OpenAI

client = OpenAI()
os.environ["OPENAI_API_KEY"] = ""

prompt_file = "analysis.prompt.md"
ontology_file = "agentic-o.ttl"
model_name = "gpt-5-mini"   # change as needed

# ---- argument handling ----
if len(sys.argv) < 2:
    print("Usage: python3 run_prompt.py <folder_path>")
    sys.exit(1)

folder = sys.argv[1]

if not os.path.isdir(folder):
    print(f"Error: folder does not exist: {folder}")
    sys.exit(1)

# ---- determine output path ----
outdir = "agent-o"
os.makedirs(outdir, exist_ok=True)

outname = os.path.basename(os.path.normpath(folder)) + "_instances.ttl"
outfile = os.path.join(outdir, outname)

# ---- skip if output already exists ----
if os.path.exists(outfile):
    print(f"Skipping {folder}: output file already exists -> {outfile}")
    sys.exit(0)

# ---- determine which source directory to use ----
src_dir = os.path.join(folder, "src")
#mastra_dir = os.path.join(folder, "mastra")

if os.path.isdir(src_dir):
    target_dir = src_dir
#elif os.path.isdir(mastra_dir):
#    target_dir = mastra_dir
else:
    target_dir = folder #Folder is the default target directory
##    print(f"Skipping {folder}: no src/ or mastra/ directory found.")
##    sys.exit(0)

# ---- load prompt ----
with open(prompt_file, "r", encoding="utf-8") as f:
    prompt_template = f.read()

# ---- load ontology ----
with open(ontology_file, "r", encoding="utf-8") as f:
    ontology_text = f.read()

# ---- read all files from folder ----
all_files = []
for root, _, files in os.walk(target_dir):
    for fn in files:
        path = os.path.join(root, fn)
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                txt = fh.read()
        except Exception as e:
            print(f"Skipping {path}: {e}")
            continue

        rel_path = os.path.relpath(path, folder)
        all_files.append(f"### {rel_path}\n\n```\n{txt}\n```")

source_code = "\n\n".join(all_files)

# ---- build prompt ----
prompt = prompt_template.replace("{{ontology}}", ontology_text)
prompt = prompt.replace("{{source_code}}", source_code)

# ---- run model and measure execution time ----
print(f"Processing folder: {folder}")

start_time = time.perf_counter()

response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are an expert in ontology population."},
        {"role": "user", "content": prompt},
    ],
)

end_time = time.perf_counter()
elapsed = end_time - start_time

# ---- collect model output ----
output_text = response.choices[0].message.content

# ---- add header ----
header_comment = (
    f"# Execution time: {elapsed:.2f} seconds\n"
    f"# Model used: {model_name}\n\n"
)

# ---- write output ----
with open(outfile, "w", encoding="utf-8") as f:
    f.write(header_comment)
    f.write(output_text)

print(f"Wrote output to {outfile}")
