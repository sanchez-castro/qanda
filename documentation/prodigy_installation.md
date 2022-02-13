# Installation process

1. Get license
2. Create VM (allowing HTTP traffic)
3. Adjust HTTP [firewall rules in GCP](https://console.cloud.google.com/networking/firewalls/list) (to add a little bit more protection):
    
    `**Source IPv4 ranges**: YOUR_API`
    
4. SSH to VM to install install dependencies

```bash
# change root access
sudo su -

#update OS
apt-get update

#packages installation
apt-get install -y build-essential
apt-get install -y unzip libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils python3-pip python3-venv \
    python3-dev libopenblas-base libopenblas-dev

pip3 install --upgrade pip
pip3 install --upgrade setuptools
```

1. [Install prodigy](https://support.prodi.gy/t/suggestions-for-running-on-google-compute-engine/1259/3) with:

```bash
pip3 install prodigy -f https://1EBB-F166-A233-7866@download.prodi.gy/
```

1. Verify installation with:

```bash
python3 -m prodigy stats
```

1. Download some data

```bash
mkdir data && cd data && curl -X GET "https://raw.githubusercontent.com/explosion/prodigy-recipes/master/example-datasets/news_headlines.jsonl" > news_headlines2.jsonl
```

1. Run the script

```bash
PRODIGY_HOST=0.0.0.0 PRODIGY_PORT=80 python3 -m prodigy ner.manual ner_news_headlines blank:en ./data/news_headlines2.jsonl --label PERSON,ORGANIZATION,PRODUCT,LOCATION
```

1. Access with 

```bash
http://YOUR_API:80
```
