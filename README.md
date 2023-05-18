# type issue showcase

```
python -m venv ./.venv
source .venv/bin/activate
pip install -r requirements.txt
```

## notes

protos were generated with: `python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. helloworld.proto --mypy_out=. --mypy_grpc_out=.`
