"""Jac's Key Elemental Abstractions"""
from __future__ import annotations
from jaclang import jac_import as __jac_import__
from enum import Enum as __jac_Enum__, auto as __jac_auto__
from jaclang.jac.features import JacFeature as __JacFeature
from datetime import datetime
from uuid import UUID, uuid4
from jaclang.jac.constant import EdgeDir
__jac_import__(target='memory_impl', base_path=__file__)
from memory_impl import *
import memory_impl
__jac_import__(target='exec_ctx_impl', base_path=__file__)
from exec_ctx_impl import *
import exec_ctx_impl
__jac_import__(target='element_impl', base_path=__file__)
from element_impl import *
import element_impl
__jac_import__(target='arch_impl', base_path=__file__)
from arch_impl import *
import arch_impl

class AccessMode(__jac_Enum__):
    READ_ONLY = __jac_auto__()
    READ_WRITE = __jac_auto__()
    PRIVATE = __jac_auto__()

@__JacFeature.make_architype('object')
class Memory:
    (index): dict[UUID, Element] = {}
    (save_queue): list[Element] = []

    def get_obj(self, caller_id: UUID, item_id: UUID, override: bool=True) -> Element:
        ret = self.index.get(item_id)
        if override or ret.__is_readable(ret is not None and caller_id):
            return ret

    def has_obj(self, item_id: UUID) -> bool:
        return item_id in self.index

    def save_obj(self, caller_id: UUID, item: Element):
        if item.is_writable(caller_id):
            self.index[item.id] = item
            if item._persist:
                self.save_obj_list.add(item)
        self.mem[item.id] = item
        if item._persist:
            self.save_obj_list.add(item)

    def del_obj(self, caller_id: UUID, item: Element):
        if item.is_writable(caller_id):
            self.index.pop(item.id)
            if item._persist:
                self.save_obj_list.remove(item)

    def get_object_distribution(self) -> dict:
        dist = {}
        for i in self.index.keys():
            t = type(self.index[i])
            if t in dist:
                dist[t] += 1
            else:
                dist[t] = 1
        return dist

    def get_mem_size(self) -> float:
        return sys.getsizeof(self.index) / 1024.0

@__JacFeature.make_architype('object')
class ExecutionContext:
    (master): Master = uuid4()
    (memory): Memory = Memory()

    def reset(self):
        self.__init__()

    def get_root(self) -> Node:
        if type(self.master) == UUID:
            self.master = Master()
        return self.master.root_node
'Global Execution Context, should be monkey patched by the user.'
exec_ctx = ExecutionContext()

@__JacFeature.make_architype('object')
class ElementInterface:
    (jid): UUID = uuid4()
    (timestamp): datetime = datetime.now()
    (persist): bool = True
    (access_mode): AccessMode = AccessMode.PRIVATE
    (rw_access): set = set()
    (ro_access): set = set()
    (owner_id): UUID = exec_ctx.master
    (mem): Memory = exec_ctx.memory

    def make_public_ro(self):
        self.__jinfo.access_mode = AccessMode.READ_ONLY

    def make_public_rw(self):
        self.__jinfo.access_mode = AccessMode.READ_WRITE

    def make_private(self):
        self.__jinfo.access_mode = AccessMode.PRIVATE

    def is_public_ro(self) -> bool:
        return self.__jinfo.access_mode == AccessMode.READ_ONLY

    def is_public_rw(self) -> bool:
        return self.__jinfo.access_mode == AccessMode.READ_WRITE

    def is_private(self) -> bool:
        return self.__jinfo.access_mode == AccessMode.PRIVATE

    def is_readable(self, caller_id: UUID) -> bool:
        return caller_id == self.owner_id or (self.is_public_read() or (caller_id in self.ro_access or caller_id in self.rw_access))

    def is_writable(self, caller_id: UUID) -> bool:
        return caller_id == self.owner_id or (self.is_public_write() or caller_id in self.rw_access)

    def give_access(self, caller_id: UUID, read_write: bool=True):
        if read_write:
            self.rw_access.add(caller_id)
        else:
            add.ro_access.self(caller_id)

    def revoke_access(self, caller_id: UUID):
        self.ro_access.discard(caller_id)
        self.rw_access.discard(caller_id)

@__JacFeature.make_architype('object')
class DataSpatialInterface:
    (ds_entry_funcs): list[dict] = []
    (ds_exit_funcs): list[dict] = []

    def on_entry(self, cls: type, triggers: list[type]):

        def decorator(func: callable) -> callable:
            cls.ds_entry_funcs.append({'types': triggers, 'func': func})

            def wrapper(*args: list, **kwargs: dict) -> callable:
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def on_exit(self, cls: type, triggers: list[type]):

        def decorator(func: callable) -> callable:
            cls.ds_exit_funcs.append({'types': triggers, 'func': func})

            def wrapper(*args: list, **kwargs: dict) -> callable:
                return func(*args, **kwargs)
            return wrapper
        return decorator

@__JacFeature.make_architype('object')
class ObjectInterface(ElementInterface):
    pass

@__JacFeature.make_architype('object')
class NodeInterface(ObjectInterface):
    (edges): dict[EdgeDir, list[Edge]] = {EdgeDir.IN: [], EdgeDir.OUT: []}

    def connect_node(self, nd: Node, edg: Edge) -> Node:
        edg.attach(self.py_obj, nd)
        return self

    def edges_to_nodes(self, dir: EdgeDir) -> list[Node]:
        ret_nodes = []
        if dir in [EdgeDir.OUT, EdgeDir.ANY]:
            for i in self.edges[EdgeDir.OUT]:
                ret_nodes.append(i.target)
        elif dir in [EdgeDir.IN, EdgeDir.ANY]:
            for i in self.edges[EdgeDir.IN]:
                ret_nodes.append(i.source)
        return ret_nodes

@__JacFeature.make_architype('object')
class EdgeInterface(ObjectInterface):
    (source): Node = None
    (target): Node = None
    (dir): EdgeDir = None

    def apply_dir(self, dir: EdgeDir) -> Edge:
        self.dir = dir
        return self

    def attach(self, src: Node, trg: Node) -> Edge:
        if self.dir == EdgeDir.IN:
            self.source = trg
            self.target = src
            src._jac_.edges[EdgeDir.IN].append(self)
            trg._jac_.edges[EdgeDir.OUT].append(self)
        else:
            self.source = src
            self.target = trg
            src._jac_.edges[EdgeDir.OUT].append(self)
            trg._jac_.edges[EdgeDir.IN].append(self)
        return self

@__JacFeature.make_architype('object')
class WalkerInterface(ObjectInterface):
    (path): list[Node] = []
    (next): list[Node] = []
    (ignores): list[Node] = []
    (disengaged): bool = True

    def visit_node(self, nds: list[Node] | (list[Edge] | (Node | Edge))):
        if isinstance(nds, list):
            for i in nds:
                if i not in self.ignores:
                    self.next.append(i)
        elif nds not in self.ignores:
            self.next.append(nds)
        return len(nds) if isinstance(nds, list) else 1

    def ignore_node(self, nds: list[Node] | (list[Edge] | (Node | Edge))):
        if isinstance(nds, list):
            for i in nds:
                self.ignores.append(i)
        else:
            self.ignores.append(nds)

    def disengage_now(self):
        self.next = []
        self.disengaged = True

@__JacFeature.make_architype('object')
class Element:
    (_jac_): ElementInterface = ElementInterface()

@__JacFeature.make_architype('object')
class Object(Element):
    (_jac_): ObjectInterface = ObjectInterface()
    (_jac_ds_): DataSpatialInterface = DataSpatialInterface()

@__JacFeature.make_architype('object')
class Node(Object):
    (_jac_): NodeInterface = NodeInterface()

    def __call__(self, walk: Walker):
        if not isinstance(walk, Walker):
            raise TypeError('Argument must be a Walker instance')
        walk(self)

@__JacFeature.make_architype('object')
class Edge(Object):
    (_jac_): EdgeInterface = EdgeInterface()

    def __call__(self, walk: Walker):
        if not isinstance(walk, Walker):
            raise TypeError('Argument must be a Walker instance')
        walk(self._jac_.target)

@__JacFeature.make_architype('object')
class Walker(Object):
    (_jac_): WalkerInterface = WalkerInterface()

    def __call__(self, nd: Node):
        self._jac_.path = []
        self._jac_.next = [nd]
        walker_type = self.__class__.__name__
        while len(self._jac_.next):
            nd = self._jac_.next.pop(0)
            node_type = nd.__class__.__name__
            for i in nd._jac_ds_.ds_entry_funcs:
                if i['func'].__qualname__.split('.')[0] == node_type and type(self) in i['types']:
                    i['func'](nd, self)
                if self._jac_.disengaged:
                    return
            for i in self._jac_ds_.ds_entry_funcs:
                if i['func'].__qualname__.split('.')[0] == walker_type and (type(nd) in i['types'] or nd in i['types']):
                    i['func'](self, nd)
                if self._jac_.disengaged:
                    return
            for i in self._jac_ds_.ds_exit_funcs:
                if i['func'].__qualname__.split('.')[0] == walker_type and (type(nd) in i['types'] or nd in i['types']):
                    i['func'](self, nd)
                if self._jac_.disengaged:
                    return
            for i in nd._jac_ds_.ds_exit_funcs:
                if i['func'].__qualname__.split('.')[0] == node_type and type(self) in i['types']:
                    i['func'](nd, self)
                if self._jac_.disengaged:
                    return
            self._jac_.path.append(nd)
        self._jac_.ignores = []

@__JacFeature.make_architype('object')
class Master(Element):
    (root_node): Node = Node()

def make_architype(base_class: type) -> type:

    def class_decorator(cls: type) -> type:
        if not issubclass(cls, base_class):
            cls = type(cls.__name__, (cls, base_class), {})
        return cls
    return class_decorator