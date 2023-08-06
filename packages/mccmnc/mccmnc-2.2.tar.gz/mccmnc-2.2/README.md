# mcc-mnc

A Mobile Country Code (MCC) is used in cellular networks (GSM, CDMA, UMTS, etc.) to determine the country in which a
mobile subscriber belongs to. To identify a mobile subscriber's network provider, the MCC is combined with a Mobile
Network Code (MNC). The combination of MCC and MNC is called the Public Land Mobile Network (PLMN) and is the
concatenation of both strings (e.g. MCC of 262 and MNC of 01 results in a PLMN of 26201). Combining the PLMN with the
Mobile Subscription Identification Number (MSIN) results in the International Mobile Subscriber Identity (IMSI), from
which a mobile subscriber can be uniquely identified.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mcc-mnc.

```bash
pip install mccmnc
```

## Usage

```bash
> python mccmnc.py -cc XXX
> python mccmnc.py -mcc XXX
> python mccmnc.py -mcc XXX -mnc XXX
> python mccmnc.py -cc XXX -mcc XXX -mnc XXX

# Updating mcc-mnc
> python mccmnc.py -update # Downloads and refreshes local CSV and JSON
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/) © Joseph Julian