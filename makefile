default:
	protoc --python_out=. --plugin=protoc-gen-custom=./ndarray_plugin_python.py --custom_out=. ndarray.proto
	protoc --python_out=. TestMessage.proto

.PHONY: default