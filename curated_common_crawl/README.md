# Data cleaning pipeline

Source code: `mangosteen` branch on [https://github.com/wannaphong/dolma](https://github.com/wannaphong/dolma)

## Install

```
pip install -R https://github.com/wannaphong/dolma/raw/refs/heads/mangosteen/requirements.txt

pip install https://github.com/wannaphong/dolma/archive/refs/heads/mangosteen.zip
```

## Usage

First, Dataset should be in jsonl file like:

```
{"text": "text1”", "metadata": {"url": "http://test1.com/index.html"}, "id": "1"}
{"text": "text2", "metadata": {"url": "http://test2.com/index.html"}, "id": "2"}
{"text": "text3", "metadata": {"url": "http://test2.com/index.html"}, "id": "3"}
```

See more: [https://github.com/allenai/dolma/blob/main/docs/data-format.md](https://github.com/allenai/dolma/blob/main/docs/data-format.md)

And save file to `name_dataset/documents/` like `data/documents/fw2.jsonl`.

Finally, run `bash run_all.sh` file. You will give file in `mix-data/documents/`.