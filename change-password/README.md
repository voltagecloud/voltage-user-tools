# Change Password and Regenerate Macaroon Root Key

## Installation
```
pip install -r requirements.txt
```

## Setup Node Connection
```
lndgrpcclient_cli environment
```

```
lndgrpcclient_cli credentials --credential_type=macaroon
lndgrpcclient_cli credentials --credential_type=tls
```

## Test Node Connection
```
lndgrpcclient_cli shell
```