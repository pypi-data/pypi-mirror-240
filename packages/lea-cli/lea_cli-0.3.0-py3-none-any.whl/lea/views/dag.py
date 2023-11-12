from __future__ import annotations

import collections
import graphlib
import io
import itertools

import lea


class DAGOfViews(graphlib.TopologicalSorter, collections.UserDict):
    def __init__(self, views: list[lea.views.View]):
        view_to_dependencies = {view.key: view.dependencies for view in views}
        graphlib.TopologicalSorter.__init__(self, view_to_dependencies)
        collections.UserDict.__init__(self, {view.key: view for view in views})
        self.dependencies = view_to_dependencies

    @property
    def schemas(self) -> set:
        return set(schema for schema, *_ in self)

    @property
    def schema_dependencies(self):
        deps = collections.defaultdict(set)
        for (src_schema, *_), dsts in self.dependencies.items():
            deps[src_schema].update([schema for schema, *_ in dsts if schema != src_schema])
        return deps

    def list_ancestors(self, node):
        """Returns a list of all the ancestors for a given node."""

        def _list_ancestors(node):
            for child in self.dependencies.get(node, []):
                yield child
                yield from _list_ancestors(child)

        return list(_list_ancestors(node))

    def list_descendants(self, node):
        """Returns a list of all the descendants for a given node."""

        def _list_descendants(node):
            for parent in self.dependencies:
                if node in self.dependencies[parent]:
                    yield parent
                    yield from _list_descendants(parent)

        return list(_list_descendants(node))

    def _to_mermaid_views(self):
        out = io.StringIO()
        out.write('%%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%\n')
        out.write("flowchart TB\n")
        nodes = set(node for deps in self.dependencies.values() for node in deps) | set(
            self.dependencies.keys()
        )
        schema_nodes = itertools.groupby(sorted(nodes), lambda node: node[0])
        for schema, nodes in schema_nodes:
            out.write(f"    subgraph {schema}\n")
            for _, *node in sorted(nodes):
                node = ".".join(node)
                out.write(f"    {schema}.{node}({node})\n")
            out.write("    end\n\n")
        for dst, srcs in sorted(self.dependencies.items()):
            dst = ".".join(dst)
            for src in sorted(srcs):
                src = ".".join(src)
                out.write(f"    {src} --> {dst}\n")
        return out.getvalue()

    def _to_mermaid_schemas(self):
        out = io.StringIO()
        out.write('%%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%\n')
        out.write("flowchart TB\n")
        schema_dependencies = self.schema_dependencies
        nodes = set(node for deps in schema_dependencies.values() for node in deps) | set(
            schema_dependencies.keys()
        )
        for node in sorted(nodes):
            out.write(f"    {node}({node})\n")
        for dst, srcs in sorted(schema_dependencies.items()):
            for src in sorted(srcs):
                out.write(f"    {src} --> {dst}\n")
        return out.getvalue()

    def to_mermaid(self, schemas_only=False):
        """

        >>> import pathlib
        >>> import lea

        >>> views_dir = pathlib.Path(__file__).parent.parent.parent / "examples" / "jaffle_shop" / "views"
        >>> views = lea.views.load_views(views_dir, sqlglot_dialect="duckdb")
        >>> views = [view for view in views if view.schema not in {"tests"}]
        >>> dag = lea.views.DAGOfViews(views)

        >>> print(dag.to_mermaid(schemas_only=True))
        %%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%
        flowchart TB
            analytics(analytics)
            core(core)
            staging(staging)
            core --> analytics
            staging --> core
        <BLANKLINE>

        >>> print(dag.to_mermaid())
        %%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%
        flowchart TB
            subgraph analytics
            analytics.finance.kpis(finance.kpis)
            analytics.kpis(kpis)
            end
        <BLANKLINE>
            subgraph core
            core.customers(customers)
            core.orders(orders)
            end
        <BLANKLINE>
            subgraph staging
            staging.customers(customers)
            staging.orders(orders)
            staging.payments(payments)
            end
        <BLANKLINE>
            core.orders --> analytics.finance.kpis
            core.customers --> analytics.kpis
            core.orders --> analytics.kpis
            staging.customers --> core.customers
            staging.orders --> core.customers
            staging.payments --> core.customers
            staging.orders --> core.orders
            staging.payments --> core.orders
        <BLANKLINE>

        """
        if schemas_only:
            return self._to_mermaid_schemas()
        return self._to_mermaid_views()
