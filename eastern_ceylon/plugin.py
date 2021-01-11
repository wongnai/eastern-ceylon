import warnings
import json

from eastern import EasternPlugin

ENV_KEY = "__ceylon"


class CeylonPlugin(EasternPlugin):
    def env_hook(self, formatter, **kwargs):
        if ENV_KEY in formatter.env:
            # For recursive format, don't run this plugin again
            return {}

        vars_file = formatter.path / "vars.json"
        namespace = formatter.env["NAMESPACE"]

        if not vars_file.is_file():
            warnings.warn("Ceylon: vars.json file not found!")
            return {}

        with vars_file.open() as fp:
            variables = json.load(fp)

            out = {}
            if namespace in variables:
                out = variables[namespace]
            elif "default" in variables:
                out = variables["default"]

            out[ENV_KEY] = True

            return out
