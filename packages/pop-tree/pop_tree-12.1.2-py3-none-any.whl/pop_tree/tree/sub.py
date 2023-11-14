import re
from typing import Any
from typing import Dict
from typing import List

from dict_tools import data as data_


def load_all(hub, pypaths: List[str] = None):
    """
    Load the named pypaths and all available dynes onto the hub
    """
    if pypaths:
        for pypath in pypaths:
            try:
                hub.pop.sub.add(
                    pypath=pypath,
                    omit_class=False,
                    omit_func=False,
                    omit_vars=False,
                    stop_on_failures=False,
                )
            except ModuleNotFoundError as e:
                hub.log.error(e)
                raise

    for dyne in hub._dynamic:
        if not hasattr(hub, dyne):
            hub.pop.sub.add(
                dyne_name=dyne,
                omit_class=False,
                omit_func=False,
                omit_vars=False,
                stop_on_failures=False,
            )
        try:
            hub.pop.sub.load_subdirs(hub[dyne], recurse=True)
        except AttributeError or TypeError:
            ...


async def recurse(hub, sub, ref: str) -> Dict[str, Any]:
    """
    Find all of the loaded subs in a Sub. I.E:
        pprint(hub.pop.tree.recurse(hub.pop))
    :param hub: The redistributed pop central hub
    :param sub: The pop object that contains the loaded module data
    :param ref: The current reference on the hub
    """
    ret = data_.NamespaceDict()
    for loaded in sorted(sub._subs):
        loaded_ref = f"{ref}.{loaded}"
        try:
            loaded_sub = getattr(sub, loaded)
        except AttributeError:
            continue
        if not (
            getattr(loaded_sub, "_virtual", False)
            and getattr(loaded_sub, "_sub_virtual", True)
        ):
            # Bail early if the sub's virtual isn't True
            continue
        recursed_sub = await hub.tree.sub.recurse(loaded_sub, ref=loaded_ref)

        for mod in sorted(loaded_sub._loaded):
            loaded_mod = getattr(loaded_sub, mod)
            recursed_sub[mod] = await hub.tree.mod.parse(
                loaded_mod, ref=f"{loaded_ref}.{mod}"
            )

        if recursed_sub:
            ret[loaded] = recursed_sub

    return ret


async def parse(hub, loaded_sub, base_ref: str = None):
    root = data_.NamespaceDict()
    sub = loaded_sub._subname
    result = re.findall(r"\[(\d+)\]", sub)
    if result:
        sub = result[-1]

    root[sub] = await hub.tree.sub.recurse(loaded_sub, ref=f"{base_ref}.{sub}")

    for loaded_mod in sorted(loaded_sub, key=lambda x: x.__name__):
        mod = loaded_mod.__name__
        if base_ref:
            ref = f"{base_ref}.{sub}.{mod}"
        else:
            ref = f"{sub}.{mod}"
        root[sub][mod] = await hub.tree.mod.parse(loaded_mod, ref=ref)

    return root
