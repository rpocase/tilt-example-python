# tilt-example-python

Small fork of [tilt-example-python](https://github.com/tilt-dev/tilt-example-python) to illustrate docker-compose.yaml.
For a step by step guide, please refer to the parent repo.

# Requirements
The wrappers in this repo assume the following tools are installed.

* k3d (1.7.x)
* kubectl
* docker
* tilt

# Compose without live_reload

`tilt up -f Tiltfile`

# Compose file with live_reload

`tilt up -f Tiltfile.reload`

# k8s

```
./k3d-with-registry.sh
export KUBE_CONFIG=$(k3d get-context)
tilt up -f Tiltfile.k8s
```

## License

Licensed under [the Apache License, Version 2.0](LICENSE)
