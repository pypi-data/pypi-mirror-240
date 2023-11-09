from __future__ import annotations

import functools
import pathlib

from typing import TYPE_CHECKING, Any

import jinja2
import jinjarope

# importing jinjahelpers in order to register globals / filters
from mknodes.utils import inspecthelpers, jinjahelpers, log  # noqa: F401


if TYPE_CHECKING:
    import mknodes as mk


logger = log.get_logger(__name__)


class NodeEnvironment(jinjarope.Environment):
    """Jinja Node environment.

    A Jinja Environment specifically for MkNode instances.

    - Sets the parent for the filters
    - Puts node context in jinja namespace
    - collects rendered nodes
    """

    def __init__(self, node: mk.MkNode, **kwargs: Any):
        """Constructor.

        Arguments:
            node: Node this environment belongs to.
            kwargs: Optional keyword arguments passed to parent
        """
        super().__init__(**kwargs)
        self.node = node
        self.rendered_nodes: list[mk.MkNode] = list()
        self.rendered_children: list[mk.MkNode] = list()
        self.setup_environment()
        loaders = [
            jinjarope.get_loader("docs/"),
            jinjarope.FsSpecProtocolPathLoader(),
        ]
        if self.node.nodefile:
            loaders.insert(0, jinjarope.NestedDictLoader(self.node.nodefile._data))
        self.loader = jinjarope.ChoiceLoader(loaders)
        path = inspecthelpers.get_file(self.node.__class__)  # type: ignore[arg-type]
        self.class_path = pathlib.Path(path or "").parent.as_posix()
        paths = self.get_extra_paths()
        self.add_template_path(*paths)

    def setup_environment(self):
        """Set up the environment by adding node/context specific filters / globals.

        Mainly this adds wrapper functions / classes for all the MkNodes in order
        to auto-set the node parent (and that way the context) and to collect
        the rendered nodes.
        """
        import mknodes as mk

        filters = {}
        wrapped_klasses = {}
        for kls_name in mk.__all__:
            kls = getattr(mk, kls_name)

            class _WrappedMkNode(kls):
                def __post_init__(_self):  # noqa: N805
                    _self.parent = self.node
                    self.rendered_nodes.append(_self)

            functools.update_wrapper(_WrappedMkNode, kls, updated=[])
            # we add <locals> here so that the classes get filtered in iter_subclasses
            _WrappedMkNode.__qualname__ = "<locals>." + _WrappedMkNode.__qualname__
            wrapped_klasses[kls_name] = _WrappedMkNode

            def wrapped(ctx, *args, kls_name=kls_name, **kwargs):
                kls = getattr(mk, kls_name)
                node = kls(*args, parent=self.node, **kwargs)
                self.rendered_nodes.append(node)
                return node

            filters[kls_name] = jinja2.pass_context(wrapped)
        self.filters.update(filters)
        self.globals["parent_page"] = self.node.parent_page
        self.globals["parent_nav"] = i[-1] if (i := self.node.parent_navs) else None
        self.globals["node"] = self.node
        self.globals["mk"] = wrapped_klasses
        # def update_env_from_context(self):
        self.filters["get_link"] = self.node.ctx.links.get_link
        self.filters["get_url"] = self.node.ctx.links.get_url
        self.globals |= self.node.ctx.as_dict()

    def get_extra_paths(self) -> list[str]:
        paths = [self.class_path]
        if self.node.parent_navs:
            nav = self.node.parent_navs[-1]
            if "created" in nav.metadata:
                file = nav.metadata["created"]["source_filename"]
                path = pathlib.Path(file).parent
                paths.append(path.as_posix())
        return paths

    def render_template(
        self,
        template_name: str,
        variables: dict[str, Any] | None = None,
        block_name: str | None = None,
        parent_template: str | None = None,
    ) -> str:
        """Render a loaded template.

        Rendered nodes can be collected from `rendered_nodes` attribute after this call.

        Arguments:
            template_name: Template name
            variables: Extra variables for this render call
            block_name: Render specific block from the template
            parent_template: The name of the parent template importing this template
        """
        # if pathlib.Path(template_name).as_posix() not in self.list_templates():
        #     self.add_template(template_name)
        self.rendered_nodes = []
        self.setup_environment()
        # self.update_env_from_context()
        result = super().render_template(
            template_name,
            variables=variables,
            block_name=block_name,
            parent_template=parent_template,
        )
        self.rendered_children = [i for i in self.rendered_nodes if i.parent == self.node]
        return result

    def render_string(self, markdown: str, variables: dict | None = None) -> str:
        """Render a template string.

        Rendered nodes can be collected from `rendered_nodes` attribute after this call.

        Arguments:
            markdown: String to render
            variables: Extra variables for the environment
        """
        self.rendered_nodes = []
        self.setup_environment()
        # self.update_env_from_context()
        result = super().render_string(markdown, variables)
        self.rendered_children = [i for i in self.rendered_nodes if i.parent == self.node]
        return result


if __name__ == "__main__":
    import mknodes as mk

    node = mk.MkText.with_context()
    env = NodeEnvironment(node)
    txt = "{{ metadata.required_python_version | MkAdmonition }}"
    print(env.render_string(txt))
    print(env.rendered_nodes)
    # text = env.render_string(r"{{ 'test' | MkHeader }}")
    # text = env.render_string(r"{{ 50 | MkProgressBar }}")
    # print(env.rendered_nodes)
    # env.render_string(r"{{test('hallo')}}")
