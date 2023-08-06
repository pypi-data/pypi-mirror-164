# SME SDK for Python

## Getting Started

### Install

```bash
pip install -U cardo-sme-sdk
```

### Usage

```python
import sme_sdk

# Create a new api config and s3 config for later use, these objects can be created only once
# in any module and can be reused in other modules.

api_config = sme_sdk.APIConfig(
    host='http://localhost:8000',
    username='username',
    password='password',
)
s3_config = sme_sdk.S3Config(
    access_key_id='access_key_id',
    secret_access_key='secret_access_key',
    bucket_name='bucket_name',
    region_name='region_name',
)

# When you want to use SME API, you need to create an APIClient object using the api_config created before.
data = {'key': 'value'}
with sme_sdk.APIClient(api_config) as client:
    s3client = sme_sdk.S3BlobStorageClient(s3_config)
    batch_result_id = client.create_new_batch(data, s3client)
    result = client.get_batch_result(batch_result_id)
```

- To learn more about how to use the SDK [refer to our docs](https://docs.service.cardoai.com/sme_sdk/index.html)
