# DMARC (Domain-based Message Authentication, Reporting & Conformance)

DMARC email authentication module implemented in Python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dmarc.

```bash
pip install dmarc
```

## Usage

```python
>>> import dmarc
>>>
>>> # represent verified SPF and DKIM status
>>> aspf = dmarc.SPF(domain='news.example.com', result=dmarc.SPF_PASS)
>>> adkim = dmarc.DKIM(domain='example.com', result=dmarc.DKIM_PASS)
>>> admarc = dmarc.DMARC() # admarc = dmarc.DMARC(publicsuffix.PublicSuffixList())
>>> try:
...     plc = admarc.parse_record(record='v=DMARC1; p=reject;', domain='example.com') # parse policy TXT RR
...     res = admarc.get_result(policy=plc, spf=aspf, dkim=adkim) # evaluate policy
...     res.verify() # check result
...     adict = res.as_dict() # dict repr
... except dmarc.RecordSyntaxError:
...     'invalid dmarc txt rr'
... except dmarc.PolicyNoneError:
...     'res.result == POLICY_FAIL and res.disposition == POLICY_DIS_NONE'
... except dmarc.PolicyQuarantineError:
...     'res.result == POLICY_FAIL and res.disposition == POLICY_DIS_QUARANTINE'
... except dmarc.PolicyRejectError:
...     'res.result == POLICY_FAIL and res.disposition == POLICY_DIS_REJECT'
... except dmarc.PolicyError:
...     'res.result == POLICY_FAIL and unknown disposition error'
...
>>> res.result == dmarc.POLICY_PASS
True
>>> res.disposition == dmarc.POLICY_DIS_NONE
True
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
