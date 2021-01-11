# Eastern-Ceylon

[![Travis](https://api.travis-ci.org/wongnai/eastern-ceylon.svg?branch=master)](https://travis-ci.org/wongnai/eastern-ceylon)
[![GitHub license](https://img.shields.io/github/license/wongnai/eastern-ceylon.svg)](https://github.com/wongnai/eastern-ceylon/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/eastern-ceylon.svg)](https://pypi.python.org/pypi/eastern-ceylon)

Make [Eastern](https://github.com/wongnai/eastern) more friendly with GitOps by storing template variables in file.

## Setup

### ArgoCD setup

1. You'll need a custom ArgoCD image with eastern and this eastern plugin installed
2. Install [config management plugin](https://argoproj.github.io/argo-cd/user-guide/config-management-plugins/):

```
configManagementPlugins: |
  - name: eastern
    generate:
      command: [sh, -c]
      args: ["eastern generate kubernetes.yaml $ARGOCD_APP_NAMESPACE"]
```

### Installing

To install this plugin, run `python setup.py install`.

This plugin is **not** designed to be disable-able. You'll have to uninstall it to restore normal eastern behavior.

## Usage

1. Name your eastern entrypoint file `kubernetes.yaml`
2. Add vars.json that store your previous `-s KEY=value` in this format

```json
{
  "namespace": {
    "KEY": "value"
  }
}
```

Repeat if deploying in multiple namespaces

## License
(C) 2020 Wongnai Media Co, Ltd.

Eastern-Ceylon is licensed under [MIT License](LICENSE)
