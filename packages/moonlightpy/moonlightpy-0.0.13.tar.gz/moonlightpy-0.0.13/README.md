# moonlight

moonlight is a reverse port forwarding tool written by python. You can run several clients connected to same server in
the intranet network and the server can balance requests between these clients.

```
intranet network              public network host
                               ----------------
intranet01                     |              |
    client1  <-------------->  |              |
    client2  <-------------->  |    server    |
                               | 1.1.1.1:9001 |    
intranet02                     |              |
    client3  <-------------->  |              |
                               ----------------
```

## install

```bash
python -m pip install moonlightpy
```

## run

### server config.yaml

```yaml
"addr": "0.0.0.0"
"port": 9001
"rules": [
  "intranet01,192.168.0.134,22,0.0.0.0,13422",
  "intranet02,192.168.0.132,22,0.0.0.0,13222"
]

```

### server & clients

```bash
# run server on one public network host (e.g. 1.1.1.1)
 python -m moonlightpy server ./config.yaml
 
 # run clients on some intranet hosts 
 python -m moonlightpy client intranet01 1.1.1.1 9001
```

Now you can access the `192.168.0.134:22` from `1.1.1.1:13422` and `192.168.0.132:22` from `1.1.1.1:13222`

