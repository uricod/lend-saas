#### Introduction

1. This is for LendingSaaS API and here is link https://app.swaggerhub.com/apis/lendsaas/LendSaaSETL/1.0.0 

# monday
A LendingSaaS Python Client Library


For an overview of the Monday API, [click here](https://monday.com/developers/v2#introduction-section).


#### Requirements
- Python >= 3.6

#### Getting started
`pip install lend-saas`

`lend-saas` is very simple to use -- take a look at the below example:
```python
from lend-saas import Client


monday = MondayClient('your token')

monday.items.create_item(board_id='12345678', group_id='today',  item_name='Do a thing')

```

**Available methods:**
#### Items Resource (monday.items)