# XDC ETL


XDC ETL lets you convert blockchain data into convenient formats like CSVs and relational databases.

*Do you just want to query XDC data right away? Use the [public dataset in BigQuery](https://console.cloud.google.com/marketplace/details/ethereum/crypto-ethereum-blockchain).*

[Full documentation available here](http://xdc-etl.readthedocs.io/).

## Quickstart

Install XDC ETL:

```bash
pip3 install xdc-etl
```

Export blocks and transactions ([Schema](docs/schema.md#blockscsv), [Reference](docs/commands.md#export_blocks_and_transactions)):

```bash
> xdcetl export_blocks_and_transactions --start-block 0 --end-block 100000 \
--blocks-output blocks.csv --transactions-output transactions.csv \
--provider-uri Https://rpc.XDC.org
```

Export ERC20 and ERC721 transfers ([Schema](docs/schema.md#token_transferscsv), [Reference](docs/commands.md##export_token_transfers)):

```bash
> xdcetl export_token_transfers --start-block 0 --end-block 500000 \
--provider-uri file://$HOME/Library/Ethereum/geth.ipc --output token_transfers.csv
```

Export traces ([Schema](docs/schema.md#tracescsv), [Reference](docs/commands.md#export_traces)):

```bash
> xdcetl export_traces --start-block 0 --end-block 500000 \
--provider-uri file://$HOME/Library/Ethereum/parity.ipc --output traces.csv
```

---

Stream blocks, transactions, logs, token_transfers continually to console ([Reference](docs/commands.md#stream)):

```bash
> pip3 install xdc-etl[streaming]
> xdcetl stream --start-block 500000 -e block,transaction,log,token_transfer --log-file log.txt \
--provider-uri Https://rpc.XDC.org
```

Find other commands [here](https://xdc-etl.readthedocs.io/en/latest/commands/).

For the latest version, check out the repo and call 
```bash
> pip3 install -e . 
> python3 xdcetl.py
```


## Running Tests

```bash
> pip3 install -e .[dev,streaming]
> export ETHEREUM_ETL_RUN_SLOW_TESTS=True
> export PROVIDER_URL=<your_porvider_uri>
> pytest -vv
``` 

### Running Tox Tests

```bash
> pip3 install tox
> tox
```

## Running in Docker

1. Install Docker: https://docs.docker.com/get-docker/

2. Build a docker image
        
        > docker build -t xdc-etl:latest .
        > docker image ls
        
3. Run a container out of the image

        > docker run -v $HOME/output:/xdc-etl/output xdc-etl:latest export_all -s 0 -e 5499999 -b 100000 -p  Https://rpc.XDC.org
        > docker run -v $HOME/output:/xdc-etl/output xdc-etl:latest export_all -s 2018-01-01 -e 2018-01-01 -p  Https://rpc.XDC.org

4. Run streaming to console or Pub/Sub

        > docker build -t xdc-etl:latest .
        > echo "Stream to console"
        > docker run xdc-etl:latest stream --start-block 500000 --log-file log.txt
        > echo "Stream to Pub/Sub"
        > docker run -v /path_to_credentials_file/:/xdc-etl/ --env GOOGLE_APPLICATION_CREDENTIALS=/xdc-etl/credentials_file.json xdc-etl:latest stream --start-block 500000 --output projects/<your-project>/topics/crypto_ethereum

If running on Apple M1 chip add the `--platform linux/x86_64` option to the `build` and `run` commands e.g.:

```
docker build --platform linux/x86_64 -t xdc-etl:latest .
docker run --platform linux/x86_64 xdc-etl:latest stream --start-block 500000
```

## Projects using Ethereum ETL
* [Google](https://goo.gl/oY5BCQ) - Public BigQuery Ethereum datasets
* [Nansen](https://nansen.ai/query?ref=xdcetl) - Analytics platform for Ethereum
 ## Useful Links on Orginal ETH ETL

- [Schema](https://xdc-etl.readthedocs.io/en/latest/schema/)
- [Command Reference](https://xdc-etl.readthedocs.io/en/latest/commands/)
- [Documentation](https://xdc-etl.readthedocs.io/)
- [Public Datasets in BigQuery](https://github.com/blockchain-etl/public-datasets)  
- [Exporting the Blockchain](https://xdc-etl.readthedocs.io/en/latest/exporting-the-blockchain/)
- [Querying in Amazon Athena](https://xdc-etl.readthedocs.io/en/latest/amazon-athena/)
- [Querying in Google BigQuery](https://xdc-etl.readthedocs.io/en/latest/google-bigquery/)
- [Querying in Kaggle](https://www.kaggle.com/bigquery/ethereum-blockchain)
- [Airflow DAGs](https://github.com/blockchain-etl/xdc-etl-airflow)
- [Postgres ETL](https://github.com/blockchain-etl/xdc-etl-postgresql)
- [Ethereum 2.0 ETL](https://github.com/blockchain-etl/ethereum2-etl)

