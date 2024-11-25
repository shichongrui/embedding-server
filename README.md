# Embeddings Server

This is a basic embedding server using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python).

You can run it with:
```bash
fastapi run main.py
```

If you have multiple CPUs and would like to run multiple processes you can run
```bash
fastapi run --workers <num_workers> main.py
```

## Docker
There is also a docker image published to Github packages that can be used as well.

https://github.com/users/shichongrui/packages/container/package/embeddings-server

## Choosing a model

By default the server will use nomic-ai/nomic-embed-text-v1.5 model quantized to Q4_K_M.

You can use any GGUF model on HuggingFace by setting the following two environment variables
```bash
REPO_ID=<hugging-face-repo-id>
FILE_NAME=<quantized-file-name-to-use>
```

## Development

1. If you don't have a virtualenv yet, create one
```bash
python -m venv .venv
```
2. Activate the virutalenv
```bash
source .venv/bin/activate
```
3. Install dependencies
```bash
pip install -r 
```
4. Start the dev server
```bash
fastapi run main.py
```

## Deployment
1. Generate a Github API token
2. Log in to ghcr.io
```bash
echo <token> | docker login ghcr.io -u shichongrui --password-stdin
```
3. Build the image
```bash
docker build -t embeddings-server .
```
4. Tag the image
```bash
docker tag embeddings-server ghcr.io/shichongrui/embeddings-server:latest
```
5. Push the image
```bash
docker push ghcr.io/shichongrui/embeddings-server:latest
```
