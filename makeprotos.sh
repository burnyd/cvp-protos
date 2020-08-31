CVPAPIS=$PWD
python -m grpc_tools.protoc -I $CVPAPIS \
--python_out=$CVPAPIS/protos \
--grpc_python_out=$CVPAPIS/protos \
$CVPAPIS/arista/event.v1/* \
$CVPAPIS/arista/inventory.v1/* \
$CVPAPIS/arista/subscriptions/* \
$CVPAPIS/arista/tag.v1/* \
$CVPAPIS/arista/time/*
