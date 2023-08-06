# This file is placed in the Public Domain.
# pylint: disable=E1101,E0611,C0116,C0413,C0411,W0406


"databases"


import os
import unittest


from bot.obj import Db, Object, Wd, cdir, last, save
from bot.obj import fns, hook
from bot.obj import dumps, loads


class Composite(Object):

    def __init__(self):
        super().__init__()
        self.dbs = Db()


class TestDbs(unittest.TestCase):

    def test_cdir(self):
        cdir(".test")
        self.assertTrue(os.path.exists(".test"))

    def test_composite(self):
        com1 = Composite()
        com2 = loads(dumps(com1))
        self.assertEqual(type(com2.dbs), type({}))

    def test_constructor(self):
        dbs = Db()
        self.assertEqual(type(dbs), Db)

    def test_fns(self):
        Wd.workdir = ".test"
        obj = Object()
        save(obj)
        self.assertTrue("Object" in fns("bot.obj.Object")[0])

    def test_hook(self):
        obj = Object()
        obj.key = "value"
        pth = save(obj)
        oobj = hook(pth)
        self.assertEqual(oobj.key, "value")

    def test_last(self):
        oobj = Object()
        oobj.key = "value"
        save(oobj)
        last(oobj)
        self.assertEqual(oobj.key, "value")
