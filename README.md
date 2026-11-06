# StockAverage: Extended Edition (WIP)

> The extended 2023 build of StockAverage: adds external configuration (`Configuration/Params.json`), native and server-side JSON databases and new parameters on top of the self-destruct release.

> **Status:** work in progress, external file fetching for the new parameters still needs a fix. For the stable build see [StockAverageSelfDestructWorking](https://github.com/optimus-node-js/StockAverageSelfDestructWorking).

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)

## Features

- Trade-journal CLI that records bid/close price, indicators and stock per trade
- Daily and running-average analytics (profit, loss, number of trades)
- Storage in local MongoDB, MongoDB Atlas **and** JSON (`NativeDataBase/`, `ServerDatabaseJSON/`)
- Matplotlib charts of indicator success and trade history
- **Self-destruct mode**: a remote parameter triggers a binary backup and wipes local program files
- Database management services (`DACFD_1`, `DADIDLJSONF_9`, `USJSONDS_10`) for create/delete/update of JSON & DB stores
- Desktop notifications on self-destruct events

## Usage

```bash
pip install -r StockAverage/requirements.txt
python "StockAverage/Body Code/StockAverage.py"
```

Supply your own MongoDB URIs (credentials in history have been redacted).

**Lineage:** [Vega_CopyTrading_Platform](https://github.com/optimus-node-js/Vega_CopyTrading_Platform) StockAverage [DBMSOfStockAverage](https://github.com/optimus-node-js/DBMSOfStockAverage)

---

## Author

**Rahul Vishwakarma**, Senior Full Stack Developer based in Ahmedabad, India

[![Portfolio](https://img.shields.io/badge/Portfolio-rahul--vishwakarma--portfolio.vercel.app-0A66C2?style=flat-square&logo=vercel&logoColor=white)](https://rahul-vishwakarma-portfolio.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rahul%20Vishwakarma-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/rahul-vishwakarma-101346192)
[![Email](https://img.shields.io/badge/Email-karmarahul67%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:karmarahul67@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-optimus--node--js-181717?style=flat-square&logo=github)](https://github.com/optimus-node-js)

