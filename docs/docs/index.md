# GenAI Intensive Course with Gemini SDK documentation!

## Description

GenAI Intensive Course with Gemini by Kaggle

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `gsutil rsync` to recursively sync files in `data/` up to `gs://bucket-genai/data/`.
* `make sync_data_down` will use `gsutil rsync` to recursively sync files in `gs://bucket-genai/data/` to `data/`.


