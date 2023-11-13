from mockito import when, mock, unstub
from expects import *
from mamba import description, context, it
import tests.vars as vars
import src.cnd_eyes_injector as cnd_eyes_injector


with description('EyesInjector') as self:
    with before.each:
        unstub()
        self.instance = cnd_eyes_injector.eyes_injector.EyesInjector(vars.host, vars.port, vars.scheme, vars._print, vars.verify)

    with context("__init__"):
        with it("shoud get an instance"):
            expect(isinstance(self.instance, cnd_eyes_injector.eyes_injector.EyesInjector)).to(equal(True))

    # with context("get_bearer"):
    #     with it("shoud get bearer"):
    #         bearer = self.instance.connect(vars.user, vars.password)
    #         expect(isinstance(self.instance, cnd_eyes_injector.eyes_injector.EyesInjector)).to(equal(True))

